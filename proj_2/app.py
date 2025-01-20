from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/")
def index():
    a = "saurav"
    mylist = [i for i in range(1,11)]
    return render_template("home.html",a=a,mylist=mylist)
@app.route("/other")
def other():
    return render_template("other.html")

@app.template_filter("rev")
def rev(s):
    return s[::-1]


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
