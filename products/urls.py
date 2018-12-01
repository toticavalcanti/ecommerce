from django.urls import path

from .views import (
                        ProductListView, 
                        #product_list_view, 
                        #ProductDetailView, 
                        ProductDetailSlugView,
                        #product_detail_view,
                        #ProductFeaturedListView,
                        #ProductFeaturedDetailView
                    )

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view())
]