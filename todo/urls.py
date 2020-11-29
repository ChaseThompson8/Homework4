from django.urls import path
from .import views

urlpatterns = [
    path('', views.view_list, name="view_list"),
    path('update/<int:id>', views.update_task, name="update_task"),
    path('delete/<int:id>', views.delete_task, name="delete_task"),
    path('complete/<int:id>', views.complete, name="complete"),
    path('add', views.add, name="add")
]