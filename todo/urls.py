from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addtodo/',views.addtodo,name='addtodo'),
    path('completed/',views.isCompleted,name='isCompleted'),
    path('delete/<str:id>',views.delete,name='delete')


]
