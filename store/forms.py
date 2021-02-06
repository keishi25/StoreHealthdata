from django import forms
from .models import Member


class MemberCreateForm(forms.ModelForm):
    """formの設定をすることで、HTML上でのformの表示を変更できる"""
    # 下記コンストラクタを設定することで、タイトルとフォームを縦並びに出来る
    def __init__(self, *args, **kwargs):
        super(MemberCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Member
        fields = ['day', 'weight']