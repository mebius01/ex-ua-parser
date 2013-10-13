#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, re, sys, os

html = 'http://www.ex.ua/17040371?r=23786'

Url_html=urllib.urlopen(html)
Read_html=Url_html.read()
List_re=re.findall("[http://www.ex.ua/show/0-9abcdef0-9]+.flv", Read_html)


def ForUrlWget(i):
	list_re=i.pop(0)
	#~ os.system('wget %s' %i)
	print list_re

ForUrlWget(List_re)

e_str='test-name'

os.chdir("TTTT")
a_str = os.listdir('.')

def RenaMe(x):
	re_x=x.pop(0)
	os.rename(re_x, e_str)

RenaMe(a_str)




