from django.shortcuts import render
from loginapp.models import registration,admin,studentregistration,attendances,marksubmit,fac_leave_management,stu_leave_management
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
def authentication(request):    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=registration.objects.filter(password=password)
        p=registration.objects.filter(username=username)
        print(u)
        c=0
        if u.count()==1 and p.count()==1:
            c+=1
            queryset = registration.objects.all().filter(username=username)
            if c==1:
                return render(request,'studentpage.html',{'authors':queryset})
            
        else:
                return HttpResponse('login unsuccessfull')
    # user=authenticate(username=request.POST['username'],password=request.POST['password'])
    # if user==None:
    #     print('hai')
    #     return HttpResponse('username or password error')
def authentication1(request):    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        a=admin.objects.filter(password=password)
        b=admin.objects.filter(username=username)
       
        if a.count()==1 and b.count()==1:
          
            return render(request,'adminpage.html')
            
        else: 
            c=registration.objects.filter(password=password)
            d=registration.objects.filter(username=username)
           
            if c.count()==1 and d.count()==1:
                request.session['usr']=username
                return render(request,'facultypage.html')
            else:
                a=studentregistration.objects.filter(password=password)
                b=studentregistration.objects.filter(name=username)
                if a.count()==1 and b.count()==1:
                    request.session['usr1']=username
                    return render(request,'studentshome.html')
def index(request):
    return render(request,'index.html') 
def display(request):
    return render(request,'signup.html')
def Addattendance(request):
    return render(request,'Addattendance.html') 
    
def display1(request):
    return render(request,'orlogin.html')
def display2(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        batch=request.POST.get('batch')
        username=request.POST.get('username')
        password=request.POST.get('password')

    a= registration(name=name,email=email,phoneno=phoneno,batch=batch,username=username,password=password)
    a.save()
    return render(request,'facultyreg.html')
def studentreg(request):
    return render(request,'studentreg.html')
def facultyreg(request):
    return render(request,'facultyreg.html')
def adminstudentreg(request):
    return render(request,'adminstudentreg.html')
def facprofile(request):
    queryset = registration.objects.all().filter(username=request.session['usr'])[0]
    return render(request,'facprofile.html',{'authors':queryset})
def studentsprofile(request):
    queryset = studentregistration.objects.all().filter(name=request.session['usr1'])[0]
    return render(request,'studentsprofile.html',{'authors':queryset})

def studentsubmit(request):
    
    if request.method=='POST':

        admission_no=request.POST.get('admission_no')
        admission_date=request.POST.get('admission_date')
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(dob)
        a= studentregistration(admission_no=admission_no,admission_date=admission_date,name=name,dob=dob,gender=gender,mobile=mobile,guardian=guardian,batch=batch,email=email,password=password)
        a.save()
        return HttpResponse('Succsessfully registered')   

def Attendancesubmit(request):
    
    if request.method=='POST':

        student_name=request.POST.get('student_name')
        date=request.POST.get('date')
        name=request.POST.get('name')
        status_h1=request.POST.get('status_h1')
        status_h2=request.POST.get('status_h2')
        status_h3=request.POST.get('status_h3')
        status_h4=request.POST.get('status_h4')
        status_h5=request.POST.get('status_h5')
        a=attendances(student_name=student_name,Date=date,status_h1=status_h1,status_h2=status_h2,status_h3=status_h3,status_h4=status_h4,status_h5=status_h5)
        a.save()
        return HttpResponse('Succsessfully registered') 
def Marksubmit(request):
    if request.method=='POST': 
        student_name=request.POST.get('student_name')
        assess_no=request.POST.get('assess_no')
        max_mark=request.POST.get('max_mark')
        subject_1=request.POST.get('subject_1')
        subject_2=request.POST.get('subject_2')
        subject_3=request.POST.get('subject_3')
        subject_4=request.POST.get('subject_4')
        subject_5=request.POST.get('subject_5')
        a=marksubmit(student_name=student_name,assess_no=assess_no,max_mark=max_mark, subject_1= subject_1, subject_2= subject_2, subject_4= subject_4, subject_5= subject_5)
        a.save()
        return HttpResponse('Succsessfully registered')    
def addmark(request):
    return render(request,'addmark.html')
def fac_leave(request):
    return render(request,'fac_leave.html')
def facleavesubmit(request):
    if request.method=='POST': 
        leave_id=request.POST.get('leave_id')
        name=request.POST.get('name')
        from_date=request.POST.get('from_date')
        To_date=request.POST.get('To_date')
        reason=request.POST.get('reason')
        status=request.POST.get('status')
        a=fac_leave_management(leave_id=leave_id,name=name,from_date=from_date, To_date= To_date, reason= reason, status= status)
        a.save()
        return HttpResponse('Succsessfully registered')
def stuleave(request):
    return render(request,'stuleave.html') 
def stuleavesubmit(request):
    if request.method=='POST': 
        leave_id=request.POST.get('leave_id')
        name=request.POST.get('name')
        from_date=request.POST.get('from_date')
        To_date=request.POST.get('To_date')
        reason=request.POST.get('reason')
        status=request.POST.get('status')
    
        a=stu_leave_management(leave_id=leave_id,name=name,from_date=from_date, To_date= To_date, reason= reason, status= status)
        a.save()
        return HttpResponse('Succsessfully registered') 
def facleaveapprove(request):
    queryset = fac_leave_management.objects.all().filter(name='')[0]
    return render(request,'facleaveapprove.html',{'authors':queryset})     

def adminfacultydeta(request):
    queryset= registration.objects.all()
    return render (request,'adminfacultydeta.html',{'authors':queryset})

def adminstudentdeta(request):
    queryset=studentregistration.objects.all()
    return render(request,'adminstudentdeta.html',{'authors':queryset})

def facultystudentdeta(request):
    queryset=studentregistration.objects.all()
    return render(request,'facultystudentdeta.html',{'authors':queryset})


def logout_view(request):
    logout(request)
    return redirect('orlogin')

def facleaveview(request):
    queryset=fac_leave_management.objects.all()
    return render(request,'facleaveview.html',{'authors':queryset})

def stuleaveview(request):
    queryset=stu_leave_management.objects.all()
    return render(request,'stuleaveview.html',{'authors':queryset})

def approvefac(request):
    if request.method=='POST':
        name=request.POST.get('name')
        fac_leave_management.objects.filter(name=name).update(status='Approved')
        return render(request,'facleaveview.html')

def approvestu(request):
    if request.method=='POST':
        name=request.POST.get('name')
        stu_leave_management.objects.filter(name=name).update(status='Approved')
        return render(request,'stuleaveview.html')

