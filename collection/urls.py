from django.urls import path

from collection import views

app_name = 'collection'

urlpatterns = [
    path('', views.ArtworkListView.as_view(), name='index'),

    path('artist/', views.ArtistListView.as_view(), name='artist_list'),
    path('artist/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artist/create/', views.ArtistCreateView.as_view(), name='artist_create'),

    path('artwork/', views.ArtworkListView.as_view(), name='artwork_list'),
    path('artwork/<int:pk>/', views.ArtworkDetailView.as_view(), name='artwork_detail'),
    path('artwork/create/', views.ArtworkCreateView.as_view(), name='artwork_create'),

    path('artwork/search/<str:search_string>/', views.ArtworkSearchView.as_view(), name='artwork_search'),
]
