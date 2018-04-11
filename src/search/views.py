from django.shortcuts import render
from django.views.generic import ListView
from universities.models import University
from django.db.models import Q
# Create your views here.
class SearchListView(ListView):

    template_name="view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return University.objects.search(query)
        return University.objects.all()
