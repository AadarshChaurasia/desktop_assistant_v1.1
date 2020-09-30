
'''
			Functions :-
				open(argument)
				query(argument)
'''



from webbrowser import open_new_tab as open_website
import os
from getmac import get_mac_address


from Time import time_status as ts
from Time import get_current_time as current_time
from Time import timer
from System import speak
from search import finder

import Browser
import Time
import System
import extra_func
import Automating

def open(data):

	words = data.split(' ')
	new_query = ''
	# print(words)
	count = 0

	if '.com' in data or '.in' in data or '.org' in data:

		for word in words:
			if '.com' in word or '.in' in words or '.org' in words:		
				new_query = word		
				break
		open_website(new_query)
		


	elif 'software' in data or 'application' in data:

			length = len(words)
			# print(length)

			for i in range(length):
				# print(i)
				word = words[i]
				# print(word)

				if word=='software'  or word=='application':
					new_query = words[i-1]
					break

			Automating.start_software(new_query)



	else:

		new_query = data[5:]
		finder(new_query)

	return f'opening {new_query}'


def query(query):

# Time module
	new_query = ''
	if 'time' in query:

		if 'status' in query:
			status = ts()
			new_query = f'this is {status} time sir.'
			print(new_query)

		if  'current' in query:          # Printing current time which has been inherted by Time part/
			new_query = current_time()        # /of projet. example :- tell me current time or what is the current time
			print(new_query)


	if 'set' in query and 'timer' in query:

		data_array = query.split(' ')

		for data in data_array:

			try:

				float(data)
				time = data
				break

			except:
				continue

		# print(data)
		new_query = f'timer set for {data}'
		timer(data)



	if 'open' in query:

		new_query = open(query)


# Automating module

	if query == 'connect to wifi':

		new_query = Automating.wifi()


# Browser module

	if 'tell me about' in query or 'ke bare mai batao' in query:

		new_query = Browser.show_info_about(query)
		print(new_query)


	if 'google' in query:

		new_query = Browser.search_on_google(query)


# System module

	if 'shut down' in query or 'shutdown' in query:

		try:
			letters = query.split(' ')

			for letter in letters:

				try:
					int(letter)
					time = int(letter)
					print(time)
					System.shutdown(minutes=letter)

				except:
					pass

		except:
			System.shutdown()
		new_query = 'shutting down...'


	if 'restart' in query:

		try:
			letters = query.split(' ')

			for letter in letters:

				try:
					int(letter)
					time = int(letter)
					print(time)
					System.restart(minutes=letter)

				except:
					pass

		except:
			System.restart()
		new_query = 'restarting...'


	if 'minimize' in query:
		if 'all' in query:
			System.min_all()
		else:
			System.minimize()

	if 'close' in query:
		System.close()
		new_query = 'clossing current window'


	if 'change' in query and 'window' in query:
		System.change_working_window()


	if 'system' in query:
		if 'info' in query or 'information' in query or 'about' in query:
			System.info()


	if 'ip' in query:
		new_query = System.IP()
		print(new_query)


	if 'mac' in query and 'address' in query:                      # work only when connected to internet
		new_query = get_mac_address()
		print(new_query)


	if 'battery' in query and 'left' in query:
		new_query = System.bettery_left()
		print(new_query)


	if 'cpu' in query:
		if 'usage' in query or 'use' in query:
			new_query = System.cpu_usage()
			print(new_query)


	if 'restore' in query:
		if 'up' in query:
			System.maxsize()
		if 'down' in query:
			System.minisize()

	return new_query






	# if 'help' in query:
	# 	open('help_commands.txt','r') as f: 






if __name__ == '__main__':
	# status = ts()
	# speak(f'Good {status} sir. How can i help you.')
	# q = input('Enter: ')
	try:
		query('restore downward')
	except:
		print('sorry but an unexpected error occured :(')