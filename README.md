# FedEx Tracking API with FastAPI

A simple Python FastAPI application that fetches FedEx shipment status using the FedEx APIs. Supports **OAuth2 authentication** and returns detailed tracking information in JSON. Works in both **Sandbox**(testing) and **Production**(live) modes.

## Features

- `/track/{tracking_number}` endpoint to get shipment status
- OAuth2 authentication with FedEx API
- Returns detailed JSON tracking data, including scan history
- Mode indicator (`SANDBOX` or `PROD`) visible at the root `/` endpoint
- Testable with Postman or any HTTP client
- Environment variable management for secure API credentials

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- python-dotenv

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Megans-Tech-Life/FEDEX_FastAPI.git
cd FEDEX_FastAPI
```

2. Create envioronment files for Sandbox and Production:

- .env.sandbox (Sandbox credentials)
- .env.prod (Production credentials)
  **Add both files to .gitignore to keep them private.**

3. Run the server in Sandbox (default):

```bash
python - m uvicorn main:app --reload
```

- Root endpoint `/` will show "mode": "SANDBOX"

4. Run the server in Production:

```bash
FEDEX_ENV=PROD python -m uvicorn main:app --reload
```

- Root endpoint `/` will show "mode": "PROD"

5. Test the tracking endpoint:

```bash
GET http://127.0.0.1:8000/track/{tracking_number}
```

- Replace {tracking_number} with a FedEx test number (Sandbox) or real shipment number (Production).
