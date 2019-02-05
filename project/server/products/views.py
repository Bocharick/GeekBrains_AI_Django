import json
import os
from django.shortcuts import render

def products_list_view(request):
    with open("products/fixtures/data/data.json") as file:
        data = json.load(file)
        return render(
            request,
            'products/index.html',
            {'object_list': data}
        )
