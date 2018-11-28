from django.views.generic import ListView
from django.shortcuts import render

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


def product_list_view(request):
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)
