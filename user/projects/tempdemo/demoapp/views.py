#from django.http import request
from django.shortcuts import render
import datetime

def display(request):
    message="Hii!!!"
    date=datetime.datetime.now()
    hour=int(date.strftime('%H'))
    if hour<12:
        message+= "  Good morning"
    else:
        message+= "  Good evening"
    name = 'MARISELVAM RAMAR'
    date_dict= {'display_date':date, 'Name':name, 'greetings':message}
    return render(request, 'demoapp/abc.html', context = date_dict)

# Create your views here.
