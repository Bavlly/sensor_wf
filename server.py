from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/index')
def index():
    return render_template('./index.html')

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('./index.html', name=username, post_id=post_id)

@app.route('/about')
def about():
    return render_template('./about.html')

@app.route('/blog/2020/dogs')
def blog2():
    return 'This will be a blog 2020'