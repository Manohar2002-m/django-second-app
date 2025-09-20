
from django.shortcuts import render
from FormApp.forms import StudentLoginForm
def studentloginpageview(request):
    sentdata = False;  # intially get-method(url)
    if request.method=='POST':
        formObj=StudentLoginForm(request.POST)
        if formObj.is_valid():
            print('Login-Form-Request-data Validation Success and printing data')
            print('User-Name : ',formObj.cleaned_data['username'])
            print('Password : ',formObj.cleaned_data['password'])
            uname = formObj.cleaned_data['username'];
            pwd = formObj.cleaned_data['password'];
            if uname=="sai" and pwd=="ram":
                sentdata=True;  #post-method(Form-submit)
                dict1 = {'sentdata': sentdata, 'username':uname}
                return render(request, 'FormApp/loginsuccess.html', context=dict1);
            else:
                return render(request, 'FormApp/loginunsuccess.html');
    else:
        return render(request, 'FormApp/loginunsuccess.html');





