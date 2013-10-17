#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2, re, sys, os
html = raw_input('input url ex.ua :'); html=str(html)
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()

#~ Парсим
List_re=re.findall("[http://www.ex.ua/show/0-9abcdef0-9]+.flv", Read_html) # Парсим url для flv
List_re_dir=re.findall("[0-9a-z]+.flv", Read_html) #шаблон имен файлов 
Title_re=re.search('(?<=<title>).*?(?=\/)', Read_html).group()

os.mkdir(Title_re)
os.chdir(Title_re)

list_title=[]
def ForTitle():
	ran=range(len(List_re)+1); ran.pop(0)
	for i in ran:
		i=str(i)
		list_title.append(i+'-'+Title_re)
	return list_title

def PopListTitle(lis):
	if len(lis) >=0:
		d=lis.pop(0)
		print d
	elif len(lis) ==0:
		print 'list пуст!!!!!!'

ForTitle() # Обязательно вызвать

def FunWget(who):
	var_who=who.pop(0)
	os.system('wget %s' %var_who)

def RenaMe(x, y):
	p_x=x.pop(0) 
	p_y=y.pop(0)
	os.rename(p_x, p_y)

int=0
while int != len(List_re):
	FunWget(List_re)
	RenaMe(List_re_dir, list_title)
	int+1

