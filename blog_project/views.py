from django.shortcuts import render
from posts.models import Post
def home_page(request):
    data=Post.objects.all()
    return render(request, 'home.html',{'data':data})