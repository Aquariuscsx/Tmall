from django.shortcuts import render

# Create your views here.
from homework.models import Category, Categorysub, Banner


def get_cate(request):
    cate_list = Category.objects.all()
    for cate in cate_list:
        cate_sub_list = Categorysub.objects.filter(cid=cate.id)
        cate.cate_sub_list = cate_sub_list

    banner_list = Banner.objects.all()

    content = {
        'cate_list': cate_list,
        'banner_list': banner_list
    }

    return render(request, 'homework/homework.html', content)
