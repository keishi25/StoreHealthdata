from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.edit import CreateView
from .models import HealthData, Person
import json


from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Author
from django.urls import reverse

class AuthorCreate(CreateView):
    """
    テンプレートフォームをmodelに登録する汎用ビュー
    CreateViewを継承する時は、'_form' の template_name_suffix が使用される
    具体的にやることは、template何のhtmlファイルの名前を、
    ’model名_form.html’にする必要がある
    """
    model = Author
    # modelからデータを取る時は、filedに配列で名前を指定する
    fields = ['name', 'sex']

    # 遷移先を指定する
    def get_success_url(self):
        return reverse('list', kwargs={'pk': self.object.pk})


class MyListView(ListView):
    """
    modlのデータを表示させる汎用ビュー
    """
    model = Author
    #paginate_by = 2  # 表示件数


@ensure_csrf_cookie
def recode(request):
    if request.method == 'GET':
        return JsonResponse({})

    # Get json request converted utf-8 character
    request = json.loads(request.body.decode("utf-8"))

    # 新規作成：
    health_data = HealthData(user_id= 1, weight=40,fat=20)
    health_data.save()  # INSERTが実行される

    # json response
    response = request
    print(response)

    # JSONに変換して戻す
    return JsonResponse(response)


@ensure_csrf_cookie
def recode_person(request):
    if request.method == 'GET':
        return JsonResponse({})

    # Get json request converted utf-8 character
    request = json.loads(request.body.decode("utf-8"))

    # 新規作成：
    person = Person(first_name="keishi", last_name="hirakawa",
                    email_address="a.gmail.com", sex = "man")
    person.save()  # INSERTが実行される

    # json response
    response = request
    print(response)

    # JSONに変換して戻す
    return JsonResponse(response)
