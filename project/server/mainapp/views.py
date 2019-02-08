from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import render_to_string, get_template
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        'mainapp/index.html'
    )

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