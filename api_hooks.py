import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_abuseipdb(ip):
    key = os.getenv('ABUSEIPDB_API_KEY')
    if not key:
        return None
    try:
        url = 'https://api.abuseipdb.com/api/v2/check'
        headers = {'Key': key, 'Accept': 'application/json'}
        params = {'ipAddress': ip, 'maxAgeInDays': '90'}
        r = requests.get(url, headers=headers, params=params, timeout=5)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None