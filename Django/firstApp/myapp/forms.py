from django import forms
from django.core import validators


class FormArticle(forms.Form):

    title = forms.CharField(label="Titulo", max_length=100, widget=forms.TextInput(
        attrs={
            'placeholder': 'Introduce el titulo'
        }
    ), validators=[
        validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
        validators.RegexValidator(
            '^[A-Za-z0-9 ]*$', "El titulo no puede contener caracteres especiales")
    ])

    content = forms.CharField(label='Contenido', widget=forms.Textarea(
        attrs={
            'placeholder': 'Introduce el contenido'
        }
    ))

    public_options = [(1, 'Si'), (0, 'No')]
    public = forms.TypedChoiceField(label="Publicado", choices=public_options)
