import urllib
from urllib.request import urlopen, pathname2url
import json
import xml.etree.ElementTree as ETree

##### debug
#from test_data import list_sitename, test_json

##### prod
from sitelist import list_sitename, test_json

from FormatDate import formatDate
from AuthDate import *

print(list_sitename)

########################
# Fill in your details #
# ########################

i = 0
for site in list_sitename:
    print(site)

    i += 1
    print(i)
    url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService'
    username = login
    password = passwd
    uri = ""
    uri = url \
          + '?domainName=' + pathname2url(site) \
          + '&username=' + pathname2url(username) \
          + '&password=' + pathname2url(password) \
          + '&outputFormat=JSON' \
    #####################################
    #### production mode#################
    ## uncomment to line
    ##  1. with urllib....
    ##  2.      data=..... 

    with urllib.request.urlopen(uri) as url:
         data = json.loads(url.read().decode())

    #####################################
    #####################################
    
    ######################
    ##   debug mode ######
    ## test_data from site_list

    # data = test_json


    ######################
    ######################

    text_out = formatDate(data,site,i)

    print(text_out)

    f = open('whois.txt', 'a')
    f.write(text_out + '\n')
    f.close()
