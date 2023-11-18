from datetime import datetime

from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://User:4lNukg1PfxSL8SZj@unistud.mhdzsny.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)


@app.route('/')
def get_events():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    events = client.unities.events.find()
    events_list = []

    for event in events:
        event_data = {
            'name': event['name'],
            'description': event['description'],
        }
        events_list.append(event_data)

    return jsonify({'events': events_list})


@app.route('/events')
def add_movie():
    date_string = "2023-11-17"
    formatted_date1 = datetime.strptime(date_string, "%Y-%m-%d").date()
    date_string = "2023-11-19"
    formatted_date2 = datetime.strptime(date_string, "%Y-%m-%d").date()
    try:
        event_data = jsonify({
            'name': 'Unihack',
            'description': 'This is a fun hackathon!',
            'county': 'Timis',
            'open': True,
            'accommodation': True,
            'dateStart': formatted_date1,
            'dateEnd': formatted_date2,
            'organizer': 'Liga AC',
            'imageUrl': ''
        })

        # Insert the movie into the collection
        result = client.unities.events.insert_one(event_data)

        # Check if the insertion was successful
        if result.inserted_id:
            return jsonify({'message': 'Event added successfully', 'event_id': str(result.inserted_id)}), 201
        else:
            return jsonify({'error': 'Failed to add event'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
