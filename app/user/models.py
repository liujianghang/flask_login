from datetime import datetime
from exts import db


class User(db.Model):
    # db.Column(类型，约束) 映射表中的类
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(32))
    icon = db.Column(db.String(100))
    isdelete = db.Column(db.Boolean, default=False)  # 逻辑删除
    registerTime = db.Column(db.DateTime, default=datetime.now)
    # 增加一个字段, 建立两张表之间有外键 关系

    def __str__(self):
        return self.username