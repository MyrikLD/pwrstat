import uvicorn as uvicorn
from fastapi import FastAPI
import os
import subprocess
import re
import socket

app = FastAPI()
bool_values = {'no': False, 'yes': True}

@app.get("/")
def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect("/var/pwrstatd.ipc")
    sock.send(b"STATUS\n\n")
    text = sock.recv(2048).decode()

    data = {}
    for i in text.strip().split("\n")[1:]:
        k, v = i.split("=")

        if v.isdigit():
            val = int(v)
        elif v in bool_values:
            val = bool_values[v]
        else:
            val = v

        data[k] = val

    return data


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=False,
    )
