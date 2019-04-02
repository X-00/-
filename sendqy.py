import requests
from get_token import read_token
from addCRM import main,make_chatroom,send_msg
import configparser
'''
转发客户聊天消息到企业微信
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
	url='http://chenk.hopto.org:8082/ckapi/api/1/select_message.jsp?token=chenksoft!@!'
	r_Client=requests.get(url).json()
	datas=r_Client['data']
	print(datas)
	dict={}
	for data in datas:
		name=data['skf5602']
		info=data['skf5596']+":"+data['skf5597']+" "
		if name in dict:
			dict[name]=dict[name]+info
		else:
			dict[name]=info
	#print(dict)
	for keys,value in dict.items():
		#print(keys)
		#print(value)
		main(keys,value)
