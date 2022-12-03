from app import login_manager
from flask_login import login_user, logout_user, current_user
import daos.users as user_dao


@login_manager.user_loader
def load_user(userid):
    return user_dao.find_user_by_id(userid)


def login(username, password):
    user = user_dao.find_user_by_username_and_password(username, password)
    if not user: return False  # 登录失败
    login_user(user)
    return True


def logout():
    logout_user()
    return True


def get_current_user():
    # return current_user
    is_login = current_user.is_authenticated
    if not is_login: return None
    else: return current_user
