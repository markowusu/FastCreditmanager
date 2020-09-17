from django.shortcuts import render,get_object_or_404,redirect
from .models import User_table
from.models import Transaction_table
from .forms import transactForm
# from django.http import HttpResponse
# Create your views here.

def homePage(request):

    return render(request,"creditApp/home.html")


def get_user(request):
    user_details = User_table.objects.all()
    context = {
        'user_details': user_details
    }
    return render(request, 'creditApp/users.html', context=context)    



def  get_individual(request,id):
    individual = get_object_or_404(User_table,pk=id)
    
    context={
        'individual': individual
    }
    return render(request,'creditApp/individual.html',context=context)


def creatTransaction(request):
    form = transactForm()
    
    context={
        'form':form
    }
    if request.method == 'POST':
        form = transactForm(request.POST)
        # print("returning {}".format(request.POST.get('trans_from')))
        
        if (request.POST.get('Transfer_from') != request.POST.get('Transfer_to')):
            if form.is_valid():
                form.save()
                # getting the fromuserin the post dict.

                # username = form_details.cleaned_data.get("from_trans")
                username = request.POST.get('Transfer_from')

                # getting the userto name from the post dict

                # username_to =form_details.cleaned_data.get("to_trans") 
                username_to = request.POST.get('Transfer_to')
                #  getting the credit being passed by the from user in post dict
                # amount = form_details.cleaned_data.get('currentCredit')
                # print("Printing the value {} and {}".format(username,username_to))
                # print("printing the post %5s" % request.POST)
                

                amount= request.POST.get('credit')
            
                    # this gets the current current of the the to user.
                from_user= User_table.objects.get(id = username)
                from_user_credit= from_user.currentCredit
                print(from_user_credit)


                to_user = User_table.objects.get(id=username_to)
                to_user_credit = to_user.currentCredit

                # option_from = Transaction_table.objects.get('trans_from'==username)
                # option_to = Transaction_table.objects.get('trans_to'== username_to)

                new_userto_credit = int(to_user_credit) + int(amount) # new credit for the to user
                new_userfrom_credit = int(from_user_credit) - int(amount) # new credit to from user

                # updating the new credting to from user
                upadate_userfrom = User_table.objects.get(id=username)
                upadate_userfrom.currentCredit = new_userfrom_credit
                upadate_userfrom.save()

                # updating the new credit to the to user
                upadate_userto = User_table.objects.get(id =username_to)
                upadate_userto.currentCredit = new_userto_credit
                upadate_userto.save()

                return redirect('/')
    return render(request,'creditApp/transaction.html',context=context )



def history(request):
    
    transact_details= Transaction_table.objects.all()
 
    context = {
        'transact_details': transact_details
    }

    return render(request,'creditApp/history.html',context=context)



        
