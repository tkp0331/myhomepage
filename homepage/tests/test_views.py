from django.test import TestCase
from django.urls import reverse_lazy


class TestIndexView(TestCase):

    def test_request_success(self):

        # clientとしてgetメソッドを実行する
        response = self.client.get(reverse_lazy("homepage:index"))

        # 想定通りのテンプレートを使っているかテスト
        # NOTE: テンプレートをテストする用なので、継承先を指定することもあるらしい
        # NOTE: 公式レファレンスだとtemplates/index.htmlのようにしているが、ファイル名だけじゃないとエラーになる
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")

    def test_request_failure(self):
        response = self.client.get(reverse_lazy("homepage:blog"))

        # 常に同じテンプレートが返されないかテストする
        # baseテンプレートは使われているのでused
        # indexテンプレートは使われていないのでnotused
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateNotUsed(response, "index.html")
