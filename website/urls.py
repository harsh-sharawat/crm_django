
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logout_user, name= 'logout'),
    path('register/',views.register_user,name = 'register'),
    path('add_data/',views.add_data,name = 'add_data'),

    path('view-record/<int:pk>',views.view_record,name = 'view-record'),
    path('delete-record/<int:pk>',views.delete_record,name = 'delete-record'),
    path('edit-record/<int:pk>',views.edit_record,name = 'edit-record'),
    

    
]