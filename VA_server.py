from socket import *
from threading import *
from main import query
from System import speak



class ChatThread(Thread):
	mute = False
	"""docstring for ChatThread"""
	def __init__(self, con):
		Thread.__init__(self)
		self.con = con

	def run(self):
		name = current_thread().getName()

		while True:

			if name=='sender':
				data = input('Enter your massage : ')
				self.con.send(bytes(data,'utf-8'))

			elif name=='receiver':
				recData = self.con.recv(1024).decode()
				print('command : ',recData)
				
				try:
					output = query(recData)
					speak(output)
				except Exception as e:
					print(e)
					print('sorry but an unexpected error occured :(')
		



host = input('Enter host IP: ')
server = socket(AF_INET,SOCK_STREAM)
server.bind((host, 1131))
print('binding the port :', 1131)
server.listen(4)
conn,add = server.accept()


sender = ChatThread(conn)
sender.setName('sender')


receiver = ChatThread(conn)
receiver.setName('receiver')


sender.start()
receiver.start()
