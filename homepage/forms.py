from django import forms
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label="お名前", max_length=255)
    email = forms.EmailField(label="メールアドレス")
    title = forms.CharField(label="件名", max_length=255)
    message = forms.CharField(label="本文", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control col-9"
        self.fields["name"].widget.attrs["placeholder"] = "鈴木太郎"

        self.fields["email"].widget.attrs["class"] = "form-control col-11"
        self.fields["email"].widget.attrs["placeholder"] = "hoge@abc.com"

        self.fields["title"].widget.attrs["class"] = "form-control col-11"
        self.fields["title"].widget.attrs["placeholder"] = "経歴について"

        self.fields["message"].widget.attrs["class"] = "form-control col-12"
        self.fields["message"].widget.attrs["placeholder"] = "詐称していないですか？"

    def send_email(self):
        # バリデーション済みの要素を取得
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        title = self.cleaned_data["title"]
        message = self.cleaned_data["message"]

        # EmailMessageクラスへの引数を作成
        subject = f"連絡：{title}"
        message = f"送信者:{name}\nメールアドレス:{email}\nメッセージ:\n{message}"
        from_email = "admin@example.com"
        to_list = [
            "merioda.seven.24@gmail.com",
        ]
        cc_list = [
            email,
        ]

        # メール送信処理
        message = EmailMessage(subject=subject, body=message,
                               from_email=from_email, to=to_list, cc=cc_list)
        message.send()
