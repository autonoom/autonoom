# File for communication protocol
import threading
import socket

TCP_IP = '0.0.0.0' #0.0.0.0 so the ip is accessible from the network
TCP_PORT = 5005 #Telnet port is 5005
BUFFER_SIZE = 20 #Telnet buffer size = 20 bytes

#Groot gedeelte van https://wiki.python.org/moin/TcpCommunication gehaald
class comProt(threading.Thread):
    class __comProt(threading.Thread):
        def __init__(self):
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket for telnet connection
            self.s.bind((TCP_IP, TCP_PORT))
            self.s.listen(1)
            threading.Thread.__init__(self)
            self.start() #Start the thread
            self.data = None

        def run(self):
            conn, addr = self.s.accept() #Accept the telnet connection if available
            print 'Connection address:', addr #Print it for debugging purposes
            while 1:
                self.data = None
                data = conn.recv(BUFFER_SIZE)   #Receive the data with a max buffer size of 20 bytes
                if data:                        #If there is any data on the bus
                    self.data = data            #Put it into self.data
                    conn.send(data)             #Send an echo for confirmation
                    if data == 'close': break
            conn.close()    #Close the connection

    # From https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    instance = None

    # Singleton implementation
    def __new__(cls):  # __new__ always a classmethod
        if not comProt.instance:
            comProt.instance = comProt.__comProt()
        return comProt.instance
