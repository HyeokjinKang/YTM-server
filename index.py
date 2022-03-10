from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)
ytmusic = YTMusic('headers_auth.json')

@app.route('/', methods=['GET'])
def index():
  results = ytmusic.get_home(5)
  return jsonify(results)

if __name__ == "__main__":
  app.run(debug=True)
  # from waitress import serve
  # serve(app, host="0.0.0.0", port=8080)
