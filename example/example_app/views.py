# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.shortcuts import render

from forms import ExampleForm, TestForm


def home(request):
    test  = u"* test测试"
    
    return render_to_response("index.html", {"settings": settings, "request": request, "test": test},
                              context_instance=RequestContext(request))

def index(request):
    form = ExampleForm()

    return render_to_response('example_form.html', {'form': form, 'request': request}, context_instance=RequestContext(request))


def test(request):
    form = TestForm()

    return render_to_response('test_form.html', {'form': form, 'request': request}, context_instance=RequestContext(request))
