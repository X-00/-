import requests
import datetime

def getToday(): 
    today=datetime.date.today() 
    return today
 
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday
 
def getLastWeekday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=7) 
    yesterday=today-oneday  
    return yesterday

def get_customer_reminder():
	url = 'https://demo.chenksoft.com:443/ckapi/api/1/v2/select_customer_reminder.jsp?token=chenksoft!@!'
	#res = urllib.request.urlopen(url)
	#retJson = json.load(res)
	#print(retJson)
	res=requests.get(url).json()
   
	dict_reminder = {}
	if res['code'] == 0:
		for item in res['data']:
			#print(item)
			if item['skt60.skf5832'] != '超过一个月未联系' or 1:
				print(item)
				namekey = item['tblemployee.name']
				if namekey == '任秀强1':
					namekey = '任秀强'
				notifyMsg = '下列客户%s，请及时跟进并录入跟单，否则将于%s转入公海客户池：\n%s' % (item['skt60.skf5832'], item['skt60.skf5834'], item['group_concat'])
		
				print(namekey)
				print(notifyMsg)
				main(namekey,notifyMsg)
	else:
		print('暂无消息')
		
		
def get_lastweek_crm_statics():
	URL_CRM='https://demo.chenksoft.com:443/ckapi/api/1/v2/SK_search_documentary.jsp'
	params_crm={'token':'chenksoft!@!','startDate':getLastWeekday(), 'endDate':getToday()}
	r_crm=requests.get(URL_CRM,params=params_crm).json()
	strStatics = '最近一周跟单统计：\n'
	for item in r_crm['data']:
		strStatics = strStatics + item['employeeName'] + ' ' + str(item['num']) + '\n'
	print(strStatics)
	return strStatics
	
def get_today_crm_statics():
	URL_CRM='https://demo.chenksoft.com:443/ckapi/api/1/v2/SK_search_documentary.jsp'
	params_crm={'token':'chenksoft!@!','startDate':getToday(), 'endDate':getToday()}
	r_crm=requests.get(URL_CRM,params=params_crm).json()
	strStatics = '今日跟单统计：\n'
	for item in r_crm['data']:
		strStatics = strStatics + item['employeeName'] + ' ' + str(item['num']) + '\n'
	print(strStatics)
	return strStatics
	
def get_yesterday_crm_statics():
	URL_CRM='https://demo.chenksoft.com:443/ckapi/api/1/v2/SK_search_documentary.jsp'
	params_crm={'token':'chenksoft!@!','startDate':getYesterday(), 'endDate':getYesterday()}
	r_crm=requests.get(URL_CRM,params=params_crm).json()
	strStatics = '昨日跟单统计：\n'
	for item in r_crm['data']:
		strStatics = strStatics + item['employeeName'] + ' ' + str(item['num']) + '\n'
	print(strStatics)
	return strStatics 
	
def get_info():
	URL_XS='http://chenk.hopto.org:8082/ckapi/api/1/getxsinfo_ex1_copy.jsp?token=&id=20000'
	URL_CRM='https://demo.chenksoft.com:443/ckapi/api/1/v2/SK_search_customerId.jsp?'
	URL_FLAG='http://chenk.hopto.org:8082/ckapi/api/1/update_info_searchflag.jsp?'
	list_info=[]
	r_xs=requests.get(URL_XS).json()
	dict_1={}
	dict_2={}
	dict_info={}
	list_data=r_xs['data']
	for data in list_data:
		dict_1[data['skf1697']]=data['skf1691']
		dict_2[data['skf1697']]=data['name']
	for item_1 in dict_1.items():
		if item_1[1]=='':
			print(str(item_1[0])+'未录入电话号码')
		
			if '无号码' in dict_info:
				dict_info['无号码'] = dict_info['无号码'] + ',' + str(item_1[0])
			else:
				dict_info['无号码'] = str(item_1[0])
		else:
			params_crm={'token':'chenksoft!@!','phoneNumber':item_1[1]}
			r_crm=requests.get(URL_CRM,params=params_crm).json()
			KH=r_crm['data']
			if len(KH)==0:			
				#print(str(dict_2[item_1[0]])+':'+str(item_1[0]))
				if item_1[0] is not None and dict_2[item_1[0]] is not None:
					info=(dict_2[item_1[0]])+':'+str(item_1[0])
					list_info.append(info)
				else:
					params_flag={"skt156.skf5585":'1',"skt156.skf1697":item_1[0]}
					r_flag=requests.get(URL_FLAG,params=params_flag).json()
					#pass
	list1=[]
	list2=[]
	for i in range(len(list_info)):
		# #print(list_info[i].split(':',1)[0])
		# #print(list_info[i].split(':',1)[1])
		list1.append(list_info[i].split(':',1)[0])
		list2.append(list_info[i].split(':',1)[1])
	# dict_info={}
	for i in range(0,len(list1)):
		if list1[i] in dict_info:
			dict_info[list1[i]]=dict_info[list1[i]]+list2[i]+'，'
		else:
			dict_info[list1[i]]=list2[i]+'，'
			
	print(dict_info)
	return dict_info
		


			
			
if __name__=='__main__':
	#get_customer_reminder()
	#get_lastweek_crm_statics()
	#get_info()
	#get_today_crm_statics()
	#get_yesterday_crm_statics()