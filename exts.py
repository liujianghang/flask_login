# 创建一个映射对象
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_wtf import CSRFProtect
from flask_restful import Api

# 第三方库
db = SQLAlchemy()
cache = Cache()
csrf = CSRFProtect()
api = Api()
