from django.contrib import admin
from loginapp import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.authentication,name="login"),
    path('signup',views.display,name="signup"),
    path('orlogin',views.display1,name="orlogin"),
    path('submit',views.display2,name="submit"),
    path('adminlogin',views.authentication1,name="login1"),
    path('studentreg',views.studentreg,name="studentreg"),
    path('studentsubmit',views.studentsubmit,name="studentsubmit"),
    path('facultyreg',views.facultyreg,name="facultyreg"),
    path('facprofile',views.facprofile,name="facprofile"),
    path('studentsprofile',views.studentsprofile,name="studentsprofile"),
    path('Addattendance',views.Addattendance,name="Addattendance"),
    path('Attendancesubmit',views.Attendancesubmit,name="Attendancesubmit"),
    path('addmark',views.addmark,name="addmark"),
    path('marksubmit',views.Marksubmit,name="marksubmit"),
    path('fac_leave',views.fac_leave,name="fac_leave"),
    path('stuleave',views.stuleave,name="stuleave"),
    path('stuleavesubmit',views.stuleavesubmit,name="stuleavesubmit"),
    path('facleaveview',views.facleaveview,name="facleaveview"),
    path('stuleaveview',views.stuleaveview,name="stuleaveview"),
    path('facleavesubmit',views.stuleavesubmit,name="facleavesubmit"),
    path('adminstudentreg',views.adminstudentreg,name="adminstudentreg"),
    path('adminfacultydeta',views.adminfacultydeta,name="adminfacultydeta"),
    path('adminstudentdeta',views.adminstudentdeta,name="adminstudentdeta"),
    path('facultystudentdeta',views.facultystudentdeta,name="facultystudentdeta"),
    path('approve',views.approvefac,name='approve'),
    path('apprv',views.approvestu,name='apprv'),
    path('logout',views.logout_view,name="logout"),


    

    
    


    
]
