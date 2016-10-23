# -*- coding: utf-8 -*-
import urllib
import ftplib
import os
import csv
import sys
from wikitools import wiki
from wikitools import api

def getNoolahamToken(i_site, i_api):
     params = {'action':'query', 'prop':'info','intoken':'edit','titles':'1'}
     req = i_api.APIRequest(i_site, params)
     response = req.query(False)
     token = response['query']['pages']['-1']['edittoken']
     return token
	 
def updateWikiPage(i_site, i_api, i_token, i_fileName, i_url):
     params = {'action':'upload', 'filename':i_fileName, 'url':i_url, 'token':i_token}
     request = i_api.APIRequest(i_site, params)
     result = request.query()
     print result
     return	 
	 
	 
# create a Wiki object
site = wiki.Wiki("https://yourwiki.org/api.php") 

# login - required for read-restricted wikis
if not site.login("Username ", "Password", verify=True):
    print("Login failed")

#Get Token (needed to edit wiki)
token = getNoolahamToken(site, api)


batchfile = open('createdata.csv', 'rt')
try:
     reader = csv.reader(batchfile)
     for row in reader:
        pgNoolahamNum = row[0]
        pgFolderPath = row[1]
        pgFileName = pgNoolahamNum + ".JPG"
        pgURL = "http://noolaham.net" + pgFolderPath + "/" + pgNoolahamNum + ".JPG"
        print pgURL
        updateWikiPage(site, api, token, pgFileName, pgURL);
  
finally:
     batchfile.close()
	 