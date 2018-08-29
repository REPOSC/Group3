# coding=utf-8
from django.http import HttpResponse
from backend import models


def get_video(request):
    name_dict = {
        'guide':'亲子阅读指导',
        'ebook':'e-book',
        'first_game':'连线游戏',
        'second_game':'看词识图',
        'third_game':'拼图游戏',
        'fourth_game':'听音选图',
        'expanding':'阅读拓展'
    }
    item_name = request.GET.get('item')
    name = name_dict[item_name]
    video_item = models.Function_video.objects.get(function=name)
    return HttpResponse(video_item.video)
