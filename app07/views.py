from django.shortcuts import render
from .models import Info_Class,Occupations

# Create your views here.
def home_view(request):
  if request.method=='POST':
    detail=Info_Class.objects.order_by("Name")
    phonelist = list()
    
    for i in detail:
      phonelist.append(i.Phone)
      
    phone=request.POST['phone']

    if phone in phonelist:
      Ob=Info_Class.objects.get(Phone=phone)
      user=Ob.Name
      roll=request.POST['Roll']
      if str(roll) == str(Ob.SSC_Roll_No) :
        User=user
        Group_Id=roll
        cotext={
      'user':User,
      'group_id':Group_Id,
      'details' :detail
          }
        return render(request, 'infrom.html',cotext)
      else:
        User="Wrong Phone Number Or Roll Number"
      Group_Id="Please try again"
      cotext={
      'user':User,
      'group_id':Group_Id,
        
      }
      return render(request, 'base.html',cotext)
    else:
      User="Wrong Phone Number Or Roll Number"
      Group_Id="Please try again"
      cotext={
      'user':User,
      'group_id':Group_Id,
        
      }
      return render(request, 'base.html',cotext)

    

  else:
    details=Info_Class.objects.order_by("Name")
    
    Home_page="It's a login Page"
    cotext={
      'details':details,
      'Home_page':Home_page,
        
      }
    return render(request, 'base.html',cotext)
def signup_view(request):
  if request.method=="POST":
    Name=request.POST['Occupation_Name']
    Oco=Occupations(Occupation_Name=Name)
    Oco.save()
  
  
  detail=Occupations.objects.order_by("Occupation_Name")
  cotext={
      'details':detail,
      }
  return render(request, 'signup.html',cotext)

def signup1_view(request):
  phonelist = list()
  rolllist= []
  detail=Info_Class.objects.order_by("Name")
  for i in detail:
    phonelist.append(i.Phone)
    rolllist.append(str(i.SSC_Roll_No))

  Phone=request.GET['Phone']
  Roll=request.GET['SSC_Roll_No']
  roll=str(Roll)
  
  print(roll)
  print(rolllist)  
  if roll in rolllist or Phone in phonelist :
    
    detail=Occupations.objects.order_by("Occupation_Name")
    cotext={
      'details':detail,
      'error':'Alreay Exist'
      }
    return render(request, 'signup.html',cotext)
  
  
 
  
  else:
    signup=Info_Class(Name=request.GET['Name'], Phone=request.GET['Phone'], SSC_Roll_No=request.GET['SSC_Roll_No'], SSC_Board=request.GET['SSC_Board'], Email=request.GET['Email'],Blood_Group=request.GET['Blood_Group'],Occupation_id=request.GET['Occupation'],Address=request.GET['Address'])
    signup.save()
    context={'message':'Now you can Login using your Phone Number and SSC Roll Number'}
    return render(request, 'base.html',context)
  
    