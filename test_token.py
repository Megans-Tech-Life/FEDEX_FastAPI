import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

# Load .env values

load_dotenv()

FEDEX_KEY = os.getenv("FEDEX_KEY")
FEDEX_SECRET = os.getenv("FEDEX_SECRET")
FEDEX_BASE_URL = os.getenv("FEDEX_BASE_URL")

def get_fedex_token():
    url = f"{FEDEX_BASE_URL}/oauth/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": FEDEX_KEY,
        "client_secret": FEDEX_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    raise HTTPException(status_code=500, detail="Failed to obtain FedEx token")

if __name__ == "__main__":
    try:
        token = get_fedex_token()
        print("FedEx Token:", token)
    except HTTPException as e:
        print("Error:", e.detail)