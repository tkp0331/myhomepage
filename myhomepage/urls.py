from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("homepage.urls")),  # 何にでもマッチすると思うと分かりやすい
]
