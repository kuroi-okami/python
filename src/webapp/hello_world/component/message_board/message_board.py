from flask import Blueprint, request, jsonify, make_response, abort

message_board = Blueprint('message_board', __name__)
recorded_messages = []  # Poor man's database
counter = 0


@message_board.route("/", methods=['GET'], defaults={'message_id': None})
@message_board.route("/<int:message_id>")
def index(message_id):
    if message_id is None:
        response = make_response(
            jsonify(messages=recorded_messages if recorded_messages else None))
        return response

    for message in recorded_messages:
        if message["id"] == message_id:
            return message
    else:
        print("Invalid message. Aborting")
        abort(400)


@message_board.route("/add", methods=['PUT'])
def create_message():
    if not request.json or 'message' not in request.json:
        print("Invalid message. Aborting")
        abort(400)

    global counter
    counter += 1
    new_message = {
        'id': counter,
        'message': request.json['message'],
        'author': request.json.get('author', '')
    }
    recorded_messages.append(new_message)

    return jsonify(response='success', id=counter)


@message_board.route("/<int:message_id>", methods=['DELETE'])
def delete_message(message_id):
    for message in recorded_messages:
        if message["id"] == message_id:
            recorded_messages.remove(message)
            break
    else:
        print("Invalid message. Aborting")
        abort(400)

    return jsonify(response='deleted', id=message_id)
