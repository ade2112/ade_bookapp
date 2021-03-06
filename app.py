from flask import Flask, request, jsonify
import book_handler
import resource_handler


app = Flask(__name__)


@app.route('/book', methods=['POST'])
def create():
    body = request.json
    book = book_handler.Book(title=body['title'], description=body['description'],content=body['content'], image_url=body['image_url'])
    mes = book.create_book()
    return mes

@app.route('/book/<id>', methods=['PUT'])
def update(id):
    body = request.json
    book = book_handler.Book(title=body['title'], description=body['description'],content=body['content'], image_url=body['image_url'])
    mes = book.update_book(id)
    return mes

@app.route('/book/<id>', methods=['DELETE'])
def delete(id):
    mes=book_handler.Book.delete_book(id)
    return mes

@app.route('/book', methods=['GET'])
def fetch():
    rows=book_handler.Book.fetch_books(id)
    return jsonify(rows)
@app.route('/', methods=['GET'])
def index():
    return "okay"

@app.route('/book/<id>', methods=['GET'])
def fetch_one(id):
    rows=book_handler.Book.fetch_book(id)
    return jsonify(rows)

@app.route('/books/<string:title>', methods=['GET'])
def search(title):
    rows=book_handler.Book.search_book(title)
    return jsonify(rows)

@app.route('/resource', methods=['POST'])
def create_res():
    body = request.json
    book = resource_handler.Resource(author=body['author'], title=body['title'],image_url=body['image_url'],link=body['link'])
    mes = book.create_resource()
    return mes

@app.route('/resource/<id>', methods=['PUT'])
def update_res(id):
    body = request.json
    book = resource_handler.Resource(author=body['author'], title=body['title'],image_url=body['image_url'],link=body['link'])
    mes = book.update_resource(id)
    return mes

@app.route('/resource/<id>', methods=['DELETE'])
def delete_res(id):
    mes=resource_handler.Resource.delete_resource(id)
    return mes


@app.route('/resource', methods=['GET'])
def fetch_res():
    rows=resource_handler.Resource.fetch_resources(id)
    return jsonify(rows)

@app.route('/resource/<string:title>', methods=['GET'])
def search_res(title):
    rows=resource_handler.Resource.search_resource(title)
    return jsonify(rows)




if __name__ == "__main__":
    app.run(debug=True)
