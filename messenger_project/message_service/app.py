from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes import message_routes
from config import Config
from flask_migrate import Migrate
import requests
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
# db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.register_blueprint(message_routes)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200
if __name__ == '__main__':
    # Register service in Consul
    consul_url = 'http://consul:8500/v1/agent/service/register'
    service_data = {
        "Name": "messageservice",
        "Address": "messageservice",
        "Port": 5001,
        "Check": {
            "HTTP": "http://messageservice:5001/health",
            "Interval": "10s"
        }
    }
    try:
        requests.put(consul_url, json=service_data)
    except Exception as e:
        print(f"Consul registration failed: {e}")
    app.run(host='0.0.0.0', port=5001)