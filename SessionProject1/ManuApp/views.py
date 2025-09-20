from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
#Session-Application-1
def page_count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    print(request.session.get_expiry_age())	#check in server-console
    print(request.session.get_expiry_date())
    return render(request,'ManuApp/pagecount.html',{'count':newcount})


