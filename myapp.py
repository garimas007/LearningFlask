from flask import Flask, request

# Instance of flask class
app = Flask(__name__)

# Route for the root URL
@app.route("/", methods=['GET', 'POST', 'PUT']) #GET, POST, PUT, DELETE methods=['GET', 'POST']
def hello_world():
    #print(request.args.get('num1'))
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    num3 = int(request.args.get('num3'))
    #return "Hello, World!"
    return str(num1+num2+num3)

@app.route("/contactus")
def contactUs():
    return "contact details"

@app.route("/aboutus")
def aboutUs():
    return "I am Garima"

@app.route("/login", methods=['POST'])  #this is an example of data sent through body from postman
def login():
    data = request.get_json()
    #print(data['name'])
    username = data['name']
    password = data['pwd']
    if username == 'Garima' and password == 'gg':
        return "Welcome"
    else:
        return "Wrong username and password"
    #return "logged in"
    #return data

# Start flask application
if __name__ == '__main__':  #binding it with main function
    app.run(debug=True)  #run the application in debug mode.
