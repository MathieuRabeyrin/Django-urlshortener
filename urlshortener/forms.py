from django.forms import ModelForm
from .models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ("long_url",)
        labels = {
            "long_url": ""
        }
    
    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields["long_url"].widget.attrs["placeholder"] = "Enter the link here"