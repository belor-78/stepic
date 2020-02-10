from django import forms
from .models import Question, Answer

pk = None
class AskForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    '''def clean_text(self):
        text = self.cleaned_data['text']
        if 'пошел нахуй' not in text:
            return text
        else:
            raise forms.ValidationError

    def save(self):
        title = self.cleaned_data['title']
        text = self.clean_text()
        print(text)
        question = Question.objects.create(title=title,text=text)
        return question'''
    class Meta:
        model = Question
        fields = ['title', 'text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
