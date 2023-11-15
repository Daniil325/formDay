from django import forms
from django.forms import TextInput, Textarea

from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            'fio': TextInput(attrs={'placeholder': 'ФИО'}),
            'faculty': TextInput(attrs={'placeholder': 'Институт'}),
            'group': TextInput(attrs={'placeholder': 'Группа'}),
            'comment': Textarea(attrs={'placeholder': 'Поздравление(не более 500 символов)'}),
            'media_link': TextInput(attrs={'placeholder': 'Ссылка на файлы с поздравлением (по желанию)'}),
        }
