from django import forms
from .models import Category



class PersonalPreferencesForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.filter(is_main=True)
        for category in categories:
            self.fields[category.slug+'_email'] = forms.BooleanField(label=category.name, required=False, widget=forms.CheckboxInput(attrs={'class': 'shadow-default switch checked-hidden', 'id': 'finances'}))
            self.fields[category.slug + '_telegram'] = forms.BooleanField(label=category.name, required=False,
                                                                       widget=forms.CheckboxInput(attrs={
                                                                           'class': 'shadow-default switch checked-hidden',
                                                                           'id': 'finances'}))
        self.fields['send_news_to_email'] = forms.BooleanField(label='send_news_to_email', required=False, widget=forms.CheckboxInput(attrs={'class': 'shadow-default switch', 'id': 'send-news-check'}))
        self.fields['countdown_to_email'] = forms.IntegerField(label='countdown_to_email', required=False, widget=forms.TextInput(attrs={'class': 'shadow-default checked-hidden', 'placeholder': 'Період в хвилинах'}))
        self.fields['send_news_to_telegram'] = forms.BooleanField(label='send_news_to_telegram', required=False,
                                                               widget=forms.CheckboxInput(
                                                                   attrs={'class': 'shadow-default switch',
                                                                          'id': 'send-news-check'}))
        self.fields['countdown_to_telegram'] = forms.IntegerField(label='countdown_to_telegram', required=False,
                                                               widget=forms.TextInput(
                                                                   attrs={'class': 'shadow-default checked-hidden',
                                                                          'placeholder': 'Період в хвилинах'}))

