from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

FEDEX_KEY = os.getenv("FEDEX_KEY")
FEDEX_SECRET = os.getenv("FEDEX_SECRET")
FEDEX_BASE_URL = os.getenv("FEDEX_BASE_URL")

app = FastAPI()

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

@app.get("/")
def home():
        return {"message": "FedEx API is running!"}
    
@app.get("/track/{tracking_number}")
def track_package(tracking_number: str):
        access_token = get_fedex_token()
        url = f"{FEDEX_BASE_URL}/track/v1/trackingnumbers"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        body = {
            "trackingInfo": [
                {
                    "trackingNumberInfo": {
                        "trackingNumber": tracking_number
                    }
                }
            ],
            "includeDetailedScans": True
        }
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=500, detail="Failed to track package")
