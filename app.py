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
    book = book_handler.Book(body['title'], body['description'], body['content'], body['image_url'])
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

@app.route('/book/<id>', methods=['GET'])
def fetch_one(id):
    rows=book_handler.Book.fetch_book(id)
    return jsonify(rows)

@app.route('/books/<string:title>', methods=['GET'])
def search(title):
    rows=book_handler.Book.search_book(title)
    return jsonify(rows)

@app.route('resource', methods=['POST'])
def create_res():
    body = request.json
    book = resource_handler.Resource(title=body['title'], author=body['author'],link=body['link'], image_url=body['image_url'])
    mes = book.create_resource()
    return mes

@app.route('/resource/<id>', methods=['PUT'])
def update_res(id):
    body = request.json
    book = resource_handler.Resource(body['author'], body['title'], body['image_url'], body['link'])
    mes = book.update_resource(id)
    return mes

@app.route('/resource/<id>', methods=['DELETE'])
def delete(id):
    mes=resource_handler.Resource.delete_resource(id)
    return mes


@app.route('/resource', methods=['GET'])
def fetch():
    rows=resource_handler.Resource.fetch_resources(id)
    return jsonify(rows)

@app.route('/books/<string:title>', methods=['GET'])
def search(title):
    rows=resource_handler.Resource.search_resource(title)
    return jsonify(rows)




if __name__ == "__main__":
    app.run(debug=True, port=3000)
