from django.conf.urls import url

from home import views

urlpatterns = [
#     url('cate/', views.get_cate),
    url('add/', views.add_photo),
    url('show/', views.show_photo),
    url('lunbo/', views.lunbo),
    url('cate/', views.get_cate),
    url('search/', views.search_shop),

]
