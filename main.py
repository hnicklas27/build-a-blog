from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blog@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(120))
    body = db.Column(db.Text)

    def __init__(self, title):
        self.title = title


@app.route('/newpost', methods=['GET','POST'])
def newpost():
    #if methods is POST
        name = request.form['name']
        entry = request.form['entry']
        error = ''
        if name == '' or entry == '':
            error = 'Please enter text'
            return render_template('newpost.html', error=error)
        else:
            new_post = Blog(name,entry)
            db.session.add(new_post)
            db.session.commit()


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