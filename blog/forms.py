from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Custom title',
        widget=forms.TextInput(attrs={"placeholder": "Write your title here!"})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Your text here)"})
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'price',
        ]