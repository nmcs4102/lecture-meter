import time
import datetime
import flaskApp
import graph

results = []

def get_result():
    current_time = datetime.datetime.now()
    weighted_sum_votes = 0
    total_weight = 0
    num_votes = 0
    votes = flaskApp.get_votes()
    for vote in votes:
        vote_time = vote['timestamp']
        print(current_time, vote_time)
        if (current_time - vote_time) <= datetime.timedelta(minutes=5):
            print("HERE")
            time_diff = (current_time - vote_time).total_seconds()  # Convert time difference to minutes

            # Calculate weight based on recency, with votes in the last minute receiving full weight
            # and decreasing linearly to 0 weight at 5 minutes old.
            weight = max(0, 1.0 - (time_diff / 300.0))

            weighted_sum_votes += vote['value'] * weight
            total_weight += weight
            num_votes += 1

    if num_votes > 0:
        average_vote = weighted_sum_votes / total_weight
        return average_vote
    else:
        return 50


def get_resultsArray():
    return results

def set_results(array):
    results = array
def get_currentScore():
    if (not results) :
        return 50
    else:
        return results[-1]