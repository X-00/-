#coding=utf-8
import requests
import time
import pymysql
import configparser
CorpID='wwcba022e890bfbb93'
SecretID='iuM9QvfnXmz_UCmO_tsLxrNmoPgxLpuLNQlhIVQ6Xc4'     
URL_ACCESSTOKEN='https://qyapi.weixin.qq.com/cgi-bin/gettoken?'

#@param CorpID:企业ID
#@param SecretID:应用ID


def gettoken():	
	params={'corpid':CorpID,'corpsecret':SecretID}
	r_token=requests.get(URL_ACCESSTOKEN,params=params).json()
	#print(r_token)
	#print(type(r_token['access_token']))
	return r_token['access_token']
		
def write_token(token):
	#_sql='UPDATE token set access_token='+"'"+token+"'"
	#db=pymysql.connect('localhost','root','','token_db',port=3308)
	#cursor=db.cursor()
	#cursor.execute(_sql)
	#db.commit()
	#cursor.close()
	#print('添加TOKEN成功')
	#db.close()
	conf=configparser.ConfigParser()
	conf.read('Group.ini',encoding='utf-8')
	conf.set('TOKEN','Token',token)
	conf.write(open("Group.ini", "w",encoding='utf-8'))
def read_token():
	conf=configparser.ConfigParser()
	conf.read('Group.ini',encoding='utf-8')
	token=conf.get('TOKEN','Token')
	# _sql='select access_token from token'
	# db=pymysql.connect('localhost','root','','token_db',port=3308)
	# cursor=db.cursor()
	# cursor.execute(_sql)
	# data=cursor.fetchone()
	# print('读取token成功')
	# db.close()
	# return data[0]
	return token
if __name__=='__main__':
	expires=7200      #失效时间
	write_token(gettoken())
	t0=time.time()
	while True:
		t=time.time()
		if t-t0>expires:
			token=gettoken()
			write_token(token)
			t0=t
		else:
			continue
	
			
			
	
