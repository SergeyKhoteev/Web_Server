from django.contrib import admin
from . import views
from qa.views import new_questions, pop_questions


from django.urls import include, re_path

urlpatterns = [
    re_path(r'^$', new_questions, name='new_questions'),
    re_path(r'question\/', include('qa.urls')),
    re_path(r'^popular\/$', pop_questions, name='pop_questions'),
    # re_path(r'^new\/$', views.test),
    # re_path(r'^signup\/$', views.test),
    # re_path(r'^ask\/$', views.test),
]



# from django.conf.urls import include, url

# urlpatterns = [
#     url(r'^$', views.test),
#     url(r'^signup\/$', views.test),
#     url(r'^question\/\d*\/?', include('qa.urls')),
#     url(r'^ask\/$', views.test),
#     url(r'^popular\/$', views.test),
#     url(r'^new\/$', views.test),
# ]
