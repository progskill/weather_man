import urllib.request
import json
from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member


# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=db61a63b1bf376b289b82b5ba3586812').read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
             "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)




def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('/membersList')  # Redirect to a success page after submission
    else:
        form = MemberForm()
    
    return render(request, 'main/addMember.html', {'form': form})

# View to display the list of members
def members_list(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'main/membersList.html', {'members': members})