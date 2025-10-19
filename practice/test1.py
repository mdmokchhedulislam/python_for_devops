# service status checker

import os

servers = ["google.com", "github.com", "mokchhhedulislam.page.gd", "gopal.com"]

def check_server(host):
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    return "UP" if response == 0 else "DOWN"
    