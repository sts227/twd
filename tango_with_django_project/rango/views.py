from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def home_page(request):
	# Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Welcome to the world of Spencer.  This is from when he was sick."}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)

	context_dict = {}#add things in here later in the tutorial

	return render_to_response('rango/about.html', context_dict, context)
	
	#(would run this if i wasn't pulling the info from html file)
	#return HttpResponse('Rango sez here is the about page. <a href="/rango/">Home</a>')

def contact_us(request):
	context = RequestContext(request)
	
	context_dict = {}#add things in here later in the tutorial

	return render_to_response('rango/contact_us.html', context_dict, context)

	#(would run this if i wasn't pulling the info from html file) 
	#return HttpResponse('Rango sez here is the contact_us page. <a href="/rango/">Home</a>')
	
def gallery(request):
	context = RequestContext(request)
	
	context_dict = {}#add things in here later in the tutorial

	return render_to_response('rango/gallery.html', context_dict, context)
		