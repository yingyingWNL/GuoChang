from user import views
from django.urls import path

urlpatterns = [
    path('register/', views.Register.as_view()),  # 注册路由
    path('login/', views.Login.as_view()),  # 登录路由
    path('logout/', views.Logout.as_view()),  # 退出登录路由
    path('updatepassword/', views.UpdataPassword.as_view()),  # 退出登录路由
    path('getinfo/', views.GetInfo.as_view()),  # 获取用户信息
    path('statistics/', views.GetStatistics.as_view()),  # 获取后台统计数据
    path('normal/', views.GetStatistics.as_view()),  # 获取后台统计数据
    path('upload/', views.Upload.as_view()),  # 获取后台统计数据
    path('api/articles/recent', views.Temp.as_view()),  # 获取后台统计数据
]
