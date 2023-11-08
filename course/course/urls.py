from django.contrib import admin
from django.urls import path
from notes.views import home, sections, sections_detail, redirect_to_section_list, search_notes, non_numeric_notes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("sections/", sections, name="sections"),
    path("notes/<str:text_passed>/", sections_detail, name="sections_detail"),
    path("notes/", redirect_to_section_list, name="redirect_to_section_list"),
    path("search/<str:search_term>/", search_notes, name="search_notes"),    
    path("nonnumeric/<str:non_numeric_string>/", non_numeric_notes, name="non_numeric_notes"),
]
