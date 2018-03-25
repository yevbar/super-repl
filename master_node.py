from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(continue_="true",action_="print ('This is not a DDOS!')")

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=False)
