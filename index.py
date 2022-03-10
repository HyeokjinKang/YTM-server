from flask import Flask, jsonify, Response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from ytmusicapi import YTMusic
import json

app = Flask(__name__)
auth = HTTPBasicAuth()
ytmusic = YTMusic('headers_auth.json')

usersFile = open("auth.json", "r")
users = json.load(usersFile)
usersFile.close()

def errorResponse(error, code):
  return Response('{"Error": %s}' % (error), status=code, mimetype='application/json')

@auth.verify_password
def verify_password(username, password):
  if username in users and check_password_hash(users.get(username), password):
    return username
  return False

@app.route('/', methods=['GET'])
def index():
  return "Welcome to the YTMusic API"

@app.route('/getHome/<limit>', methods=['GET'])
@auth.login_required
def getHome(limit):
  results = ytmusic.get_home(int(limit))
  return jsonify(results)

@app.route('/getMood', methods=['GET'])
@auth.login_required
def getMood():
  results = ytmusic.get_mood_categories()
  return jsonify(results)

@app.route('/getMood/<id>', methods=['GET'])
@auth.login_required
def getMoodPlaylists(id):
  results = ytmusic.get_mood_playlists(id)
  return jsonify(results)

@app.route('/getChart/<country>', methods=['GET'])
@auth.login_required
def getChart(country):
  results = ytmusic.get_charts(country)
  return jsonify(results)

@app.route('/search/<query>', methods=['GET'])
@auth.login_required
def search(query):
  results = ytmusic.search(query)
  return jsonify(results)

@app.route('/search/<query>/<advanced>', methods=['GET'])
@auth.login_required
def advancedSearch(query, advanced):
  results = ytmusic.search(query, advanced)
  return jsonify(results)

@app.route('/artist/<id>', methods=['GET'])
@auth.login_required
def artist(id):
  results = ytmusic.get_artist(id)
  return jsonify(results)

@app.route('/album/<id>', methods=['GET'])
@auth.login_required
def album(id):
  results = ytmusic.get_album(id)
  return jsonify(results)

@app.route('/track/<id>', methods=['GET'])
@auth.login_required
def track(id):
  results = ytmusic.get_song(id)
  return jsonify(results)

@app.route('/history', methods=['GET'])
@auth.login_required
def history():
  results = ytmusic.get_history()
  return jsonify(results)

@app.route('/rate/<id>/<rate>', methods=['GET'])
@auth.login_required
def rating(id, rate):
  results = ytmusic.rate_song(id, rate)
  return jsonify(results)

if __name__ == "__main__":
  # app.run(debug=True)
  from waitress import serve
  serve(app, host="0.0.0.0", port=5000)
