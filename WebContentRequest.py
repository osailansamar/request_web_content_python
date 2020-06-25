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


# In[ ]:





# In[ ]:




