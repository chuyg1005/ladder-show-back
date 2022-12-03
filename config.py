class Config:
    """flask app config object."""
    DEBUG = True
    SECRET_KEY = 'A_VERY_LONG_SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = "mysql://cyg:cyg123456@47.103.222.250:3306/escalator?charset=utf8"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
