import socket
import re

host = input('Enter host name: ')
port = int(input('Enter port number: '))
cmd = 'GET / HTTP/1.0\r\n\r\n'.encode()
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, port))
except:
    print('Cannot connect')

print('Connected')

try:
    mysock.send(cmd)
except:
    print('Cannot send data')

print('Data sent')

with open('data_stream.txt', 'w') as fhandle:
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        fhandle.write(data.decode())

mysock.close()

with open('data_stream.txt', 'r') as fhandle:
    for line in fhandle:
        line = line.rstrip()
        
        match1 = re.match(r'Last-Modified: ([\w,: ]+)', line)
        if match1:
            last_modified = match1.group(1)
            print(last_modified)
        
        match2 = re.match(r'ETag: ([\w"-]+)', line)
        if match2:
            etag = match2.group(1)
            print(etag)

        match3 = re.match(r'Content-Length: (\d{1,})', line)
        if match3:
            content_length = match3.group(1)
            print(content_length)
