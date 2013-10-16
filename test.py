#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, re, sys, os

html = 'http://www.ex.ua/17040371?r=23786'
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()

#~ Парсим
List_re=re.findall("[http://www.ex.ua/show/0-9abcdef0-9]+.flv", Read_html) # Парсим url для flv
List_re_dir=re.findall("[0-9a-z]+.flv", Read_html) #шаблон имен файлов 
Title_re=re.search('(?<=<title>).*?(?=\/)', Read_html).group()

#~ os.mkdir(Title_re)
os.chdir(Title_re)
#~ список фалов, для сопостовления с List_re_dir
dir=os.listdir('.')


#~ функция формирования title + 1,2,3,4...ГОТОВА.
List_for_title=[]
Xran=range(len(List_re)+1); Xran.pop(0)
def ForName():
	""" renge из элементов в списке с flv файлами - List_re
	Формируем список с будущеми именами окончательных файлов"""
	for r in Xran:
		r=str(r)
		
		List_for_title.append(r+' - '+Title_re)
ForName()



#~ Функция загрузки flv для List_re ГОТОВА
def ForUrlWget(i):
	""" i == List_re - list из прямых урлов
	Удаляем первый элемент из списка с урлами flv
	Загружаем этот элемент с помощью wget"""
	list_re=i.pop(0)
	os.system('wget %s' %list_re) # разкоментить
	#print list_re # закоментить

#~ Фун. переименования flv в 1 - titla.flv ГОТОВА
def RenaMe(x, y):
	""" x= List_re_dir - list flv файлов 
	y = List_for_title - list 'правельных' имен
	Загруженную flv переименовываем на первый элемент взятый из
	списка List_for_title"""
	p_x=x.pop(0) 
	p_y=y.pop(0)
	os.rename(p_x, p_y)


#~ Функция сопостовления List_re_dir с dir для rename ГОТОВА
def ForListDir():
	for i in List_re_dir:
		if i in dir:
			print "List_dir in path", i
			RenaMe(List_re_dir, List_for_title)
		else:
			print 'No flv!++++++++++++++++++++++++++++++!'



#~ Цикл вызовов == количесву элементов в списке загрузок ГОТОВ
int=0
while int <= len(List_re)+1:
	#~ ForUrlWget(List_re)
	ForListDir()




