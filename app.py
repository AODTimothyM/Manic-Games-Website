from flask import Flask, redirect, render_template, request, url_for
from urllib.request import Request, urlopen
import json

DEVELOPMENT_ENV = True

app = Flask(__name__)

app_data = {
    "name": "Manic Games",
    "description": "Manic Games website",
    "author": "Manic",
    "html_title": "Manic Games",
    "project_name": "Manic Game Website",

    "missionStatement": "Dedicated to crafting immersive gaming experiences.",
    "motto": "Mashin' Imagination with Innovation",

    "keywords": "manic, indie, indiedev, godot, videogame, game, gamedev",
}

WEBHOOK_URL = "https://discord.com/api/webhooks/1181365969914957864/-IUDLQOS-mR7sqXCjlb9qnott8d1EKj0fwIqAX3XUeompFbJ2ovDLO9vdSeHZfllAPJW"
WEBHOOK_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
payload = json.dumps({"content": "Message"})

def sendMessage(name, email, message):
    try:
        payload = json.dumps({"content": f"Name: {name}\nEmail: {email}\nMessage: {message}"})
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=WEBHOOK_HEADERS)
        urlopen(req)
    except:
        print("ERROR: Couldn't send message.")


# ---ROUTES---

@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)


@app.route("/blog")
def blogs():
    file = open(f'blogs.txt', encoding="utf8")
    contents = file.read()

    blogs = contents.split('# ')
    blogs = [blog.split('\n', 1) for blog in blogs[1:]]

    return render_template("blog.html", app_data=app_data, blogs=blogs)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        sendMessage(name, email, message)

        return redirect(url_for('contact'))

    return render_template('contact.html', app_data=app_data)


if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)




