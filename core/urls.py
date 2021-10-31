from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls'), name='blog'),
    path('api/', include('blog_api.urls'), name='blog_api'),
    path('admin/', admin.site.urls),
]
