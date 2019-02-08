import json
from django.shortcuts import render

from .models import Product


def product_list_view(request):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)

    data = None
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", data)
    data = Product.objects.all()
    print("????????????????????????????????????????", data)

    return render(
        request,
        'products/index.html',
        {'object_list': data}
    )

def product_detail_view(request, pk):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)

    data = Product.objects.get(pk=pk)

    return render(
        request,
        'products/detail.html',
        {'object': data}
        # {'object': data[idx]}
    )