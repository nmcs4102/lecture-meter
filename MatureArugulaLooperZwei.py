import threading

import graph
import resultifier
import time

lock = threading.Lock()

def ArugulaLooper():
    with lock:
        while True:
            time.sleep(1)
            resultifier.set_results(resultifier.get_resultsArray().append(resultifier.get_result()))
            graph.generate_graph(resultifier.get_resultsArray())

