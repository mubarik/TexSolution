# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

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


