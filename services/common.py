from app import app
import daos.basic as basic_dao
import daos.operation as op_dao
import daos.users as user_dao
import daos.sensor as sensor_dao


def find_all_operations():
    ops = op_dao.find_all_ops()
    result = []
    for op in ops:
        result.append({
            'es_no': op.es_no,
            'mode': int(op.mode),
            'status': int(op.status),
            'direction': int(op.direction),
            'err_code': int(op.err_code)
        })

    return result


def find_basicInfo_by_esNo(es_no):
    op = op_dao.find_op_by_esNo(es_no)
    basic = basic_dao.find_basic_by_esNo(es_no)

    return {
        'es_no': op.es_no,
        'mode': int(op.mode),
        'status': int(op.status),
        'direction': int(op.direction),
        'err_code': int(op.err_code),
        'cc_no': basic.cc_no,
        'zc_no': basic.zc_no,
        'dtype': basic.dtype,
        'loc': basic.loc,
        'coord': basic.coord,
        'maker': basic.maker,
        'release_date': basic.release_date.strftime('%Y-%m-%d'),
        'install_date': basic.install_date.strftime('%Y-%m-%d'),
        'maintainer': basic.maintainer,
        'phone': basic.phone,
        'use_org': basic.use_org,
        'velocity': basic.velocity,
        'height': basic.height,
        'tilt_angle': basic.tilt_angle,
        'width': basic.width
    }


def find_sensor_data(es_no, point_id, feature_id, limit=30 * 24):
    sensor_data = sensor_dao.find_data_by_esNo(es_no, limit)
    op = op_dao.find_op_by_esNo(es_no)
    assert 1 <= point_id <= 5
    assert 1 <= feature_id <= 6

    # 对数据进行处理
    total_data = {
        'times': [],
        'feat11': [op.thres11], 'feat12': [op.thres12], 'feat13': [op.thres13], 'feat14': [op.thres14],
        'feat15': [op.thres15], 'feat16': [op.thres16],
        'feat21': [op.thres21], 'feat22': [op.thres22], 'feat23': [op.thres23], 'feat24': [op.thres24],
        'feat25': [op.thres25], 'feat26': [op.thres26],
        'feat31': [op.thres31], 'feat32': [op.thres32], 'feat33': [op.thres33], 'feat34': [op.thres34],
        'feat35': [op.thres35], 'feat36': [op.thres36],
        'feat41': [op.thres41], 'feat42': [op.thres42], 'feat43': [op.thres43], 'feat44': [op.thres44],
        'feat45': [op.thres45], 'feat46': [op.thres46],
        'feat51': [op.thres51], 'feat52': [op.thres52], 'feat53': [op.thres53], 'feat54': [op.thres54],
        'feat55': [op.thres55], 'feat56': [op.thres56],
    }

    for item in sensor_data:
        # print(item.data_time, item.fea11)
        total_data['times'].append(item.data_time.strftime('%Y-%m-%d %H:%M:%S'))
        total_data['feat11'].append(item.fea11)
        total_data['feat12'].append(item.fea12)
        total_data['feat13'].append(item.fea13)
        total_data['feat14'].append(item.fea14)
        total_data['feat15'].append(item.fea15)
        total_data['feat16'].append(item.fea16)

        total_data['feat21'].append(item.fea21)
        total_data['feat22'].append(item.fea22)
        total_data['feat23'].append(item.fea23)
        total_data['feat24'].append(item.fea24)
        total_data['feat25'].append(item.fea25)
        total_data['feat26'].append(item.fea26)

        total_data['feat31'].append(item.fea31)
        total_data['feat32'].append(item.fea32)
        total_data['feat33'].append(item.fea33)
        total_data['feat34'].append(item.fea34)
        total_data['feat35'].append(item.fea35)
        total_data['feat36'].append(item.fea36)

        total_data['feat41'].append(item.fea41)
        total_data['feat42'].append(item.fea42)
        total_data['feat43'].append(item.fea43)
        total_data['feat44'].append(item.fea44)
        total_data['feat45'].append(item.fea45)
        total_data['feat46'].append(item.fea46)

        total_data['feat51'].append(item.fea51)
        total_data['feat52'].append(item.fea52)
        total_data['feat53'].append(item.fea53)
        total_data['feat54'].append(item.fea54)
        total_data['feat55'].append(item.fea55)
        total_data['feat56'].append(item.fea56)

    values = total_data[f'feat{point_id}{feature_id}']
    return {
        'title': f'测点{point_id}特征{feature_id}',
        'times': total_data['times'][::-1],
        'threshold': values[0],
        'values': values[1:][::-1]
    }


def count_device_modes():
    stats = op_dao.count_device_modes()
    stats = dict(stats)
    total_cnt = sum(stats.values())  # 获取总数
    for mode in ['0', '1', '2']:
        if mode in stats:
            stats[mode] = stats[mode] / total_cnt
        else:
            stats[mode] = 0.
    return stats


def get_device_positions():
    basics = basic_dao.find_all_basics()
    result = []
    for basic in basics:
        result.append({
            'name': f'设备{basic.es_no}',
            'value': list(map(float, basic.coord.split(',')))
        })

    return result


if __name__ == '__main__':
    with app.app_context():
        print(get_device_positions())
