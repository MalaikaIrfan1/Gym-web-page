from flask import Flask , render_template
app = Flask(__name__)

@app.route("/homepage")
def index():
    return render_template("homepage.html")

@app.route("/about")
def about():        
    return render_template("about.html")

@app.route("/member")
def member():
    return render_template("member.html")

if __name__ == '__main__':
    app.run(debug=True)