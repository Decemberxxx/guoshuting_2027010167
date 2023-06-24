import socket
import  json
from socket_server import *

HOST = '127.0.0.1'  # 服务端IP地址
Server_PORT  = 35000        # 服务端端口号
ENCODING = 'utf-8'  # 字符编码方式

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, Server_PORT))
        send_message = dict()

        msg = dict()
        msg["path"] = r"D:\精英班\机器学习\train\test\20230101092449_frame_27_00_00_01_080"
        msg["index"] = "0"

        send_message['type'] = 'classify'
        send_message['params'] = msg

        message = json.dumps(send_message, ensure_ascii=False)
        print("Send data: ",message)
        message = message.encode(ENCODING)
        s.sendall(message)
        data = s.recv(10240)
        data = data.decode(ENCODING)
    print('Received data: ', data)

