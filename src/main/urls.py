from django.urls import path
from .views import main_view,profile_view
# from .views import profile_view
urlpatterns = [
    path('', main_view, name='home'),
    path('profile/', profile_view, name='profile'),
]
