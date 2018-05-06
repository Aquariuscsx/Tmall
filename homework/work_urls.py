from django.conf.urls import url

from homework import views

urlpatterns = [
    url('work/', views.get_cate),
    # url('work/', views.get_cate),


]
