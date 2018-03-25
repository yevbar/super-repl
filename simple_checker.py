# I import requests because checking to continue or not shouldn't require a browser, just a simple call
import requests

response = requests.get("https://xocazp03cg.execute-api.us-east-1.amazonaws.com/dev/hello")

data_json = response.json()

print (data_json)
