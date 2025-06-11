from django.urls import path, include

urlpatterns = [
    path('', include('allauth.urls')),  # Delegar a django-allauth
]

