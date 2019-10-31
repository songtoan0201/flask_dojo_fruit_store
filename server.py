from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    date = datetime.now()

    sum = int(strawberry) + int(raspberry) + int(apple)
    return render_template("checkout.html", strawberry=strawberry, date=date,raspberry=raspberry, apple=apple, first_name=first_name, last_name=last_name, student_id=student_id, sum=sum)


@app.route('/fruits')
def fruits():
    print(request.form)
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
