import requests
import json

#################################
# UpMan By Zombiebattler
# https://github.com/Zombiebattler/Update-Manager
#################################

class Console:
    @staticmethod
    def msg(log,msg):
        if log:
            print(f"\033[92m{msg}\033[0m")
    @staticmethod
    def log(log, msg):
        if log:
            print(f"> {msg}\033[0m")
    @staticmethod
    def error(msg):
        print(f"\033[91mX {msg}\033[0m")
    @staticmethod
    def info(log, msg):
        if log:
            print(f"\033[93m! {msg}\033[0m")


def check_upman():
    url = "https://raw.githubusercontent.com/Zombiebattler/Update-Manager/main/VERSION.txt"
    online_version = str(requests.get(url).text).strip('\n')
    with open("./UpMan.json", 'r') as file:
        file = json.load(file)
        local_version = str(file['upman_version']).strip('\n')
    if online_version != local_version:
        Console.info(True, "new UpMan version")


def check(json_url, logs, force):   # URL to your "UpMan.json" ||| log (True/False) if you want to output logs in the console ||| force (True/False) if you want to force the user to use the newest version (True -> Yes)
    check_upman()
    try:
        with open("./UpMan.json", 'r') as file:
            file = json.load(file)
            local_version = file['script_version']
            Console.log(logs, f"local version :{local_version}")
    except Exception as e:
        Console.error(f"{e}")
        local_version = False

    try:
        response = requests.get(json_url).json()
        online_version = response['script_version']
        Console.log(logs, f"online version :{online_version}")
    except Exception as e:
        Console.error(f"{e}")
        online_version = False


    if local_version and online_version:
        if local_version != online_version:
            if force:
                Console.error(f"New version Available Please Update")
                exit(1)
            else:
                Console.info(True, f"New version Available")
        else:
            Console.msg(logs, f"version Up to date")
