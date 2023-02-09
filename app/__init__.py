from flask import Flask
from flask_cors import CORS
import config
from app.user.view import user_bp
from exts import db

def create_app():
    app = Flask(__name__, static_folder='../static')  # 默认是找同级的文件夹，这里一定要调整
    app.config.from_object(config.DevelopmentConfig)
    db.init_app(app=app)
    # 初始化 app与映射关系产生关联
    CORS(app, supports_credentials=True)
    # csrf.init_app(user=user)
    app.register_blueprint(user_bp)

    return app
