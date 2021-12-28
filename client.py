import socket
import os
import random 

def clear():
    os.system('cls')
 
#host=socket.gethostbyname(socket.gethostname())
my_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clear()
name=input("enter your name : ")
clear() 

my_client.connect(('127.0.0.1',1000))

#get name from server 
sName=my_client.recv(123456).decode('utf-8')
print(sName,'  connected!  ')
#send name to server
my_client.sendall(name.encode('utf-8'))
################################################
startMessage="Are you ready?"
my_client.sendall(startMessage.encode('utf-8'))


try:
    # while True:
    #     sMessage=my_client.recv(123456)
    #     print(sMessage.decode("utf-8"))

    #     Message=input("enter your Message : ")
    #     my_client.sendall(Message.encode('utf-8'))

   
    while True:
         #message fake
        fmessage1="<--"
        fmessage2="-->"

        fmessage=my_client.recv(123456).decode("utf-8")
        print(fmessage)
        
        #create random number
        number=random.randint(0,100)
        print(number)
        my_client.sendall(str(number).encode("utf-8"))
        #recive meesage from  server
        m2=my_client.recv(123456).decode('utf-8')
        print(m2)
        #send facke mseeage to server
        my_client.sendall(fmessage2.encode("utf-8"))

        #print why number
        num=my_client.recv(123456).decode('utf-8')
        print('why {}'.format(num))
        aw=input(" if you ok push key (Y)")
        if aw=="y" or aw=="y":
                 clear()
                 server.close()

            
        else:
            #send how many meeage to server
            shm="so how many?"
            my_client.sendall(shm.encode('utf-8'))

        print(my_client.recv(123456).decode('utf-8'))

        # #create number
        # number=random.randint(0,100)
        # print(number)
        # my_client.sendall(str(number).encode("utf-8"))

        # m2=my_client.recv(123456).decode('utf-8')
        # print(m2)













except:
    clear()
    my_client.close()


def createNumber():
    number=random.randint(0,100)
    my_client.sendall(str(number).encode("utf-8"))
