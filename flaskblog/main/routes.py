from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


'''
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
'''

#Se mostrara por inicio esta "/"
@main.route("/")
@main.route("/home")
def home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)  # recibe la pagina
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5) #paginate para que en la pagina no aparezcan todos
    return render_template('home.html', posts=posts)


'''
    posts = Post.query.paginate()
    dir(posts)

    for post in posts.items:
        print(post)
    <Post 1>
'''


@main.route("/about")
def about():
    return render_template('about.html', title="About")
