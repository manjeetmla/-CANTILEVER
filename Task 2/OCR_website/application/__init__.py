from flask import Flask
import os
from flask_dropzone import Dropzone

from flask_session import Session
#
#
app = Flask(__name__)

app.config['SECRET_KEY'] = '2b2e6a26623260b24d3ad7b898b574c596e077b06236265684c1341a1f04'

#

# Sessions
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

#
dir_path = os.path.dirname(os.path.realpath(__file__))
#
#
app.config.update(
    UPLOADED_PATH=os.path.join(dir_path, 'static/uploaded_files/'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1,
    AUDIO_FILE_UPLOAD = os.path.join(dir_path, 'static/audio_files/')
)
app.config['DROPZONE_REDIRECT_VIEW'] = 'decoded'
#
dropzone = Dropzone(app)
#
from . import routes