from django import forms
from django.core.exceptions import ValidationError

from app.catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise ValidationError(f'Вы использовали запрещенное слово "{forbidden_word}"')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise ValidationError(f'Вы использовали запрещенное слово "{forbidden_word}"')

        return cleaned_data


class ConfirmDeleteForm(StyleFormMixin, forms.Form):
    pass


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        active = cleaned_data.get('is_active')

        if active:
            product_id = self.instance.product_id
            active_versions = Version.objects.filter(product_id=product_id, is_active=True)
            if active_versions.exists():
                raise forms.ValidationError(
                    'В один момент времени может быть только одна активная версия продукта. Пожалуйста, выберите только одну активную версию.'
                )

        return cleaned_data
