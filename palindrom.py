# This prog is basic task given in class
# Find out if the number is palindrom or not

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def pallindromeCheck():
    taken_num = request.data
    reversed_num = taken_num[::-1]
    print("number :", taken_num)
    print("reverse number :", reversed_num)
    if taken_num == reversed_num:
        print("The number is pallindrom")
        return "yes pallindrom"
    else:
        print("The number is not pallindrom")
        return "not pallindrom"

if __name__ == '__main__':
    app.run(debug=True)