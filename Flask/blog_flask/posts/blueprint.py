from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_security import login_required

from models import Post, Tag
from .forms import PostForm
from app import db


# class instance blueprint, 'posts' == name for blueprint, __name__ == name file
posts = Blueprint('posts', __name__, template_folder='templates')


# function to create post who get methods POST and GET
@posts.route('/create', methods=['POST', 'GET'])
# decorator for login user
@login_required
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
    # form for create post
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


# function to edit post who get methods POST adn GET
@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
# decorator for login user
@login_required
def edit_post(slug):
	# define post which need edit by slug
	post = Post.query.filter(Post.slug==slug).first_or_404()

	if request.method == 'POST':
		# create form and fill it exist data
		form = PostForm(formdata=request.form, obj=post)
		# enter new data which use enter
		form.populate_obj(post)
		db.session.commit()

        # redirect to post_detail.html
		return redirect(url_for('posts.post_detail', slug=post.slug))

    # form for edit post
	form = PostForm(obj=post)
	return render_template('posts/edit_post.html', post=post, form=form)	


# function to define main way
@posts.route('/')
def index():
    # request for search
    query = request.args.get('query')
    # get number of page in url
    page = request.args.get('page')

    # define number of page for pagination
    if page and page.isdigit():
    	page = int(page)
    else:
    	page = 1
    
    # make request to find all posts
    if query:
        posts = Post.query.filter(Post.title.contains(query) | Post.body.contains(query)) # .all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    # difine quantity of pages on one page
    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', pages=pages)


# function which route us to post which choice
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    # request all tags of post
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


# function which route us to page with posts united one tag
@posts.route('/tag/<slug>')
def tag_detail(slug):
    # if slug invalid func route us to page 404
    tag = Tag.query.filter(Tag.slug==slug).first_or_404()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)