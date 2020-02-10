from django.urls import path
from .views import new_questions, popular_questions, question_detail, test

urlpatterns = [
    path('login/',test),
    path('signup/',test),
    path('question/<int:pk>/',question_detail, name='detail'),
    path('ask/',test),
    path('popular/',popular_questions, name='popular'),
    path('new/',test),
    path('',new_questions, name='main'),
]
