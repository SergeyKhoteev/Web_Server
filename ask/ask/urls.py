from django.contrib import admin
from qa.views import new_questions, pop_questions, add_question_page, index
from ask.views import signup, login, logout
from source.views import index_start_view, share_start_view, company_start_view, indexes_start_page
from portfolios.views import new_portfolio, delete_symbol_from_portfolio, portfolio_page
from users.views import user_page

from django.urls import include, re_path, path

urlpatterns = [
    path('questions/', include('qa.urls')),
    path('indexes/', indexes_start_page, name='indexes_start_page'),
    path('indexes/<slug:ticker>/', index_start_view, name='index_start_view'),
    path('shares/<int:pk>/', share_start_view, name='share_start_view'),
    path('company/<int:pk>/', company_start_view, name='company_start_view'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('<slug:username>/', user_page, name='user_page'),
    path('<slug:username>/add/', new_portfolio, name='new_portfolio' ),
    path('<slug:username>/<int:portfolio_pk>/', portfolio_page, name='portfolio_page'),
    path('<slug:username>/<int:portfolio_pk>/delete/<int:port_struct_pk>', delete_symbol_from_portfolio, name='delete_symbol_from_portfolio'),
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
