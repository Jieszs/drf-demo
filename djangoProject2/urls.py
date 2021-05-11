from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.musics import views

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    # 登入验证，使用JWT的模块，只要用户密码正确会自动生成一个token返回
    url(r'^login/', obtain_jwt_token),
]