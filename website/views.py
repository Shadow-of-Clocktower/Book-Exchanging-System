from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
from .models import Book,User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
views=Blueprint('views',__name__)

# @login_required
# def home():
#     return render_template("home.html")
@views.route('/')
@views.route('/search/',methods=['GET','POST'])
@login_required
def search():
    users = User.query
    book = request.args.get('bookname')
    if book:
        books=Book.query.filter(Book.bookname.like('%'+book+'%')).all()
        return render_template("search.html",books=books,users=users)
        
    return render_template("search.html")



@views.route('/add',methods=['GET','POST'])
@login_required
def add():
    print(current_user)
    if request.method=="POST":       
        bookname=request.form.get('bookname')
        authorname=request.form.get('authorname')
        genre=request.form.get('genre')
        review=request.form.get('review')
        new_book=Book(bookname=bookname,authorname=authorname,genre=genre,review=review,user_id=current_user.id)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('views.home'))
    return render_template("add.html", user=current_user)
@views.route('/profile',methods=['GET'])
@login_required
def profile():
    return render_template("profile.html",user=current_user)

    

@views.route('/about',methods=['GET'])
def about():
    return render_template("about.html")

@views.route('/changePassword',methods=['PUT'])
def getValue():
    data=request.get_json()
    old=data["oldpwd"]
    new=data["newpwd"]
    res={
        "message":"successfully changed the password",
    
    }
    return jsonify(res)


