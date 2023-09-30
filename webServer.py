#import socket module
from socket import *
import sys

def webServer(port=13331):

   serverSocket = socket(AF_INET, SOCK_STREAM)
   #Prepare a server socket
   serverSocket.bind(('',port))
   serverSocket.listen(1)

   while True:

       #print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
       try:
           message = connectionSocket.recv(1024) #Fill in start -a client is sending you a message   #Fill in end
           filename = message.split()[1]
           #opens the client requested file.
           #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
           f = open(filename[1:]) #fill in start
           outputdata = f.read()
           f.close()

           #fill in end
           #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
           #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html

           connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())  # http OK message
           connectionSocket.send('\r\n'.encode())
           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())
           connectionSocket.send("\r\n".encode())
           connectionSocket.close()

       except IOError:
           # Send response message for invalid request due to the file not being found (404)
           

           connectionSocket.send('HTTP/1.1 404 not found \r\n'.encode())
           connectionSocket.close()

       except BrokenPipeError:
           break
           #Close client socket
   #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
   #serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(port=13331)
