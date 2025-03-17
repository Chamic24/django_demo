import json

from django.db.models import Q
from django.http import JsonResponse

from auth_app.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        rd = json.loads(request.body)
        username = rd.get('username', '')
        password = rd.get('password', '')
        if not all([username, password]):
            return JsonResponse({'code': 9, 'msg': 'The account or password is incorrect'})
        qs = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not qs or not qs.check_password(password):
            return JsonResponse({'code': 9, 'msg': 'The account or password is incorrect'})
        return JsonResponse({'code': 0, 'msg': 'login successfully', 'data': {"username": qs.username,"email":qs.email}})


def register(request):
    if request.method == 'POST':
        rd = json.loads(request.body)
        username = rd.get('username', '')
        password = rd.get('password', '')
        email = rd.get('email', '')
        if not all([username, password, email]):
            return JsonResponse({'code': 9, 'msg': 'Please fill in the information completely'})

        if len(password) < 6:
            return JsonResponse({'code': 9, 'msg': 'The password must contain at least six characters'})
        qs = User.objects.filter(username=username)
        if qs:
            return JsonResponse({'code': 9, 'msg': 'The user name already exists'})
        user = User()
        user.username = username
        user.set_password(password)
        user.email = email
        user.save()
        return JsonResponse({'code': 0, 'msg': 'registered successfully', 'data': {"username": user.username}})
