from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('blog_post.html')


@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        text = request.form['text']
    return render_template('blog.html', text=text)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
