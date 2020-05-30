from django.forms import ModelForm, TextInput
from core.models import User

class AddEmail(ModelForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'email': TextInput(attrs={'class': 'input',
                                    'type': 'email',
                                    'placeholder': 'Digite Seu Email'}),
        }
