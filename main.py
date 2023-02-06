from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1> Hello World...! </h1>"


@app.route('/armstrong/<int:n>')
def armstrong(n):
    m = n
    sum1 = 0
    order = len(str(n))
    copy_n = n
    while n > 0:
        digit = n%10
        sum1 += digit**order
        n = n//10

    if sum1 == copy_n:
        print(f"{copy_n} is an armstrong number. ")
        result = {
            "Number": m,
            "armstrong number": True,
            "Server Id": f"http://127.0.0.1:5000/armstrong/{m}",
        }
    else:
        print(f"{copy_n} is not an armstrong number. ")
        result = {
            "Number": m,
            "armstrong number": False,
            "Server Id": f"http://127.0.0.1:5000/armstrong/{m}",
        }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
