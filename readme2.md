# part 2 of the readme file 

# How to not hardcode things in html pages...
The urls in url has a attribute name which can be used directly in html pages instead of hardcoding the links.  

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),

<font color='red'>the name here can be used in </font>

    <li> <a href = "{% url 'detail' album.id %}"> {{ album.album_title }}</a> </li>

but what is there is the same named url in other apps also , in that case we'll have to specify app_name in url.py file and instead of just writing name of url in html page we'll write app_name:url_name and that works.  

# URLS aren't always fixed to a new page but can also perform some logic operation