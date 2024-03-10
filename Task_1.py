import requests

def get_request(url:str)->None:
    try:
        r = requests.get(url, auth=('user', 'pass'))
        print(r.text)
        #print(r.json())
        #print(r.encoding)
        #print(r.headers['content-type'])
    except Exception as e:
        print(e)

get_request("https://requests.readthedocs.io/en/latest/")
