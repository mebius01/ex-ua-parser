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

#~ функция формирования title + 1,2,3,4...ГОТОВА.
List_for_title=[]
Xran=range(len(List_re)+1); Xran.pop(0)
def ForName():
	for r in Xran:
		r=str(r)
		
		List_for_title.append(r+' - '+Title_re)




#~ Функция загрузки flv для List_re ГОТОВА
def ForUrlWget(i):
	list_re=i.pop(0)
	#~ os.system('wget %s' %i) # разкоментить
	print list_re # закоментить


#~ список фалов, для сопостовления с List_re_dir
dir=os.listdir('.')

#~ Фун. переименования flv в 1 - titla.flv ГОТОВА
def RenaMe(x, y):
	""" x= List_re_dir, y = List_for_title """
	p_x=x.pop(0) 
	p_y=y.pop(0)
	os.rename(p_x, p_y)

RenaMe()

#~ Функция сопостовления List_re_dir с dir для rename ГОТОВА
def ForListDir():
	for i in List_re_dir:
		if i in dir:
			print "List_dir in path", i
			re_dir=dir.pop(0)
			os.rename(re_dir, Title_re)
		else:
			print "Not"

#~ Цикл вызовов == количесву элементов в списке загрузок ГОТОВ
#~ int=0
#~ while int <= len(List_re)+1:
	#~ ForUrlWget(List_re)
	#~ ForListDir()
#~ 







#~ --------------------------------------------


#~ e_str='test-name'
#~ 
#~ os.chdir("TTTT")
#~ a_str = os.listdir('.')
#~ 
#~ def RenaMe(x):
	#~ re_x=x.pop(0)
	#~ os.rename(re_x, e_str)
#~ 
#~ RenaMe(a_str)




