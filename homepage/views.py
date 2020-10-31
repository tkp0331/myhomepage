import logging

from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from .forms import ContactForm

# 実行中のファイル名を取得してログを吐く
logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):  # TemplateViewはテンプレート表示に特化したview
    template_name = 'index.html'


class ContactView(generic.FormView):  # FormViewはフォーム処理に特化したview
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("homepage:contact")  # 処理が成功したらリダイレクト

    def form_valid(self, form):  # バリデーションに成功した場合に実行されるメソッド
        form.send_email()
        messages.success(self.request, "メッセージの送信に成功しました。")
        # cleaned_dataはバリデーション済みのデータを指す
        logger.info("E-mail sent by {}".format(form.cleaned_data["name"]))
        return super().form_valid(form)


class ResearchView(generic.TemplateView):
    template_name = "research.html"
