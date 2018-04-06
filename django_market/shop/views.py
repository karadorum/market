from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.views import generic
from shop.models import Product
from shop.models import User
from shop.models import Category
from shop.models import Order
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User



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


class CategoryDetailView(generic.DetailView):
    template_name = 'category_list.html'
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    

class ProductCreate(generic.CreateView): 
    model = Product 
    template_name = 'product_new.html' 
    fields = '__all__'
    

class OrderFormView(LoginRequiredMixin, generic.CreateView): 
      model = Order 
      template_name = 'order_form.html' 
      success_url = '/products' 
      fields = ['customer_name' , 'customer_phone']

    

      
      def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        #user = self.request.user
        user = User.objects.get(id = self.request.user.id)
        form.instance.user = user
        form.instance.product = product
        return super().form_valid(form)  

class SignUpView(generic.CreateView): 
        model = User
        form_class = UserCreationForm 
        success_url = reverse_lazy('login') 
        template_name = 'signup.html'

        
        


