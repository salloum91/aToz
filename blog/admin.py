from django.contrib import admin

from .models import Category, Hadith_Post, Fatwa_Post, Question_Post

admin.site.register(Category)
admin.site.register(Hadith_Post)
admin.site.register(Fatwa_Post)
admin.site.register(Question_Post)
