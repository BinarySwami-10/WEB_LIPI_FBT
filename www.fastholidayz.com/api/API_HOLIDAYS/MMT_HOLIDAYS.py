
from mxproxy import mx
import requests
import json
url = 'https://holidayservice.makemytrip.com/HolidayServices/service/listing/packages/grouped'

data = {
    "accept": "application/json, text/plain, */*, application/json ; charset=utf-8",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8,pl;q=0.7",
    "content-encoding": "gzip",
    "content-type": "application/json ; charset=UTF-8",
    "correlation_id": "a98e130a-dd99-43b3-ba3a-0885e982eddd",
    "dvc_type": "DESKTOP",
    "dvid": "d78a882f-9aa6-4354-8222-2370a4ccb58f",
    "funnel_binding_key": "d5aa251eed26a18c420ffdd129ade619",
    "mcid": "55551169140182881631581548821943609194",
    "os": "Windows",
    "osver": "Windows 10",
    "request_id": "0c119f42-45d3-3563-0442-a5fc88e11465",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "session_mmt_id": "bd167f937a8bda8ec9b805deb793fb27",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
# print(mx.parse_raw_headers('./headers.raw'))
requests = requests.session()
# data = mx.jdumps(data, indent=0)
print(json.dumps(data))

print(requests.post(url, json=json.dumps(data),
                    headers=mx.parse_raw_headers('./headers.raw')).json())
