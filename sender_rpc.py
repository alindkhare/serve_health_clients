import requests
import json

def fire_remote_patient(url, req_params):
    payload = {
        "method": "fire_client",
        "params": req_params,
        "jsonrpc": "2.0",
        "id": 0
    }
    response = requests.post(url, json=payload).json()
    print("{}".format(response))

if __name__ == "__main__":
    url = "http://localhost:4000/jsonrpc"
    req_params = {"npatients":1, "serve_ip":"localhost", "serve_port":8000}
    fire_remote_patient(url, req_params)