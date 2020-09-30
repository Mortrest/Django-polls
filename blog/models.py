from django.db import models
from django.contrib.auth.models import User


# class UserModel(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     def __str__(self):
#         return self.name
class UserClass(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=400,null=True,blank=True)



class Question(models.Model):
    questionText = models.TextField(null=True)
    datePublished = models.DateTimeField(auto_now_add=True)
    #user = models.ManyToManyField(User)
    likes = models.IntegerField(default=0, null=True)
    #likeStatus = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.questionText


class Choices(models.Model):
    choiceText = models.CharField(null=True, max_length=400)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText


class Comment(models.Model):
    text = models.TextField()
    author = models.OneToOneField(UserClass, on_delete=models.CASCADE, null=True)
    datePublished = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

