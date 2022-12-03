from models import db
from models import User


def find_user_by_id(userid):
    # return User.query.filter_by(id=userid).first()
    # return db.session.execute(db.select(User).filter_by(id=userid)).one()
    return db.session.execute(db.select(User).filter_by(id=userid)).scalar()  # 相当于first


def find_user_by_username_and_password(username, password):
    return db.session.execute(db.select(User).filter_by(username=username).filter_by(password=password)).scalar()
