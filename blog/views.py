# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Hadith_Post, Fatwa_Post, Question_Post

def hadith_posts(request):
    posts = Hadith_Post.objects.all()
    return render(request, 'hadith_posts.html', {'posts': posts})

def hadith_detail(request, hadith_id):
    hadith = get_object_or_404(Hadith_Post, pk=hadith_id)
    return render(request, 'hadith_detail.html', {'hadith': hadith})

#####################

def fatwa_posts(request):
    posts = Fatwa_Post.objects.all()
    return render(request, 'fatwa_posts.html', {'posts': posts})

def fatwa_detail(request, fatwa_id):
    fatwa = get_object_or_404(Fatwa_Post, pk=fatwa_id)
    return render(request, 'fatwa_detail.html', {'fatwa': fatwa})

####################
def question_posts(request):
    posts = Question_Post.objects.all()
    return render(request, 'question_posts.html', {'posts': posts})

def question_detail(request , question_id):
    question = get_object_or_404(Question_Post,pk=question_id)
    return render (request,'question_detail.html',{'question':question})