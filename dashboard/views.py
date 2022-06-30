from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied

from django.db.models import Count, Q, Max, Min, Avg, Sum

from collection.models import Artwork, Artist
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


class StaffDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/staff/dash.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return super(StaffDashboard, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(StaffDashboard, self).get_context_data(**kwargs)

        artist_list = Artist.objects.filter(is_confirmed='C').annotate(num_artworks=Count('artwork'))
        artist_list = artist_list.annotate(below_100=Count('artwork', filter=Q(artwork__canvas_size__lte=100)))
        artist_list = artist_list.annotate(min_price=Min('artwork__price'),
                                           max_price=Max('artwork__price'),
                                           avg_price=Avg('artwork__price'),
                                           sum_price=Sum('artwork__price'), )

        context['artist_list'] = artist_list
        context['artwork_list'] = Artwork.objects.all()
        context['waiting_list'] = Artist.objects.filter(is_confirmed='W').order_by('pk')
        context['confirmed_list'] = Artist.objects.filter(is_confirmed='C').order_by('pk')
        context['rejected_list'] = Artist.objects.filter(is_confirmed='R').order_by('pk')
        context['exhibition_list'] = Exhibition.objects.all()
        return context


def confirm_or_reject(request):
    if request.user.is_staff:
        if request.method == 'POST':
            for artist_pk in request.POST.getlist('artist_pks'):
                artist = get_object_or_404(Artist, pk=artist_pk)
                if artist.is_confirmed == 'W':
                    artist.is_confirmed = request.POST.get('action_type')
                    artist.save()
            return redirect(reverse('dashboard:staff'))
        else:
            return PermissionDenied
    else:
        raise PermissionDenied
