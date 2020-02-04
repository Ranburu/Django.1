from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='Custom title',
        widget=forms.TextInput(attrs={"placeholder": "Write your title here!"})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Your text here)"})
    )
    price = forms.DecimalField()
    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if "@gmail.com" in email:
            return email
        else:
            raise forms.ValidationError("This is not a valid email, try gmail domain.")


class RawProductForms(forms.Form):
    title = forms.CharField(label='123', widget=forms.TextInput(attrs={"placeholder": "Write your title here!"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Your text here)"}))
    price = forms.DecimalField()