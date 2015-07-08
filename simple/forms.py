from django import forms
from multiupload.fields import MultiFileField


class UploadForm(forms.Form):
    uploads = MultiFileField(min_num=1, max_num=100, max_file_size=1024*1024*5)
    csv = forms.FileField()
