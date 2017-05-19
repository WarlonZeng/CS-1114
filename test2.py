#Warlon Zeng

from socket import *

import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

def main():
    serverPort=9999
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print 'the web server is up on port:',serverPort
    while True:
        print 'Ready to serve...'
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            print message,'::', message.split()[0],':',message.split()[1]
            filename = message.split()[1]
            print filename,'11',filename[1:]
            f = open(filename[1:])
            outputdata = f.read()
            print outputdata 
            connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
            connectionSocket.send(outputdata)
            connectionSocket.close()

        except I0Error:
            pass
        # TEMP BREAK
        break
    pass

if __name__ == '__main__':
    main()
