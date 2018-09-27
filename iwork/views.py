# -*- coding: utf-8 -*-
from django.shortcuts import render
from common.mymako import render_mako_context
from iwork.models import WorkRecord
from common.log import logger
from django.http import HttpResponse
import json
# Create your views here.
def home(request):
    records = WorkRecord.objects.all()
    logger.info("{}. data loged:{}".format(str(request.user.username), str(records)))
    return render_mako_context(request, '/iwork/meeting.html', {"operator":"cyc","records":records})

def toDicts(objs):
    obj_arr=[]
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr
    
def datas(request):
    resp = WorkRecord.objects.all()
    dicts=toDicts(resp)
    return HttpResponse(json.dumps(dicts,ensure_ascii=False))

