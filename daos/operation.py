from models import Operation
from app import db
from app import app
from sqlalchemy import func


def find_all_ops():
    ops = db.session.execute(db.select(Operation).order_by(Operation.es_no)).scalars()
    return ops
    # orders = []
    #
    # for op in ops:
    #     orders.append({
    #         'es_no': int(op.es_no),
    #         'mode': int(op.mode),
    #         'status': int(op.status),
    #         'direction': int(op.direction),
    #         'err_code': int(op.err_code)
    #     })
    #
    # return orders


def find_op_by_esNo(es_no):
    return db.session.execute(db.select(Operation).filter_by(es_no=es_no)).scalar()


def count_device_modes():
    return db.session.query(Operation.mode, func.count('*').label('count')).group_by(Operation.mode).all()


if __name__ == '__main__':
    with app.app_context():
        print(count_device_modes())
