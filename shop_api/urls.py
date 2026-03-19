from django.contrib import admin
from django.urls import path
from product.views import (
	ShopProductsWithReviewsView,
    ShopListCategoryView,
    ShopDetailCategoryView,
    ShopListProductView,
    ShopDetailProductView,
    ShopListReviewView,
    ShopDetailReviewView,
)

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('api/v1/categories/', views.shop_list_category_view),
#     path('api/v1/categories/<int:id>/', views.shop_detail_category_view),
    
#     path('api/v1/products/', views.shop_list_product_view),
#     path('api/v1/products/<int:id>/', views.shop_detatil_product_view),
    
#     path('api/v1/reviews/', views.shop_list_review_view),
#     path('api/v1/reviews/<int:id>/', views.shop_detatil_review_view),
    
#     path('api/v1/products/reviews/', views.shop_products_with_reviews_view)
# ]
# from product.views import (
# 	ShopProductsWithReviewsView,
#     ShopListCategoryView,
#     ShopDetailCategoryView,
#     ShopListProductView,
#     ShopDetailProductView,
#     ShopListReviewView,
#     ShopDetailReviewView,
# )
# from django.urls import path
# from .views import (
#     ShopProductsWithReviewsView,
#     ShopListCategoryView,
#     ShopDetailCategoryView,
#     ShopListProductView,
#     ShopDetailProductView,
#     ShopListReviewView,
#     ShopDetailReviewView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    # products + reviews
    path('api/v1/categories/', ShopProductsWithReviewsView.as_view()),

    # categories
    path('api/v1/categories/', ShopListCategoryView.as_view()),
    path('api/v1/categories/<int:id>/', ShopDetailCategoryView.as_view()),

    # products
    path('api/v1/products/', ShopListProductView.as_view()),
    path('api/v1/products/<int:id>/', ShopDetailProductView.as_view()),

    # reviews
    path('api/v1/reviews/', ShopListReviewView.as_view()),
    path('api/v1/reviews/<int:id>/', ShopDetailReviewView.as_view()),
]