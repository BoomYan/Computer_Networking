from socket import *
from datetime import datetime 


serverName = '127.0.0.1'  
serverPort = 12000 
counter = 0;
message = "i love to study computer networking"        
while counter < 10:
    counter = counter +1     
    mainSocket = socket(AF_INET,SOCK_DGRAM)       

    try:
        mainSocket.settimeout(1.0) 
        startTime = datetime.now() 
        mainSocket.sendto(message,(serverName, serverPort))
        modifiedMessage, serverAddress = mainSocket.recvfrom(1024) 
        endTime = datetime.now() 

    except timeout:  
        print 'PING ' +str(counter)+' '+ str(startTime)+ ': Request timed out!' 
        mainSocket.close() 
    else:  
        print 'PING ' +str(counter)+' '+ str(startTime)+': Returned: ' + modifiedMessage + ' RTT:'+ str(endTime-startTime)

mainSocket.close()           