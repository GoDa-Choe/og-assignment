from django.urls import path

from exhibition import views

app_name = 'exhibition'

urlpatterns = [
    path('', views.ExhibitionListView.as_view(), name='list'),
    path('<int:pk>/', views.ExhibitionDetailView.as_view(), name='detail'),
    path('create/', views.ExhibitionCreateView.as_view(), name='create'),
]
