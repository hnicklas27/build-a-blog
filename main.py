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


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        name = request.form['name']
        blog = request.form['blog']
        new_post = Blog(name,blog)
        db.session.add(new_post)
        db.session.commit()

    blogs = Blog.query.all()
    return render_template('blog.html',title=title, 
        name=name , blog=blog)


@app.route('/blog', methods=['POST'])
def blogposts():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')

@app.route('/', methods=['POST','GET']) 
def index():
    return redirect('/blog')   


if __name__ == '__main__':
    app.run()