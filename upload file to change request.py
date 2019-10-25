import requests
import json
#url='https://dev94041.service-now.com/api/now/table/sc_req_item'
#url='https://dev94041.service-now.com/api/now/attachment/file'
url = 'https://dev94041.service-now.com/api/now/attachment/upload'

user='admin'
pwd='Preethi@2019'
page_size=50
payload = {

'table_name':'change_request',

'table_sys_id':'2de5121347c12200e0ef563dbb9a71eb',
}
filename='PROFILE.txt'
files = {'image':(filename, open(filename, 'rb'), 'txt')}
headers = {"Accept":"*/*"}
r = requests.post(url=url, auth=(user, pwd),data=payload,files=files)

print(r.status_code)
print('Reponse Payload:')
print(json.dumps(r.json(), indent=4))
