# app.py
from flask import Flask

import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("my_swagger.yml")


@app.route("/")
def home():
    return 0


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    
    