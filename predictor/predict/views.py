from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from .models import predict
from django.template import loader
from .forms import user_forms


def index(request):
    context = {}
    context['form'] = user_forms()
    return render(request , "predict/NIT_Mizo_Mainpage.html", context)

def user_forms_view(request):
    t=0
    b=""
    if request.method == "POST":
        
        # Take in the data the user submitted and save it as form
        form = user_forms(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():
            t = int(request.POST.get('Time_hour'))
            b = str(request.POST.get('block_'))
            # Redirect user to list of tasks
            #return HttpResponseRedirect(reverse("predict:NIT_Mizo_Mainpage.html"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return redirect(index)

    # return render(request, "predict/NIT_Mizo_Mainpage.html", {"form": form})
    return render(request, "predict/NIT_Mizo_Mainpage.html", {"ff":calc(t,b)})



def submit(request):
    return render(request, "predict/template.html", {
        "form": user_forms()
    })

def testing(request):
    #mydata = predict.objects.filter(city="patna")
    T = predict.objects.values_list('Date_Time')
    #mydata = predict.objects.values_list('country')
    #template = loader.get_template('predict/template.html')
    #context = {
    #'mymembers': mydata,
  #}
    return HttpResponse(T)
  
def calc(t, b):
   mydata = predict.objects.filter(block=b)
   count =0
   
   for x in mydata:
        if (t>=(x.time_hour-1) and t<=(x.time_hour+1)):
           count = count+1 
   if(count<=5 and count>=1):
       return "moderate"
   if(count <=1) :
       return "safe"
   else:
        return "high risk"

