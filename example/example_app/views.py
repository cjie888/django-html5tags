# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings

from forms import ExampleForm, TestForm

"""此处可以直接调用toollib的get_page函数"""
from django.core.paginator import Paginator
class ExtensionPaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=4, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num
 
    def page(self, number):
        self.page_num = number
        return super(ExtensionPaginator, self).page(number)
 
    def _page_range_extension(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        self.page_num = int(self.page_num)
        num_list.append(self.page_num)
 
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)
            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
 
        num_list.sort()
        return num_list
    page_range_extension = property(_page_range_extension)
 
 
def do_paginate(datas, pageno=1, pagesize=10):
    paginator = ExtensionPaginator(datas, pagesize)
    try:
        result_page = paginator.page(pageno)
    except:
        result_page = paginator.page(paginator.num_pages)
    return result_page



def home(request):
    test  = u"* test测试"
    datas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    pages = do_paginate(datas, 1, 2)
    return render_to_response("index.html", {"settings": settings, "request": request, "test": test,
                                             "pages": pages}, context_instance=RequestContext(request))

def form_tag(request):
    form = ExampleForm()

    return render_to_response('form_tag.html', {'form': form, 'request': request}, context_instance=RequestContext(request))


def rewrite_form(request):
    form = TestForm()

    return render_to_response('rewrite_form.html', {'form': form, 'request': request}, context_instance=RequestContext(request))
