import logging

from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from .forms import ContactForm
from .models import Blog

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


class CareerView(generic.TemplateView):
    template_name = "career.html"


class MaterialsView(generic.TemplateView):
    template_name = "materials.html"


class BlogView(generic.ListView):  # ListViewはモデルオブジェクトの一覧を表示することに特化したView
    model = Blog
    # template_name = "blog.html"  まだ実装できていない
    template_name = "constructing.html"
    paginate_by = 5


class BDetailView(generic.DetailView):  # DetailViewはDBの特定のデータ詳細を表示するのに特化したview
    model = Blog
    template_name = "detail.html"
    # pk_url_kwarg = "bnum"   パスコンバータで変数名を「pk」でなくする場合に必要な記述
