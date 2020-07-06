#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests as rqst

# retrieve the html content file for the web page.
content1 = rqst.request(method='GET', url="http://github.com/osailansamar") #way 1 
# OR
# content2 = rqst.get('http://github.com/osailansamar')

# check if found
if content1.status_code == 200:
    print('Success!')
elif content1.status_code == 404:
    print('Not Found.')

print("------------------")
print(content1.url) # display the web url
print("------------------")
print(content1.text) # html file content


# In[9]:


import bs4
import urllib.request as rqst1

# try another way retrieve the content of the web page as text
content2 = rqst1.urlopen('http://github.com/osailansamar').read()
rslt = bs4.BeautifulSoup(content2,'lxml')

for i in rslt.find_all('p'):
    print (i.text)


# In[ ]:




