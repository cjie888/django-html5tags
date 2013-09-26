django-html5tags
================

# 说明
* app是基于bootstrap >=3
* 需要安装适当版本的markdown,安装命令 easy_install markdown

# 各个tag在template中的使用
* breadcrumb 使用

{% load breadcrumb %}
{% breadcrumb tuple request %}
其中tuple的格式为[{"name": "abc", "url": "/"}, {},....]


* add_crumb使用

{% load breadcrumb %}
{% add_crumb 'People' 'people_link' %}
第一个参数为name第二个参数为url
渲染的页面为：breadcrumb.html


* render_navbar使用

{% load navigation %}
{% render_navbar %}
网站顶部的浮栏显示出来，需要在settings中配置页面显示需要的全局配置
LOGIN_URL  登陆URL
LOGOUT_URL  注销URL
REGISTER_URL  注册URL
SITE_NAME  站点名称
悬浮高度是70px
下面的控件  marggin-top=70


* render_footer使用

{% load navigation %}
{% render_footer %}
在settings文件中配置FOOTER
例如：[
		[
			{"name": u"问题反馈", },
			{"name": u"常见问题解答", "url": "/"}
		],
		[
			{"name": u"合作伙伴", },
           	{"name": u"技术支持：应用研发系统组", "url": "/"}
        ]
   ]
其中每个list表示这一列要显示的项，第一项当做标题使用


* horizon_nav使用

{% load navigation %}
{% horizon_nav "当前选中的名称" 所有要显示的项  %}
或是可以在settings中配置HORIZON_SECTION
HORIZION_SECTION = [{"name": u"首页", "url": "/"},...]


* vertical_nav使用

{% load navigation %}
{% vertical_nav "当前选中的名称" 所有要显示的项  %}


* navtagitem使用
{% load navigation %}
<ul class="nav nav-pills nav-stacked">
	<li> {% navtagitem "手动添加垂直导航" "/" %}</li>
	<li>{% navtagitem "测试" "/" %}</li>
</ul>


* markdown2html使用

将markdown格式的转化为html
{% load markdown2html %}
{% markdowncss|markdown2html %}


* pagination使用

{% load pagination %}
{% pagination page_datas prefix request %}

* bootstrap tag 使用

{% load bootstrap %}
{{form|bootstrap}}
tag不支持textarea的markdown显示，如果需要markdown显示需要用下面的方式

* bootstrap form

写form类的时候引入
import html5tags.bootstrap as forms
bootstrap_textarea = forms.CharField(widget=forms.MarkDownTextarea)
其他的form的field使用方法和默认的forms一样
页面上的布局要自己定义
