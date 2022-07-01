from django.views.generic import ListView, DetailView, CreateView

from exhibition import models
from exhibition import forms
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class ExhibitionListView(ListView):
    model = models.Exhibition
    template_name = 'exhibition/list.html'
    paginate_by = 10


class ExhibitionDetailView(DetailView):
    model = models.Exhibition
    template_name = 'exhibition/detail.html'


class ExhibitionCreateView(CreateView):
    model = models.Exhibition
    form_class = forms.ExhibitionForm
    template_name = 'exhibition/create.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'artist'):
                if user.artist.is_confirmed == 'C':
                    if user.artist.artwork_set.exists():
                        return super(ExhibitionCreateView, self).dispatch(request, *args, **kwargs)
                    else:
                        return redirect(reverse_lazy('collection:artwork_create'))
                else:
                    return render(request=request, context={'artist': user.artist},
                                  template_name='collection/artist/confirm_required.html')
            else:
                return redirect(reverse_lazy('collection:artist_create'))
        else:
            return super(ExhibitionCreateView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        """to filter artworks by ownership"""

        kwargs = super(ExhibitionCreateView, self).get_form_kwargs()
        kwargs['artist'] = self.request.user.artist
        return kwargs

    def form_valid(self, form):
        form.instance.artist = self.request.user.artist
        return super(ExhibitionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('exhibition:detail', args=(self.object.pk,))
