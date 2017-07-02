from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blog@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'thisisasecret'


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(120))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/newpost', methods=['GET','POST'])
def newpost():
    if request.method == 'POST':
        blog_title = request.form['name']
        blog_body = request.form['body']
        if blog_title == '' or blog_body == '':
            flash('Please enter text')
            return redirect('/newpost')
        else:
            new_post = Blog(name,entry)
            db.session.add(new_post)
            db.session.commit()
            return redirect ('/')

    return render_template('newpost.html')


@app.route('/blog', methods=['GET'])
def blogposts():
    blogs = Blog.query.all()
    return render_template('blog.html',title=title, 
        name=name , body=body)


@app.route('/', methods=['GET']) 
def index():
    return redirect('/blog')   


if __name__ == '__main__':
    app.run()