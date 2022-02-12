from django.shortcuts import render
from dashboard.models import Post

def post_rec(request): 
    context = {
        'title':'Rec'
    }

    print(Post.objects.all())

    return render(request, 'rec/rec.html', context)
