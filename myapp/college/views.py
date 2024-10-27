from django.shortcuts import render,redirect
from college.models import user_master,college_master,add_book,book_issuse
from django.contrib.auth import logout
def user(request):#signup
    if request.method=='POST':
        student_name=request.POST['student_name']
        regd_no=request.POST['regd_no']
        branch=request.POST['branch']
        year=request.POST['year']
        section=request.POST['section']
        image=request.FILES['image']
        mobile=request.POST['mobile']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        ob=user_master.objects.create(student_name=student_name,regd_no=regd_no,branch=branch,year=year,section=section,image=image,mobile=mobile,email=email,address=address,password=password)
        ob.save()
        return render(request,'signup.html',{"output":'saved '})
    return render(request,'signup.html')
def slogin(request):#login
    if request.method=='POST':
        regd_no=request.POST['regd_no']
        password=request.POST['password']
        
        o=user_master.objects.get(regd_no=regd_no,password=password)
        request.session['regd_no']=o.regd_no
      
        return redirect('shome')
    return render(request,'slogin.html')
def qview(request):#student view/ home page 
   
    regd_no=request.session.get('regd_no')

    w=user_master.objects.get(regd_no=regd_no)
    v=book_issuse.objects.filter(regd_no=w)
    print(v)
    
    
    return render(request,'sview.html',{'regd_no':regd_no,'ob':w,'ob2':v})

#---------------------------------------------------------------------------------------------------------------
def admin(request):# admin login
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        o=college_master.objects.get(email=email,password=password)
        return redirect('ahome')
    return render(request,'alogin.html')

def whome(request):
    sn=user_master.objects.all()
    bn=add_book.objects.all()[::-1]
    if request.method=="POST":
        btn=request.POST['btn']
        if btn=="delete":
            book_no=request.POST['book_no']
            print(book_no)
            b=add_book.objects.get(book_no=book_no).delete()
            return  redirect('ahome')  
        if btn=="Delete":
            regd_no=request.POST['regd_no']
            b=user_master.objects.get(regd_no=regd_no).delete()
            return  redirect('ahome')
        if btn=='edit':
            regd_no=request.POST['regd_no']
            sn=user_master.objects.get(regd_no=regd_no)
            return render(request,'edit.html',{'sname':sn})
    return render(request,'ahome.html',{'data3':sn,'data4':bn})


#-------------------------------admin part end here--------------------------------------------------------------------

def addbook(request):#addbook
    if request.method=='POST':
        book_name=request.POST['book_name']
        book_no=request.POST['book_no']
        b=add_book.objects.create(book_name=book_name,book_no=book_no)
        b.save()
        return render(request,'addbook.html',{'bo':'add book sucess'})
    return render(request,'addbook.html')

def bookissuse(request):
    bk=add_book.objects.all()
    s=user_master.objects.all()
    if request.method=='POST':
        book_name=request.POST['book_name']
        regd_no=request.POST['regd_no']
        f=add_book.objects.get(book_name=book_name) #get the data
        g=user_master.objects.get(regd_no=regd_no)
        date=request.POST['date']
        bi=book_issuse.objects.create(book_name=f,regd_no=g,date=date)
        bi.save()
        return render(request,'bookissuse.html',{'data9':'book issuse sucessfully'})
    return render (request,'bookissuse.html',{'data':bk,'data2':s})
 
def issueshow(request):
    bs=book_issuse.objects.all()
    return render(request,'issuedetails.html',{'show':bs})

#------------------------------------------------------------------------------------
def logout_view(request):
    logout(request) 
    return redirect('alogin')
def logout_sview(request):
    logout(request) 
    return redirect('slogin')

#-----------------------------------------------------------------------------------------------
def update(request): #update
    if request.method=='POST':
        student_name=request.POST['student_name']
        regd_no=request.POST['regd_no']
        branch=request.POST['branch']
        year=request.POST['year']
        section=request.POST['section']
        # image=request.FILES['image']
        mobile=request.POST['mobile']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        
        ob=user_master.objects.filter(regd_no=regd_no).update(student_name=student_name,regd_no=regd_no,branch=branch,year=year,section=section,mobile=mobile,email=email,address=address,password=password)
        return redirect('ahome')
    return render(request,'ahome.html')
