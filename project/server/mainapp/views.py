from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # template = Template(
    #     'Hello {{ name }}'
    # )
    # context = Context({
    #     'name': 'Anton'
    # })
    template = get_template(
        'mainapp/index.html'
    )
    context = {
        'name': 'Proverka'
    }
    return HttpResponse(
        template.render(context)
    )
    # return render(
    #     request,
    #     'main/index.html'
    # )

def about(request):
    return render(
        request,
        'mainapp/about.html'
    )

def contacts(request):
    rendered_page = render_to_string(
        'mainapp/contacts.html',
        {
            'contacts': [
                'Контакт 1',
                'Контакт 2',
                'Контакт 3',
                'Контакт 4',
                'Контакт 5',
                'Контакт 6',
                'Контакт 7',
                'Три раза по трубе'
            ]
        }
    )
    return HttpResponse(
        rendered_page
    )
    # return render(
    #     request,
    #     'mainapp/contacts.html'
    # )