import socket
import os
import random

#function of system
def clear():
    os.system('cls')

clear()

#name server  
name=input("enter your name : ")
clear()

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',1000))
server.listen(5)
client,address=server.accept()

#send name to cilent
client.sendall(name.encode('utf-8'))
#get name from client
cName=client.recv(123456).decode('utf-8')
print(cName,"  from ",str(address), 'connected !')

##########################################
startMessage=client.recv(123456).decode('utf-8')
print(startMessage)
awnser=input("enter your awnser by Y/N:  ")


##############################################
if awnser=="y" or awnser =="Y":

    try:
        while True:
    
            fmessage1="-"
            fmessage2="-"
            

            client.sendall(fmessage1.encode('utf-8'))

            #recive number from client
            number=client.recv(123456).decode("utf-8")
            m1='whay {}'.format(number)
            print(m1)
            aw=input("else --> if you accept number push key (Y)")
            if aw=="y" or aw=="y":
                 clear()
                 server.close()

            else:
                m2='so how many?'
                client.sendall(m2.encode('utf-8'))

            print(client.recv(123456).decode("utf-8"))
            
            #create random number
            number=random.randint(0,100)
            print("server select number : {}".format(number))
            client.sendall(str(number).encode("utf-8"))

            print(client.recv(123456).decode('utf-8'))

            client.sendall(fmessage1.encode('utf-8'))



    except :
    
        clear()
        server.close()
elif awnser=="N" or awnser=="n":
    clear()
    server.close()
