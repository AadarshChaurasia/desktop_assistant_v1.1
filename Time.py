import datetime
import time


def time_status():                                               # done

	hour = int(datetime.datetime.now().hour)
	# print(hour)
	if hour >= 0 and hour<12:
		tme = 'Morning'

	elif hour >= 12 and hour<18:
		tme = 'afternoon'

	else:
		tme = 'evening'

	return tme


# done
def timer(count):

	count = int(count)
	print('Satarted 😊')

	while count>=0:
		# print(count)
		time.sleep(1)
		count = count-1

	print('Timer is over now !')
		

	# for x in range(0,count+1):
	# 	print(x)
	# 	time.sleep(1)

# done
def get_current_time():

	wkt = datetime.datetime.now()
	current_time = wkt.strftime('%H,%M minutes and %S seconds')

	hh,rest = current_time.split(',')
	status = 'AM'

	if int(hh) > 12:
		hh = int(hh)-12
		status = 'PM'

	current_time = str(hh)+' '+status+' '+rest

	return current_time




if __name__ == '__main__':
	# count = time_status()
	# print(f"Good {time}.")
	# timer(12)
	# print(reminder())
	# set_reminder(set_date='2020-06-30',set_time='22:02:20',task='test')
	time=get_current_time()
	print(time)
	# with Listener(on_press=stopwatch) as l:

	# 	l.join()






