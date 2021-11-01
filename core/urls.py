from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), name='blog'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('api/brl/', include('brl.urls'), name='blog_api'),
    path('api/blog/', include('blog_api.urls'), name='brl-api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/brl/', include('brl.urls'), name='blog_api'),
    path('api/v1/', include('api.urls') , name='main-api'),
]
