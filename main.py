from flask import Flask
from flask_restful import Resource, Api

from routes.dome import dome
from routes.observing_conditions import observing_conditions
from routes.cover_calibrator import cover_calibrator


app = Flask(__name__)
api = Api(app)

app.register_blueprint(dome , url_prefix='/api/v1/dome/')
app.register_blueprint(observing_conditions, url_prefix='/api/v1/observingconditions/')
app.register_blueprint(cover_calibrator, url_prefix='/api/v1/covercalibrator/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11111, debug=True)
