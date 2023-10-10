from cropdata import views
from django.urls import path

urlpatterns = [
    path('ishealth/', views.IsHealth.as_view()),  # 注册路由
    path('prevent/', views.Prevent.as_view()),  #
    path('allprevent/', views.AllPrevent.as_view()),  #
    path('predict/temperature/', views.PredictTemperature.as_view()),  #
    path('predict/humidity/', views.PredictHumidity.as_view()),  #

]
