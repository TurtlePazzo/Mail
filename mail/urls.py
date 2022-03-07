from django.urls import path
from .views import *

app_name = 'mail'
urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('compose/', compose_view, name='compose_view'),
    path('email/<int:id>', email_view, name='email'),
    path('email/<int:id>/delete/', delete_email_view, name='delete'),
    path('email/<int:id>/toggle_archive/', toggle_archive_email_view, name='toggle_archive'),
    path('<str:mailbox>/', mailbox, name='mailbox'),
]