#/usr/bin/python
# coding=utf-8

import requests
import json


def verifyreceipt(receipt, sandbox=False):
    headers = {"Content-type": "application/json"}
    post_url = sandbox and "sandbox.itunes.apple.com" or "buy.itunes.apple.com"
    receipt_data = json.dumps({"receipt-data": receipt})
    ret = requests.post("https://" + post_url + '/verifyReceipt', data=receipt_data, timeout=3, verify=False)
    if ret.status_code == 200:
        return ret.json()
    else:
        return False
