import os
import sys
from pyotp import TOTP
from SmartApi import SmartConnect

key_path = os.path.dirname(os.path.abspath(__file__)) + "/key.txt"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if not os.path.exists(key_path):
    print("Key file not found. Please create a key.txt file with the following format:")
    print("api_key:your_api_key")
    print("api_secret:your_api_secret")
    print("totp_secret:your_totp_secret")
    sys.exit(1)

with open(key_path, "r") as f:
    data = {}
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
        elif "=" in line:
            k, v = line.split("=", 1)
        else:
            continue
        data[k.strip().lower()] = v.strip()

    def find_key(candidates):
        for c in candidates:
            if c in data:
                return data[c]
        for k in data:
            for c in candidates:
                if c in k:
                    return data[k]
        return None

    api_key = find_key(["api_key", "angelone_api_key"])
    api_secret = find_key(["api_secret", "angelone_secret_key", "secret"])
    client_id = find_key(["client_id", "angelone_client_id", "username", "user"])
    password = find_key(["password", "angelone_password", "pwd"])
    totp_secret = find_key(["totp_secret", "angelone_totp", "totp"])

if not api_key or not client_id or not password or not totp_secret:
    print("Key file missing required fields. Expected at least: api_key, client_id, password, totp")
    sys.exit(1)

obj = SmartConnect(api_key=api_key)
data = obj.generateSession(client_id, password, TOTP(totp_secret).now())
# refreshToken = data['data']['refreshToken']
# feedToken = obj.getfeedToken()
# print("Login successful!")

if data.get("status") != True:
    print("Login failed. Please check your credentials and try again.")
    sys.exit(1)
else:
    auth_token = data['data']['jwtToken']   
    feedToken  = obj.getfeedToken()
    print("Login successful!")