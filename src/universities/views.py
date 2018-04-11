from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.

from .models import University

class UniversityListView(ListView):
    queryset = University.objects.all()
    template_name="universities/unilist.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return University.objects.all

def university_list_view(request):
    queryset = University.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request,"universities/unilist.html",context)

class UniversityDetailView(DetailView):
    template_name="universities/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityDetailView,self).get_context_data(*args,**kwargs)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = University.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Not such a university")
        return instance
        print("aaaaaaa")
        print(instance)


def university_detail_view(request,pk=None, *args, **kwargs):
    instance = University.objects.get_by_id(pk=pk)
    print(instance)
    context = {
        'object':instance
    }
    return render(request,"universities/detail.html",context)

class UniversityDetailSlugView(DetailView):
    template_name="universities/detail.html"
    queryset = University.objects.all()

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = University.objects.get(slug = slug)
        except University.DoesNotExist:
            raise Http404("Not found")
        except University.MultipleObjectsReturned:
            qs = University.objects.filter(slug = slug)
            instance = qs.first()
        except:
            raise Http404("nothing is wrong u are just dumb")
        return instance;
