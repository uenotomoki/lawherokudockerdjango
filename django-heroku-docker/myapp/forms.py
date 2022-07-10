from django import forms

class SendUrlForm(forms.Form):
    url_contents = forms.CharField(
        label='SendUrl',
        widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'})
        )