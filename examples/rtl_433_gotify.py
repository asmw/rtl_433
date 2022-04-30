#!/usr/bin/env python3

"""
Push messages via gotify example

rtl_433 ... -F json | examples/rtl_433_gotify.py
"""

import requests
import sys
import fire
import json
from datetime import datetime

def main(host, token, protocol='https', port=443, priority=8, models=[], debounce_secs=15):
    print(f"Running, host: {host}:{port}, model filter: {models}")

    last_ts = datetime.now()

    for line in sys.stdin:
        print(f"Parsing: {line}")
        current_ts = datetime.now()
        delta = current_ts - last_ts
        if delta.seconds < debounce_secs:
            continue

        last_ts = current_ts

        try:
            data = json.loads(line)
            if data["model"] not in models:
                continue

            try:
                req = requests.post(f'{protocol}://{host}:{port}/message?token={token}', json={
                    "message": data["time"],
                    "priority": priority,
                    "title": data["model"]
                })
                print(req)
            except Exception as e:
                print(f"Request failed: {e}")
        except json.decoder.JSONDecodeError as e:
            print("Parse error: %s" % e.msg)
            continue
    

if __name__ == '__main__':
  fire.Fire(main)
