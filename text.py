import requests
import json
from datetime import datetime

webhook_url = "https://flow.zoho.com/886846795/flow/webhook/incoming?zapikey=1001.a155e174ee504cc1062405e2f9288592.fcd9d6cb84d59e610895da5144f2fc65&isdebug=false"

payload = {
    "systolic": 120,
    "diastolic": 80,
    "pulse": 72,
    "category": "Normal",
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "readableDate": datetime.now().strftime("%m/%d/%Y %I:%M %p"),
    "person": "Friend",
    "source": "bp_tracker_v1"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
