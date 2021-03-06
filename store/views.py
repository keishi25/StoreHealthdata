import json
from datetime import datetime, date, time

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse,  reverse_lazy

from .models import Member
from .forms import MemberCreateForm


class MemberList(ListView):
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す

        weight_list = Member.objects.all()

        context['data_list'] = weight_list
        return context


def json_serial(obj):
    """date datetimeの変換関数"""
    # 日付型の場合は、文字列に変換
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()


class MemberDetail(DetailView):
    model = Member


class MemberCreateList(CreateView):
    # template_name = 'user/member_form.html'
    model = Member
    # CreateViewでform_clasの指定は、fieldsの設定をしている限り、必須ではない
    form_class = MemberCreateForm
    # fields = ['day', 'weight']

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        kwargs["object_list"] = Member.objects.order_by("id").reverse()  # 最新のデータを上部に表示
        scatter_data_list = list(Member.objects.values("day", "weight"))  # カラム指定
        scatter_data_dict = {"scatter_data": scatter_data_list}
        scatter_data_json_str = json.dumps(scatter_data_dict, default=json_serial)
        # chart.js用にデータ構造の成型
        #scatter_data_json_str = scatter_data_json_str.replace("day", "x")
        #scatter_data_json_str = scatter_data_json_str.replace("weight", "y")
        kwargs["scatter_data"] = scatter_data_json_str
        return super(MemberCreateList, self).get_context_data(**kwargs)


class MemberUpdate(UpdateView):
    template_name = 'store/member_update_form.html'
    model = Member
    fields = ['day', 'weight', 'fat_percentage']

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(MemberUpdate, self).get_form()
        form.fields['day'].label = '登録日'
        form.fields['weight'].label = '体重'
        form.fields['fat_percentage'].label = '体脂肪率'
        return form


class MemberDelete(DeleteView):
    # template_name = 'user/member_confirm_delete.html'
    model = Member

    # 処理後の遷移先のurlsのname
    success_url = reverse_lazy('create')





