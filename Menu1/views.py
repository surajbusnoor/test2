from django.shortcuts import render
from Menu1.forms import form1

# Create your views here.
def style1_1(request):

    form = form1()
    print(form)
    d1 = {
        'form': form
    }
    return render(request, 'mnu1.html',d1)

def index1(request):
    return render(request, 'Index.html')
