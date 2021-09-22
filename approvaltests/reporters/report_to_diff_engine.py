import socket
import json

from approvaltests import Reporter


class ReportToDiffEngineTray(Reporter):
    def report(self, received_path: str, approved_path: str) -> bool:
        payload = {
            "Type": "Move",
            "Temp": received_path,
            "Target": approved_path,
            "CanKill": False,
        }

        self.sendTcpSocket("localhost", 3492, json.dumps(payload))

    def sendTcpSocket(self, HOST, PORT, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, encoding="utf-8"))
        finally:
            sock.close()