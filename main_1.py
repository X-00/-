from send import get_today_crm_statics, get_lastweek_crm_statics
import time
import datetime
if __name__=='__main__':
	while True:
		now=datetime.datetime.now()
		if now.hour==19 and now.minute==0 and now.second==0:
			get_today_crm_statics()
			get_lastweek_crm_statics()
		time.sleep(0.5)