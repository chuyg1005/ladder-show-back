from models import Basic
from app import db
from app import app


def find_basic_by_esNo(es_no):
    basic_info = db.session.execute(db.select(Basic).filter_by(es_no=es_no)).scalar()

    return basic_info


def find_all_basics():
    return db.session.execute(db.select(Basic)).scalars()
    # return {
    #     'es_no': basic_info.es_no,
    #     'cc_no': basic_info.cc_no,
    #     'zc_no': basic_info.zc_no,
    #     'dtype': basic_info.dtype,
    #     'loc': basic_info.loc,
    #     'coord': basic_info.loc,
    #     'maker': basic_info.maker,
    #     'release_date': basic_info.release_date.strftime('%Y-%m-%d'),
    #     'install_date': basic_info.install_date.strftime('%Y-%m-%d'),
    #     'maintainer': basic_info.maintainer,
    #     'phone': basic_info.phone,
    #     'use_org': basic_info.use_org,
    #     'velocity': basic_info.velocity,
    #     'height': basic_info.height,
    #     'tilt_angle': basic_info.tilt_angle,
    #     'width': basic_info.width
    # }


if __name__ == '__main__':
    with app.app_context():
        print(find_basic_by_esNo(1))
