import requests
import json
url='https://dev94041.service-now.com/api/sn_chg_rest/change/standard'

user='admin'
pwd={$your_password}
headers = {"Accept":"*/*"}
r = requests.get(url=url, auth=(user, pwd),headers=headers)
a=r.json()
print(r.status_code)


for key in range(0,len(a[u'result'])):
    try:

        b=a[u'result'][key][u'number']
        c=b[u'display_value']
        d=a[u'result'][key][u'sys_id']
        f=d[u'display_value']
        print(c,'-->' ,f)
        
        
    except TypeError:
        print('no change request')
