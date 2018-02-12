from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def HelloPageView(request):
    return HttpResponse('Hello, World!')

class HomePageView(TemplateView):
    template_name = 'home.html'

class ShowTableView(TemplateView):
	template_name = 'tableView.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

# Create your views here.