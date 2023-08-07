from django.urls import path

from auth.views import login_view

urlpatterns = [
    path('login/', login_view)
]
