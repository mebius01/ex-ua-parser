#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, re, sys, os
html = 'http://www.ex.ua/21522453?r=23786'
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()
List_re=re.findall("[http://www.ex.ua/show/0-9abcdef0-9]+.flv", Read_html)

for i in List_re:
	#os.system('wget %s' %i)
	print i

Xran=range(len(List_re)+1); Xran.pop(0)
for r in Xran:
	r=str(r)
	Title_re=re.search('(?<=<title>).*(?=\s/)', Read_html).group()
	print r+'-'+Title_re

#~ Я зделал то!!
#~ print re.search('(?<=<title>).*(?=\s/)', Read_html).group()
