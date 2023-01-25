import socket

# function(convert fahrenheit to celsius)
def f2c(temp_f):
    temp_c = (temp_f - 32) * (5/9)
    return temp_c

def main():
  
    ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    ssocket.bind(("127.0.0.1", 8888))                                  
    ssocket.listen(1)

    print("Server is ready...")
    print("Pending for respond...")

    while True:
        # establish a connection
        csocket, address = ssocket.accept()      
        print("Got a connection from %s" % str(address))

        temp_f = csocket.recv(1024).decode()
        temp_c = f2c(float(temp_f))
        temp_c = round(temp_c,2)
        temp_c = str(temp_c)
        csocket.send(temp_c.encode())

#execute main function
main()