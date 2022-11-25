import requests.exceptions
import scratchclient
import time
import json

print("Scratch F4F bot")
print("-------------------------------------")
print("You must be following at least one user who has at least a few followers to use this.")
print("I don't take responsiblity if you get banned for using this.")

config = open("config.json", "r")
config_loaded = json.loads(config.read())

session = scratchclient.ScratchSession(config_loaded["userName"], config_loaded["password"])

while True:
    following = session.get_user(config_loaded["userName"]).get_following()

    for f in following:
        try:
            gotten = f.get_followers()
            if len(gotten) > 0:
                for g in gotten:
                    if not g.username == config_loaded["userName"]:
                        print(g.username)
                        g.follow()
                        time.sleep(config_loaded["timeInterval"])
        except requests.exceptions.JSONDecodeError:
            pass
