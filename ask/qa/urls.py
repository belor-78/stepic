from django.urls import path
from .views import new_questions, popular_questions, question_detail, test, to_ask, to_answer

urlpatterns = [
    path('login/',test),
    path('signup/',test),
    path('question/<int:pk>/',to_answer, name='detail'),
    path('ask/',to_ask, name='ask'),
    path('popular/',popular_questions, name='popular'),
    path('new/',test),
    path('',new_questions, name='main'),
]