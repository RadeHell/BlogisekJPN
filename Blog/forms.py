from django import forms
from .models import Comment
from .models import VocabularyList, VocabularyWord


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


class VocabularyListForm(forms.ModelForm):
    class Meta:
        model = VocabularyList
        fields = ['name']

class VocabularyWordForm(forms.ModelForm):
    class Meta:
        model = VocabularyWord
        fields = ['japanese_word', 'english_translation']
