from django.shortcuts import render
from source.models import ETF, Shares, Company
from django.http import HttpResponseNotFound, Http404, HttpResponse, HttpResponseRedirect
from django.template import loader

from ask.views import MainMenu, SideMenu


# Create your views here.


def indexes_start_page(request):

	ETFList = ETF.objects.all()

	context = {
	'User' : request._user,
	'MainMenu' : MainMenu,
	'SideMenu': SideMenu,
	'ETFList' : ETFList,
	} 

	return render( request,
		'source/start_page.html',
		context
		)

def index_start_view(request, ticker):

	try:
		shares_list = ETF.objects.show_content(ticker)
		index = ETF.objects.get(ticker = ticker)
		context = {
		'MainMenu' : MainMenu,
		'SideMenu': SideMenu,
		'index' : index,
		'shares_list' : shares_list,} 

		return render(
			request, 
			'source/index.html',
			context
			)

	except ETF.DoesNotExist:
		raise Http404

def share_start_view(request, pk):

	try:
		share = Shares.objects.get(pk=pk)

		return render(
			request,
			'source/share_base_template.html',
			{'share' : share}
			)

	except Shares.DoesNotExist:
		raise Http404

def company_start_view(request, pk):

	try:
		company = Company.objects.get(pk=pk)

		return render(
			request,
			'source/company_base_template.html',
			{'company' : Company}
			)

	except Company.DoesNotExist:
		raise Http404