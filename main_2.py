from send import get_info
import time
import datetime
if __name__=='__main__':
	while True:
		now=datetime.datetime.now()
		if now.hour==8 and now.minute==0 and now.second==0:
			get_info()
		time.sleep(0.5)