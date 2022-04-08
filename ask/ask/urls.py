from django.contrib import admin
from qa.views import new_questions, pop_questions, index


# from django.urls import include, re_path

# urlpatterns = [
#     re_path(r'^$', new_questions, name='new_questions'),
#     re_path(r'question\/', include('qa.urls')),
#     re_path(r'^popular\/$', pop_questions, name='pop_questions'),
#     re_path(r'^new\/$', index),
#     re_path(r'^signup\/$', index),
#     re_path(r'^ask\/$', index),
# ]



from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', new_questions, name='new_questions'),
    url(r'question\/', include('qa.urls')),
    url(r'^popular\/$', pop_questions, name='pop_questions'),
    url(r'^new\/$', index),
    url(r'^signup\/$', index),
    url(r'^ask\/$', index),
]
