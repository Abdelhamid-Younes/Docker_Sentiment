import os
import requests
import time
# definition of the API address
#api_address = 'fastapi'
# API port
#api_port = '8000'
# requête

def test_authentication(username: str, password: str):
	r = requests.get(
    		url='http://172.27.1.1:8000/permissions',
    		params= {
        	'username': username,
        	'password': password
    			}
	)

	output = '''
	============================
    	    Authentication test
	============================
	request done at "/permissions"
	| username= {username}
	| password= {password}
	|expected result = 200
	|actual restult = {status_code}
	==>  {test_status}
	'''
	# query status
	status_code = r.status_code

	# display the results
	if status_code == 200:
           test_status = 'SUCCESS'
	else:
    	   test_status = 'FAILURE'

	output=output.format(status_code=status_code, test_status=test_status, username=username, password=password )
	print(output)
	# printing in a file
	if os.environ.get('LOG') == '1':
	    with open('/shared_volume/api_test.txt', 'a') as file:
        	file.write(output)

##############################################################################
test_authentication("alice", "wonderland")
test_authentication("bob", "builder")
test_authentication("clementine", "mandarine")
