from django.shortcuts import render
from django.http import HttpResponse
from unecorn.models import *


def index(request):

	contex = {
		"discounts": Discount.objects.get(),
		"categories": Category.objects.get()
	}

	ds = Discount.objects.get()
	return render(request, 'unecorn', contex)