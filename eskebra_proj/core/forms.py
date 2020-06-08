from django import forms
from core.models import User, Ads

class AddEmail(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'input',
                                    'type': 'email',
                                    'placeholder': 'Digite Seu Email'}),
        }

class Vendor(forms.ModelForm):
    category = forms.BooleanField(
    widget=forms.CheckboxSelectMultiple(choices=Ads.CATEGORY, attrs={
            # "checked": "",
            "onClick": "this.form.submit()"
        }
    ),
    required=False
    )


    vendor_name = forms.BooleanField(
    widget=forms.CheckboxSelectMultiple(choices=Ads.STORE, attrs={
            # "checked": "",
            "onClick": "this.form.submit()"
        }
    ),
    required=True
    )

    class Meta:
        model = Ads 
        fields = ('vendor_name', 'category')


