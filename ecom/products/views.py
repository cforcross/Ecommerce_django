from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DetailView)
from django.http import Http404
from cart.models import Cart

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'products/product_feature_list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeatureDetailView(DetailView):
    template_name = 'products/feature_detail.html'

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list_view.html', context=context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # context['abc'] = 123
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exist")
    #     return instance


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)

    instance = Product.objects.get_by_id(pk)
    print(instance)
    qs = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.filter()
    else:
        raise Http404("Product doesn't exist")
    context = {
        'object_list': instance
    }
    return render(request, 'products/product_list_view.html', context=context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
