from django import forms
from django.contrib.auth.models import User
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200, label="Заголовок")
#     text = forms.CharField(widget=forms.Textarea, label="Текст поста")
#     author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
#     image = forms.ImageField(required=False, label="Изображение")

class PostForm(forms.ModelForm):
    # дополняем конструктор родительского класса
    def __init__(self, *args, **kwargs):
        # получаем author из именнованных аргументов (его передали во views)
        author = kwargs.pop('author', None)
        # вызываем констроуктор родительского
        super().__init__(*args, **kwargs)
        # устанавливаем начальное значение поля author
        self.fields['author'].initial = author
        # отключаем видимость этого поля в форме
        self.fields['author'].diabled = True
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'author')

        labels = {
            'title': "Заголовок",
            'text': "Текст поста",
            'image': "Изображение",
            'author': "Автор"
        }

        # fields = ('title', 'text') добавляет перечисленные
        # exclude = ('author', 'created_at') все кроме перечисленных


class FilterForm(forms.Form):
    author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор')
    created_at = forms.DateField(label='Дата публикации',
                                 widget=forms.DateInput(attrs={'type': 'date'}),
                                 input_formats=["%Y-5m-%d"],
                                 required=False)