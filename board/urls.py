from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path(r'', views.MainPageLV.as_view()),
    path(r'create', create_new),
    path(r'detail/<int:b_id>/', detail, name='detail'),
    path(r'update/<int:b_id>', update, name='update'),
    path(r'delete/<int:b_id>', delete, name='delete'),
    path(r'accounts/signup', create_user, name='signup'),
    path(r'accounts/login', sign_in, name='login'),
    path(r'accounts/logout', sign_out, name='logout')

]