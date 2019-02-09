import json
from django.shortcuts import (
    render, redirect
)

from .models import Product, Category
from .forms import CategoryForm, CategoryModelForm

from django.urls import reverse
from django.http import Http404

def product_list_view(request):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)

    data = Product.objects.all()

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


def category_create_view(request):
    form = CategoryModelForm()
    success_url = reverse('list')

    if request.method == 'POST':
        form = CategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()

            # obj = Category(
            #     name=form.cleaned_data.get("name"),
            #     description=form.cleaned_data.get("description")
            # )
            # obj.save()

            return redirect(success_url)

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )

def category_update_view(request, pk):
    print(11111111111111)
    try:
        obj = Category.objects.get(pk=pk)
        print(obj)
    except Exception as err:
        print("JOPAAAAAAAAA404")
        raise Http404

    form = CategoryModelForm(instance=obj)
    print("FORM:")
    print(form)
    success_url = reverse('list')

    print("success_url:")
    print(success_url)
    print(2222222222222222)


    if request.method == 'POST':
        print("request.method == 'POST' 55555555555555555")
        form = CategoryModelForm(
            request.POST,
            request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()

            return redirect(success_url)

    print(333333333333333333)


    return render(
        request,
        'categories/update.html',
        {'form': form}
    )