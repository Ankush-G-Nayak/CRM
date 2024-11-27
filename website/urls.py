from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('record/<int:pk>',views.record,name='record'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('updrec/<int:pk>',views.updrec,name='updrec'),
    path('addrec',views.addrec,name='addrec'),
    path('reset/', views.reset_table, name='reset_table'),
]
