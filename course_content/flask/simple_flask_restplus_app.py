from flask import Flask, jsonify
from flask_restplus import Api
from flask_restplus import Resource
from flask import request
import psycopg2 as pg
app = Flask(__name__)
api = Api(app)

@api.route('/home/<int:limit>', methods=['GET', 'POST'])
class Home(Resource):

    def get(self, limit):

        connection = pg.connect(user="postgres",
                                password="postgres",
                                host="127.0.0.1",
                                port="5432",
                                database="dvdrental")
        cursor = connection.cursor()
        result = cursor.execute("select first_name from actor limit {};".format(int(limit)))
        all_rows = cursor.fetchall()
        return jsonify(all_rows)

    def post(self):
        print(request.get_json())
        return jsonify("Hello World....")

if __name__ == "__main__":
    app.run(port=5050, debug=True)