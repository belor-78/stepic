from django import forms
from .models import Question, Answer

pk = None
class AskForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    '''def clean_text(self):
        text = self.cleaned_data['text']
        if 'fuck off' not in text:
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


class AnswerForm(forms.Form):
    text = forms.CharField(forms.Textarea)
    question = forms.CharField()

    def change_question(self):

