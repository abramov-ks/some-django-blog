from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "ITMO superstudent blog"
admin.site.site_title = "ITMO superstudent blog"
admin.site.index_title = "Administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

