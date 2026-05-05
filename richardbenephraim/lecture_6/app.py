from flask import Flask, jsonify,Response
from json import JSONDecodeError
import json

app = Flask(__name__)


data_file = "./files/config.json"

"""
  ==== learning face ====

TODO =>
. a function to load json file,
- a function to save file
- get all channels
- get tv / radio channels
- get channel by id
note: the POST methods will come later 
"""


def load_file():
    try:
        with open(file=data_file, mode="r",  encoding="utf-8") as file:
            content = json.load(file)
            return content
    except (JSONDecodeError, FileNotFoundError):
        return {"tv":[],"radio":[]}


def save_file(data):
    with open(file=data_file, mode= "w",  encoding="utf-8") as file:
        json.dump(file, data, indent=4)

@app.route("/")
def index():
    return {"BackEnd Server": "server is working"}



@app.route("/api/channels", methods =["GET"])
def get_all_channel():
    data = load_file()
    all_channel = data["tv"] + data["radio"]
    return Response.json(all_channel)

@app.route("/api/channels/tv", methods = ["GET"])
def get_all_tv_channel():
    data = load_file()
    tv_channels = data["tv"]
    return jsonify(tv_channels)


@app.route("/api/channels/radio", methods = ["GET"])
def get_all_radio_station():
    data = load_file()
    radio_station = data["radio"]
    return jsonify(radio_station)

@app.route("/api/channels/<int:channel_id>", methods = ["GET"])
def get_channel_by_id(channel_id):
    data = load_file()
    all_channels = data["tv"] + data ["radio"]
    for station in all_channels:
        if station["id"] == channel_id:
            return jsonify(station)
        else:
            return jsonify({"error" : "Channel not found"})


if __name__ == "__main__":
    app.run(debug=True)