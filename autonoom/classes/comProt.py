# File for communication protocol
import threading
import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 20


class comProt(threading.Thread):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((TCP_IP, TCP_PORT))
        self.s.listen(1)
        threading.Thread.__init__(self)
        self.start()
        self.data = ''

    def run(self):
        conn, addr = self.s.accept()
        print 'Connection address:', addr
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if data:
                self.data = data
                conn.send(data)  # echo
                if data == 'close': break
        conn.close()
