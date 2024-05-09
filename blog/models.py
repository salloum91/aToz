from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

##################################################################
class Hadith_Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField(default=0) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define choices for the Darajet_alhadith field
    DARAJET_CHOICES = [
        ('صحيح متفق عليه', 'صحيح متفق عليه'),
        ('صحيح أخرجه بخاري', 'صحيح أخرجه بخاري'),
        ('أخرجه أصحاب السُنَن', 'أخرجه أصحاب السُنَن'),
        ('إسناده صحيح', 'إسناده صحيح'),
        ('صحيح بشواهد', 'صحيح بشواهد'),
        ('إسناده حسن', 'إسناده حسن'),
        ('حسن مع إمعاض', 'حسن مع إمعاض'),
        ('ضعيف منجبر', 'ضعيف منجبر'),
        ('موقوف', 'موقوف'),
        ('معلول', 'معلول'),
        ('لا وجود له', 'لا وجود له'),
        ('مكذوب', 'مكذوب'),
        ('لا أصل له', 'لا أصل له'),
        ('لا يصح', 'لا يصح'),
        ('باطل', 'باطل'),
        ('مُنكر', 'مُنكر'),
        ('ضعيف جداً', 'ضعيف جداً'),
        ('ضعيف', 'ضعيف'),
        ('شاذ', 'شاذ'),

    ]
    Darajet_alhadith = models.CharField(max_length=100, choices=DARAJET_CHOICES)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk:  # If the post is being created (not updated)
            # Get the highest number value among existing posts
            highest_number = Hadith_Post.objects.aggregate(models.Max('number'))['number__max']
            if highest_number is None:
                self.number = 1  # If no posts exist, start from 1
            else:
                self.number = highest_number + 1  # Increment the highest number
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # When deleting a post, renumber the remaining posts
        remaining_posts = Hadith_Post.objects.filter(number__gt=self.number)
        for post in remaining_posts:
            post.number -= 1
            post.save()
        super().delete(*args, **kwargs)

###################################################################
class Fatwa_Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Question_Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title