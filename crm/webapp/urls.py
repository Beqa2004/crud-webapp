from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name='register'),
    path("my-login", views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name='user-logout'),

    #CRUD
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-record', views.create_record, name='create-record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'), #დინამიური ურლ <int:pk> - int იჭერს ინტერჯერს და აზუსტებს რომ URL უნდა იყოს ინტეჯერი,
    path('record/<int:pk>', views.view_record, name='record'),# pk აზუსტებს ცვლადის სახელს რომელიც გადაეცემა ვიუს ფუნქციას
    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),
]                                                                              
