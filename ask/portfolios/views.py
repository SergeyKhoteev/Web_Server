from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from portfolios.forms import AddPortfolioForm, AddSymbolToPortfolioForm
from portfolios.models import UserPortfolio, PortfolioStructure
from users.models import MyUser
from ask.views import MainMenu, SideMenu


# Create your views here.

def new_portfolio(request, username):

	if request._user is None:
		return redirect(reverse('login'))

	if request.method == 'POST':
		form = AddPortfolioForm(request._user, request.POST)
		if form.is_valid():
			portfolio = form.save_portfolio()
			return redirect('portfolio_page', username=request._user.username, portfolio_pk=portfolio.pk)
		else:
			form.add_error(None, 'Failed to add portfolio')
	else:
		form = AddPortfolioForm(request._user)
	
	context = {
	'User': request._user,
	'form': form
	}

	return render(request, 'portfolios/add_portfolio.html', context)


def my_portfolios(request, username):

	if not request._user:
		return redirect(reverse('login'))

	url_user = MyUser.objects.get(username=username)

	if request._user != url_user:
		raise PermissionDenied

	PortfolioList = UserPortfolio.objects.filter(Owner=request._user)

	context = {
	'User': request._user,
	'PortfolioList': PortfolioList,
	'MainMenu': MainMenu,
	'SideMenu': SideMenu
	}

	return render(
		request,
		'portfolios/my_portfolios.html',
		context)


def portfolio_page(request, username, portfolio_pk):

	if not request._user:
		return redirect(reverse('login'))
	
	Portfolio = UserPortfolio.objects.get(pk=portfolio_pk)
	PortfolioList = PortfolioStructure.objects.filter(Portfolio=Portfolio, TargetQuantity__gt=0)
	# PortfolioList = PortfolioList.filter(TargetQuantity__gt=0)

	if request.method == 'POST':
		add_symbol_form = AddSymbolToPortfolioForm(Portfolio, request.POST)
		if add_symbol_form.is_valid():
				add_symbol_form.save_symbol()
				return redirect('portfolio_page',username=request._user, portfolio_pk=portfolio_pk)

	else:
		add_symbol_form = AddSymbolToPortfolioForm(Portfolio)

	context = {
	'User': request._user,
	'PortfolioList': PortfolioList,
	'Portfolio': Portfolio,
	'form': add_symbol_form,
	}

	return render(
		request,
		'portfolios/portfolio_page.html',
		context)


def delete_symbol_from_portfolio(request, username, portfolio_pk, port_struct_pk):

	if not request._user:
		return redirect(reverse('login'))

	url_user = MyUser.objects.get(username=username)

	if request._user != url_user:
		raise PermissionDenied

	item = PortfolioStructure.objects.get(pk=port_struct_pk)
	item.delete()

	return redirect('portfolio_page', username=request._user.username, portfolio_pk=portfolio_pk)