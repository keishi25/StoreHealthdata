from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

import json


@ensure_csrf_cookie
def index(request):
    if request.method == 'GET':
        return JsonResponse({})

    # json request
    request = json.loads(request.body.decode("sjis"))

    # json response
    response = request
    # JSONに変換して戻す
    return JsonResponse(response)