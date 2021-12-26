from config.settings import app


@app.route('/')
def hello_world():
    return "Hello world"


if __name__ == '__main__':
    app.run(port=8989)
