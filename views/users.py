from flask import Blueprint
from flask import request
import services.users as user_service
import json

blueprint = Blueprint('users', __name__, url_prefix='/users')


@blueprint.route('/login', methods=['POST'])
def login():
    data = json.loads(request.get_data(as_text=True))
    username = data['username']
    password = data['password']

    flag = user_service.login(username, password)

    return {'success': flag}


@blueprint.route('/logout', methods=['GET'])
def logout():
    flag = user_service.logout()
    return {'success': flag}


@blueprint.route('/current_user', methods=['GET'])
def get_current_user():
    user = user_service.get_current_user()
    # print(user)
    if not user:
        return {
            'success': False,
            'message': '用户还未登录！'
        }
    else:
        return {
            'success': True,
            'user': {
                'username': user.username
            }
        }
# @blueprint.route('/login_required_page', methods=['GET'])
# def get_login_required_page():
#     if not check_auth():
#         return {'success': False, 'message': "user doesn't login!"}
#     else:
#         return {'success': True}
# current_user = services.get_current_user()
# return str(services.get_current_user())
