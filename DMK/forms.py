from django import forms

class LessonForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Текст')