import requests
from colorama import Fore, init
import os
init(autoreset=True)
api_endpoint = "https://public.api.bsky.app/xrpc/com.atproto.identity.resolveHandle?handle="
def get_usernames(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except:
        print(f"error with file '{file_path}'.")
        return []
def check_username(username):
    try:
        res = requests.get(f"{api_endpoint}{username}.bsky.social")
        return res.status_code == 400 and "Unable to resolve handle" in res.json().get("message", "")
    except:
        return False
def main():
    file_path = input("file path: ").strip()
    usernames = get_usernames(file_path)
    if not usernames:
        print("no usernames found.")
        return
    for idx, username in enumerate(usernames, 1):
        if check_username(username):
            print(f"{Fore.GREEN}{username} is available")
        print(f"checked {idx}/{len(usernames)}", end="\r")
    print("\ndone.")
if __name__ == "__main__":
    main()


















