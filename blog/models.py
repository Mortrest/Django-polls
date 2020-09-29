from django.db import models

class Question(models.Model):
    questionText = models.TextField(null=True)
    datePublished = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questionText


class Choices(models.Model):
    choiceText = models.CharField(null=True, max_length=400)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText