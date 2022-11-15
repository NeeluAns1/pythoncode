import socket
s = socket.socket()
print("Socket successfully created")
port = 40674
s.bind(('',port))
print("socket is binded to %s" %(port))
s.listen(5) #put the socket into listening mode
print("socket is listening")
while True:  #a forever loop until we interrupt it or an error ocuurs
   c,addr = s.accept() #establish connection with client
   
   print('Got connection from',addr) #sent thankypu message to the client
   
   c.send(b'Thank you for connection')
   
   c.close()                            #close the connection with the client
   
     