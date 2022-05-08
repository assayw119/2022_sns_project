from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# introduce view 함수
def showintroduce(request):
    info = Post.objects.all()
    return render(request, 'main/introduce.html')

# activities view 함수
def showactivities(request):
    activities = Post.objects.all()
    return render(request, 'main/activities.html', {'activities':activities})

# contact view 함수
def showfavorite(request):
    return render(request, 'main/favorite.html')

# contact view 함수
def showcontact(request):
    contact = Contact.objects.all()
    return render(request, 'main/contact.html')


def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_acti = Post()
    new_acti.acti_title = request.POST['acti_title']
    new_acti.acti_insert = request.POST['acti_insert']
    new_acti.acti_date = request.POST['acti_date']
    new_acti.save()
    return redirect('detail', new_acti.id)