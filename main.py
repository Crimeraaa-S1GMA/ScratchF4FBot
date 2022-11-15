import requests.exceptions
import scratchclient
import time

print("Scratch F4F bot")
print("-------------------------------------")
print("This is just some sucky code which searches for Scratch users in your following tab, and checks the users they follow as well.")
print("If you don't follow any new people, follow someone else manually.")
print("I don't take responsiblity if you get banned for using this.")

username = input("Enter Scratch account username: ")
password = input("Enter Scratch account password: ")

session = scratchclient.ScratchSession(username, password)

while True:
    following = session.get_user("SIGMA_a").get_following()

    for f in following:
        try:
            gotten = f.get_followers()
            if len(gotten) > 0:
                for g in gotten:
                    if not g.username == username:
                        print(g.username)
                        g.follow()
        except requests.exceptions.JSONDecodeError:
            pass
