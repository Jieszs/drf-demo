#### 环境准备
```
pip install django-filter
pip install django-cors-headers
pip install djangorestframework
pip install django

```

### 实现功能
1. 基础的CRUD
2. 跨域设置
3. 分页设置
4. 原生sql查询与修改更新
5. 异常统一处理
6. 查询条件的筛选
#### 后端：
```
django 3.2.2

django rest framework 3.12.4

django-filter 2.4.0

django-cors-headers 3.7.0
```
### 软件运行环境
```
Python 3.9

MySql 8.0
```

### 修改配置
```
vi rest_xops/settings.py 
# 修改数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drf-test',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': '3306',
    }
}
```

### 登陆MYSQL，创建数据库

```
CREATE DATABASE drf-test DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

### 执行创建表信息

```
python manage.py makemigrations 

python manage.py migrate
```
参考项目地址：
https://github.com/twtrubiks/django-rest-framework-tutorial
https://github.com/xufqing/rest_xops