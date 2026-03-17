from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CategoryListSerializers,
    ProductDetailSerializers,
    CategoryDetailSerializers,
    ProductListSerializers,
    ReviewListSerializers,
    ReviewDetailSerializers
)
from . import models


# 📌 Products + Reviews + Average rating
@api_view(['GET'])
def shop_products_with_reviews_view(request):
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


# 📌 Category list
@api_view(['GET'])
def shop_list_category_view(request):
    categories = models.Category.objects.all()
    data = CategoryListSerializers(categories, many=True).data

    for i, cat in enumerate(categories):
        data[i]['products_count'] = cat.products.count()

    return Response(data)


# 📌 Category detail (GET / PUT / DELETE)
@api_view(['GET', 'PUT', 'DELETE'])
def shop_detail_category_view(request, id):
    try:
        category = models.Category.objects.get(id=id)
    except models.Category.DoesNotExist:
        return Response({'error': 'not exist'}, status=404)

    if request.method == "GET":
        data = CategoryDetailSerializers(category).data
        data['products_count'] = category.products.count()
        return Response(data)

    if request.method == "DELETE":
        category.delete()
        return Response(status=204)

    if request.method == "PUT":
        serializer = CategoryDetailSerializers(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# 📌 Product list
@api_view(['GET'])
def shop_list_product_view(request):
    products = models.Product.objects.all()
    data = ProductListSerializers(products, many=True).data
    return Response(data)


# 📌 Product detail (GET / PUT / DELETE)
@api_view(['GET', 'PUT', 'DELETE'])
def shop_detatil_product_view(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response({'error': 'Не найден айди'}, status=404)

    if request.method == "GET":
        return Response(ProductDetailSerializers(product).data)

    if request.method == "DELETE":
        product.delete()
        return Response(status=204)

    if request.method == "PUT":
        serializer = ProductDetailSerializers(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# 📌 Review list
@api_view(['GET'])
def shop_list_review_view(request):
    reviews = models.Review.objects.all()
    data = ReviewListSerializers(reviews, many=True).data
    return Response(data)


# 📌 Review detail (GET / PUT / DELETE)
@api_view(['GET', 'PUT', 'DELETE'])
def shop_detatil_review_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response({'error': 'Не найден айди'}, status=404)

    if request.method == "GET":
        return Response(ReviewDetailSerializers(review).data)

    if request.method == "DELETE":
        review.delete()
        return Response(status=204)

    if request.method == "PUT":
        serializer = ReviewDetailSerializers(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)