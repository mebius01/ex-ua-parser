#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, re, os
html = raw_input('input url ex.ua :'); html=str(html)
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()

#~ Парсим
List_re=re.findall("[http://www.ex.ua/show/0-9abcdef0-9]+.flv", Read_html)
List_re_dir=re.findall("[0-9a-z]+.flv", Read_html) 
Title_re=re.search('(?<=<title>).*?(?=\/)', Read_html).group()
image=re.search('(?<="cover": ").*(?=\/)', Read_html).group()
#~ Создать директорию. Перейти в директорию
os.mkdir(Title_re)
os.chdir(Title_re)
#~ Формируем 'читабельное +.flv' имя файла и добавляем в список 
list_title=[]
def ForTitle():
	ran=range(len(List_re)+1); ran.pop(0)
	for i in ran:
		i=str(i)
		list_title.append(i+'-'+Title_re+'.flv')
	return list_title

ForTitle() # обязательно вызвать!!!
#~ - первый элемент из списка с url. Скачиваем
def FunWget(who):
	var_who=who.pop(0)
	os.system('wget %s' %var_who)
#~ элемент из списка с hash-name rename в читабельное +.flv
def RenaMe(x, y):
	p_x=x.pop(0) 
	p_y=y.pop(0)
	os.rename(p_x, p_y)
#~ Скачиваем, rename в цикле 
int=0
while int != len(List_re):
	FunWget(List_re)
	RenaMe(List_re_dir, list_title)
	int+1
os.system('wget %s' %image)
