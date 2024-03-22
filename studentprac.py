# This program is part of Advance Task

from flask import Flask, request

app = Flask(__name__)

student = [
    {
        "name" : "Garima",
        "age" : 25
    },
    {
        "name" : "Kshitij",
        "age" : 27
    },
    {
        "name" : "Aparna",
        "age" : 29
    }
]

@app.route('/name')
def knowUrAge():
    urlname = request.args.get('name')
    for x in student:
        if str(x["name"]) == urlname:
            print(x['age'])
            return str(x['age'])
    return "No such data"
            
if __name__ == '__main__':
    app.run(debug=True)