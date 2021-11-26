from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('crud.urls')),
    path('crud/', include('crud.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='static/imagens/favicon.ico')),
]

