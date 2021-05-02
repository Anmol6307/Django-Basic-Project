from django.shortcuts import render

# Create your views here.

def Fees_Django(request):
    return render(request, 'fees/fees1.html', {'title':'feesdjango', 'cname':'Django', 'charge':'500'})
