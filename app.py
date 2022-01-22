from flask import Flask, request

from loader import bot

app = Flask(__name__)


@app.route('/', methods=['POST'])
async def hello_world():
    print(request.json)
    return {'ok': 'Hello World!'}


if __name__ == '__main__':
    app.run()
