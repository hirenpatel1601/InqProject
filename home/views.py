from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from twilio.rest import Client
# Create your views here.
def index (request):
    if request.method == "POST":
        email=request.POST.get('email')
        StudentFirstName=request.POST.get('sfname')
        StudentMidleName=request.POST.get('smname')
        StudentLastName=request.POST.get('slname')
        StudentMobile=request.POST.get('smobile')
        ParentFirstName=request.POST.get('pfname')
        ParentMidleName=request.POST.get('pmname')
        ParentLastName=request.POST.get('plname')
        ParentMobile=request.POST.get('pmobile')
        Address=request.POST.get('address')
        Selection=request.POST.get('selection')
        Question=request.POST.get('question')
        date=datetime.today()


        ParentLastName=request.POST.get('plname')
        ParentLastName=request.POST.get('plname')
        msg= "New Inquiry Done on By\n " + StudentFirstName + " " + StudentMidleName +" "+StudentLastName+ "\nMobile No - " + StudentMobile + "\nParent Name - \n" + ParentFirstName +" "+ ParentMidleName +" " + ParentLastName + "\nParent Mobile - " + ParentMobile + "\nFrom - " + Address + "\n For - "+ Selection + "\nQuestion - " + Question



        account_sid = 'AC380dac77b1d3582768d934ef2667d980'
        auth_token = 'b65e29a7e8280f26d66cbde0c8fb4e19'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=msg,
                              to='whatsapp:+918450968630'
                          )
        print(message.sid)




        objcontact = Contact(email=email,
                        StudentFirstName=StudentFirstName,
                        StudentMidleName=StudentMidleName,
                        StudentLastName=StudentLastName,
                        StudentMobile=StudentMobile,
                        ParentFirstName=ParentFirstName,
                        ParentMidleName=ParentMidleName,
                        ParentLastName=ParentLastName,
                        ParentMobile=ParentMobile,
                        Adress=Address,
                        Selection=Selection,
                        Question=Question,
                        date=date
                        )
        objcontact.save()
        





    return render(request, "index.html")
   #return HttpResponse("This is Home page")

