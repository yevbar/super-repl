print "Hello from Flask!"

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def hello():
  if request.method == "GET":
    return jsonify(continue_="true",action_="import requests\nr = requests.post('https://MasterNodeCool--yevbar.repl.co', json={'ip' : ''})")
  else:
    print request.get_json(silent=True)
    return "Thanks!"

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=False)
