from flask import Flask

app = Flask(__name__)

@app.route('/', , methods=['GET', 'POST']) # endpoint("/"), HTTP Methods (GET, POST, PUT, DELETE)
def function(): # fungsi tertentu yang akan menangani logika untuk URL tersebut


    return value # mengembalikan nilai

if __name__ == '__main__':
    app.run(debug=True)