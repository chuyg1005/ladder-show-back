from app import app

from views import users
from views import protected

app.register_blueprint(users.blueprint)
app.register_blueprint(protected.blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 启动程序
