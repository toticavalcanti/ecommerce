from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
	context = {
				"title": "Home Page",
				"content": "Bem vindo a Home Page"
			  }
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
				"title": "About Page",
				"content": "Bem vindo a About Page"
			  }
	return render(request, "about/view.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
				"title": "Contact Page",
				"content": "Bem vindo a Contact Page",
				"form": contact_form	
			  }
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request, "contact/view.html", context)

