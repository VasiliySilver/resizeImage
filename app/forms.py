from django import forms


class AddImageForm(forms.Form):
    link = forms.CharField(label='Ссылка', max_length=500, required=False)
    image = forms.ImageField(label='Файл', required=False)


class ChangeSizeForm(forms.Form):
    height = forms.IntegerField(label='Высота')
    width = forms.IntegerField(label='Ширина')
