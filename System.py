from Automating import Keyboard

from os import system
import winsound
import socket
from getmac import get_mac_address
# from win10toast import ToastNotifier
import pyttsx3
import psutil

k = Keyboard()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 120)


def speak(audio):                                                     # done
	engine.say(audio)
	engine.runAndWait()


def close():
	k.multi_press(['alt', 'f4'])


def minisize():                                                       # done
	k.multi_press(['win', 'down'])


def minimize():                                                       #done
	k.multi_press(['win', 'down'])
	k.multi_press(['win', 'down'])


def maxsize():                                                         # done
	k.multi_press(['win', 'up'])


def shutdown(minutes=0):                                                 # done
	system(f"shutdown /s /t {minutes * 60}")


def restart(minutes=0):                                                  # done
	system(f"shutdown /r /t {minutes * 60}")


def min_all():                                                           # done
	k.multi_press(['win', 'd'])


def change_working_window():                                            # done
	k.multi_press(['alt', 'tab'])


def info():                                                               # done
	system("systeminfo")


def beep():
	winsound.Beep(2500,500)


def IP():                                                                  # done
	socket.gethostbyname(socket.gethostname())
	

def mac_address():                                                         # done
	return get_mac_address()


def cmd(command):
	system(f'cmd /k {command}')


def notify(title,content,duration=20):
	toast = ToastNotifier()
	toast.show_toast(title, content, duration=duration)

def cpu_usage():                                                            # done
	usage = str(psutil.cpu_percent())
	return usage


def bettery_left():                                                         # done
	usage = str(psutil.sensors_battery())
	waste,percentage,time_left,pluged = usage.split('=')
	percentage,w2 = percentage.split(',')
	time_left,w2 = time_left.split(',')
	pluged = pluged[0].lower()
	if pluged == 't':
		pluged = 'device is connected to power source'
	else:
		pluged = 'device is not connected to any power source'

	return percentage+'% battery left'+', '+time_left+'second battery life is left'+' and '+pluged

if __name__ == '__main__':
	speak('i have no problem check somewhere else !')