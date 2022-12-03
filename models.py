# import app
from app import db
from app import app
import sqlalchemy
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """用户表"""
    __tablename__ = 't_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return f'id: {self.id}, username: {self.username}, password: {self.password}'


class Operation(db.Model):
    __tablename__ = 'operation'

    es_no = db.Column(db.SmallInteger, primary_key=True)
    mode = db.Column(db.Enum('0', '1', '2', '3'), name='fwms')
    status = db.Column(db.Enum('0', '1'), name='yxzt')
    direction = db.Column(db.Enum('0', '1', '2'), name='yxfx')
    err_code = db.Column(db.Enum('60', '61', '62', '63', '64', '65'), name='gzdm')

    thres11 = db.Column(db.Float)
    thres12 = db.Column(db.Float)
    thres13 = db.Column(db.Float)
    thres14 = db.Column(db.Float)
    thres15 = db.Column(db.Float)
    thres16 = db.Column(db.Float)

    thres21 = db.Column(db.Float)
    thres22 = db.Column(db.Float)
    thres23 = db.Column(db.Float)
    thres24 = db.Column(db.Float)
    thres25 = db.Column(db.Float)
    thres26 = db.Column(db.Float)

    thres31 = db.Column(db.Float)
    thres32 = db.Column(db.Float)
    thres33 = db.Column(db.Float)
    thres34 = db.Column(db.Float)
    thres35 = db.Column(db.Float)
    thres36 = db.Column(db.Float)

    thres41 = db.Column(db.Float)
    thres42 = db.Column(db.Float)
    thres43 = db.Column(db.Float)
    thres44 = db.Column(db.Float)
    thres45 = db.Column(db.Float)
    thres46 = db.Column(db.Float)

    thres51 = db.Column(db.Float)
    thres52 = db.Column(db.Float)
    thres53 = db.Column(db.Float)
    thres54 = db.Column(db.Float)
    thres55 = db.Column(db.Float)
    thres56 = db.Column(db.Float)

    def __str__(self):
        return f'es_no: {self.es_no}, mode: {self.mode}, status: {self.status},' \
               f' direction: {self.direction}, err_code: {self.err_code}'


class Basic(db.Model):
    __tablename__ = 'basic'

    # db = sqlalchemy
    es_no = db.Column(db.SmallInteger, primary_key=True)
    cc_no = db.Column(db.String(20))
    zc_no = db.Column(db.String(20))
    dtype = db.Column(db.String(20), name='xh')
    loc = db.Column(db.String(30), name='azdz')
    coord = db.Column(db.String(20), name='jwd')
    maker = db.Column(db.String(20), name='zzs')
    release_date = db.Column(db.Date, name='ccrq')
    install_date = db.Column(db.Date, name='azrq')
    maintainer = db.Column(db.String(20), name='wbdw')
    phone = db.Column(db.String(20), name='jydh')
    use_org = db.Column(db.String(20), name='sydw')
    velocity = db.Column(db.Float, name='mysd')
    height = db.Column(db.Float, name='tsgd')
    tilt_angle = db.Column(db.Float, name='qxj')
    width = db.Column(db.Float, name='mykd')

    def __str__(self):
        return f'es_no: {self.es_no}, cc_no: {self.cc_no}'


class Sensor(db.Model):
    __tablename__ = 'sensor'
    # db = sqlalchemy
    sensor_id = db.Column(db.Integer, primary_key=True)
    es_no = db.Column(db.SmallInteger)
    data_time = db.Column(db.DateTime)
    fea11 = db.Column(db.Float)
    fea12 = db.Column(db.Float)
    fea13 = db.Column(db.Float)
    fea14 = db.Column(db.Float)
    fea15 = db.Column(db.Float)
    fea16 = db.Column(db.Float)
    fea21 = db.Column(db.Float)
    fea22 = db.Column(db.Float)
    fea23 = db.Column(db.Float)
    fea24 = db.Column(db.Float)
    fea25 = db.Column(db.Float)
    fea26 = db.Column(db.Float)
    fea31 = db.Column(db.Float)
    fea32 = db.Column(db.Float)
    fea33 = db.Column(db.Float)
    fea34 = db.Column(db.Float)
    fea35 = db.Column(db.Float)
    fea36 = db.Column(db.Float)
    fea41 = db.Column(db.Float)
    fea42 = db.Column(db.Float)
    fea43 = db.Column(db.Float)
    fea44 = db.Column(db.Float)
    fea45 = db.Column(db.Float)
    fea46 = db.Column(db.Float)
    fea51 = db.Column(db.Float)
    fea52 = db.Column(db.Float)
    fea53 = db.Column(db.Float)
    fea54 = db.Column(db.Float)
    fea55 = db.Column(db.Float)
    fea56 = db.Column(db.Float)


if __name__ == '__main__':
    # db.create_all() # 创建数据表，required once
    # user = User(username='sjtu', password='ShiLab2022')
    # user = User(username='test', password='test')
    # db.session.add(user)
    # db.session.commit()
    # 查看系统中的所有用户
    # with app.app_context():
    #     users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    #     for user in users:
    #         print(user)
    with app.app_context():
        ops = db.session.execute(db.select(Sensor)).scalars()
        for op in ops:
            print(op.fea11)

