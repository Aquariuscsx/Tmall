from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Banner, Category, Categorysub, Product


def add_photo(request):
    imgs = [Banner(img='/static/img/banner/banner01.jpg'), Banner(img='/static/img/banner/banner02.jpg'),
            Banner(img='/static/img/banner/banner03.jpg'),
            Banner(img='/static/img/banner/banner04.jpg'), Banner(img='/static/img/banner/banner05.jpg'),
            ]
    Banner.objects.bulk_create(imgs)

    return render(request, 'home.html')


def show_photo(request):
    imgs = Banner.objects.all()
    centent = {'imgs': imgs}
    return render(request, 'home01.html', centent)


def lunbo(request):
    return render(request, 'lunbo.html')


def get_cate(request):
    # 导航菜单
    cate_list = Category.objects.all()
    for cate in cate_list:
        cate_sub_list = Categorysub.objects.filter(cid=cate.id)
        cate.cate = cate_sub_list

    banner_list = Banner.objects.all()

    content = {
        'cate_list': cate_list,
        'banner_list': banner_list,
    }
    return render(request, 'home.html', content)

def search_shop(request):
    keywords = request.GET.get('keywords')
    product_list = Product.objects.filter(name__contains=keywords)
    return HttpResponse(serializers.serialize('list', product_list),content_type='application/json')
