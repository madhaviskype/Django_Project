from django.urls import path
from .import views

urlpatterns = [
    path('',views.teachers,name='teachersdata'),
    path('add/',views.add_teacher,name='addteacher'),
    path('edit/<int:id>/',views.update_teacher,name='updteteacher'),
    path('delete/<int:id>/',views.delete_teacher,name='delete')
]