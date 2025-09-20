from django.shortcuts import render
def manu(request):
    return render(request,'FirstApp/empolyee1.html')
# Create your views here.
def manu2(request):
    return render(request,'FirstApp/empolyee2.html')
import datetime
def wishes3(request):
    date1=datetime.datetime.now()
    msg1='Hello User...GOOD'
    hr=int(date1.strftime('%H'))
    imgs='bgimage.jpg'
    if hr<12:
        msg1+=' Morning!!'
        imgs = 'bgimage.jpg'
    elif hr<16:
        msg1+=' Afternoon!!'
        imgs = 'bgimage.jpg'
    elif hr<20:
        msg1+=' Evening!!'
        imgs = 'image1 .jpg'
    else:
        msg1='Hello User...Very Good Night!!'
        imgs = 'bgimage.jpg'
    dict1={'date1':date1,'msg1':msg1,'imgs':imgs}
    return render(request,'FirstApp/wishes3.html',context=dict1)
