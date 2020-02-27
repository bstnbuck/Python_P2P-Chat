import socket
import sys
import time
import threading
import secrets
from hashlib import sha512
from colorama import Fore, Style, init

class Server(threading.Thread):                                             #class Server
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)          #initialise tcp socket
        #print("Server started!")                                           #DEBUG
        hostname=''                                                         #initialise hostname variable
        port=8080                                                           #port
        self.sock.bind((hostname,port))                                     #bind socket to the hostname with port
        self.sock.listen(1)                                                 #listen on binded socket
        print ("Listening on port: ",port)                                  #DEBUG
        #time.sleep(1)                                                       #for better performance sleep 1 sec
        (clientname,address)=self.sock.accept()                             #if request make connection with partner
        print ("Connection from: "+str(address)+"\n")                           #DEBUG
        while 1:                                                            #endless while
            if Client.countMe:                                              #if countMe variable in class Client not null
                recieve=clientname.recv(4096)                               #recieve tcp packet from socket
                print(Fore.YELLOW)                                          #after that, all text is yellow
                print ("[COINFLIP] Got Random: "+str(recieve.decode("utf-8"))+" from: "+str(address)) #DEBUG
                binaryOther = bin(int(recieve.decode("utf-8"), 16))[2:]     #make recieved hash to binary string
                #print(binaryOther)                                         #DEBUG
                countOther = binaryOther.count('1')                         #count setted bits
                print("[COINFLIP] countOther: "+str(countOther))            #DEBUG

                print("[COINFLIP] Making CoinFlip... Just wait a second:D ") #DEBUG
                #time.sleep(0.5)                                               #for better performance wait 0,5 sec
                if Client.countMe%2 == 0 and countOther%2 == 0:             #if countMe and countOther are even -> HEAD!
                    print("[COINFLIP] CoinFlip is:\tHEADS!")                 #print it!
                elif Client.countMe%2 == 1 and countOther%2 == 1:           #if both odd -> HEAD!
                    print("[COINFLIP] CoinFlip is:\tHEADS!")                 #print it!
                else:                                                       #if countMe=even, countOther=odd -> TAIL!; countMe=odd, countOther=even -> TAIL!
                    print("[COINFLIP] CoinFlip is:\tTAILS!")                 #print it!
                Client.countMe = 0                                          #countMe to 0
                print(Style.RESET_ALL)                                      #text is now again white
            elif Client.chat == True:                                       #if chat variable is True
                message = clientname.recv(4096)                             #recieve message from socket
                print("\nGot message from: "+str(address)+": "+str(message.decode("utf-8")))  #print message to user
                Client.chat = False                                         #make chat to False


class Client(threading.Thread):                                             #class Client 
    countMe = 0                                                             #initialise countMe with 0
    chat = False                                                            #initialise chat with False
    def connect(self,host,port):                                            
        self.sock.connect((host,port))                                      #connect to the given hostname and port of partner
    def client(self,host,port,msg):               
        self.sock.send(bytes(msg.encode("utf-8")))                          #send message encoded with "utf-8" as bytes to partner
        print("Message sent!")                                              #DEBUG
    def run(self):  
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)          #initialise TCP Socket
        try:
            host=input("Enter hostname\n>>")                                #enter hostname of partner
            port=int(input("Enter port\n>>"))                               #enter port of partner
        except:
            print(Fore.RED)                                                 #if failed, color now red
            print ("Error")                                                 #DEBUG
            input("Press any Key to continue")                              #EXIT by clicking any key
            print(Style.RESET_ALL)                                          #reset Styles
            return 1        
        
        #print ("Connecting...")                                            #DEBUG
        self.connect(host,port)                                             #connect to partner
        #print ("Connected")                                                #DEBUG
        print ("Now you can Chat with your friend! Let the Coin flipping with: >>coinflip<<. If you want to close program and the connection type in >>exit<<") #welcome message
        while 1:                                                            #endless while
            try:                                                            
                print ("Send message; make a CoinFlip >>coinflip<<. Close program and the connection >>exit<<") #send codewords you can use
                msg=input('>>')                                             #make a user input 
                if msg=='exit':                                             #if message like 'exit'
                    break                                                   #close program
                elif msg == 'coinflip':                                     #if like 'coinflip
                    try: 
                        randomstring = secrets.token_urlsafe(20)            #make a very secure random String of 20 character
                        print(Fore.YELLOW)                                  #text is now yellow
                        print("[COINFLIP] Generated random String is: "+str(randomstring))  #DEBUG
                        hasht = sha512((str(randomstring)).encode()).hexdigest()    #make sha512 hash from generated string
                        print("[COINFLIP] Generated hash is: "+hasht)       #DEBUG
                    
                        binaryMe = bin(int(hasht, 16))[2:]                  #make hash to binary string
                        Client.countMe = binaryMe.count('1')                #count setted bits
                        print("[COINFLIP] countMe: "+str(Client.countMe))   #DEBUG
                        print(Style.RESET_ALL)                              #text is again white
                        self.client(host,port,hasht)                        #send hash to partner
                    except:
                        print(Fore.RED)                                     #if something failed, exception red
                        print("[COINFLIP] Error generating random Hash")    #DEBUG
                        print(Style.RESET_ALL)                              #reset red text
                        continue                                            
                elif msg =='':                                              #if user entered nothing, continue
                    continue
                else:
                    #print("Sending...")                                    #else -> it is a message to the partner
                    self.client(host,port,msg)                              #send message to partner
                    Client.chat = True                                      #chat variable true
                time.sleep(0.25)
            except:
                print(Fore.RED)                                             #if something failed, exception red
                print("Error!")                                             #DEBUG
                print(Style.RESET_ALL)                                      #reset color
                continue
        return(1)


if __name__=='__main__':
    init()
    print("Welcome to P2P-Chat")                                            #Welcome!
    server=Server()                                                         #initialize server variable
    server.daemon=True                                                      #server process to background
    #print ("Starting server")                          
    server.start()                                                          #let the server start
    time.sleep(1)                                                           #for better performance sleep 1 sec
    #print ("Starting client")
    client=Client()                                                         #initialize client variable
    #print ("Started Client!")
    client.start()                                                          #let the client start