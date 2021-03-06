from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('artist/<int:pk>/', views.ArtistDashboard.as_view(), name='artist'),

    path('staff/', views.StaffDashboard.as_view(), name='staff'),
    path('staff/confirm_or_reject/', views.confirm_or_reject, name='confirm_or_reject'),

]
