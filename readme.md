#My First Website with Django backend

## <h1 style= "color:red">working </style>

>When some page request is done , server checks url.py in the main app's name folder.  
it checks if there is any specific page or action mentioned for that url and executes that action or goes to that page

...
>Now we make changes in the models , define classes and database and do makemigration which makes database in sqlite

...
<h3 style="color:green">NOTE</h3>  
Whenever we make change in model and database we apply makemigrations and migrate to make sure everything's synced up.   

...

## another features: decide what to print when a model is called
make a function called __str__ and return whatever string you want   
it acts like the string representation of a object


...

# Admin section 
>As the name suggests it manages the whole database as admin , can edit , delete or add anything in there.

# Passing variables from url to views - 
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),     

this passes the album_id from url to views and the views.py recieves it as    

    def detail(request,album_id):
        return HttpResponse("<h1>Details for album_id: "+ str(album_id) + "</h1>")
    
and passes it to the front-end web-page that we see....


# connect the backend with frontend
This is done using loader from django.templates  
    
    template = loader.get_template('music/index.html')

Now it gets the index.html file from music folder  
next thing is to 

      return HttpResponse( template.render(context,request) )

so this is the return HttpsResponse  
it contains context which is a dictionary which has a few set of variables which can be used in html page.

# How to use pyhton in html page 

 we use 
    
    {% for x in the dict %}
        some statement 
    {% endfor %}

similarly if is used the same way

<h3 style="color:yellow"> NOTE : Realisation about views</h3>  
the functions in it are actually the html pages and the functions call the pages and denote what to pass in it.


# 404 ERROR

        from django.http import Http404

        try:
            album = Album.objects.get(id=album_id)
        except Album.DoesNotExist: 
            raise Http404("Album does not exist") 

That all about 404ERROR

 
