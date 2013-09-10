# -*- coding: utf-8 -*-
from django import template
from django.template import Context
from django.core.paginator import Paginator

register = template.Library()


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


@register.tag("pagination")
def do_pagination(parser, token):
    try:
        tag_name, data_pager, pageno, pagesize, url_path = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires two argument" % token.contents.split()[0])

    if url_path[0] != url_path[-1] and url_path[0] in ('"', "'"):
        raise template.TemplateSyntaxError("%r tag's second argument should be in quotes" % tag_name)
    return PaginationNode(data_pager, pageno, pagesize, url_path)


class PaginationNode(template.Node):
    def __init__(self, data_pager, pageno, pagesize, url_path):
        self._data_pager = template.Variable(data_pager)
        self._pageno = template.Variable(pageno)
        self._pagesize = template.Variable(pagesize)
        self._url_path = template.Variable(url_path)

    def render(self, context):
        t = template.loader.get_template("tags/pagination.html")
        url = self._url_path.resolve(context)
        pagesize = self._pagesize.resolve(context)
        pageno = self._pageno.resolve(context)
        data_pager = self._data_pager.resolve(context)
        result_page = do_paginate(data_pager, pageno, pagesize)

        if "?" in url:
            prefix = url.split("?")[0]
            parameter = url.split("?")[1]
            new_context = Context({"pager": result_page,#self._pager.resolve(context),
                                   "prefix": prefix, "parameter": parameter},
                                  autoescape=context.autoescape)
        else:
            new_context = Context({"pager": result_page,#self._pager.resolve(context),
                                   "prefix": url},
                                  autoescape=context.autoescape)
        return t.render(new_context)
