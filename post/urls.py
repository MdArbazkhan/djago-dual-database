from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user , name='login-page'),
    path('landing', views.landingpage, name='landing-page'),
    path('logout', views.logout_user, name='logout-url'),
    path('add', views.addNewPost, name='add-new-post'),
    path('list', views.list, name='list'),
    path('edit/<str:post_id>', views.edit, name='edit')
]