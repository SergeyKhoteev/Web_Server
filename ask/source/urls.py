from django.urls import path, re_path
from source.views import *

urlpatterns = [

	re_path(r'indexes/(?P<ticker>\w+)\/$', index_start_view, name='index_start_view'),
	re_path(r'shares/(?P<ticker>[\w\-]+)\/$', share_start_view, name='share_start_view'),
	path('company/<int:pk>/', company_start_view, name='company_start_view'),

	]
