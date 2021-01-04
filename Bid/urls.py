from django.contrib import admin
from django.urls import path, include
from . import views

appname = 'Bids'
urlpatterns = [
    path('',views.index, name= 'index'),
    path('home_page/',views.home_page, name = 'home_page'),
    path('<int:id>/user_home_page/',views.user_home_page, name = 'user_home_page'),

    path('<int:id>/new_post/',views.new_post, name = 'new_post'),
    path('<int:id>/new_post_validator/',views.new_post_validator, name = 'new_post_validator'),
    

    path('<int:user_id>/<int:bid_id>/bid_detail/',views.bid_detail, name = 'bid_detail'),
    path('<int:user_id>/<int:bid_id>/bid/',views.bid, name = 'bid'),

    path('to_login_form/',views.to_login_form, name ='to_login_form'),
    path('login_validator/',views.login_validator, name ='login_validator'),

    path('to_sing_in_form/',views.to_sing_in_form, name ='to_sing_in_form'),
    path('sign_in_validator/',views.sign_in_validator, name ='sign_in_validator'),
]