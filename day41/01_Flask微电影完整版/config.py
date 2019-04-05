# 数据库配置信息
import os

SQLALCHEMY_DATABASE_URI = "mysql://root:redhat@localhost/MovieProjectBak"
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 表单的配置(CSRF)
SECRET_KEY = "WESTOS"

# 用户上传信息存储位置的配置
BASEDIR = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目所在目录的绝对路径/root/PycharmProjects/day38_MovieProject
# /root/PycharmProjects/day38_MovieProject/app/static/upload/userFaceImg/
FC_DIR_LAST = 'upload/userFaceImg/'
FC_DIR = os.path.join(BASEDIR, 'app/static',FC_DIR_LAST )
# 电影文件保存位置
MOVIE_UP_DIR_LAST = 'upload/movieImg/'
MOVIE_UP_DIR = os.path.join(BASEDIR, 'app/static', MOVIE_UP_DIR_LAST)
# 预告文件保存位置
PREVIEW_UP_DIR_LAST = 'upload/previewImg/'
PREVIEW_UP_DIR = os.path.join(BASEDIR, 'app/static', 'upload/previewImg/')

# 分页的配置
PER_PAGE = 5
MOVIE_PER_PAGE = 12
