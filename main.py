from flask import Flask, json, request
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import firestore as fs

cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)


@app.after_request
def apply_cors(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/message', methods=['POST'])
async def message():
    if not request.is_json:
        return {"error": "Data is not JSON"}, 400
    data = request.get_json(force=True)
    # get message from data or return error if not found
    message = data['message'] if 'message' in data else None
    # id message is None, or trimmed length is 0, return error
    if message is None or len(message.strip()) == 0:
        return {"error": "No message found"}, 400

    # get conversation ID from data or return error if not found
    conversation_id = data['conversation_id'] if 'conversation_id' in data else None
    if conversation_id is None:
        return {"error": "No conversation ID found"}, 400

    db.collection('conversations').document(conversation_id).set({
        "messages": fs.ArrayUnion([
            {"content": message, "sender": "user"},
            {"content": "Your message was: " + message, "sender": "bot"}
        ])
    }, True)

    return {"response": "Your message was: " + message}


@app.route('/conversations', methods=['POST'])
async def conversations():
    if not request.is_json:
        return {"error": "Data is not JSON"}, 400
    data = request.get_json(force=True)
    # get conversation ID from data or return empty list if not found
    conversation_id = data['conversation_id'] if 'conversation_id' in data else None

    if conversation_id is None:
        return [], 200

    # get messages from firestore
    messages_stream = db.collection('conversations').document(conversation_id).get().to_dict()

    if (messages_stream is None) or ('messages' not in messages_stream):
        return [], 200

    print(messages_stream['messages'])

    return messages_stream['messages'], 200


if __name__ == '__main__':
    app.run()
