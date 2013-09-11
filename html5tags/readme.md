# 说明
* app是基于bootstrap >=3
* 需要安装适当版本的markdown
* 在运行app的example时需要将app复制到example文件中，否则会有找不到module的错误

# 各个tag在template中的使用
* breadcrumb 使用

{% load breadcrumb %}
{% breadcrumb tuple request %}
其中tuple的格式为[{"name": "abc", "url": "/"}, {},....]


* add_crumb使用

{% load breadcrumb %}
{% add_crumb 'People' 'list_people' %}
第一个参数为name第二个参数为url
渲染的页面为：breadcrumb.html


* render_header使用

{% load nav %}
{% render_header %}
网站顶部的浮栏显示出来，需要在settings中配置页面显示需要的全局配置
LOGIN_URL  登陆URL
LOGOUT_URL  注销URL
REGISTER_URL  注册URL
SITE_NAME  站点名称

* horizon_nav使用

{% load nav %}
{% horizon_nav "当前选中的名称" 所有要显示的项  %}
或是可以在settings中配置HORIZON_SECTION
HORIZION_SECTION = [{"name": u"首页", "url": "/"},...]


* vertical_nav使用

{% load nav %}
{% vertical_nav "当前选中的名称" 所有要显示的项  %}


* navtagitem使用

<ul class="nav nav-pills nav-stacked">
	<li> {% navtagitem "手动添加垂直导航" "/" %}</li>
	<li>{% navtagitem "测试" "/" %}</li>
</ul>


* markdown2html使用

将markdown格式的转化为html
{% load markdown2html %}
{% markdown2html markdowncss %}


* pagination使用

{% pagination page_datas pageno pagesize prefix %}
