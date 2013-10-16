#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2, re, sys, os
html = 'http://www.ex.ua/73353094?r=23786,23775'
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()

#~ Парсим
List_re=re.findall("[http://www.ex.ua/show/0-9abcdef0-9]+.flv", Read_html) # Парсим url для flv
List_re_dir=re.findall("[0-9a-z]+.flv", Read_html) #шаблон имен файлов 
Title_re=re.search('(?<=<title>).*?(?=\/)', Read_html).group()

def ForUrlWget(i):
	""" i == List_re - list из прямых урлов
	Удаляем первый элемент из списка с урлами flv
	Загружаем этот элемент с помощью wget"""
	for r in i:
		os.system('wget %s' %r) # разкоментить
		
ForUrlWget(List_re)
