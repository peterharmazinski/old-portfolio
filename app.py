from flask import Flask, current_app, render_template, send_from_directory

app = Flask(__name__, static_folder="react/build/static", template_folder="react/build")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/manifest.json")
def manifest():
    return send_from_directory('./build', 'manifest.json')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./build', 'favicon.ico')


if __name__ == '__main__':
    app.run()
