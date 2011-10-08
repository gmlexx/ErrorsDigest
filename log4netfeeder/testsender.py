import socket, time, os, codecs

HOST = '127.0.0.1'
PORT = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_data(s, data):
    if data != "":
        s.sendto(data, (HOST, PORT))
        print data

data_path = os.path.join(os.path.realpath('./testdata'), 'errors')
try:
    if os.path.exists(data_path):
        f = codecs.open(data_path, mode='r', encoding='utf-8')
        data = ""
        for line in f:
            if line[:5] == 'ERROR':
                send_data(s, data)
                time.sleep(2)
                data = ""
            data += line
        send_data(s, data)
    s.close()
except KeyboardInterrupt:
    s.close()
