from django import forms
from core.models import Collection, Item, File

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        exclude = ('added','user')


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('added','user')


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        exclude = ('temporarysession','user')
