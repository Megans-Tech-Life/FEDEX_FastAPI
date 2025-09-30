# FedEx Tracking API with FastAPI

A simple Python FastAPI application that fetches FedEx shipment status using the FedEx sandbox API. Supports OAuth2 authentication and returns detailed tracking information in JSON.

## Features

- `/track/{tracking_number}` endpoint to get shipment status
- OAuth2 authentication with FedEx sandbox
- Returns detailed JSON tracking data, including scan history
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
