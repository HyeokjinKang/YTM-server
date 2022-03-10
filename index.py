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

@app.route('/getMood', methods=['GET'])
def getMood():
  results = ytmusic.get_mood_categories()
  return jsonify(results)

@app.route('/getMood/<id>', methods=['GET'])
def getMoodPlaylists(id):
  results = ytmusic.get_mood_playlists(id)
  return jsonify(results)

@app.route('/getChart/<country>', methods=['GET'])
def getChart(country):
  results = ytmusic.get_charts(country)
  return jsonify(results)

@app.route('/search/<query>', methods=['GET'])
def search(query):
  results = ytmusic.search(query)
  return jsonify(results)

@app.route('/search/<query>/<advanced>', methods=['GET'])
def advancedSearch(query, advanced):
  results = ytmusic.search(query, advanced)
  return jsonify(results)

@app.route('/artist/<id>', methods=['GET'])
def artist(id):
  results = ytmusic.get_artist(id)
  return jsonify(results)

@app.route('/album/<id>', methods=['GET'])
def album(id):
  results = ytmusic.get_album(id)
  return jsonify(results)

@app.route('/track/<id>', methods=['GET'])
def track(id):
  results = ytmusic.get_song(id)
  return jsonify(results)

@app.route('/history', methods=['GET'])
def history():
  results = ytmusic.get_history()
  return jsonify(results)

@app.route('/rate/<id>/<rate>', methods=['GET'])
def rating(id, rate):
  results = ytmusic.rate_song(id, rate)
  return jsonify(results)

if __name__ == "__main__":
  # app.run(debug=True)
  from waitress import serve
  serve(app, host="0.0.0.0", port=5000)
