from qa.views import question_page


from django.urls import path, re_path

urlpatterns = [
	re_path(r'(?P<pk>\d+)\/$', question_page, name='question_page'),
]

# from django.conf.urls import include, url

# urlpatterns = [
#     url(r'(?P<pk>\d+)\/$', question_page, name='question_page')
# ]