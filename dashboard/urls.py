from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    # path('artist/<int:pk>/', views.ArtistDashboard.as_view(), name='artist_dashboard'),
    path('artist/<int:pk>/', views.ArtistDashboard.as_view(), name='artist_dashboard'),
    # path('artist/<int:pk>/', views.ArtistExhibitionDashboard.as_view(), name='artist_exhibition_dashboard'),
]
