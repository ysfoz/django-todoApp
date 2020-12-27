  
from django.urls import path
from .views import todo_list, add_todo,go_home, update_todo, delete_todo

urlpatterns = [
    path('', go_home, name='main'),
    path('list/',todo_list, name = 'list'),
    path('add/',add_todo,name = 'add'),
    path('<int:id>/update/',update_todo,name = 'update'),
    path('<int:id>/delete/',delete_todo,name = 'delete')
]