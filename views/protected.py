from flask import Blueprint
from flask import request, jsonify
import services.users as user_service
import services.common as common_service

blueprint = Blueprint('protected', __name__, url_prefix='/protected')


@blueprint.before_request
def check_auth():
    # pass  # 测试模式下暂时不进行验证
    user = user_service.get_current_user()
    if not user:
        return {
            'success': False,
            'message': '请先登录！'
        }


@blueprint.route('/operations')
def find_all_operations():
    return jsonify(common_service.find_all_operations())


@blueprint.route('/basic_info')
def find_basic_info_by_es_no():
    es_no = int(request.args.get('es_no'))
    basic_info = common_service.find_basicInfo_by_esNo(es_no)

    return jsonify(basic_info)


@blueprint.route('/sensor_data')
def find_sensor_data():
    es_no = int(request.args.get('es_no'))
    point_id = int(request.args.get('point_id'))
    feature_id = int(request.args.get('feature_id'))

    sensor_data = common_service.find_sensor_data(es_no, point_id, feature_id)

    return jsonify(sensor_data)


@blueprint.route('/device_mode_counts')
def count_device_modes():
    stats = common_service.count_device_modes()
    return jsonify(stats)


@blueprint.route('/device_positions')
def get_device_positions():
    positions = common_service.get_device_positions()
    return jsonify(positions)


@blueprint.route('/test')
def get_protected_pages():
    return 'successfully get test page.'
