#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, re, sys, os

html = 'http://www.ex.ua/17040371?r=23786'
Url_html=urllib.urlopen(html)
Read_html=Url_html.read()

List_re=re.findall("[0-9a-z]+.flv", Read_html)

dir=os.listdir('.')
for i in List_re:
	if i in dir:
		print "List_dir in path", i

print List_re

print dir
