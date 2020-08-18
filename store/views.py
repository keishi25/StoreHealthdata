from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

import json


@ensure_csrf_cookie
def index(request):
    if request.method == 'GET':
        return JsonResponse({})

    # Get json request converted utf-8 character
    request = json.loads(request.body.decode("utf-8"))

    # json response
    response = request
    print(response)

    # JSONに変換して戻す
    return JsonResponse(response)
