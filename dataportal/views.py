# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import ProductForm, UploadFileForm
import csv
from datetime import timedelta, datetime

from .models import Product

class ProductList(ListView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy('product_list')
    fields = ['p_id', 'p_description', 'p_datetime' , 'p_longitude' , 'p_latitude' , 'p_elevation']

class ProductUpdate(UpdateView):
    model = Product
    success_url = reverse_lazy('product_list')
    fields = ['p_id', 'p_description', 'p_datetime' , 'p_longitude' , 'p_latitude' , 'p_elevation']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

def format_datetime(time):
    strs = time
    #replace the last ':' with an empty string, as python UTC offset format is +HHMM
    strs = strs[::-1].replace(':','',1)[::-1]
    try:
        offset = int(strs[-5:])
    except:
        print "Error"

    delta = timedelta(hours = offset / 100)

    time = datetime.strptime(strs[:-5], "%Y-%m-%dT%H:%M:%S")
    time -= delta                #reduce the delta from this time object

    return time    

def import_data():
    with open('files_static/import.txt', 'rU') as f:
        for row in csv.reader(f.read().splitlines()[1:]):
            data = row[0].split('\t')
            time = format_datetime(data[2])
            obj, flag = Product.objects.get_or_create(
                                product_id = data[0],
                                description = data[1],
                                datetime = time,
                                longitude = data[3],
                                latitude = data[4],
                                elevation = data[5]
            )
    return True

def handle_uploaded_file(f):
    with open('files_static/import.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            import_data()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'dataportal/import_data.html', {'form': form})
