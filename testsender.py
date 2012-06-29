#!/usr/bin/python
import socket, time, os, codecs
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_data(s, data):
	if data != "":
		d = data.encode('cp1251')
		s.sendto(d, (HOST, PORT))
		print "Sending data..."
		print d

data_path = os.path.join(os.path.realpath('./testdata'), 'errors.1251')
try:
	if os.path.exists(data_path):
		f = codecs.open(data_path, mode='r', encoding='cp1251')
		data = ""
		for line in f:
			if line[:5] == 'ERROR':
				send_data(s, data)
				time.sleep(2)
				data = ""
				parts = line.split()
				line = line.replace(" ".join(parts[1:3]), datetime.now().strftime("%Y-%m-%d %H:%M:%S,000") )
			data += line
		send_data(s, data)
	s.close()
except KeyboardInterrupt:
	s.close()
