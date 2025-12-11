from django.urls import path
from . import views 

urlpatterns = [
    path('home/',views.home, name='home'),
    path('',views.login_view,name = 'login'),
    path('signup/',views.signup_view,name='signup'),
    path('add/',views.add_view,name = 'add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name="delete")
]
