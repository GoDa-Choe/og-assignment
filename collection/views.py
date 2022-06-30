from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from collection import models
from collection import forms
from django.urls import reverse, reverse_lazy


class ArtistListView(ListView):
    model = models.Artist
    template_name = 'collection/artist/list.html'
    context_object_name = 'artist_list'
    paginate_by = 10


class ArtistDetailView(DetailView):
    model = models.Artist
    template_name = 'collection/artist/detail.html'


class ArtistCreateView(CreateView):
    model = models.Artist
    form_class = forms.ArtistForm
    template_name = 'collection/artist/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('collection:artist_detail', args=(self.object.pk,))


class ArtworkListView(ListView):
    model = models.Artwork
    template_name = 'collection/artwork/list.html'
    context_object_name = 'artwork_list'
    paginate_by = 10


class ArtworkDetailView(DetailView):
    model = models.Artwork
    template_name = 'collection/artwork/detail.html'


class ArtworkCreateView(CreateView):
    model = models.Artwork
    form_class = forms.ArtWorkForm
    template_name = 'collection/artwork/create.html'

    def form_valid(self, form):
        form.instance.artist = self.request.user.artist
        return super(ArtworkCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('collection:artwork_detail', args=(self.object.pk,))
