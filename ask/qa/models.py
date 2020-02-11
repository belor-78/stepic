from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/'+str(self.pk)

    class Meta:
        ordering = ['rating']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.text
