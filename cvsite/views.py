from django.shortcuts import render
from .forms import Contact
#from .models import Event

def home(request):

	if request.method == "POST":

		name = request.POST['Name']
		phone = request.POST['Phone']
		email = request.POST['Email']
		message = request.POST['message']
		
		return render(request, 'home.html', {'sub_message': name})
	else:
		pass
#	form = Contact


	return render(request, 'home.html', {})
