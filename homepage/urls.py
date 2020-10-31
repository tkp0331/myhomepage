from django.urls import path
from . import views

app_name = "homepage"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('research/', views.ResearchView.as_view(), name='research'),
    path('career/', views.CareerView.as_view(), name='career'),
    # path('/', views..as_view(), name=''),
    # path('/', views..as_view(), name=''),
]
