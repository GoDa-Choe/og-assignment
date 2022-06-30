from django.views.generic import ListView, DetailView, CreateView

from exhibition import models
from exhibition import forms
from django.urls import reverse_lazy


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
