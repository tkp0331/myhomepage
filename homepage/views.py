from django.views import generic


class IndexView(generic.TemplateView):  # TemplateViewはテンプレート表示に特化したview
    template_name = 'index.html'
