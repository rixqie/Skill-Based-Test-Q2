import socket

def main():
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # connection to server on the port.
    s.connect(("127.0.0.1", 8888))                               

    print("Hello, this software is for converting temperature in Fahrenheit to Celcius!");

    #Input temperature
    temp_f = input("Please enter the temperature: ")
    s.send(temp_f.encode())
    
    #Output
    temp_c = s.recv(1024).decode()
    print("The temperature in Celcius is: ",temp_c)

main()