from django import forms


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
