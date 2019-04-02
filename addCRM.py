#coding=utf-8
from get_token import read_token,gettoken
import requests
import json
import configparser
import time


def get_trace_customer_record():
	conf=configparser.ConfigParser()
	conf.read('Group.ini',encoding='utf-8')
	tc_code=conf.get('TraceCT','SKno')
	#tc_code=read_str_from_config('TraceCT','SKno')
	#print('tc_code',tc_code)
	if tc_code is None or tc_code=='':
		return
	try:
		url='https://demo.chenksoft.com:443/ckapi/api/1/v2/SK_documentary_select.jsp?token=chenksoft!@!&SKcode={0}'.format(tc_code)
		print(url)
		res=requests.get(url).json()
		#print(res)
		if res !=None and res['data']!=None and len(res['data']) > 0:
			tc_code=res['data'][0]['SKno']
			#print(tc_code)
			conf.set('TraceCT','SKno',tc_code)
			conf.write(open("Group.ini", "w",encoding='utf-8'))
			#print(res['data'])
			return res['data']
		else:
			#print('无跟单记录')
			return []
	except:
		print('异常')
		return []
	
		
		
		
'''
创建群聊
@chat_name：群聊名称
@token:
设定默认群主以及默认群聊成员
返回参数：chat_id
'''
def make_chatroom(chat_name,token):
	data={
		"name" : chat_name,
		"owner" :'btaileng',
		"userlist" :["btaileng",'CaoMeiDian','cleem@ChenKeRuanJian']
	}
	creaturl="https://qyapi.weixin.qq.com/cgi-bin/appchat/create?access_token={0}".format(token)
	r=requests.post(url=creaturl,data=json.dumps(data)).json()
	print(r)
	return r['chatid']
	

'''
发送消息
@chatid：群聊的唯一id
@info：要发送的消息，字符串
@token:

'''
def send_msg(chatid,info,token):
	contents = {
		"chatid": chatid,
		"msgtype":"text",
		"text":{
		"content" : info},
		"safe":0
	}
	sendurl="https://qyapi.weixin.qq.com/cgi-bin/appchat/send?access_token={0}".format(token)
	r=requests.post(url=sendurl,data=json.dumps(contents)).json()

'''
@name:要发送的人员
@info:发送的消息
'''
def main(name,info):
	conf=configparser.ConfigParser()
	conf.read('Group.ini',encoding='utf-8')
	value=conf.sections()
	token=read_token()
	CHATROOM_NAME=conf.sections()
	if name+'CRM' not in CHATROOM_NAME:
		chat_id=make_chatroom(name+'CRM',token)
		send_msg(chat_id,info,token)
		print(name+'CRM'+':'+info)
		conf.add_section(name+'CRM')
		conf.set(name+'CRM','chat_id',chat_id)
		conf.set(name+'CRM','NAME',name+'CRM')
		conf.write(open("Group.ini", "w",encoding='utf-8'))

	else:
		chat_id=conf.get(name+'CRM','chat_id')
		#conf.write(open("Group.ini", "w"))
		send_msg(chat_id,info,token)
		print(name+'CRM'+':'+info)

if __name__=='__main__':
	while True:
		traceCT=get_trace_customer_record()
		if traceCT!=[]:
			#print(traceCT)
			for item in traceCT:
				#print(item)
			#time.sleep(200)
				notifyMsg = '客户名称：%s\n跟单人员：%s\n跟单日期：%s\n跟单方式：%s\n跟单结果：%s' % (item['SKname'], item['SKempname'], item['SKdate'], item['SKtype'], item['SKresult'])
				#print(notifyMsg)
				#print(item['SKno'])
				namekey=item['SKempname2']
				if namekey=='任秀强1':
					namekey='任秀强'
				print(namekey)
				print(notifyMsg)
			# time.sleep(10)
				main(namekey,notifyMsg)
				time.sleep(20)
				
		else:
			print('暂无跟单')
			time.sleep(20)

			#main(namekey,'notifyMsg')
			