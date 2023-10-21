from django.urls import path, include
from .views import (AlbumView, MusicianView, CategoryView, TagView, ArticleView)

urlpatterns = [
    #ArticleView
    path('articles/', ArticleView.as_view({'get': 'list', 'post': 'create'}), name = 'Article-list'),
    path('articles/<int:id>', ArticleView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}), name = 'Article-detail'),
    #TagView
    path('tags/', TagView.as_view({'get' : 'list', 'post' : 'create'}), name = 'Tags-list'),
    path('tags/<int:id>', TagView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}), name = 'Tag-detail'),
    #CategoryView
    path('categories/', CategoryView.as_view({'get': 'list', 'post': 'create'}), name = 'Category-list'),
    path('categories/<int:id>', CategoryView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}), name = 'Category-detail'),
    #AlbumView {NOT PART OF THE ACTIVITY AT THIS MOMENT. I JUST INCLUDED IT JUST IN CASE.}
    path('albums/', AlbumView.as_view({'get': 'list', 'post': 'create'}), name= 'Album-list'),
    path('albums/<int:id>', AlbumView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}), name='Album-detail'),
    #MusicianView {NOT PART OF THE ACTIVITY AT THIS MOMENT. I JUST INCLUDED IT JUST IN CASE.}
    path('musicians/', MusicianView.as_view({'get': 'list', 'post': 'create'}), name = 'Musician-list'),
    path('musicians/<int:id>', MusicianView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}), name = 'Musician-detail')
]
