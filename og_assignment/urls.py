from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='collection')),
    path('collection/', include('collection.urls')),
    path('exhibition/', include('exhibition.urls')),
    path('dashboard/', include('dashboard.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
