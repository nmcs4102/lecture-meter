# Time
import os

from flask import Flask, request, make_response, jsonify, send_file
import datetime

import resultifier
import sitetemplates
import threading
import MatureArugulaLooperZwei

app = Flask(__name__)

# List to store votes
votes = []


def get_votes():
    voties = []
    if os.path.exists('./storage/votes.txt'):
        f = open("./storage/votes.txt", "r")
        raw = f.readline().split(";")
        for g in raw:
            cur = g.split(",")
            voties.append({"value": int(cur[0]), "timestamp": datetime.datetime.strptime(cur[1], '%Y-%m-%dT%H:%M:%S.%f')})
    return voties
@app.route('/')
def index():
    return sitetemplates.home()
@app.route('/graph.png')
def graphPNG():
    image_path = './templates/graph.png'
    return send_file(image_path, mimetype='image/png')


@app.route('/vote', methods=['POST'])
def vote():
    vote_value = int(request.json.get('value'))
    if vote_value is None or not 0 <= vote_value <= 100:
        return jsonify({'error': 'Invalid vote value'}), 400
        #
    # Check if user has already voted
    # old_vote_time = request.cookies.get('vote_time')

    global votes
    # for vote in votes:
    #    if old_vote_time == vote['timestamp']:
    #        votes.remove(vote)
    #        break

    timestamp = datetime.datetime.now().isoformat()
    # Append vote to the votes list
    if (not os.path.exists('./storage/votes.txt')):
        f = open("./storage/votes.txt", "w")
        f.write(f"{vote_value},{timestamp}")
        f.close()
    else:
        f = open("./storage/votes.txt", "a")
        f.write(f";{vote_value},{timestamp}")
        f.close()
    # Create a response and set a cookie to prevent multiple votes
    response = make_response(jsonify({'success': f'Vote received: {vote_value}'}))
    response.set_cookie('vote_time', timestamp)
    # Add resu
    return response

@app.route('/current-score')
def current_score():
    # This is a placeholder for how you calculate or retrieve the current score
    score = resultifier.get_currentScore()  # Assume this function returns the current score
    return jsonify(score=round(score))

def run_app():
    app.run(host='0.0.0.0', port=5000, threaded=True)

if __name__ == '__main__':
    thread1 = threading.Thread(target=run_app)
    thread2 = threading.Thread(target=MatureArugulaLooperZwei.ArugulaLooper)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()





