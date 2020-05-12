from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, ProductQuerySet, ProductManager
from django.db.models import Q


# Create your views here.
class SearchProductListView(ListView):
    model = Product
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            lookups = Q(title__icontains=query)

            # return Product.objects.search(query)
            return Product.objects.filter(lookups).distinct()
        return Product.objects.none()
