from app import db, app
from models import Sensor


def find_data_by_esNo(es_no, limit=30 * 24):
    return db.session.execute(
        db.select(Sensor).filter_by(es_no=es_no).order_by(Sensor.data_time.desc()).limit(limit)).scalars()


if __name__ == '__main__':
    with app.app_context():
        data = find_data_by_esNo(1)
        for item in data:
            print(item.data_time)
