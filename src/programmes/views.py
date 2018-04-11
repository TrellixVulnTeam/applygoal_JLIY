from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Programme
from cart.models import Cart

def prog_list_view(request):
    queryset = Programme.objects.all()
    context = {
        'object_list':queryset
    }
    print(queryset)
    return render(request,"programmes/proglist.html",context)

def prog_detail_view(request,pk=None, *args, **kwargs):
    instance = Programme.objects.get_by_id(pk=pk)
    print(instance)
    context = {
        'object':instance
    }
    return render(request,"programmes/progdetail.html",context)

class ProgrammeDetailSlugView(DetailView):
    template_name="programmes/progdetail.html"
    queryset = Programme.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProgrammeDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Programme.objects.get(slug = slug)
        except Programme.DoesNotExist:
            raise Http404("Not found")
        except Programme.MultipleObjectsReturned:
            qs = Programme.objects.filter(slug = slug)
            instance = qs.first()
        except:
            raise Http404("nothing is wrong u are just dumb")
        return instance;
