from django.shortcuts import render
import json
from django.views import View
from user.models import User, UserImages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse


# Create your views here.
# 用户注册的逻辑
class Register(View):

    def post(self, request):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        mobile = request.POST.get('phoneNumber')
        if all([username, password1, password2, email, mobile]):
            return JsonResponse({'code': 400, 'errmsg': '参数不全'})
        if password1 != password2:
            return JsonResponse({'code': 400, 'errmsg': '两次密码不正确'})
        try:
            user = User.objects.create_user(username=username, password=password1, email=email, mobile=mobile)
            user.save()
            login(request, user)
            response = JsonResponse({'code': 200, 'errmsg': 'ok', 'isLogin': True})
        except:
            response = JsonResponse({'code': 400, 'errmsg': '创建用户失败', 'isLogin': False})
        return response

    def get(self, request):
        return HttpResponse('get')


class Login(View):

    def post(self, request):
        body_bytes = request.body
        body_str = body_bytes.decode()
        body_dict = json.loads(body_str)

        username = body_dict['username']
        password = body_dict['username']
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({"code": 400, 'errmsg': '账号或密码错误', 'isLogin': False})

        login(request, user)
        # 默认cookie不保存
        request.session.set_expiry(0)
        response = JsonResponse({'code': 0, 'errmsg': 'ok', 'isLogin': True, 'username': username})
        response.set_cookie('username', username)

        return response


class Logout(View):

    def post(self, request):
        logout(request)

        return JsonResponse({
            "msg": "ok",
            "data": "退出登录成功"
        })


class UpdataPassword(View):

    def post(self, request):
        body_bytes = request.body
        body_str = body_bytes.decode()
        body_dict = json.loads(body_str)

        oldpassword = body_dict['username']['oldpassword']
        password = body_dict['username']['password']
        repassword = body_dict['username']['repassword']

        return JsonResponse({
            "msg": "ok",
            "data": "修改密码的逻辑已经完成！"
        })


class GetInfo(View):

    def post(self, request):
        return JsonResponse({
            "msg": "ok",
            "data": {
                "username": "admin",
                'value': 'is'
            }
        })


class GetStatistics(View):

    def get(self, request):
        return JsonResponse({
            "msg": "ok",
            "data": {
                "panels": [
                    {
                        "title": "监测农田数量",
                        "value": 50,
                        "unit": "个",
                        "unitColor": "text-current",
                        "subTitle": "增幅",
                        "subValue": '10%',
                        "subUnit": ""
                    },
                    {
                        "title": "总体农田健康指数",
                        "value": 88,
                        "unit": "",
                        "unitColor": "text-green-500/50",
                        "subTitle": "转化率",
                        "subValue": "6%",
                        "subUnit": ""
                    },
                    {
                        "title": "最差农田健康指数",
                        "value": "44",
                        "unit": "",
                        "unitColor": "text-yellow-500",
                        "subTitle": "变化",
                        "subValue": '3.54%',
                        "subUnit": ""
                    },
                    {
                        "title": "最好农田健康指数",
                        "value": 97,
                        "unit": "",
                        "unitColor": "text-red-500/50",
                        "subTitle": "变化",
                        "subValue": '16',
                        "subUnit": ""
                    }
                ]
            }
        })


class Upload(View):
    def post(self, request):
        import re
        from PIL import Image
        from fdfs_client.client import Fdfs_client

        img = request.FILES.get('file')
        im = Image.open(img)
        # 存放路径
        path = 'temp{}'.format(re.findall(r'\..*', img.name)[0])
        im.save(path)

        # 根据该图片获取详细字段
        """ 分类 """

        # 将票据种类获取到之后
        client = Fdfs_client('utils/fastdfs/client.conf')
        result = client.upload_by_filename('temp{}'.format(re.findall(r'\..*', img.name)[0]))
        file_id = result['Remote file_id']

        # 将用户上传的图片入库
        # models.TbA.objects.create(user_id=request.user.id, file_id=file_id)
        UserImages.objects.create(file_id=file_id, file_name=img.name, user_id=1)

        return JsonResponse({"msg": "文件上传成功", "code": 200, "data": {
            "id": UserImages.objects.get(file_id=file_id).file_id,
        }})


class Temp(View):
    print(1)

    def get(self, request):
        import json
        with open('./user/x.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        data_dict = dict(json_data)
        print(data_dict)

        return JsonResponse(data_dict)
