from django.urls import path
from . import views

urlpatterns = [
    path('', views.reverse_to_home),
    path('home',views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('profile-user', views.profile_user, name='profile-user'),
    path('create', views.create, name='create'),
    path('event/<int:event_id>', views.event, name='event'),
    path('<str:event_category>', views.events_by_category, name='event_category')
]

