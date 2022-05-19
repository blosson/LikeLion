from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist),  # 이거 해주고 터미널에 python manage.py runserver 입력해주어야 함
    path('first/', views.productfirst),
]