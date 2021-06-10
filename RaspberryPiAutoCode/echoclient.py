import socket
import runpy
#'54.206.202.192'
#'54.253.175.63'
#'54.206.231.79'
#'10.118.0.79'
#'10.118.0.168' 
#dronewebpage.netlify.app
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.118.0.79', 65432))
filename = '/home/ai-drone/Desktop/AAA.waypoints'

data = " "
message = 'test'
while True:
    s.sendall(bytes(message.encode('utf-8')))
    m = s.recv(1024)
    if m:
        while m:
            data = s.recv(1024)
            print(repr(data))
            E = data.decode()
            print(E)
            with open(filename, 'w') as file1:
                file1.write(E)
            runpy.run_path(path_name='clicks/clicks.py')
            print('complete')
        else:

            break

