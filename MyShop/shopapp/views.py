from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

# here we give decorator from rest framework
# this rest api take request and give response not a httpresponse


from .models import ProductTrali

from .serializer import ProductsSerializer


@api_view()
def Products(request):
    queryset = ProductTrali.objects.all()
    # here we give queryset in this serializer that's the reason we give many true
    serializer = ProductsSerializer(queryset, many=True)
    print(serializer)
    print(serializer.data)
    return Response(serializer.data)


# @api_view()
# def myprod(request, id):
#     return Response(id)


@api_view()
def myprod(request, id):
    # Product = ProductTrali.objects.get(pk=id)
    # instead of we need to use it
    # if value is not found then it will show status not found instead of giving error
    Product = get_object_or_404(ProductTrali, pk=id)
    # here we give object in this serializer
    serializer = ProductsSerializer(Product)
    return Response(serializer.data)
