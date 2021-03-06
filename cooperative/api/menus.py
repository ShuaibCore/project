import sys, os
from django.http import HttpResponse, JsonResponse
import json, datetime, time
from numpy import random
import numpy as np
import pandas as pd
import csv
import urllib.request
from django.db import connection
from authentication.query_columns import dictfetchall
from authentication.writer import write_error
import pickle
import base64



def admin_menus(request):
    try:
        pagename = request.GET['pagename']
        userid = request.session['userdata']['id']
        with connection.cursor() as cursor:
           counter = cursor.execute("SELECT t1.category, t1.menuName, t1.menu_description, t1.menu_icon, t1.uniqueCode FROM "
                                    "user_menus as t1 INNER JOIN user_priviledges as t2 "
                                    "ON t1.id=t2.menu_id "
                                    "WHERE t1.record_status=%s AND t1.status_id=%s AND "
                                    "t2.record_status=%s AND "
                                    "t2.user_id=%s " 
                                    "ORDER BY t2.time_modified, t2.date_modified, t2.status_id ",
                                    [1, 1, 1, userid])
           row = dictfetchall(cursor)
           cursor.close()
           if counter > 0:
               pageexist = admin_menus_check_page(request)
               if pageexist:
                   msg=''
                   loaderstatus = 'none'
               else:
                   loaderstatus = 'none'
                   msg="""We are sorry, the page ({}) you requested cannot be found.
                       The URL may be misspelled, 
                       no longer available or you do not have access, 
                       please contact the Administrator or use other menus.""".format(pagename)

               feedback = {
                   'status': 'success',
                   'confirmed': 'success',
                   'msg': str(msg),
                   'result': row,
                   'loaderstatus':loaderstatus,
                   'ifUserHasAccess': pageexist,
                   'classname': '',
               }
           else:
               feedback = {
                   'status': 'failed',
                   'ifUserHasAccess': 'false',
                   'msg': 'We are sorry, the page you requested cannot be found.'
                          'The URL may be misspelled, no longer available or you do not have access, '
                          'please contact the Administrator.',
                   'classname': '',
               }

    except Exception as e:
        write_error('widget_list', e)
        feedback = {
            'status': 'failed',
            'ifUserHasAccess': 'false',
            'msg': 'Something went wrong, kindly reload this'
                   ' page or contact the administrator.',
            'classname': 'alert alert-danger p-1 text-center',
        }

    return JsonResponse(feedback, safe=False)


def admin_menus_check_page(request):
    pagename = request.GET['pagename']
    userid = request.session['userdata']['id']
    with connection.cursor() as cursor:
       counter = cursor.execute("SELECT t1.category, t1.menuName, t1.menu_description, t1.menu_icon, t1.uniqueCode FROM "
                                "user_menus as t1 INNER JOIN user_priviledges as t2 "
                                "ON t1.id=t2.menu_id "
                                "WHERE t1.record_status=%s AND "
                                "t2.record_status=%s AND t2.status_id=%s AND "
                                "t2.user_id=%s AND menuName =%s " 
                                "ORDER BY t2.time_modified, t2.date_modified, t2.status_id ",
                                [1, 1, 1, userid, pagename])
       cursor.close()
       if counter > 0:
           return True
       else:
           return False

