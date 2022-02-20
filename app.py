from pickle import TRUE
from sys import flags
from flask import Flask


app=Flask(__name__)


@app.route("/")
def main():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=TRUE,host="0.0.0.0",port=8000)