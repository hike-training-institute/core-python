from flask import Flask, jsonify
from flask_restplus import Resource , Api
from multiprocessing import Process
from threading import Thread
import time

app = Flask(__name__)
api = Api(app, title='testing multi tasking')

def func():
    print("starting.......")
    time.sleep(10)
    # emmail trigger
    print("ending.......")

class SampleClass(Resource):

    def get(self):

        p1 = Process(target=func)
        p2 = Process(target=func)
        p1.start()
        p2.start()

        t1 = Thread(target=func)
        t1.start()
        return jsonify({"msg":"successs"})

api.add_resource(SampleClass, '/home', methods=['GET'])

if __name__ == "__main__":
    app.run(host='127.0.0.1')