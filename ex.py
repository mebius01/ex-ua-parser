#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A="[a-z:/[a-z./[0-9/[abcdef0-9]+.flv"
#B=re.compile(A)
#C=re.findall(
import urllib, urllib2, re, sys, os
html = 'http://www.ex.ua/21522453?r=23786'
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()
List_re=re.findall("[http://www.ex.ua/show/0-9abcdef0-9]+.flv", Read_html)

for i in List_re:
	#os.system('wget %s' %i)
	print i
#~ List_reII=re.findall("[\[A-D\] | 0-9].+mp4", Read_html)
#~ 
#~ for ii in List_reII:
	#~ print ii
