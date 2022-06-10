from django.db import models
from django.db.models import Sum, F

from users.models import MyUser
from source.models import Shares as Shares_model
from source.models import ETF

# Create your models here.

class PortfolioManager(models.Manager):

	def port_content(self):

		content = PortfolioStructure.objects.filter(Portfolio=self)
		return content

class UserPortfolio(models.Model):

	Name = models.CharField(max_length=255, blank=True, null=True)
	Description = models.TextField(blank=True, null=True)
	Target = models.PositiveIntegerField(blank=True, null=True)
	IndexToFollow = models.ForeignKey(ETF, on_delete=models.SET_NULL, blank=True, null=True)
	Owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

	dt_created = models.DateTimeField(auto_now_add=True)
	dt_modified = models.DateTimeField(auto_now=True)

	objects = PortfolioManager()

	def get_absolute_url(self):

		from django.urls import reverse
		return reverse('portfolio_page', kwargs={'username': self.Owner.username, 'portfolio_pk' : self.id})

	def total_cost_market(self):

		portfolio = UserPortfolio.objects.get(pk=self.pk)
		content = PortfolioStructure.objects.filter(Portfolio=portfolio)

		count = content.aggregate(total=Sum(F('Symbol__market_price')*F('Quantity')))
		result = count.get('total')

		if result:
			return float(result)
		else:
			return float(0)

	def total_cost_user(self):

		portfolio = UserPortfolio.objects.get(pk=self.pk)
		content = PortfolioStructure.objects.filter(Portfolio=portfolio)

		count = content.aggregate(total=Sum(F('Cost')*F('Quantity')))
		result = count.get('total')

		if result:
			return float(result)
		else:
			return float(0)

	def total_change_abs(self):

		change = self.total_cost_market() - self.total_cost_user()
		return change

	def total_change_rel(self):

		try:
			change = (self.total_cost_market() / self.total_cost_user() * 100) - 100
		except ZeroDivisionError:
			change = 0.00
		return change

	def calculate_required_composition(self):
		etfstructuresymbols = self.IndexToFollow.etfstructure_set.select_related()
		for etfstructuresymbol in etfstructuresymbols:
			Symbol = etfstructuresymbol.share
			TargetSum = round(float(self.Target * etfstructuresymbol.weight / 100), 2)
			TargetQuantity = TargetSum / float(Symbol.market_price)
			record, created = PortfolioStructure.objects.get_or_create(Portfolio=self, Symbol=Symbol)

			if record.TargetSum != TargetSum or record.TargetQuantity != TargetQuantity:
				record.TargetSum = TargetSum
				record.TargetQuantity = TargetQuantity
				record.save()






class PortfolioStructure(models.Model):

	Symbol = models.ForeignKey(Shares_model, null=True, on_delete=models.SET_NULL)
	TargetSum = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	TargetQuantity = models.IntegerField(null=True)
	Quantity = models.PositiveIntegerField(default=0, null=True)
	Cost = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	TradeDate = models.DateField(null=True)
	Portfolio = models.ForeignKey('UserPortfolio', null=True, on_delete=models.SET_NULL)

	class Meta:

		unique_together = [['Symbol', 'Portfolio']]
		ordering = ['-TargetSum']


	def delete_symbol(portfolio_pk, symbol_pk):

		try:
			portfolio = UserPortfolio.objects.get(pk=portfolio_pk)
			symbol = Shares_model.objects.get(pk=symbol_pk)
			item = PortfolioStructure.objects.get(Portfolio=portfolio, Symbol=symbol)
			item.delete()
		except:
			return None
