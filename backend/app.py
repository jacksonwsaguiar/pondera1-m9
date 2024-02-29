from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class SensorInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    period = db.Column(db.String(100), nullable=False)
    env_temperature = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.String(100), nullable=False)
    radiation_intensity = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/save-info', methods=['POST'])
def create_info():
    try:
        new_info = request.get_json()

        # Check if new_info is a dictionary
        if not isinstance(new_info, dict):
            raise ValueError('Invalid JSON data. Expected a dictionary.')

        new_sensor_info = SensorInfo(
            period=new_info.get('period', ''),
            env_temperature=new_info.get('env_temperature', ''),
            date_time=new_info.get('date_time', ''),
            radiation_intensity=new_info.get('radiation_intensity', '')
        )

        db.session.add(new_sensor_info)
        db.session.commit()
        
        return '',201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    

if __name__ == '__main__':
    app.run(debug=True)