from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models import Post, Tag
from .forms import PostForm
from app import db


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    # request for method POST
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        # Check title != None
        if title:
            try:
                post = Post(title=title, body=body)
                db.session.add(post)
                db.session.commit()
            except:
                print('Something wrong')
        
        # redirect to index page
        return redirect(url_for('posts.index'))

    # request for method GET
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    query = request.args.get('query')
    
    if query:
        posts = Post.query.filter(Post.title.contains(query) | Post.body.contains(query)).all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)