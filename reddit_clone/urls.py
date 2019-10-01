from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomepageView.as_view(), name="homepage"),
    path('accounts', include('accounts.urls', namespace='accounts')),
    path('accounts', include('django.contrib.auth.urls')),
]
