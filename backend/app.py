from flask import Flask, jsonify, request

import pymongo
from pymongo.server_api import ServerApi
from pymongo import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://jacksonaguiar:SETuWqupEulsU25F@cluster0.zkykwzk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

cluster = MongoClient(uri)
db = cluster["ponderada"]

@app.route('/save-info', methods=['POST'])
def create_info():
    collection = db["sensor_data"]
    try:
        new_info = request.get_json()

        if not isinstance(new_info, dict):
            raise ValueError('Invalid JSON data. Expected a dictionary.')
        
        period=new_info.get('period', '')
        temp=new_info.get('env_temperature', '')
        dt=new_info.get('date_time', '')
        rad=new_info.get('radiation_intensity', '')
        
        collection.insert_one({"period":period, "env_temperature":temp, "date_time":dt,"radiation_intensity":rad})
  
        
        return '',201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    

if __name__ == '__main__':
    app.run(debug=True)