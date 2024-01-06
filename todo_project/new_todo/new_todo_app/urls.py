from django.contrib import admin
from django.urls import path, include

from. import views

urlpatterns = [
     # path('',views.home,name="home"),
    path("",views.TasklistView.as_view(),name='cbvhome'),
path("cbvdetail/<int:pk>/",views.TaskdetailView.as_view(),name='cbvdetail'),
path("cbvupdate/<int:pk>/",views.TaskupdateView.as_view(),name='cbvupdate'),
path("cbvdelete/<int:pk>/",views.TaskdeleteView.as_view(),name='cbvdelete')

]
