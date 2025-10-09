# controllers/pincode_controller.py
from odoo import http
from odoo.http import request

import requests

def fetch_pincode_details(pincode):
    try:
        response = requests.get(
            f"https://api.postalpincode.in/pincode/{pincode}",
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        if data and data[0]['Status'] == 'Success':
            return data[0]['PostOffice'][0]
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API Error: {e}")
    return None
