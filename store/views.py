from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import HealthData, Person
import json


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
