from flask import Flask

app = Flask("My first application")

@app.route("/")
def hello() : 
    return "Hello Flask!"

@app.route("/<string:name>")
def hello_name(name) : 
    return f"Hello Flask from {name}!"

if __name__ == "__main__":
    app.run(debug=True)