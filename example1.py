'''
pip3 install fastapi httptools==0.1.* uvloop uvicorn

'''

from fastapi import FastAPI
api = FastAPI()
@api.get('/')
def get_index():
    return {'data' : 'Hello World'}

'''
Once this file is saved, run the API in another console by executing the following command :
uvicorn name_of_this_file:api --reload

Here, we specify the main file and the name of the API to run inside this file: api. 
The argument --reload allows to automatically update the API when changes are made to the source file. 
In the console, the following line should be observed :
INFO: Uvicorn running on http://127.0.0.1:8000(Press CTRL+C to quit)
This line gives us the address at which the API works.
In another console, issue the following command to query the endpoint / :
curl -X GET http://127.0.0.1:8000/            
'''