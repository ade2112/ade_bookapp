from flask import Flask, request, jsonify
import book_handler


app = Flask(__name__)


@app.route('/book', methods=['POST'])
def create():
    body = request.json
    book = book_handler.Book(title=body['title'], description=body['description'],content=body['content'])
    book.create_book()
    return ({"message": "done"})

@app.route('/book/<id>', methods=['PUT'])
def update(id):
    body = request.json
    book = book_handler.Book(body['title'], body['description'], body['content'])
    book.update_book(id)
    return ({"message": "done"})

@app.route('/book/<id>', methods=['DELETE'])
def delete(id):
    book_handler.Book.delete_book(id)
    return ({"message": "done"})

@app.route('/book', methods=['GET'])
def fetch():
    rows=book_handler.Book.fetch_books(id)
    return jsonify(rows)

@app.route('/book/<id>', methods=['GET'])
def fetch_one(id):
    rows=book_handler.Book.fetch_book(id)
    return jsonify(rows)

@app.route('/books/<title>', methods=['GET'])
def search(title):
    rows=book_handler.Book.search_book(title)
    return jsonify(rows)



if __name__ == "__main__":
    app.run(debug=True, port=3000)
