from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from .forms import UploadForm
from .models import Upload


class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['uploads']:
            Upload.objects.create(file=each)
        sec = form.cleaned_data['csv']
        Upload.objects.create(csv_file=sec)
        return super(UploadView, self).form_valid(form)

class DoneView(TemplateView):
	template_name = 'done.html'
