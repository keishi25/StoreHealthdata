from django.shortcuts import render
from .models import Member
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse,  reverse_lazy


class MemberList(ListView):
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す

        weight_list = Member.objects.all()

        context['data_list'] = weight_list
        return context


class MemberDetail(DetailView):
    model = Member


class MemberCreateList(CreateView):
    # template_name = 'user/member_form.html'
    model = Member
    fields = ['day', 'weight']

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        kwargs["object_list"] = Member.objects.order_by("id").reverse()  # 最新のデータを上部に表示
        return super(MemberCreateList, self).get_context_data(**kwargs)


class MemberUpdate(UpdateView):
    template_name = 'store/member_update_form.html'
    model = Member
    fields = ['day', 'weight']

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(MemberUpdate, self).get_form()
        form.fields['day'].label = '登録日'
        form.fields['weight'].label = '体重'
        return form


class MemberDelete(DeleteView):
    # template_name = 'user/member_confirm_delete.html'
    model = Member

    # 処理後の遷移先のurlsのname
    success_url = reverse_lazy('create')





