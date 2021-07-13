from flask import Flask, request
import book_handler


app = Flask(__name__)


@app.route('/book', methods=['POST'])
def create():
    body = request.json
    book = book_handler.Book(body['title'], body['description'], body['content'], body['image_url'])
    book.create_book()
    return ({"message": "done"})


if __name__ == "__main__":
    app.run(debug=True, port=3000)
