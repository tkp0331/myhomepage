from django.views import generic

from .forms import ContactForm


class IndexView(generic.TemplateView):  # TemplateViewはテンプレート表示に特化したview
    template_name = 'index.html'


class ContactView(generic.FormView):  # FormViewはフォーム処理に特化したview
    template_name = 'contact.html'
    form_class = ContactForm
