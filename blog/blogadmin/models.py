from django.db import models

# Create your models here.

#here i am going to create post and categry 

class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='category/')
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True,null=True)

class post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    categ=models.ForeignKey(category,on_delete=models.CASCADE)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True,null=True)
