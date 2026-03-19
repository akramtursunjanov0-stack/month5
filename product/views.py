from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from . import models
from .serializers import (
    CategoryListSerializers,
    ProductDetailSerializers,
    CategoryDetailSerializers,
    ProductListSerializers,
    ReviewListSerializers,
    ReviewDetailSerializers
)


class ShopProductsWithReviewsView(APIView):
    def get(self, request):
        products = models.Product.objects.prefetch_related('reviews').all()
        result = []

        for product in products:
            reviews = product.reviews.all()

            if reviews:
                avg = sum(r.stars for r in reviews) / len(reviews)
                avg = round(avg, 1)
            else:
                avg = None

            product_data = ProductListSerializers(product).data
            product_data['reviews'] = ReviewListSerializers(reviews, many=True).data
            product_data['average_rating'] = avg

            result.append(product_data)

        return Response(result)


class ShopListCategoryView(APIView):
    def get(self, request):
        categories = models.Category.objects.all()
        data = CategoryListSerializers(categories, many=True).data

        for i, cat in enumerate(categories):
            data[i]['products_count'] = cat.products.count()

        return Response(data)


class ShopDetailCategoryView(APIView):

    def get_object(self, id):
        return get_object_or_404(models.Category, id=id)

    def get(self, request, id):
        category = self.get_object(id)
        data = CategoryDetailSerializers(category).data
        data['products_count'] = category.products.count()
        return Response(data)

    def put(self, request, id):
        category = self.get_object(id)
        serializer = CategoryDetailSerializers(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShopListProductView(APIView):
    def get(self, request):
        products = models.Product.objects.all()
        data = ProductListSerializers(products, many=True).data
        return Response(data)


class ShopDetailProductView(APIView):

    def get_object(self, id):
        return get_object_or_404(models.Product, id=id)

    def get(self, request, id):
        product = self.get_object(id)
        return Response(ProductDetailSerializers(product).data)

    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductDetailSerializers(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShopListReviewView(APIView):
    def get(self, request):
        reviews = models.Review.objects.all()
        data = ReviewListSerializers(reviews, many=True).data
        return Response(data)


class ShopDetailReviewView(APIView):

    def get_object(self, id):
        return get_object_or_404(models.Review, id=id)

    def get(self, request, id):
        review = self.get_object(id)
        return Response(ReviewDetailSerializers(review).data)

    def put(self, request, id):
        review = self.get_object(id)
        serializer = ReviewDetailSerializers(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        review = self.get_object(id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)