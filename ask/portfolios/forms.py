from django import forms
from django.db.utils import IntegrityError

from source.models import Shares, ETF
from portfolios.models import UserPortfolio, PortfolioStructure


class AddPortfolioForm(forms.Form):

	Name = forms.CharField(max_length=255)
	Description = forms.CharField(max_length=255, required=False)
	Target = forms.IntegerField()
	IndexToFollow = forms.ModelChoiceField(queryset=ETF.objects.all())

	def __init__(self, user,*args, **kwargs):
		self._user = user
		super(AddPortfolioForm, self).__init__(*args, **kwargs)

	def save_portfolio(self):
		self.cleaned_data['Owner'] = self._user
		portfolio = UserPortfolio.objects.create(**self.cleaned_data)
		return portfolio



class AddSymbolToPortfolioForm(forms.Form):

	Symbol = forms.ModelChoiceField(queryset=Shares.objects.all(), required=True)
	Quantity = forms.IntegerField(min_value=1, required=True)
	Cost = forms.DecimalField(decimal_places=2, required=False)
	TradeDate = forms.DateField(widget=forms.DateInput(), required=False)

	def __init__(self, portfolio, *args, **kwargs):
		self.portfolio = portfolio
		super(AddSymbolToPortfolioForm, self).__init__(*args, **kwargs)

	def save_symbol(self):
		self.cleaned_data['Portfolio'] = self.portfolio

		try:
			symbol = PortfolioStructure.objects.create(**self.cleaned_data)
		except IntegrityError:
			self.add_error(None, "Symbol with indicated tradedate already exists. Please change quantity")
			print(self.non_field_errors())

