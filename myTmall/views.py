from django.shortcuts import render


# Create your views here.
from home.models import Category, Categorysub


def get_cate(request):
    cate_list = Category.objects.all()
    for cate in cate_list:
        Categorysub.objects.filter(cid=cate.id)
        cate.cate_sub_list = cate_list

    content = {
        'cate_list': cate_list
    }

    return render(request, 'home.html', content)
