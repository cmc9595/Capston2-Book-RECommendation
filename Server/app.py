from flask import Flask, request, render_template, redirect, url_for
import k

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hi'

@app.route('/hello')
def hellohtml():
    return 'good'

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/recommend', methods=['GET', 'POST'])
def rec():
    if request.method == 'GET':
        string = str(request.args.to_dict())

        string = string.split("'")[1]
        string = string.strip("=")
        string = k.sentence_to_nouns(string)
        l=[]
        l = k.fetch_keywords(l)
        p=[]
        res = k.get_title_by_purchase_count(l, string, p)

        return res
    else:
        args_dict = request.args.to_dict()
        print(args_dict)

        return args_dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
