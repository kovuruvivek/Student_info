from django.urls import path
from .views import student_form,thank_you,student_list,edit_details,delete_details,home

urlpatterns = [
    path('',home,name='home'),
    path('student_form/',student_form,name='student_form'),
    path('thank_you/',thank_you,name='thank_you'),
    path('student_list/',student_list,name='student_list'),
    path('edit_list/<int:sedit_id>/',edit_details,name='edit_list'),
    path('delete_details/<int:sdel_id>/',delete_details,name='delete'),

]