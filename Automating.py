import pyautogui as pg
from os import startfile
from os import getcwd
from subprocess import Popen
import time
class Keyboard():
	"""docstring for Keyboard
	   have functions related to keyboard automation """
	def __init__(self):
		super(Keyboard, self).__init__()


	# @staticmethod
	def speech_to_text(self,audio,name):
		''' save input ina text file in same directory '''
		name = name+'.txt'
		with open(name,'a') as f:
			f.write(audio)

		# path = os.getcwd()
		# path = path+"\\"+name
		startfile(getcwd()+'\\'+name)
		# Popen([name])

		pg.typewrite(audio)
	def write(self,data):
		pass

	@staticmethod
	def press(key):
		pg.typewrite(key)

	def multi_press(self,keys):
		''' press multiple keys at the same time '''
		try:
			pg.hotkey(keys[0],keys[1],keys[2])
		except:
			pg.hotkey(keys[0],keys[1])

def start_software(software):                                        # Done
	''' start any software (by search automation) '''
	pg.click(109,748)
	time.sleep(6)
	pg.write(software)
	time.sleep(3)
	pg.click(476,414)



def wifi():                                                          # Done
	''' Connect or disconnect wifi '''
	pg.click(1174, 749)
	print('clicked')
	time.sleep(6)
	pg.click(1115, 267)
	time.sleep(4)
	pg.click(1277, 361)
	print('connecting....')
	return 'connecting....'

		

		
if __name__ == '__main__':
	# keyboard = Keyboard()
	# keyboard.speech_to_text('csdj','try')
	wifi()
