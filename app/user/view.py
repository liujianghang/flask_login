import time

from flask import Blueprint, request, jsonify, g
from werkzeug.security import generate_password_hash, check_password_hash

from app.user.utils import create_token, validate_token
from exts import db

user_bp = Blueprint('user', __name__, url_prefix='/user')

from app.user.models import User


@user_bp.before_request
def before_request():
    # 来的时候先校验，有token就加g，没有就不加
    payload, msg = validate_token(request.headers.get('token'))
    # print(payload)
    if payload is not None and msg == '成功':
        user = User.query.filter(User.id == payload.get('user_id')).first()
        g.user = user


@user_bp.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        if hasattr(g, 'user'):  # 已经登录了
            return jsonify(code=200, msg='已经登陆了')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        flag = check_password_hash(user.password, password)  # 判断是否一致
        if flag:
            g.user = user
            return jsonify(code=200, msg='登录成功')
        return jsonify(code=403, msg='用户名有误或密码错误')
    return jsonify(code=403, msg='登陆失败')


@user_bp.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User()
        user.username = username
        user.password = generate_password_hash(password)
        user.email = email
        db.session.add(user)  # 缓存
        db.session.commit()  # 提交
        return jsonify(code=200, msg='注册成功')
    return jsonify(code=403, msg='注册失败')


@user_bp.route('getUserInfo')
def user_info():
    if hasattr(g, 'user'):  # 已经登录了
        user = User.query.filter(User.username == g.user.username).first()
        return jsonify(code=200, msg='成功返回用户信息', username=user.username)
    else:
        return jsonify(code=403, msg='失败返回用户信息', username='')


@user_bp.after_request
def after_request(response):
    if hasattr(g, 'user'):  # 登陆了
        token = create_token(g.user)
        response.headers['token'] = token
        return response
    else:
        response.headers['token'] = ''
        return response
