from flask import Flask, request
from flask_cors import CORS

from .scraper import lookup_item

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET','POST'])
def index():

    item_req = request.json['item_name']
    items_table = lookup_item(str(item_req))
    return items_table.to_json(orient='records')


if __name__ == '__main__':
    app.run(debug=True)