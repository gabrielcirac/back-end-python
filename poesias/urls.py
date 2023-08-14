from django.contrib import admin
from django.urls import path
from poesias.views import my_view, home, user_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', my_view),
    path('user/<str:username>/', user_view),
]