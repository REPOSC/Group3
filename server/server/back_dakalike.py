from django.http import JsonResponse
from backend import models


def daka_like(request):
    item = request.POST.get('item', '')
    dakalikes = models.User_like.objects.filter(book_number = item.book_num,
                                                user_number = item.user_name)
    #获取所有点赞对象
    str1 = []
    str2 = ''
    like_user_numbers = []
    like_user_nicknames = ''
    for i in dakalikes:
        like_user_numbers.append(i.like_user_number)
        nicknames = models.User_info.objects.filter(number = i.user_number)#获取点赞对象的昵称
    for j in nicknames:
        str1.append(str(j.nickname))
    str2 = '、'.join(str1)#将所有昵称用顿号连接
    like_user_nicknames = str2
    str1 = []
    str2 = ''
    return JsonResponse({
      'like_nicknames': like_user_nicknames
    })
