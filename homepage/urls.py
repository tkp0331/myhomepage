from django.urls import path
from . import views

app_name = "homepage"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('research/', views.ResearchView.as_view(), name='research'),
    path('career/', views.CareerView.as_view(), name='career'),
    path('materials/', views.MaterialsView.as_view(), name='materials'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    # path('b-detail/<int:pk>/', views.BDetailView.as_view(), name='b-detail'),
]
