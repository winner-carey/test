from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models
from django.views import View


# Create your views here.


def index(request):
    return render(request, 'index.html')


def add_publish(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        models.Publish.objects.create(name=name, addr=addr, email=email)
        return redirect(reverse('publish_list'))

    return render(request, 'add_publish.html')


def publish_list(request):
    publish = models.Publish.objects.all()
    return render(request, 'publish_list.html', {"publish": publish})


def del_publish(request, nid):
    # nid = request.GET.get('nid')
    models.Publish.objects.filter(pk=nid).delete()
    return redirect(reverse('publish_list'))


def edit_publish(request, nid):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        models.Publish.objects.filter(nid=nid).update(name=name, addr=addr, email=email)
        return redirect(reverse('publish_list'))

    # nid = request.GET.get('nid')
    obj = models.Publish.objects.filter(nid=nid).first()
    return render(request, 'edit_publish.html', {'obj': obj})


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        pub_id = request.POST.get('pub')
        authors_id = request.POST.getlist('author')

        book = models.Book.objects.create(name=name, price=price, publish_date=pub_date, publish_id=pub_id)
        book.authors.add(*authors_id)

        return redirect(reverse('book_list'))

    author_list = models.Author.objects.all()
    pub_list = models.Publish.objects.all()
    return render(request, 'add_book.html', {'publish_list': pub_list, 'author_list': author_list})


def book_list(request):
    book_li = models.Book.objects.all()

    return render(request, 'book_list.html', locals())


def del_book(request, nid):
    # nid = request.GET.get('nid')
    models.Book.objects.filter(pk=nid).delete()

    return redirect(reverse('book_list'))


def edit_book(request, nid):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')

        publish_id = request.POST.get('publish')
        authors = request.POST.getlist('authors')

        # book_obj = models.Book.objects.filter(pk=nid)
        # book_obj.update(name=name, price=price, publish_date=publish_date,
        #                 publish_id=publish_id)
        # book_obj.first().authors.set(authors)
        models.Book.objects.filter(pk=nid).update(name=name, price=price, publish_date=publish_date,
                                                  publish_id=publish_id)
        book_obj = models.Book.objects.filter(pk=nid).first()
        book_obj.authors.set(authors)
        # book_obj.authors.clear()
        # book_obj.authors.add(*authors)

        return redirect(reverse('book_list'))

    publish_id = models.Publish.objects.all()

    author_id = models.Author.objects.all()

    # nid = request.GET.get('nid')
    book = models.Book.objects.filter(pk=nid).first()
    return render(request, 'edit_book.html', locals())


def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        models.Author.objects.create(name=name, age=age)
        return redirect(reverse('author_list'))

    return render(request, 'add_author.html')


def author_list(request):
    authors = models.Author.objects.all()

    return render(request, 'author_list.html', locals())


def del_author(request, nid):
    # nid = request.GET.get('nid')
    models.Author.objects.filter(pk=nid).delete()

    return redirect(reverse('author_list'))


def edit_author(request, nid):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        age = request.POST.get('age')
        models.Author.objects.filter(pk=nid).update(name=name, age=age)
        return redirect(reverse('author_list'))

    # nid = request.GET.get('nid')
    author = models.Author.objects.filter(pk=nid).first()
    return render(request, 'edit_author.html', locals())


def test(request):
    return HttpResponse('app01 de luyou')


# def login(request):
#     # return redirect(reverse('app01:n1'))
#     # return redirect(reverse('app02:n1'))
#     # return redirect(reverse('n1'))
#     return render(request, 'login.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        ff = request.FILES.get('myfile')

        with open(ff.name, 'wb') as f:
            for line in ff.chunks():
                f.write(line)

        return HttpResponse('上传成功')


def index1(request):
    return HttpResponse('index1')


def login1(request):
    name = request.GET.get('name')
    names = request.GET.getlist('name')
    print(name)
    print(names)
    return render(request, 'login.html')


def login2(request):
    dic = {'name': 'lqz', 'age': 18}
    li = [1, 2, 3, 4]

    import json
    from django.http import JsonResponse
    # return HttpResponse(json.dumps(dic))
    return JsonResponse(li, safe=False)
