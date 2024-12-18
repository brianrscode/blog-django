from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitulo', 'description', 'imagen_portada']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        # Agrega clases CSS a los campos
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['subtitulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagen_portada'].widget.attrs.update({'class': 'form-control'})