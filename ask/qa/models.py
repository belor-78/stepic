from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок вопроса')
    text = models.TextField()
    added_at =models.DateField(auto_now_add=True)
    rating = models.IntegerField(verbose_name='рейтинг вопроса',default=0)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'вопрос'
        ordering = ['rating']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return self.text

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')