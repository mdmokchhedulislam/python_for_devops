# check and start container

import subprocess
def check_start_docker():
    running_containers=subprocess.check_output(["docker", "ps"]).decode('utf-8')
# imagine that container name is ecom_app

    if "ecom_app" not in running_containers:
        print("app is not running , need to start")
        subprocess.run(['docker', 'start','ecom_app'])
    else:
        print("container is ok")

check_start_docker()