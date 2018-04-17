# data	status	style	city	type	group	introduce	detail

from django.shortcuts import render
from django_web.models import itemInfo
from django.core.paginator import Paginator

# Create your views here.

# 每天订单量
def get_day_ord():
    pipeline = [
        {'$group': {'_id': '$data', 'count': {'$sum': 1}}},
        {'$sort':{'_id':1}}
    ]

    for i in itemInfo._get_collection().aggregate(pipeline):
        #print(i['_id'], i['count'])
        data = {
            'name':i['_id'],
            'y':i['count']
        }

        yield data

series_day_ord = [i for i in get_day_ord()]

# 解决、关闭工单占比
def get_status():
    pipeline = [
        {'$group': {'_id':'$status', 'count': {'$sum': 1}}},
    ]

    for i in itemInfo._get_collection().aggregate(pipeline):
        #print(i['_id'], i['count'])
        data = {
            'name':i['_id'],
            'y':i['count']
        }

        yield data

series_status = [i for i in get_status()]

# 临时/长期占比
def get_style():
    pipeline = [
        {'$group': {'_id':'$style', 'count': {'$sum': 1}}},
    ]

    for i in itemInfo._get_collection().aggregate(pipeline):
        #print(i['_id'], i['count'])
        data = {
            'name':i['_id'],
            'y':i['count']
        }

        yield data

series_style = [i for i in get_style()]

# 工单类型占比
def get_type():
    pipeline = [
        {'$group': {'_id':'$type', 'count': {'$sum': 1}}},
    ]

    for i in itemInfo._get_collection().aggregate(pipeline):
        #print(i['_id'], i['count'])
        data = {
            'name':i['_id'],
            'y':i['count']
        }

        yield data

series_type = [i for i in get_type()]




def index(request):
    limit=10
    item_info = itemInfo.objects
    paginator = Paginator(item_info,limit)
    page = request.GET.get('page',1)
    loaded = paginator.page(page)

    context = {
        'itemInfo':loaded,
        'count':item_info.count(),
    }

    return render(request, 'index.html', context)

def chart(request):
    context = {
        'chart1':series_day_ord,
        'chart2':series_status,
        'chart3':series_style,
        'chart4':series_type
    }
    return render(request, 'chart.html',context)