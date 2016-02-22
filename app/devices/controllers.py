import pychromecast
import re
from flask import Blueprint, jsonify, abort

devices = Blueprint('devices', __name__)


@devices.route('/')
def devicesList():
    chromecasts = []
    for key in pychromecast.get_chromecasts_as_dict().keys():
        chromecasts.append(key)

    return jsonify({'list': chromecasts})


@devices.route('/<string:chromecast>')
def devicesShow(chromecast):
    cast = pychromecast.get_chromecast(friendly_name=chromecast)
    if cast is None:
        abort(404)

    cast.wait()
    return jsonify({'device': cast.device})


@devices.route('/<string:chromecast>/media/<string:url>')
def mediaPlayUrl(chromecast, url):
    cast = pychromecast.get_chromecast(friendly_name=chromecast)
    if cast is None:
        abort(404)

    cast.wait()
    mc = cast.media_controller
    mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
    return jsonify({'play': 'playing'})


@devices.route('/<string:chromecast>/status')
def mediaStatus(chromecast, url):
    cast = pychromecast.get_chromecast(friendly_name=chromecast)
    if cast is None:
        abort(404)

    cast.wait()
    mc = cast.media_controller
    return jsonify({'device': mc})
