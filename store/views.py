from django.shortcuts import render
from .models import Member
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse,  reverse_lazy


class MemberList(ListView):
    model = Member


class MemberDetail(DetailView):
    model = Member



class MemberCreate(CreateView):
    # template_name = 'user/member_form.html'
    model = Member
    fields = ['name', 'nickname', 'age']


    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class MemberUpdate(UpdateView):
    template_name = 'app/member_update_form.html'
    model = Member
    fields = ['name', 'nickname', 'age']

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(MemberUpdate, self).get_form()
        form.fields['name'].label = '名前'
        form.fields['nickname'].label = 'ニックネーム'
        form.fields['age'].label = '年齢'
        return form


class MemberDelete(DeleteView):
    # template_name = 'user/member_confirm_delete.html'
    model = Member

    success_url = reverse_lazy('member')





