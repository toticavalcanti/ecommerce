from django.views.generic import ListView
from django.shortcuts import render

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

def product_list_view(request):
    context = {
        'qs': queryset
    }
    return render(request, "products/list.html", context)
