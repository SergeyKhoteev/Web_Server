from django.db import models
from django.urls import reverse
import requests

class ETFManager(models.Manager):

	def show_content(self, ticker):

		index = self.get(ticker=ticker)
		content = index.etfstructure_set.select_related()
		content = content.order_by('-weight')


		return content


class ETF(models.Model):

	ticker= models.CharField(max_length=255, default='Unnamed index', unique=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.ticker

	def get_absolute_url(self):
		return reverse('index_start_view', kwargs={'ticker' : self.ticker})

	objects = ETFManager()


class Company(models.Model):

	company_name = models.CharField(max_length=255, blank=False, null=True, default='No longName')
	address = models.CharField(max_length=255, blank=False, null=True)
	city = models.CharField(max_length=255, blank=False, null=True)
	country = models.CharField(max_length=255, blank=False, null=True)
	website = models.CharField(max_length=255, blank=False, null=True)
	industry = models.CharField(max_length=255, blank=False, null=True)
	sector = models.CharField(max_length=255, blank=False, null=True)
	BusinessSummary = models.TextField(blank=False, null=True)
	# share = models.ForeignKey('Shares', on_delete=models.CASCADE)

	def __str__ (self):
		return self.company_name


class Shares(models.Model):

	ticker = models.CharField(max_length=6, blank=False, null=True, unique=True)
	index_sector = models.CharField(max_length=255, blank=False, null=True)
	index_short_name = models.CharField(max_length=255, blank=False, null=True)
	market_currency = models.CharField(max_length=255, blank=False, null=True)
	market_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	market_day_high = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	market_day_low = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	market_fiftyTwoWeekLow = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	market_fiftyTwoWeekHigh = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
	

	def __str__ (self):
		return self.ticker

	def get_absolute_url(self):
		return reverse('share_start_view', kwargs={'pk' : self.pk})


class ETFStructure(models.Model):

	index = models.ForeignKey('ETF', on_delete=models.CASCADE)
	share = models.ForeignKey('Shares', on_delete=models.CASCADE)
	weight = models.DecimalField(max_digits=8, decimal_places=5)
	dt_modified = models.DateTimeField(auto_now=True)

	class Meta:
		pass

	def __str__ (self):	
		return f'{self.share.ticker} in {self.index.ticker}'


def index_update(index_name):

	index_source_links = {
		'SP100': 'https://www.ishares.com/us/products/239723/ishares-sp-100-etf/1467271812596.ajax?tab=all&fileType=json',
		'SP500': 'https://www.ishares.com/us/products/239726/ishares-core-sp-500-etf/1467271812596.ajax?tab=all&fileType=json'
		}
	index_content = {}

	source_link = index_source_links.get(index_name, None)

	if source_link is not None:

		# Obtaining data from IShares source 

		req = requests.get(source_link)
	
		req.encoding = 'utf-8-sig'
		js = req.json()

		for key, values in js.items():
			for value in values:
				if value[3] == 'Equity':
					if value[0] == 'BRKB':
						value[0] = 'BRK-B'
					if value[0] == 'BFB':
						value[0] = 'BF-B'
					values_list = []
					values_list.append(value[1])
					values_list.append(value[2])
					values_list.append(value[5].get('raw', None))
					index_content.update({value[0]: values_list})

		# Updating of database
			
		index, index_created = ETF.objects.get_or_create(ticker=index_name)

		#  Removal of outdated index parts

		DB_ETF_STRUCTURE = ETFStructure.objects.filter(index = index)

		for structure_share in DB_ETF_STRUCTURE:
			if structure_share.share.ticker not in index_content.keys():
				print(f'share {structure_share.share.ticker} is not needed for {index.name}')
				structure_share.delete()

		# Updating data in shares realation

		for ticker in index_content.keys():
			share, share_created = Shares.objects.get_or_create(ticker=ticker)

			if share_created is True:
				share.index_sector = index_content.get(ticker)[1]
				share.index_short_name = index_content.get(ticker)[0]
				share.save()

			try:
				weight = ETFStructure.objects.get(index=index, share=share)
				if float(weight.weight) != float(index_content.get(ticker)[2]):

					weight.weight = index_content.get(ticker)[2]
					weight.save()

			except ETFStructure.DoesNotExist:
				
				ETFStructure.objects.get_or_create(index=index, share=share, weight=index_content.get(ticker)[2])
				print(f'new object created for index:{index} with share:{share.ticker}')

	else:
		print('source link corrupted or doesnot exist')


def all_shares_data_update():


	import requests
	url = "https://yfapi.net/v6/finance/quote"

	symbols = [symbol.ticker for symbol in Shares.objects.order_by('id')[:]]
	count = 1
	symbol_string = []

	for i in range(len(symbols)):

		if count <= 9 and i != (len(symbols) - 1):
			symbol_string.append(symbols[i])
			count += 1

		else:
			symbol_string.append(symbols[i])
			request_list = ','.join(symbol_string)
			querystring = {"symbols":request_list}
			print(querystring)

			count = 1
			symbol_string = []

			headers = {
			# 'x-api-key': "cBvXhkcniw5mlBV5W7YmxaFk1oXVwVxZ4pCpXrm4"
			'x-api-key': "Al5k0MVcbY1zWVF3V0Z3S55zdnDcZiH13Q6xhZZS"
			}

			response = requests.request("GET", url, headers=headers, params=querystring)

			if response.status_code == 200:

				print(response.status_code)

				js = response.json()

				js_response = js.get('quoteResponse', None)

				if js_response:
					js_response = js_response.get('result', None)
					if js_response:
						for share_data in js_response:
							company, created = Company.objects.get_or_create(company_name=share_data.get('longName', None))
							if created is True:
								company.company_name = share_data.get('longName', None)
								company.save()

							share = Shares.objects.get(ticker=share_data.get('symbol'))
							share.market_price = share_data.get('regularMarketPrice', None)
							share.market_currency = share_data.get('currency', None)
							share.market_day_high = share_data.get('regularMarketDayHigh', None)
							share.market_day_low = share_data.get('regularMarketDayLow', None)
							share.market_fiftyTwoWeekLow = share_data.get('fiftyTwoWeekLow', None)
							share.market_fiftyTwoWeekHigh = share_data.get('fiftyTwoWeekHigh', None)
							share.company = company
							share.save()
			else:

				status_code = response.status_code	
				print(f'status code is {status_code}')


def companies_data_creation():

	import requests

	shares_list = Shares.objects.all()

	for share in shares_list:

		company, created = Company.objects.get_or_create(share=share)

		if not company.sector:

			symbol = share.ticker
			url = f'https://yfapi.net/v11/finance/quoteSummary/{symbol}'

			headers = {
			'x-api-key': "c6xma5DaEQ8wJxDa5u8MNaHTWbdtLp6AaURUmTIo"
			}

			querystring = {
				'lang': 'en',
				'region': 'US',
				'modules': 'assetProfile'
			}

			response = requests.request("GET", url, headers=headers, params=querystring)

			if response.status_code == 200:

				js_response = response.json()

				js_response = js_response.get("quoteSummary", None)

				if js_response:
					js_response = js_response.get('result', None)

					if js_response:
						js_response = js_response[0].get('assetProfile', None)

						if js_response:

								company.address = js_response.get('address1', None)
								company.city = js_response.get('city', None)
								company.country = js_response.get('country', None)
								company.website = js_response.get('website', None)
								company.industry = js_response.get('industry', None)
								company.sector = js_response.get('sector', None)
								company.BusinessSummary = js_response.get('longBusinessSummary', None)
								company.save()

			else:
				print(response.status_code)
