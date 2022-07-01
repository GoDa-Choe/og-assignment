from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect

from django.db.models import Q

from collection import models
from collection import forms


class ArtistListView(ListView):
    model = models.Artist
    template_name = 'collection/artist/list.html'
    context_object_name = 'artist_list'
    ordering = '-pk'
    paginate_by = 9

    def get_queryset(self):
        queryset = super(ArtistListView, self).get_queryset()
        return queryset.filter(is_confirmed='C')


class ArtistDetailView(DetailView):
    model = models.Artist
    template_name = 'collection/artist/detail.html'


class ArtistCreateView(LoginRequiredMixin, CreateView):
    model = models.Artist
    form_class = forms.ArtistForm
    template_name = 'collection/artist/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('collection:artist_detail', args=(self.object.pk,))


class SearchMixin(FormMixin):
    form_class = forms.ArtworkSearchForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        search_string = form.cleaned_data['search_string']
        return redirect(reverse_lazy('collection:artwork_search', args=(search_string,)))

    def form_invalid(self, form):
        return redirect(reverse_lazy('collection:artwork_list'))

    @staticmethod
    def get_keywords(search_string):
        """
        :param search_string: str
        :return keywords: List[str]

        verified test cases
        1. "aa bb cc"
        2. "#aa#bb#cc#"
        3. "#aa #bb #cc"
        -> ["aa", "bb", "cc"]
        """
        keywords = search_string.strip(" #").replace("#", " ").split()

        return keywords


class ArtworkListView(SearchMixin, ListView):
    model = models.Artwork
    template_name = 'collection/artwork/list.html'
    context_object_name = 'artwork_list'
    ordering = '-pk'
    paginate_by = 9


class ArtworkSearchView(ArtworkListView):
    def get_queryset(self):
        """
        :return queryset
        Big-O O(n + nlog(n))
        n: search by keyword
        nlong(n): sort by '-pk'
        """

        search_string = self.kwargs['search_string']
        search_keywords = self.get_keywords(search_string)

        lookups = []

        # O(n)
        for keyword in search_keywords:
            title_lookup = Q(title__contains=keyword)
            artist_lookup = Q(artist__name__contains=keyword)

            try:
                price_lookup = Q(price=int(keyword))  # search keyword = "이중섭"
                canvas_size_lookup = Q(canvas_size=int(keyword))
            except ValueError:
                lookups.append(title_lookup | artist_lookup)
            else:
                lookups.append(title_lookup | price_lookup | canvas_size_lookup | artist_lookup)

        # O(nlog(n))
        queryset = models.Artwork.objects.filter(*lookups).order_by('-pk').distinct()
        return queryset


class ArtworkDetailView(DetailView):
    model = models.Artwork
    template_name = 'collection/artwork/detail.html'


class ArtworkCreateView(LoginRequiredMixin, CreateView):
    model = models.Artwork
    form_class = forms.ArtWorkForm
    template_name = 'collection/artwork/create.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'artist'):
                if user.artist.is_confirmed == 'C':
                    return super(ArtworkCreateView, self).dispatch(request, *args, **kwargs)
                else:
                    return render(request=request, template_name='collection/artist/confirm_required.html')
            else:
                return redirect(reverse_lazy('collection:artist_create'))
        else:
            return super(ArtworkCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.artist = self.request.user.artist
        return super(ArtworkCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('collection:artwork_detail', args=(self.object.pk,))
