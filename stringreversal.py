# This task is for intermediate level
# Reverse any given string passed by Postman

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def getReverseString():
    originalstr = request.data
    reversedstr = originalstr[::-1]
    print("Str passed: ", originalstr)
    print("Reverse is: ", reversedstr)
    return reversedstr

if __name__ == '__main__':
    app.run(debug=True)