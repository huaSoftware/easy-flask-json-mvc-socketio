from app import app
from flask_cors import CORS

app = app
CORS(app, supports_credentials=True)
if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=500, threaded=True)
