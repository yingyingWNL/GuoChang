from django.shortcuts import render
from django.http import JsonResponse
from cropdata import models

from django.views import View
import random

import json


# Create your views here.

class IsHealth(View):
    def get(self, request):
        return JsonResponse({
            'code': 200,
            'data': {
                "content": "风险",
                "url": "/icons/yujing.svg"
            }
        })


class Prevent(View):
    def get(self, request):
        return JsonResponse({
            'code': '200',
            'data': [
                {
                    'date': '2022-05-13',
                    'name': '在后续版本中，我们会利用无人机采集农田信息进行具体展示',
                    'state': '主要为害叶鞘，叶片次之',
                    'city': 'San Francisco',
                    'family': [
                        {
                            'method': '选种抗病品种',
                            'describe': '打捞菌核，减少菌源；科学管水，贯彻“前浅、中晒、后湿润”的用水原则，避免长期深灌或晒田过度；合理施肥，贯彻“施足基肥，早施追肥，灵活追肥”的原则，增强植株长势；合理密植，增加通透性',
                        },
                        {
                            'method': '打药',
                            'describe': '分蘖后期病穴率达15%即施药防治，可选用下列药剂：苯甲•丙环唑；氟环唑；或已唑醇',
                        },
                    ]
                },
                {
                    'date': '2022-05-06',
                    'name': '水稻纹枯病',
                    'state': '稻瘟灵；硫磺•三环唑；或三环唑，重病区需防治2次，间隔期为7～10天。',
                    'city': 'San Francisco',
                    'family': [
                        {
                            'method': '选种抗病品种',
                            'describe': '科学管水，底肥足、追肥早、施充分腐熟的农家肥、增施磷钾肥，增强植株抗病能力；合理密植，增加通透性',
                        },
                        {
                            'method': '选用以下药剂防治',
                            'describe': '稻瘟灵；硫磺•三环唑；或三环唑，重病区需防治2次，间隔期为7～10天。',
                        },
                    ]
                }
            ]
        })


class AllPrevent(View):
    def get(self, request):
        queryset = models.Prevents.objects.all()
        data = []
        for i in queryset.values():
            data.append(i)
        return JsonResponse({
            'code': '200',
            'data': data})


class PredictHumidity(View):
    def get(self, request):
        return JsonResponse({
            'code': '200',
            'data': [
                {'date': '2023/3/19',
                 'color': '#8B0000',
                 'title': '星期日湿度情况：最高为{}%，最低{}%'.format(random.randint(20, 35), random.randint(1, 5)),
                 'tip': '一切正常'
                 }, {
                    'date': '2023/3/18',
                    'color': '#008b61',
                    'title': '星期六湿度情况：最高为{}%，最低{}%'.format(random.randint(20, 35), random.randint(1, 5)),
                    'tip': '一切正常'
                }, {
                    'date': '2023/3/17',
                    'color': '#d30f0f',
                    'title': '星期五湿度情况：最高为{}%，最低{}%'.format(random.randint(20, 35), random.randint(1, 5)),
                    'tip': '温度异常'
                }, {
                    'date': '2023/3/16',
                    'color': '#d30f0f',
                    'title': '星期四湿度情况：最高为{}%，最低{}%'.format(random.randint(20, 35), random.randint(1, 5)),
                    'tip': '温度异常'
                }
            ]
        })


class PredictTemperature(View):
    def get(self, request):
        return JsonResponse({
            'code': '200',
            'data': [
                {'date': '2023/3/19',
                 'color': '#8B0000',
                 'title': '星期日温度情况：最高为9°C，最低0°C',
                 'tip': '一切正常'
                 }, {
                    'date': '2023/3/18',
                    'color': '#008b61',
                    'title': '星期六温度情况：最高为12°C，最低2°C',
                    'tip': '一切正常'
                }, {
                    'date': '2023/3/17',
                    'color': '#d30f0f',
                    'title': '星期五温度情况：最高为15°C，最低3°C',
                    'tip': '温度异常'
                }, {
                    'date': '2023/3/16',
                    'color': '#d30f0f',
                    'title': '星期四温度情况：最高为15°C，最低3°C',
                    'tip': '温度异常'
                }
            ]
        })
