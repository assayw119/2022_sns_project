from django.urls import path, include
from .views import *

app_name = 'main'
urlpatterns = [
    # introduce page URL 연결하기 with 별명사용
    path('', showintroduce, name="showintroduce"),

    # activities page URL 연결하기 with 별명사용
    path('activities/', showactivities, name="showactivities"),

    # favorite page URL 연결하기 with 별명사용
    path('favorite/', showfavorite, name="showfavorite"),

    # contact page URL 연결하기 with 별명사용
    path('contact/', showcontact, name="showcontact"),

    path('<int:id>', detail, name='detail'),

    path('new/', new, name='new'),
    
    path('create/', create, name='create'),

    path('edit/<int:id>', edit, name='edit'),

    path('update/<int:id>', update, name='update'),

    path('delete/<int:id>', delete, name='delete'),

    path('<str:post_id>/create_comment', create_comment, name='create_comment'),
]