from django import forms
from news.models import News

class NewsForm(forms.Form):
    class Meta:
        model = News
        fields = ['title', 'body', 'created_at', ]