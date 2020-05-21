from django.forms import Form, ModelForm
from django.contrib.auth.models import User

from main.models import Document

class UploadFileForm(ModelForm):
    class Meta:
        model = Document
        fields = [
            'file',
        ]
