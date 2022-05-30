from django.contrib import admin
from qa.views import new_questions, pop_questions, add_question_page, index
from users.views import signup, login, logout


from django.urls import include, re_path, path

urlpatterns = [
    re_path(r'^$', new_questions, name='new_questions'),
    re_path(r'question\/', include('qa.urls')),
    re_path(r'^popular\/$', pop_questions, name='pop_questions'),
    re_path(r'^new\/$', index),
    re_path(r'^signup\/$', signup, name='signup'),
    re_path(r'login\/$', login, name='login'),
    re_path(r'^ask\/$', add_question_page, name='add_question_page'),
    path('logout', logout, name='logout')
]



# from django.conf.urls import include, url

# urlpatterns = [
#     url(r'^$', new_questions, name='new_questions'),
#     url(r'question\/', include('qa.urls')),
#     url(r'^popular\/$', pop_questions, name='pop_questions'),
#     url(r'^new\/$', index),
#     url(r'^signup\/$', signup, name='signup'),
#     url(r'login\/$', login, name='login'),
#     url(r'^ask\/$', add_question_page, name='add_question_page'),
# ]
