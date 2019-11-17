from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect



def bc(request):
    return render(request, 'bc/base.html', {})
# Create your views here.
