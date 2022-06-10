from django.urls import path, re_path
from .views import new_portfolio, my_portfolios, portfolio_page, add_symbol_to_portfolio, delete_symbol_from_portfolio

urlpatterns = [
	path('add/', new_portfolio, name='new_portfolio' ),
	# path('', my_portfolios, name='my_portfolios'),
	path('<int:portfolio_pk>', portfolio_page, name='portfolio_page'),
	path('<int:portfolio_pk>/add_symbol/', add_symbol_to_portfolio, name='add_symbol_to_portfolio'),
	path('<int:portfolio_pk>/delete/<int:symbol_pk>', delete_symbol_from_portfolio, name='delete_symbol_from_portfolio'),
]