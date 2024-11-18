from django.urls import path
from .views import HomeView,BlogdetailView,addCreateView,UpdatePost,DeletePost,addCategory,Categoryview,CategoryListview,Likeview,addComment
urlpatterns = [
    path('',HomeView.as_view(),name = "home"),
    path('details/<int:pk>/',BlogdetailView.as_view(),name="details"),
    path('update_post/<int:pk>',UpdatePost.as_view(),name = "update"),
    # path('update_all/',UpdatePost.as_view(),name = "update_all"),
    path('addpost/',addCreateView.as_view(),name = "addpost"),
    
    # path('deletepost/<int:pk>/remove',DeletePost.as_view(),name ="delete_post"),
    path('delete_post/<int:pk>',DeletePost.as_view(), name = "deletepost"),
    path('add_category/',addCategory.as_view(),name = "category"),
    path('category/<str:cat>/',Categoryview,name = "cat"),
    path('category-list/',CategoryListview,name = "categorylist"),
    path('like/<int:pk>',Likeview,name = "liked"),
    path('details/<int:pk>/comment/',addComment.as_view(),name="addcomment")

]
