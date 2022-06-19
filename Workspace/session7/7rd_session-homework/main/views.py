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
    contact = Post.objects.all()
    return render(request, 'main/contact.html')


def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_acti = Post()
    new_acti.writer = request.user
    new_acti.acti_title = request.POST['acti_title']
    new_acti.acti_insert = request.POST['acti_insert']
    new_acti.acti_date = request.POST['acti_date']
    new_acti.acti_image = request.FILES.get('acti_image')
    new_acti.save()
    return redirect('main:detail', new_acti.id)

def edit(request, id):
    edit_acti = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post':edit_acti})

def update(request, id):
    update_acti = Post.objects.get(id=id)
    update_acti.writer = request.user
    update_acti.acti_title = request.POST['acti_title']
    update_acti.acti_insert = request.POST['acti_insert']
    update_acti.acti_date = request.POST['acti_date']
    update_acti.save()
    return redirect('main:detail', update_acti.id)

def delete(request, id):
    delete_acti = Post.objects.get(id=id)
    delete_acti.delete()
    return redirect('main:showactivities')