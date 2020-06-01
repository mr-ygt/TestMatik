from django import forms
from .models import Soru
from captcha.fields import ReCaptchaField


class SoruForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model = Soru
        fields = [
            'title',
            'sınıf',
            'ders',
            'konu',
            'zorluk',
            'soru',
            'image',
        ]
