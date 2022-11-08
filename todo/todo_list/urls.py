from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='login'),
    path('todos/',views.todos,name='todos'),
    path('logout/',views.signout,name='signout'),
    # path('todos/<str:todo_tle>/', views.todo_delete,name='todo_delete'),
#     path('todos/<str:todo_element>/',views.todo_delete)
 ]
