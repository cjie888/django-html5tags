# -*- coding: utf-8 -*-
# from django.shortcuts import redirect
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as djangologin
# from django.contrib.auth import logout as djangologout
# from django.contrib.auth.models import User as DjangoUser
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings


def home(request):
    test  = u"* test测试"
    
    return render_to_response("index.html", {"settings": settings, "request": request, "test": test},
                              context_instance=RequestContext(request))

