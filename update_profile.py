# update_profile.py
import os
import sys
import requests

API_URL = os.getenv("PROFILE_API_URL")  # e.g. https://api.example.com/v1/profile
TOKEN = os.getenv("PROFILE_API_TOKEN")
NEW_NAME = os.getenv("NEW_DISPLAY_NAME")

if not API_URL or not TOKEN or not NEW_NAME:
    print("ERROR: PROFILE_API_URL, PROFILE_API_TOKEN and NEW_DISPLAY_NAME must be set", file=sys.stderr)
    sys.exit(2)

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Example payload — change field names to the API's contract
payload = {
    "display_name": NEW_NAME
}

try:
    resp = requests.patch(API_URL, json=payload, headers=headers, timeout=15)
except requests.RequestException as e:
    print("Request failed:", e, file=sys.stderr)
    sys.exit(3)

if resp.status_code in (200, 204):
    print("Profile updated successfully.")
    sys.exit(0)
else:
    print(f"Failed to update profile. Status: {resp.status_code}\nBody: {resp.text}", file=sys.stderr)
    sys.exit(4)
