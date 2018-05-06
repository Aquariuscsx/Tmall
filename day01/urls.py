from django.conf.urls import url

from day01 import views

urlpatterns = [
    url('render/', views.render_method),
    url('redirect/', views.redirect_method),


]
