import os
import requests
import json
import time
# definition of the API address
#api_address = 'fastapi_from_compose'
# API port
#api_port = 8000
# request1
def test_content_v1(username: str, password: str, sentence: str):
	r = requests.get(
    	url='http://172.27.1.1:8000/v1/sentiment',
    	params= {
        	'username': username,
        	'password': password,
		'sentence': sentence
   	 }
	)

	output = '''
	============================
	    Content test
	============================
	request done at "v1/sentiment"
	| username={username}
	| password={password}
	| sentence= {sentence}
	| expected result = 200
	| actual restult = {status_code}
	| test_score = {test_score}
	==>  {test_status}
	'''
	result = r.json()
	# query status
	status_code = r.status_code

	# display the results
	if status_code == 200:
	   test_status = 'SUCCESS'
	   test_score = str(result['score'])
	else:
	   test_status = 'FAILURE'
	output=output.format(status_code=status_code, test_status=test_status, username=username, password=password, sentence=sentence, test_score=test_score)
	print(output)

	# printing in a file
	if os.environ.get('LOG') == '1':
	    with open('/shared_volume/api_test.txt', 'a') as file:
	        file.write(output)

# request2
def test_content_v2(username: str, password: str, sentence: str):
	r = requests.get(
    	url='http://172.27.1.1:8000/v2/sentiment',
    	params= {
        	'username': username,
        	'password': password,
		'sentence': sentence
   	 }
	)

	output = '''
	============================
	    Content test
	============================
	request done at "v2/sentiment"
	| username={username}
	| password={password}
	| sentence= {sentence}
	| expected result = 200
	| actual restult = {status_code}
	| test_score = {test_score}
	==>  {test_status}
	'''
	result = r.json()
	# query status
	status_code = r.status_code

	# display the results
	if status_code == 200:
	   test_status = 'SUCCESS'
	   test_score = str(result['score'])
	else:
	   test_status = 'FAILURE'
	output=output.format(status_code=status_code, test_status=test_status, username=username, password=password, sentence=sentence, test_score=test_score)
	print(output)

	# printing in a file
	if os.environ.get('LOG') == '1':
	    with open('/shared_volume/api_test.txt', 'a') as file:
	        file.write(output)

###################################################################################
test_content_v1('alice', 'wonderland', 'life is beautiful')
test_content_v2('alice', 'wonderland', 'life is beautiful')

test_content_v1('alice', 'wonderland', 'that sucks')
test_content_v2('alice', 'wonderland', 'that sucks')
