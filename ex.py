#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A="[a-z:/[a-z./[0-9/[abcdef0-9]+.flv"
#B=re.compile(A)
#C=re.findall(
import urllib, urllib2, re, sys, os
#~ 
html = 'http://www.ex.ua/73222171?r=23786,23775'; html=str(html)
#~ tit_le= raw_input('name title: '); tit_le=str(tit_le)
#~ 
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()
List_re=re.findall("http://www.ex.ua/show/0-9abcdef0-9+.flv", Read_html)
#~ 
#~ for i in List_re:
	#~ i=str(i)
	#~ print i
print List_re
