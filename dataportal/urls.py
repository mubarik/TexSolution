from django.conf.urls import url

from . import views
from .views import upload_file

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='product_list'),
  	url(r'^new$', views.ProductCreate.as_view(), name='product_new'),
  	url(r'^edit/(?P<pk>\d+)$', views.ProductUpdate.as_view(), name='product_edit'),
  	url(r'^delete/(?P<pk>\d+)$', views.ProductDelete.as_view(), name='product_delete'),
  	url(r'^import/data/$', upload_file, name='upload_file'),
]