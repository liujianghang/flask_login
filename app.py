from flask_script import Manager
# flask_script的第十五行改一下 改成from flask_script._compat import text_type
from flask_migrate import Migrate, MigrateCommand  # 特别注意版本为2.7.0
from app import create_app
from app.user.models import User
from exts import db

# 应用工程模式创建
app = create_app()


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


manager = Manager(app)
# app与db产生命令
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
# 脚本形式启动
manager.run()  # python app.py runserver -h 0.0.0.0 -p 5000
# root/flask_login/venv/lib/python3.11/site-packages/flask_script/__init__.py
