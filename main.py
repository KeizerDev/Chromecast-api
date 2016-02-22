#! /usr/bin/python

from __future__ import print_function
from app.devices.controllers import devices
from flask import Flask, jsonify

app = Flask(__name__)

routes = [
    {
        'path': u'/devices',
        'description': u'Lists chromecast on a local network'
    },
    {
        'path': u'/devices/{chromecast}',
        'description': u'Connect to a chromecast from /devices'
    },
    {
        'path': u'/controllers',
        'description': u'Lists available controllers'
    }
]


@app.route('/')
def index():
    return jsonify({'routes': routes})

app.register_blueprint(devices, url_prefix='/devices')





# print(json.dumps(pychromecast.get_chromecasts_as_dict().value()))

# print(pychromecast.get_chromecasts_as_dict().keys())

# cast = pychromecast.get_chromecast(friendly_name="ChromecastRob")
# # # Wait for cast device to be ready
# cast.wait()
# print(cast.device)

# print(cast.status)


# yt = youtube.YouTubeController()
# cast.register_handler(yt)

# CastStatus(is_active_input=True, is_stand_by=False, volume_level=1.0, volume_muted=False, app_id=u'CC1AD845', display_name=u'Default Media Receiver', namespaces=[u'urn:x-cast:com.google.cast.player.message', u'urn:x-cast:com.google.cast.media'], session_id=u'CCA39713-9A4F-34A6-A8BF-5D97BE7ECA5C', transport_id=u'web-9', status_text='')

# mc = cast.media_controller
# mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
# print(mc.status)
# MediaStatus(current_time=42.458322, content_id=u'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', content_type=u'video/mp4', duration=596.474195, stream_type=u'BUFFERED', idle_reason=None, media_session_id=1, playback_rate=1, player_state=u'PLAYING', supported_media_commands=15, volume_level=1, volume_muted=False)

# mc.pause()
# time.sleep(5)
# mc.play()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

