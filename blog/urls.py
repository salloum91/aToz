# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hadith/', views.hadith_posts, name='hadith_posts'),
    path('hadith/<int:hadith_id>/', views.hadith_detail, name='hadith_detail'),

    path('fatwa/', views.fatwa_posts, name='fatwa_posts'),
    path('fatwa/<int:fatwa_id>/', views.fatwa_detail, name='fatwa_detail'),

    path('question/', views.question_posts, name='question_posts'),
    path('question/<int:question_id>', views.question_detail, name='question_detail')

]   
