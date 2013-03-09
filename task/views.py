# Create your views here.
from pymongo import Connection
from django import forms
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson


def add(request):
    if request.POST['task'] and request.POST['detail']:
        databaseName = "test"
        connection = Connection()

        db = connection[databaseName]
        todo = db['tasks']
        task = {"task" : request.POST['task'], "detail" : request.POST['detail']}

        todo.save(task)
        
        return HttpResponseRedirect("http://tasklist/#/list")

def list(response):
    databaseName = "test"
    connection = Connection()

    db = connection[databaseName]
    todo = db['tasks']
    tasks = [] 
    for task in todo.find():
        tasks.append({ 'task': task['task'], 'detail': task['detail']})
        #tasks.append(task['task'])
    return HttpResponse(simplejson.dumps(tasks))


