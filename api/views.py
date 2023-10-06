from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .PostSerializer import PostSerializer


# Create your views here.
@api_view(["GET"])
def getAllPost(request):
    try:
        if("name" in request.GET):
            print(request.GET["name"])
        else:
            print("errr")
        posts = Post.objects.all()
        srilaze = PostSerializer(posts, many=True)
        return Response(srilaze.data)
    except:
        return Response({"e"})
