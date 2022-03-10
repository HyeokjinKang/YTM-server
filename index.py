from flask import Flask, jsonify, Response
from ytmusicapi import YTMusic

app = Flask(__name__)
ytmusic = YTMusic('headers_auth.json')

def errorResponse(error, code):
  return Response('{"Error": %s}' % (error), status=code, mimetype='application/json')

@app.route('/', methods=['GET'])
def index():
  return "Welcome to the YTMusic API"

@app.route('/getHome/<limit>', methods=['GET'])
def getHome(limit):
  results = ytmusic.get_home(int(limit))
  return jsonify(results)

if __name__ == "__main__":
  app.run(debug=True)
  # from waitress import serve
  # serve(app, host="0.0.0.0", port=8080)
