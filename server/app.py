from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False

app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):

    session["hello"] = session.get("hello") or "World" # Sets to World if called the first time
    session["goodnight"] = session.get("goodnight") or "Moon" # Sets toMoon if called the first time

    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]} #Key-value pair(dictionary)
            for cookie in request.cookies],
    }), 200)

    response.set_cookie('mouse', 'Cookie') # Key of mouse and value pf Cookie

    return response

if __name__ == '__main__':
    app.run(port=5555)
    