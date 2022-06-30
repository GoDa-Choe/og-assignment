from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

from collection.models import Artwork
from exhibition.models import Exhibition


class ArtistDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/artist/dash.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'artist'):
                if user.artist.pk == self.kwargs['pk']:
                    return super(ArtistDashboard, self).dispatch(request, *args, **kwargs)
                else:
                    raise PermissionDenied

            else:
                return redirect(reverse_lazy('collection:artist_create'))
        else:
            return super(ArtistDashboard, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ArtistDashboard, self).get_context_data(**kwargs)
        context['artist'] = self.request.user.artist
        context['artwork_list'] = Artwork.objects.filter(artist=self.request.user.artist)
        context['exhibition_list'] = Exhibition.objects.filter(artist=self.request.user.artist)
        return context
