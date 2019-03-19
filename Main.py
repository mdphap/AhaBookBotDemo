
from flask import Flask, request

app = Flask(__name__)
# ACCESS_TOKEN = 'EAAhHeZBvbHScBADmsfaKRTYWZCFg5zLBZAUzw5RYiD08UwOEVdvPg0yQJulBdz2H7r1qGaW01mOQPPRZBNg4qma43vC94UOOYAHflJDyHomVKPMjPg2vdl5zbBrlggiChDqNSL2KMVbMhZAutbM6DEr3RZB539ZBJ3nAsdUCXLS87vHnt9JEZB1e'
# VERIFY_TOKEN = 'MEU@&(*#!'
# bot = Bot(ACCESS_TOKEN)


# We will receive messages that Facebook sends our bot at this endpoint

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()