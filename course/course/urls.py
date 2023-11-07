from django.contrib import admin
from django.urls import path
from notes.views import home, sections




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("sections/", sections, name="sections"),
    
]
