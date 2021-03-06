from django.urls import path
from .views import new_questions, popular_questions, MyLoginView, test, to_ask, detail_page, MyRegisterView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', MyRegisterView.as_view(), name='registration'),
    path('question/<int:pk>/', detail_page, name='detail'),
    path('ask/', to_ask, name='ask'),
    path('popular/', popular_questions, name='popular'),
    path('new/', test),
    path('', new_questions, name='main'),
]
