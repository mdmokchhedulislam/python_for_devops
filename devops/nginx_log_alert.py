import re
import smtplib
from email.message import EmailMessage

# Configuration
LOG_FILE = "/var/log/nginx/error.log"
FROM_EMAIL = "yourgmail@gmail.com"         
TO_EMAIL = "admin@example.com"             
APP_PASSWORD = "your-app-password"         

# Read log file and find 500 errors
with open(LOG_FILE) as f:
    errors = [line.strip() for line in f if "500" in line]

# Print errors if found
if errors:
    print(f"Found {len(errors)} 500 errors:")
    for e in errors:
        print(e)

    # Prepare email
    msg = EmailMessage()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = f"Nginx Alert: {len(errors)} Internal Server Errors"
    msg.set_content("\n".join(errors))

    # Send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(FROM_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        print("Alert email sent successfully!")
    except Exception as e:
        print("Failed to send email:", str(e))
else:
    print("No 500 errors found.")
