from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    browser_info = request.META['HTTP_USER_AGENT']
    return HttpResponse('Привет! Я знаю много информации о твоём браузере{}'.format(browser_info))

from django.views import generic
from .models import Product

class ProductListView(generic.ListView):

    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetail(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product