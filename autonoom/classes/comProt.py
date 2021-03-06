# File for communication protocol
import threading
import socket

#Groot gedeelte van https://wiki.python.org/moin/TcpCommunication gehaald
class comProt(threading.Thread):
    def __init__(self, tcp_port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket for telnet connection
        self.tcp_port = tcp_port
        self.s.bind(('0.0.0.0', self.tcp_port))
        self.s.listen(1)
        threading.Thread.__init__(self)
        self.start() #Start the thread
        self.data = None
	
    def getData(self):
	return self.data
    
    def run(self):
        while 1:
            conn, addr = self.s.accept() #Accept the telnet connection if available
            print 'Connection address:', addr #Print it for debugging purposes
            while 1:
                try:
                    data = conn.recv(20)   #Receive the data with a max buffer size of 20 bytes
                    if data:                        #If there is any data on the bus
                        self.data = data            #Put it into self.data
                        conn.send(data)             #Send an echo for confirmation
                        if data == 'close': break #If the data == close. Close the connection
                except socket.error:
                    print("Socket disconnect error!")
            conn.close()    #Close the connection
