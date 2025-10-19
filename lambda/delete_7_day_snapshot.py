import os
import boto3
from datetime import datetime, timezone, timedelta
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


ec2 = boto3.client("ec2")


def lambda_handler(event, context):
    # environment vars
    days = int(os.getenv("DAYS", "7"))
    dry_run = os.getenv("DRY_RUN", "true").lower() in ("1","true","yes")
    owner_filter = os.getenv("OWNER", "self")  

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    logger.info(f"Deleting snapshots older than {days} days (cutoff={cutoff.isoformat()}). DRY_RUN={dry_run}")

    paginator = ec2.get_paginator("describe_snapshots")
    # OwnerIds accepts 'self' or a specific account id
    owner_ids = [owner_filter] if owner_filter else ["self"]

    deleted = []
    skipped = []
    errors = []

    for page in paginator.paginate(OwnerIds=owner_ids):
        snapshots = page.get("Snapshots", [])
        for s in snapshots:
            snap_id = s.get("SnapshotId")
            start_time = s.get("StartTime")  # datetime with tzinfo
            desc = s.get("Description", "")
            # safety: skip snapshots that appear to be AMI root snapshots? (optional)
            if not start_time:
                skipped.append((snap_id, "no StartTime"))
                continue

            if start_time < cutoff:
                logger.info(f"Snapshot {snap_id} created {start_time.isoformat()} is older than cutoff.")
                if dry_run:
                    deleted.append((snap_id, "dry-run"))
                    continue
                try:
                    resp = ec2.delete_snapshot(SnapshotId=snap_id)
                    logger.info(f"Deleted snapshot {snap_id}")
                    deleted.append((snap_id, "deleted"))
                except Exception as e:
                    logger.exception(f"Failed to delete {snap_id}: {e}")
                    errors.append((snap_id, str(e)))
            else:
                skipped.append((snap_id, f"too recent: {start_time.isoformat()}"))

    result = {
        "cutoff": cutoff.isoformat(),
        "days": days,
        "dry_run": dry_run,
        "deleted_count": len([d for d in deleted if d[1]!="dry-run"]),
        "deleted": deleted,
        "skipped_count": len(skipped),
        "skipped": skipped,
        "errors": errors
    }

    logger.info("Finished snapshot cleanup")
    return result
