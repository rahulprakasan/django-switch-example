from django.shortcuts import render
import datetime
from waterapp import forms
from waterapp.models import button
def index(request):
    if request.method == 'POST':
        if 'btn1' in request.POST:
            now = datetime.datetime.now()
            now1 = now.strftime("%Y-%m-%d")
            t = button(button="on", date=now1)
            t.save()
            print("newrecord created successfully")
        if 'btn2' in request.POST:
            now = datetime.datetime.now()
            now1=now.strftime("%Y-%m-%d")
            t = button(button="off", date=now1)
            t.save()
            print("newrecord created successfully")

    return render(request,'basicapp/index.html')
def form_name_view(request):
    form =forms.formName
    if request.method =='POST':
        form=forms.formName(request.POST)
        if form.is_valid():
            print("VALIDATION  SUCCESSFUL")
            print('NAME: '+form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])

    return render(request,'basicapp/forms.html',{'form':form})
# Create your views here.
def status (request):
    status_list = button.objects.order_by('id')
    status_dict = {'button_status': status_list}
    return render(request, 'basicapp/status.html', context=status_dict)


def switch(request):
    status_list = button.objects.order_by('id')
    status_dict={'status':status_list.last()}
    return render(request, 'basicapp/switch.html',context=status_dict)



