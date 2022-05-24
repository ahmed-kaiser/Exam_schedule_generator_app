from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import random
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q, Count, Sum
from datetime import datetime, date, time, timedelta
from django.utils.timezone import make_aware
from .models import Rooms
from .models import CSE_eve_batch_info, CSE_eve_course_list, CSE_eve_trimister, CSE_day_batch_info, CSE_day_course_list, CSE_day_trimister
from .models import EEE_eve_batch_info, EEE_eve_course_list, EEE_eve_trimister, EEE_day_batch_info, EEE_day_course_list, EEE_day_trimister
from .models import CEN_eve_batch_info, CEN_eve_course_list, CEN_eve_trimister, CEN_day_batch_info, CEN_day_course_list, CEN_day_trimister
from .models import BTE_eve_batch_info, BTE_eve_course_list, BTE_eve_trimister, BTE_day_batch_info, BTE_day_course_list, BTE_day_trimister
from .models import EVE_routine, DAY_routine, publish
from .forms import cse_eve_batch_info_form, cse_eve_course_list_form, cse_day_batch_info_form, cse_day_course_list_form
from .forms import eee_eve_batch_info_form, eee_eve_course_list_form, eee_day_batch_info_form, eee_day_course_list_form
from .forms import cen_eve_batch_info_form, cen_eve_course_list_form, cen_day_batch_info_form, cen_day_course_list_form
from .forms import bte_eve_batch_info_form, bte_eve_course_list_form, bte_day_batch_info_form, bte_day_course_list_form
from .forms import eve_routine_form, day_routine_form

#.....View..........
def index(request):
    return render(request, 'home/index.html')

def view_routine_eve(request):
    if publish.objects.filter(batch="Evening").exists():
        schedule = EVE_routine.objects.all().order_by('exam_date', 'dept', 'batch', 'section')
        date_list = EVE_routine.objects.all().distinct('exam_date').values('exam_date', 'exam_time', 'weekday')
        info = publish.objects.get(batch="Evening")
        return render(request, 'home/view_routine_eve.html', {'schedule':schedule, 'date_list':date_list, 'info':info})
    else:
        messages.warning(request, "Exam Schedule Not Published Yet............!!")
        return render(request, 'home/index.html')

def view_routine_day(request):
    if publish.objects.filter(batch="Day").exists():
        schedule = DAY_routine.objects.all().order_by('exam_date', 'dept', 'batch', 'section')
        course_list = DAY_routine.objects.all().distinct('course_code').values('course_code', 'course_name')
        date_list = DAY_routine.objects.all().distinct('exam_date').values('exam_date', 'exam_time', 'weekday')
        info = publish.objects.get(batch="Day")
        return render(request, 'home/view_routine_day.html', {'schedule':schedule, 'date_list':date_list, 'info':info, 'course_list':course_list})
    else:
        messages.warning(request, "Exam Schedule Not Published Yet............!!")
        return render(request, 'home/index.html')

def view_search_schedule_day(request):
    try:
        if request.method == "POST":
            dept = request.POST.get('dept')
            dept = dept.upper()
            batch = int(request.POST.get('batch'))

            try:    
                if DAY_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).exists():
                    routine = DAY_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).order_by('exam_date', 'section')
                    info = publish.objects.get(batch="Day")
                    return render(request, 'home/view_search_schedule_day.html', {'schedule':routine, 'info':info})
                else:
                    messages.warning(request, "No Information Exist.....")
                    return redirect('/view_routine_day.html')
            except:
                messages.warning(request, "No Information Exist.....")
                return redirect('/view_routine_day.html')
    except:
        messages.warning(request, "You Enter Wrong Information.....")
        return redirect('/view_routine_day.html')

def view_search_schedule_eve(request):
    try:
        if request.method == "POST":
            dept = request.POST.get('dept')
            dept = dept.upper()
            batch = int(request.POST.get('batch'))

            try:    
                if EVE_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).exists():
                    routine = EVE_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).order_by('exam_date', 'section')
                    info = publish.objects.get(batch="Evening")
                    return render(request, 'home/view_search_schedule_eve.html', {'schedule':routine, 'info':info})
                else:
                    messages.warning(request, "No Information Exist.....")
                    return redirect('/view_routine_eve.html')
            except:
                messages.warning(request, "No Information Exist.....")
                return redirect('/view_routine_eve.html')
    except:
        messages.warning(request, "You Enter Wrong Information.....")
        return redirect('/view_routine_eve.html')

#.....log ........

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user = User.objects.get(username=username)
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    messages.success(request, 'Welcome Admin.......')
                    return redirect('/admin.html')
                elif user.username == 'CSE':
                    messages.success(request, 'Welcome Admin.......')
                    return redirect('/cse_admin.html')
                elif user.username == 'EEE':
                    messages.success(request, 'Welcome Admin.......')
                    return redirect('/eee_admin.html')
                elif user.username == 'CEN':
                    messages.success(request, 'Welcome Admin.......')
                    return redirect('/cen_admin.html')
                elif user.username == 'BTE':
                    messages.success(request, 'Welcome Admin.......')
                    return redirect('/bte_admin.html')
        else:
            messages.info(request, 'Username Or Password Is Incorrect....')
            return redirect('/login.html')
    else:
        return render(request, 'login.html')

@login_required(login_url='/login.html')
def logout_user(request):
    logout(request)
    return redirect('/login.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def admin(request):
    return render(request, 'admin.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def changepass(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            if pass1 == pass2:
                user = User.objects.get(username=username)
                user.set_password(pass1)
                user.save()
                messages.success(request, 'Password Changed Successfully...')
                return redirect('changepass.html')
            else:
                messages.warning(request, 'Password Are Not Same....')
                return redirect('changepass.html')
        else:
            messages.warning(request, 'Invalid Username Or Password....')
            return redirect('changepass.html')
    else:            
        return render(request, 'changepass.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def subuser(request):
    user_list = User.objects.all().filter(is_superuser=False)
    return render(request, 'subuser.html', {'user_list':user_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def superuser(request):
    user_list = User.objects.all().filter(is_superuser=True)
    return render(request, 'superuser.html', {'user_list':user_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def create_superuser(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        first_name = first_name.title().strip()
        last_name = last_name.title().strip()

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exist....')
                return redirect('/superuser.html')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist....')
                return redirect('/superuser.html')
            else:
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name, last_name=last_name, is_superuser=True, is_staff=True)
                user.save()
                messages.success(request, 'User Created Successfully.....')
                return redirect('/superuser.html')
        else:
            messages.warning(request, 'Password Not Match....')
            return redirect('/superuser.html')
    else:
        return render(request, 'superuser.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def createuser(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        first_name = first_name.title().strip()
        last_name = last_name.title().strip()
        username = username.upper().strip()

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exist....')
                return redirect('/subuser.html')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist....')
                return redirect('/subuser.html')
            else:
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'User Created Successfully.....')
                return redirect('/subuser.html')
        else:
            messages.warning(request, 'Password Not Match....')
            return redirect('/subuser.html')
    else:
        return render(request, 'subuser.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def remove_user(request, value):
    try:
        user = User.objects.get(id=value)
        user.delete()
        return redirect('/subuser.html')
    except:
        return redirect('/subuser.html')

@login_required(login_url='/login.html')
def error(request):
    return render(request, 'error.html')

#.........Room.......

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def room(request):
    if request.method == 'POST':
        room_no = request.POST.get('room_no')
        room_capacity = request.POST.get('room_capacity')
        if Rooms.objects.filter(room_no= room_no).exists():
            messages.warning(request, 'Room Already Exist....')
            return redirect('/room.html')
        else:
            add_room = Rooms(room_no=room_no, room_capacity=room_capacity)
            add_room.save()
            messages.success(request, 'Room Details Added Successfully......')
            return redirect('/room.html')

    room_list = Rooms.objects.all().order_by('room_no')
    return render(request, 'room.html', {'room_list':room_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def room_search(request):
    try:
        if request.method == 'POST':
                search = request.POST.get('search')
                if Rooms.objects.all().filter(room_no=search).exists():
                    room_list = Rooms.objects.filter(room_no=search)
                    return render(request, 'room_search.html', {'room_list': room_list})
                else:
                    messages.warning(request, 'Room Info Does Not Exist In The List......')
    except:
        messages.warning(request, 'Room Info Does Not Exist In The List......')
    return redirect('/room.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def room_delete(request, value):
    room_no = value
    if request.method == 'POST':
        if Rooms.objects.filter(room_no=room_no).exists():
            Rooms.objects.filter(room_no=room_no).delete()
            messages.success(request, 'Info Successfully Deleted...')
            return redirect('/room.html') 
    else:
        messages.warning(request, 'Info Not Deleted..')
        return redirect('/room.html') 

# .........CSE Evening...........

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_admin(request):
     return render(request, 'cse/cse_admin.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = CSE_eve_trimister.objects.filter(trimister=request.POST.get('trimister')).first()

            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()

            if CSE_eve_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Similler Course Info Already Exist In The Course List...')
                return redirect('/cse_eve_offered_courses.html')
            else:
                course_list = CSE_eve_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/cse_eve_offered_courses.html')

    trimister_list = CSE_eve_trimister.objects.all().order_by('trimister')
    course_list = CSE_eve_course_list.objects.all().order_by('trimister')
    return render(request, 'cse/cse_eve_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 11):
                if CSE_eve_course_list.objects.all().filter(trimister=search).exists():
                    course_list = CSE_eve_course_list.objects.filter(trimister=search)
                    return render(request, 'cse/cse_eve_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/cse_eve_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/cse_eve_offered_courses.html')
        except:
            search = search.upper()
            if CSE_eve_course_list.objects.all().filter(course_code=search).exists():
                course_list = CSE_eve_course_list.objects.filter(course_code=search)
                return render(request, 'cse/cse_eve_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/cse_eve_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')   
def cse_eve_course_delete(request, value):
    if request.method == 'POST':
        if CSE_eve_course_list.objects.filter(id=value).exists():
            CSE_eve_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/cse_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/cse_eve_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_get_offered_courses(request, value):
    offered_courses = CSE_eve_course_list.objects.filter(id=value)
    return render(request, 'cse/cse_eve_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_edit_offered_courses(request):
    return render(request, 'cse/cse_eve_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_update_offered_courses(request, value):
    offered_courses = CSE_eve_course_list.objects.get(id=value)
    form = cse_eve_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cse_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cse_eve_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = CSE_eve_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = CSE_eve_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/cse_eve_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/cse_eve_batch_info.html')

    trimister_list = CSE_eve_trimister.objects.all().order_by('trimister')
    info_list = CSE_eve_batch_info.objects.all().order_by('batch_no')
    return render(request, 'cse/cse_eve_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_get_batch_info(request, value1, value2):
    batch_info = CSE_eve_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'cse/cse_eve_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_edit_batch_info(request):
    return render(request, 'cse/cse_eve_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_update_batch_info(request, value):
    batch_info = CSE_eve_batch_info.objects.get(id=value)
    form = cse_eve_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cse_eve_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cse_eve_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_delete_batch_info(request, value):
    if request.method == 'POST':
        if CSE_eve_batch_info.objects.filter(id=value).exists():
            CSE_eve_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/cse_eve_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/cse_eve_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = CSE_eve_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/cse_eve_trimister.html')
    
    batch_list = CSE_eve_batch_info.objects.all().order_by('batch_no')
    trimister_info = CSE_eve_trimister.objects.all().order_by('trimister')
    return render(request, 'cse/cse_eve_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_eve_delete_trimister(request, value):
    if request.method == 'POST':
        if CSE_eve_trimister.objects.filter(trimister=value).exists():
            CSE_eve_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/cse_eve_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/cse_eve_trimister.html')

# ......CSE DAY........

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = CSE_day_trimister.objects.filter(trimister=request.POST.get('trimister')).first()

            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()

            if CSE_day_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Similler Course Info Already Exist In The Course List')
                return redirect('/cse_day_offered_courses.html')
            else:
                course_list = CSE_day_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/cse_day_offered_courses.html')

    trimister_list = CSE_day_trimister.objects.all().order_by('trimister')
    course_list = CSE_day_course_list.objects.all().order_by('trimister')
    return render(request, 'cse/cse_day_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 13):
                if CSE_day_course_list.objects.all().filter(trimister=search).exists():
                    course_list = CSE_day_course_list.objects.filter(trimister=search)
                    return render(request, 'cse/cse_day_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/cse_day_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/cse_day_offered_courses.html')
        except:
            search = search.upper()
            if CSE_day_course_list.objects.all().filter(course_code=search).exists():
                course_list = CSE_day_course_list.objects.filter(course_code=search)
                return render(request, 'cse/cse_day_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/cse_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')    
def cse_day_course_delete(request, value):
    if request.method == 'POST':
        if CSE_day_course_list.objects.filter(id=value).exists():
            CSE_day_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/cse_day_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/cse_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_get_offered_courses(request, value):
    offered_courses = CSE_day_course_list.objects.filter(id=value)
    return render(request, 'cse/cse_day_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_edit_offered_courses(request):
    return render(request, 'cse/cse_day_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_update_offered_courses(request, value):
    offered_courses = CSE_day_course_list.objects.get(id=value)
    form = cse_day_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cse_day_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cse_day_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = CSE_day_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = CSE_day_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/cse_day_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/cse_day_batch_info.html')

    trimister_list = CSE_day_trimister.objects.all().order_by('trimister')
    info_list = CSE_day_batch_info.objects.all().order_by('batch_no')
    return render(request, 'cse/cse_day_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_get_batch_info(request, value1, value2):
    batch_info = CSE_day_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'cse/cse_day_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_edit_batch_info(request):
    return render(request, 'cse/cse_day_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_update_batch_info(request, value):
    batch_info = CSE_day_batch_info.objects.get(id=value)
    form = cse_day_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cse_day_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cse_day_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_delete_batch_info(request, value):
    if request.method == 'POST':
        if CSE_day_batch_info.objects.filter(id=value).exists():
            CSE_day_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/cse_day_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/cse_day_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = CSE_day_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/cse_day_trimister.html')
    
    batch_list = CSE_day_batch_info.objects.all().order_by('batch_no')
    trimister_info = CSE_day_trimister.objects.all().order_by('trimister')
    return render(request, 'cse/cse_day_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CSE' or user.is_superuser, login_url='error.html')
def cse_day_delete_trimister(request, value):
    if request.method == 'POST':
        if CSE_day_trimister.objects.filter(trimister=value).exists():
            CSE_day_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/cse_day_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/cse_day_trimister.html')

#...EEE Evening........

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_admin(request):
     return render(request, 'eee/eee_admin.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = EEE_eve_trimister.objects.get(trimister=request.POST.get('trimister'))

            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()

            if EEE_eve_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Similler Course Info Already Exist In The Course List')
                return redirect('/eee_eve_offered_courses.html')
            else:
                course_list = EEE_eve_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/eee_eve_offered_courses.html')

    trimister_list = EEE_eve_trimister.objects.all().order_by('trimister')
    course_list = EEE_eve_course_list.objects.all().order_by('trimister')
    return render(request, 'eee/eee_eve_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 11):
                if EEE_eve_course_list.objects.all().filter(trimister=search).exists():
                    course_list = EEE_eve_course_list.objects.filter(trimister=search)
                    return render(request, 'eee/eee_eve_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/eee_eve_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/eee_eve_offered_courses.html')
        except:
            search = search.upper()
            if EEE_eve_course_list.objects.all().filter(course_code=search).exists():
                course_list = EEE_eve_course_list.objects.filter(course_code=search)
                return render(request, 'eee/eee_eve_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/eee_eve_offered_courses.html') 
 
@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')    
def eee_eve_course_delete(request, value):
    if request.method == 'POST':
        if EEE_eve_course_list.objects.filter(id=value).exists():
            EEE_eve_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/eee_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/eee_eve_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_get_offered_courses(request, value):
    offered_courses = EEE_eve_course_list.objects.filter(id=value)
    return render(request, 'eee/eee_eve_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_edit_offered_courses(request):
    return render(request, 'eee/eee_eve_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_update_offered_courses(request, value):
    offered_courses = EEE_eve_course_list.objects.get(id=value)
    form = eee_eve_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/eee_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/eee_eve_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = EEE_eve_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = EEE_eve_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/eee_eve_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/eee_eve_batch_info.html')

    trimister_list = EEE_eve_trimister.objects.all().order_by('trimister')
    info_list = EEE_eve_batch_info.objects.all().order_by('batch_no')
    return render(request, 'eee/eee_eve_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_get_batch_info(request, value1, value2):
    batch_info = EEE_eve_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'eee/eee_eve_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_edit_batch_info(request):
    return render(request, 'eee/eee_eve_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_update_batch_info(request, value):
    batch_info = EEE_eve_batch_info.objects.get(id=value)
    form = eee_eve_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/eee_eve_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/eee_eve_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_delete_batch_info(request, value):
    if request.method == 'POST':
        if EEE_eve_batch_info.objects.filter(id=value).exists():
            EEE_eve_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/eee_eve_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/eee_eve_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = EEE_eve_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/eee_eve_trimister.html')
    
    batch_list = EEE_eve_batch_info.objects.all().order_by('batch_no')
    trimister_info = EEE_eve_trimister.objects.all().order_by('trimister')
    return render(request, 'eee/eee_eve_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_eve_delete_trimister(request, value):
    if request.method == 'POST':
        if EEE_eve_trimister.objects.filter(trimister=value).exists():
            EEE_eve_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/eee_eve_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/eee_eve_trimister.html')

#...EEE Day....

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = EEE_day_trimister.objects.get(trimister=request.POST.get('trimister'))

            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()

            if EEE_day_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Similler Course Info Already Exist In The Course List')
                return redirect('/eee_day_offered_courses.html')
            else:
                course_list = EEE_day_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/eee_day_offered_courses.html')

    trimister_list = EEE_day_trimister.objects.all().order_by('trimister')
    course_list = EEE_day_course_list.objects.all().order_by('trimister')
    return render(request, 'eee/eee_day_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 13):
                if EEE_day_course_list.objects.all().filter(trimister=search).exists():
                    course_list = EEE_day_course_list.objects.filter(trimister=search)
                    return render(request, 'eee/eee_day_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/eee_day_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/eee_day_offered_courses.html')
        except:
            search = search.upper()
            if EEE_day_course_list.objects.all().filter(course_code=search).exists():
                course_list = EEE_day_course_list.objects.filter(course_code=search)
                return render(request, 'eee/eee_day_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/eee_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')    
def eee_day_course_delete(request, value):
    if request.method == 'POST':
        if EEE_day_course_list.objects.filter(id=value).exists():
            EEE_day_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/eee_day_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/eee_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_get_offered_courses(request, value):
    offered_courses = EEE_day_course_list.objects.filter(id=value)
    return render(request, 'eee/eee_day_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_edit_offered_courses(request):
    return render(request, 'eee/eee_day_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_update_offered_courses(request, value):
    offered_courses = EEE_day_course_list.objects.get(id=value)
    form = eee_day_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/eee_day_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/eee_day_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = EEE_day_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = EEE_day_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/eee_day_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/eee_day_batch_info.html')

    trimister_list = EEE_day_trimister.objects.all().order_by('trimister')
    info_list = EEE_day_batch_info.objects.all().order_by('batch_no')
    return render(request, 'eee/eee_day_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_get_batch_info(request, value1, value2):
    batch_info = EEE_day_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'eee/eee_day_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_edit_batch_info(request):
    return render(request, 'eee/eee_day_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_update_batch_info(request, value):
    batch_info = EEE_day_batch_info.objects.get(id=value)
    form = eee_day_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/eee_day_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/eee_day_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_delete_batch_info(request, value):
    if request.method == 'POST':
        if EEE_day_batch_info.objects.filter(id=value).exists():
            EEE_day_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/eee_day_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/eee_day_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = EEE_day_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/eee_day_trimister.html')
    
    batch_list = EEE_day_batch_info.objects.all().order_by('batch_no')
    trimister_info = EEE_day_trimister.objects.all().order_by('trimister')
    return render(request, 'eee/eee_day_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='EEE' or user.is_superuser, login_url='error.html')
def eee_day_delete_trimister(request, value):
    if request.method == 'POST':
        if EEE_day_trimister.objects.filter(trimister=value).exists():
            EEE_day_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/eee_day_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/eee_day_trimister.html')

#....CEN Evening.......

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_admin(request):
     return render(request, 'cen/cen_admin.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = CEN_eve_trimister.objects.get(trimister=request.POST.get('trimister'))
            
            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()

            if CEN_eve_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Similler Course Info Already Exist In The Course List')
                return redirect('/cen_eve_offered_courses.html')
            else:
                course_list = CEN_eve_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/cen_eve_offered_courses.html')

    trimister_list = CEN_eve_trimister.objects.all().order_by('trimister')
    course_list = CEN_eve_course_list.objects.all().order_by('trimister')
    return render(request, 'cen/cen_eve_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 11):
                if CEN_eve_course_list.objects.all().filter(trimister=search).exists():
                    course_list = CEN_eve_course_list.objects.filter(trimister=search)
                    return render(request, 'cen/cen_eve_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/cen_eve_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/cen_eve_offered_courses.html')
        except:
            search = search.upper()
            if CEN_eve_course_list.objects.all().filter(course_code=search).exists():
                course_list = CEN_eve_course_list.objects.filter(course_code=search)
                return render(request, 'cen/cen_eve_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/cen_eve_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')    
def cen_eve_course_delete(request, value):
    if request.method == 'POST':
        if CEN_eve_course_list.objects.filter(id=value).exists():
            CEN_eve_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/cen_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/cen_eve_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_get_offered_courses(request, value):
    offered_courses = CEN_eve_course_list.objects.filter(id=value)
    return render(request, 'cen/cen_eve_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_edit_offered_courses(request):
    return render(request, 'cen/cen_eve_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_update_offered_courses(request, value):
    offered_courses = CEN_eve_course_list.objects.get(id=value)
    form = cen_eve_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cen_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cen_eve_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = CEN_eve_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = CEN_eve_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/cen_eve_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/cen_eve_batch_info.html')

    trimister_list = CEN_eve_trimister.objects.all().order_by('trimister')
    info_list = CEN_eve_batch_info.objects.all().order_by('batch_no')
    return render(request, 'cen/cen_eve_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_get_batch_info(request, value1, value2):
    batch_info = CEN_eve_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'cen/cen_eve_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_edit_batch_info(request):
    return render(request, 'cen/cen_eve_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_update_batch_info(request, value):
    batch_info = CEN_eve_batch_info.objects.get(id=value)
    form = cen_eve_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cen_eve_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cen_eve_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_delete_batch_info(request, value):
    if request.method == 'POST':
        if CEN_eve_batch_info.objects.filter(id=value).exists():
            CEN_eve_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/cen_eve_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/cen_eve_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = CEN_eve_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/cen_eve_trimister.html')
    
    batch_list = CEN_eve_batch_info.objects.all().order_by('batch_no')
    trimister_info = CEN_eve_trimister.objects.all().order_by('trimister')
    return render(request, 'cen/cen_eve_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_eve_delete_trimister(request, value):
    if request.method == 'POST':
        if CEN_eve_trimister.objects.filter(trimister=value).exists():
            CEN_eve_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/cen_eve_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/cen_eve_trimister.html')

#....CEN Day........

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = CEN_day_trimister.objects.get(trimister=request.POST.get('trimister'))

            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()

            if CEN_day_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Similler Course Info Already Exist The Course List')
                return redirect('/cen_day_offered_courses.html')
            else:
                course_list = CEN_day_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/cen_day_offered_courses.html')

    trimister_list = CEN_day_trimister.objects.all().order_by('trimister')
    course_list = CEN_day_course_list.objects.all().order_by('trimister')
    return render(request, 'cen/cen_day_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 13):
                if CEN_day_course_list.objects.all().filter(trimister=search).exists():
                    course_list = CEN_day_course_list.objects.filter(trimister=search)
                    return render(request, 'cen/cen_day_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/cen_day_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/cen_day_offered_courses.html')
        except:
            search = search.upper()
            if CEN_day_course_list.objects.all().filter(course_code=search).exists():
                course_list = CEN_day_course_list.objects.filter(course_code=search)
                return render(request, 'cen/cen_day_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/cen_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')    
def cen_day_course_delete(request, value):
    if request.method == 'POST':
        if CEN_day_course_list.objects.filter(id=value).exists():
            CEN_day_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/cen_day_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/cen_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_get_offered_courses(request, value):
    offered_courses = CEN_day_course_list.objects.filter(id=value)
    return render(request, 'cen/cen_day_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_edit_offered_courses(request):
    return render(request, 'cen/cen_day_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_update_offered_courses(request, value):
    offered_courses = CEN_day_course_list.objects.get(id=value)
    form = cen_day_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cen_day_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cen_day_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = CEN_day_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = CEN_day_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/cen_day_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/cen_day_batch_info.html')

    trimister_list = CEN_day_trimister.objects.all().order_by('trimister')
    info_list = CEN_day_batch_info.objects.all().order_by('batch_no')
    return render(request, 'cen/cen_day_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_get_batch_info(request, value1, value2):
    batch_info = CEN_day_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'cen/cen_day_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_edit_batch_info(request):
    return render(request, 'cen/cen_day_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_update_batch_info(request, value):
    batch_info = CEN_day_batch_info.objects.get(id=value)
    form = cen_day_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/cen_day_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/cen_day_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_delete_batch_info(request, value):
    if request.method == 'POST':
        if CEN_day_batch_info.objects.filter(id=value).exists():
            CEN_day_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/cen_day_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/cen_day_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = CEN_day_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/cen_day_trimister.html')
    
    batch_list = CEN_day_batch_info.objects.all().order_by('batch_no')
    trimister_info = CEN_day_trimister.objects.all().order_by('trimister')
    return render(request, 'cen/cen_day_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='CEN' or user.is_superuser, login_url='error.html')
def cen_day_delete_trimister(request, value):
    if request.method == 'POST':
        if CEN_day_trimister.objects.filter(trimister=value).exists():
            CEN_day_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/cen_day_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/cen_day_trimister.html')

# .........BTE...........

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_admin(request):
     return render(request, 'bte/bte_admin.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = BTE_eve_trimister.objects.filter(trimister=request.POST.get('trimister')).first()

            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()

            if BTE_eve_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Smiller Course Info Already Exist In The Course List')
                return redirect('/bte_eve_offered_courses.html')
            else:
                course_list = BTE_eve_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/bte_eve_offered_courses.html')

    trimister_list = BTE_eve_trimister.objects.all().order_by('trimister')
    course_list = BTE_eve_course_list.objects.all().order_by('trimister')
    return render(request, 'bte/bte_eve_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 11):
                if BTE_eve_course_list.objects.all().filter(trimister=search).exists():
                    course_list = BTE_eve_course_list.objects.filter(trimister=search)
                    return render(request, 'bte/bte_eve_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/bte_eve_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/bte_eve_offered_courses.html')
        except:
            search = search.upper()
            if BTE_eve_course_list.objects.all().filter(course_code=search).exists():
                course_list = BTE_eve_course_list.objects.filter(course_code=search)
                return render(request, 'bte/bte_eve_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/bte_eve_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')    
def bte_eve_course_delete(request, value):
    if request.method == 'POST':
        if BTE_eve_course_list.objects.filter(id=value).exists():
            BTE_eve_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/bte_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/bte_eve_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_get_offered_courses(request, value):
    offered_courses = BTE_eve_course_list.objects.filter(id=value)
    return render(request, 'bte/bte_eve_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_edit_offered_courses(request):
    return render(request, 'bte/bte_eve_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_update_offered_courses(request, value):
    offered_courses = BTE_eve_course_list.objects.get(id=value)
    form = bte_eve_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/bte_eve_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/bte_eve_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = BTE_eve_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = BTE_eve_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/bte_eve_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/bte_eve_batch_info.html')

    trimister_list = BTE_eve_trimister.objects.all().order_by('trimister')
    info_list = BTE_eve_batch_info.objects.all().order_by('batch_no')
    return render(request, 'bte/bte_eve_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_get_batch_info(request, value1, value2):
    batch_info = BTE_eve_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'bte/bte_eve_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_edit_batch_info(request):
    return render(request, 'bte/bte_eve_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_update_batch_info(request, value):
    batch_info = BTE_eve_batch_info.objects.get(id=value)
    form = bte_eve_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/bte_eve_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/bte_eve_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_delete_batch_info(request, value):
    if request.method == 'POST':
        if BTE_eve_batch_info.objects.filter(id=value).exists():
            BTE_eve_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/bte_eve_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/bte_eve_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = BTE_eve_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/bte_eve_trimister.html')
    
    batch_list = BTE_eve_batch_info.objects.all().order_by('batch_no')
    trimister_info = BTE_eve_trimister.objects.all().order_by('trimister')
    return render(request, 'bte/bte_eve_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_eve_delete_trimister(request, value):
    if request.method == 'POST':
        if BTE_eve_trimister.objects.filter(trimister=value).exists():
            BTE_eve_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/bte_eve_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/bte_eve_trimister.html')

#...BTE Day......

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_offered_courses(request):
    if request.method == 'POST':
            course_code = request.POST.get('course_code')
            course_name = request.POST.get('course_name')
            trimister = BTE_day_trimister.objects.filter(trimister=request.POST.get('trimister')).first()
            course_code = course_code.upper().strip()
            course_name = course_name.title().strip()
            if BTE_day_course_list.objects.filter(Q(course_code=course_code) & Q(course_name=course_name) & Q(trimister=trimister)).exists():
                messages.warning(request, 'Similler Course Info Already Exist In The Course List')
                return redirect('/bte_day_offered_courses.html')
            else:
                course_list = BTE_day_course_list(course_code=course_code, course_name=course_name, trimister=trimister)
                course_list.save()
                messages.success(request, 'New Course Added Into The Couse List Successfully......')
                return redirect('/bte_day_offered_courses.html')

    trimister_list = BTE_day_trimister.objects.all().order_by('trimister')
    course_list = BTE_day_course_list.objects.all().order_by('trimister')
    return render(request, 'bte/bte_day_offered_courses.html', {'course_list': course_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_course_search(request):  
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            if int(search) in range(1, 13):
                if BTE_day_course_list.objects.all().filter(trimister=search).exists():
                    course_list = BTE_day_course_list.objects.filter(trimister=search)
                    return render(request, 'bte/bte_day_course_search.html', {'course_list': course_list})
                else:
                    messages.warning(request, 'No Record Exist In The Course List....!')
                    return redirect('/bte_day_offered_courses.html') 
            else:
                messages.warning(request, 'No Record Exist In The Course List....!')
                return redirect('/bte_day_offered_courses.html')
        except:
            search = search.upper()
            if BTE_day_course_list.objects.all().filter(course_code=search).exists():
                course_list = BTE_day_course_list.objects.filter(course_code=search)
                return render(request, 'bte/bte_day_course_search.html', {'course_list': course_list})
            else:
                messages.warning(request, 'Course Does Not Exist In The Course List....!')
                return redirect('/bte_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')    
def bte_day_course_delete(request, value):
    if request.method == 'POST':
        if BTE_day_course_list.objects.filter(id=value).exists():
            BTE_day_course_list.objects.filter(id=value).delete()
            messages.success(request, 'Course Record Successfully Deleted...')
            return redirect('/bte_day_offered_courses.html') 
    else:
        messages.warning(request, 'Course Record Not deleted....')
        return redirect('/bte_day_offered_courses.html') 

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_get_offered_courses(request, value):
    offered_courses = BTE_day_course_list.objects.filter(id=value)
    return render(request, 'bte/bte_day_edit_offered_courses.html', {'offered_courses': offered_courses})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_edit_offered_courses(request):
    return render(request, 'bte/bte_day_edit_offered_courses.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_update_offered_courses(request, value):
    offered_courses = BTE_day_course_list.objects.get(id=value)
    form = bte_day_course_list_form(request.POST, instance=offered_courses)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/bte_day_offered_courses.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/bte_day_offered_courses.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_batch_info(request):
    try:
        if request.method == 'POST':
            batch_no = request.POST.get('batch_no')
            section = request.POST.get('section')
            st_number = request.POST.get('st_number')
            trimister = BTE_day_trimister.objects.get(trimister=request.POST.get('trimister'))

            batch_info = BTE_day_batch_info(batch_no= batch_no, section=section, st_number=st_number, trimister=trimister)
            batch_info.save()
            messages.success(request, 'New Information Added Successfully......')
            return redirect('/bte_day_batch_info.html')
    except:
        messages.warning(request, 'Somthing Wrong Information Not Added......')
        return redirect('/bte_day_batch_info.html')

    trimister_list = BTE_day_trimister.objects.all().order_by('trimister')
    info_list = BTE_day_batch_info.objects.all().order_by('batch_no')
    return render(request, 'bte/bte_day_batch_info.html', {'info_list':info_list, 'trimister_list':trimister_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_get_batch_info(request, value1, value2):
    batch_info = BTE_day_batch_info.objects.filter(Q(batch_no=value1) & Q(section=value2))
    return render(request, 'bte/bte_day_edit_batch_info.html', {'batch_info': batch_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_edit_batch_info(request):
    return render(request, 'bte/bte_day_edit_bstch_info.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_update_batch_info(request, value):
    batch_info = BTE_day_batch_info.objects.get(id=value)
    form = bte_day_batch_info_form(request.POST, instance=batch_info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/bte_day_batch_info.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/bte_day_batch_info.html')    

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_delete_batch_info(request, value):
    if request.method == 'POST':
        if BTE_day_batch_info.objects.filter(id=value).exists():
            BTE_day_batch_info.objects.filter(id=value).delete()
            messages.success(request, 'Batch Information Successfully Deleted......')
            return redirect('/bte_day_batch_info.html') 
    else:
        messages.warning(request, 'Batch Information Not deleted.....')
        return redirect('/bte_day_batch_info.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_trimister(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        trimister = request.POST.get('trimister')

        trimister_info = BTE_day_trimister(dept=dept, trimister=trimister)
        trimister_info.save()
        messages.success(request, 'New Record Added Successfully...........')
        return redirect('/bte_day_trimister.html')
    
    batch_list = BTE_day_batch_info.objects.all().order_by('batch_no')
    trimister_info = BTE_day_trimister.objects.all().order_by('trimister')
    return render(request, 'bte/bte_day_trimister.html', {'trimister_info':trimister_info, 'batch_list':batch_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.username =='BTE' or user.is_superuser, login_url='error.html')
def bte_day_delete_trimister(request, value):
    if request.method == 'POST':
        if BTE_day_trimister.objects.filter(trimister=value).exists():
            BTE_day_trimister.objects.filter(trimister=value).delete()
            messages.success(request, 'Trimister Information Successfully Deleted......')
            return redirect('/bte_day_trimister.html')
    else:
        messages.warning(request, 'Trimister Information Not deleted.....')
        return redirect('/bte_day_trimister.html')

#....Routine Evening........
@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_routine(request):
    if request.method == 'POST':
        exam_date = request.POST.get('exam_date')
        exam_time = request.POST.get('exam_time')
        course_code = request.POST.get('course_code')
        course_name = request.POST.get('course_name')
        dept = request.POST.get('dept')
        batch = request.POST.get('batch')
        section = request.POST.get('section')
        st_number = request.POST.get('st_number')
        room = request.POST.get('room')

        exam_date = datetime.strptime(exam_date, '%Y-%m-%d').date()
        weekday = exam_date.strftime('%A')
        course_code = course_code.upper()
        course_name = course_name.upper()
        dept = dept.upper()
        section = section.upper()

        schedule = EVE_routine(course_code= course_code, course_name=course_name, dept=dept, batch=batch,
                     section=section, st_number=st_number, room=room, exam_date=exam_date, exam_time=exam_time, weekday=weekday)
        schedule.save()

    routine_list = EVE_routine.objects.all().order_by('exam_date', 'dept', 'batch', 'section')
    date_list = EVE_routine.objects.all().distinct('exam_date').values('exam_date', 'exam_time', 'weekday')
    return render(request, 'eve_routine/eve_routine.html', {'routine_list': routine_list, 'date_list':date_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_generate_routine(request):
    if request.method == 'POST':
        exam_date = request.POST.get('date')
        exam_time = request.POST.get('time')

        exam_date = datetime.strptime(exam_date, '%Y-%m-%d').date()

    if EVE_routine.objects.all().exists():
        messages.info(request, "A Routine Already Exist....")
        return redirect('/eve_routine.html')
    else:
        departments = ['CSE', 'EEE', 'BTE', 'CEN']
        for dept in departments:
            
            if dept == 'CSE':
                even_batch = CSE_eve_trimister.objects.values(
                    'dept', 'cse_eve_batch_info__batch_no', 'cse_eve_batch_info__section', 'cse_eve_batch_info__st_number', 
                    'cse_eve_course_list__course_code','cse_eve_course_list__course_name'
                )
            
                for y in even_batch.iterator():
                    if y['cse_eve_batch_info__batch_no'] == None or y['cse_eve_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['cse_eve_batch_info__batch_no']
                        section = y['cse_eve_batch_info__section']
                        total_student = y['cse_eve_batch_info__st_number']
                        course_code = y['cse_eve_course_list__course_code']
                        course_name = y['cse_eve_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_eve(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)

            elif dept == 'EEE':
                even_batch = EEE_eve_trimister.objects.values(
                    'dept', 'eee_eve_batch_info__batch_no', 'eee_eve_batch_info__section', 'eee_eve_batch_info__st_number', 
                    'eee_eve_course_list__course_code','eee_eve_course_list__course_name'
                )
            
                for y in even_batch.iterator():
                    if y['eee_eve_batch_info__batch_no'] == None or y['eee_eve_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['eee_eve_batch_info__batch_no']
                        section = y['eee_eve_batch_info__section']
                        total_student = y['eee_eve_batch_info__st_number']
                        course_code = y['eee_eve_course_list__course_code']
                        course_name = y['eee_eve_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_eve(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)
           
            elif dept == 'CEN':
                even_batch = CEN_eve_trimister.objects.values(
                    'dept', 'cen_eve_batch_info__batch_no', 'cen_eve_batch_info__section', 'cen_eve_batch_info__st_number', 
                    'cen_eve_course_list__course_code','cen_eve_course_list__course_name'
                )
            
                for y in even_batch.iterator():
                    if y['cen_eve_batch_info__batch_no'] == None or y['cen_eve_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['cen_eve_batch_info__batch_no']
                        section = y['cen_eve_batch_info__section']
                        total_student = y['cen_eve_batch_info__st_number']
                        course_code = y['cen_eve_course_list__course_code']
                        course_name = y['cen_eve_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_eve(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)

            elif dept == 'BTE':
                even_batch = BTE_eve_trimister.objects.values(
                    'dept', 'bte_eve_batch_info__batch_no', 'bte_eve_batch_info__section', 'bte_eve_batch_info__st_number', 
                    'bte_eve_course_list__course_code','bte_eve_course_list__course_name'
                    )
                        
                for y in even_batch.iterator():
                    if y['bte_eve_batch_info__batch_no'] == None or y['bte_eve_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['bte_eve_batch_info__batch_no']
                        section = y['bte_eve_batch_info__section']
                        total_student = y['bte_eve_batch_info__st_number']
                        course_code = y['bte_eve_course_list__course_code']
                        course_name = y['bte_eve_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_eve(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)

        return redirect('/eve_routine.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_delete_routine(request):
    routine = EVE_routine.objects.all()
    routine.delete()
    routine_list = EVE_routine.objects.all().order_by('exam_date')
    return redirect('/eve_routine.html', {'routine_list': routine_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_search_schedule(request, value):
    try:
        if request.method == 'POST' and value == 1:
            dept = request.POST.get('dept')
            dept = dept.upper()
            batch = int(request.POST.get('batch'))
            
            if EVE_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).exists():
                routine_list = EVE_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).order_by('exam_date', 'section')
                return render(request, 'eve_routine/eve_search_schedule.html', {'routine_list': routine_list})
            else:
                messages.warning(request, 'No Record Found.....')
                return redirect('/eve_routine.html')

        elif request.method == 'POST' and value == 2:
            date = request.POST.get('date')
            room = int(request.POST.get('room'))

            if EVE_routine.objects.all().filter(Q(exam_date=date) & Q(room=room)).exists():
                routine_list = EVE_routine.objects.all().filter(Q(exam_date=date) & Q(room=room))
                return render(request, 'eve_routine/eve_search_schedule.html', {'routine_list': routine_list})
            else:
                messages.warning(request, 'No Record Found.....')
                return redirect('/eve_routine.html')

    except:
        messages.warning(request, 'No Record Found.....')
        return redirect('/eve_routine.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_edit_schedule(request):
    return render(request, 'eve_routine/eve_edit_schedule.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_get_schedule_info(request, value):
    schedule_info = EVE_routine.objects.filter(id=value)
    return render(request, 'eve_routine/eve_edit_schedule.html', {'schedule_info': schedule_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_update_schedule_info(request, value):
    info = EVE_routine.objects.get(id=value)
    form = eve_routine_form(request.POST, instance=info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/eve_routine.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/eve_routine.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_delete_schedule_info(request, value):
    if request.method == 'POST':
        if EVE_routine.objects.filter(id=value).exists():
            EVE_routine.objects.filter(id=value).delete()
            messages.success(request, 'Information Successfully Deleted......')
            return redirect('/eve_routine.html')
    else:
        messages.warning(request, 'Information Not deleted.....')
        return redirect('/eve_routine.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_publish_schedule(request):
    if request.method == 'POST':
        batch = request.POST.get('batch')
        trimister = request.POST.get('trimister')
        term = request.POST.get('term')
        date = request.POST.get('date')

        if publish.objects.filter(batch='Evening').exists():
            messages.warning(request, "Schedule Already Published....")
            return redirect('/eve_publish_schedule.html')
        else:
            info = publish(batch=batch, trimister=trimister, term=term, pub_date=date)
            info.save()

            messages.success(request, "Exam Schedule Published Successfully.....")
            return redirect('/eve_publish_schedule.html')

    return render(request, 'eve_routine/eve_publish_schedule.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def eve_cancel_publish_schedule(request):
    if request.method == 'POST':
        if publish.objects.filter(batch='Evening').exists():
            publish.objects.filter(batch='Evening').delete()
            messages.success(request, 'Published Schedule Canceled Successfully......')
            return redirect('/eve_publish_schedule.html')
        else:
            messages.warning(request, 'No Published Info Exist....')
            return redirect('/eve_publish_schedule.html')
    else:
        return render(request, 'eve_publish_schedule.html')

#....Routine Day......

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_routine(request):
    if request.method == 'POST':
        exam_date = request.POST.get('exam_date')
        exam_time = request.POST.get('exam_time')
        course_code = request.POST.get('course_code')
        course_name = request.POST.get('course_name')
        dept = request.POST.get('dept')
        batch = request.POST.get('batch')
        section = request.POST.get('section')
        st_number = request.POST.get('st_number')
        room = request.POST.get('room')

        exam_date = datetime.strptime(exam_date, '%Y-%m-%d').date()
        weekday = exam_date.strftime('%A')
        course_code = course_code.upper()
        course_name = course_name.upper()
        dept = dept.upper()
        section = section.upper()

        schedule = DAY_routine(course_code= course_code, course_name=course_name, dept=dept, batch=batch,
                     section=section, st_number=st_number, room=room, exam_date=exam_date, exam_time=exam_time, weekday=weekday)
        schedule.save()

    routine_list = DAY_routine.objects.all().order_by('exam_date', 'dept', 'batch', 'section')
    date_list = DAY_routine.objects.all().distinct('exam_date').values('exam_date', 'exam_time', 'weekday')
    return render(request, 'day_routine/day_routine.html', {'routine_list': routine_list, 'date_list':date_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_generate_routine(request):
    if request.method == 'POST':
        exam_date = request.POST.get('date')
        exam_time = request.POST.get('time')

        exam_date = datetime.strptime(exam_date, '%Y-%m-%d').date()

    if DAY_routine.objects.all().exists():
        messages.info(request, "A Routine Already Exist....")
        return redirect('/day_routine.html')
    else:
        departments = ['CSE', 'EEE', 'BTE', 'CEN']
        for dept in departments:
            
            if dept == 'CSE':
                even_batch = CSE_day_trimister.objects.values(
                    'dept', 'cse_day_batch_info__batch_no', 'cse_day_batch_info__section', 'cse_day_batch_info__st_number', 
                    'cse_day_course_list__course_code','cse_day_course_list__course_name'
                )
            
                for y in even_batch.iterator():
                    if y['cse_day_batch_info__batch_no'] == None or y['cse_day_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['cse_day_batch_info__batch_no']
                        section = y['cse_day_batch_info__section']
                        total_student = y['cse_day_batch_info__st_number']
                        course_code = y['cse_day_course_list__course_code']
                        course_name = y['cse_day_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_day(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)

            elif dept == 'EEE':
                even_batch = EEE_day_trimister.objects.values(
                    'dept', 'eee_day_batch_info__batch_no', 'eee_day_batch_info__section', 'eee_day_batch_info__st_number', 
                    'eee_day_course_list__course_code','eee_day_course_list__course_name'
                )
            
                for y in even_batch.iterator():
                    if y['eee_day_batch_info__batch_no'] == None or y['eee_day_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['eee_day_batch_info__batch_no']
                        section = y['eee_day_batch_info__section']
                        total_student = y['eee_day_batch_info__st_number']
                        course_code = y['eee_day_course_list__course_code']
                        course_name = y['eee_day_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_day(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)
           
            elif dept == 'CEN':
                even_batch = CEN_day_trimister.objects.values(
                    'dept', 'cen_day_batch_info__batch_no', 'cen_day_batch_info__section', 'cen_day_batch_info__st_number', 
                    'cen_day_course_list__course_code','cen_day_course_list__course_name'
                )
            
                for y in even_batch.iterator():
                    if y['cen_day_batch_info__batch_no'] == None or y['cen_day_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['cen_day_batch_info__batch_no']
                        section = y['cen_day_batch_info__section']
                        total_student = y['cen_day_batch_info__st_number']
                        course_code = y['cen_day_course_list__course_code']
                        course_name = y['cen_day_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_day(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)

            elif dept == 'BTE':
                even_batch = BTE_day_trimister.objects.values(
                    'dept', 'bte_day_batch_info__batch_no', 'bte_day_batch_info__section', 'bte_day_batch_info__st_number', 
                    'bte_day_course_list__course_code','bte_day_course_list__course_name'
                )
                        
                for y in even_batch.iterator():
                    if y['bte_day_batch_info__batch_no'] == None or y['bte_day_course_list__course_code'] == None: 
                        pass
                    else:
                        dept = y['dept']
                        batch = y['bte_day_batch_info__batch_no']
                        section = y['bte_day_batch_info__section']
                        total_student = y['bte_day_batch_info__st_number']
                        course_code = y['bte_day_course_list__course_code']
                        course_name = y['bte_day_course_list__course_name']
                        exam_date = exam_date
                        exam_time = exam_time

                        make_schedule_day(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time)

        return redirect('/day_routine.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_delete_routine(request):
    routine = DAY_routine.objects.all()
    routine.delete()
    routine_list = DAY_routine.objects.all().order_by('exam_date')
    return redirect('/day_routine.html', {'routine_list': routine_list})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_search_schedule(request, value):
    try:
        if request.method == 'POST' and value == 1:
            dept = request.POST.get('dept')
            dept = dept.upper()
            batch = int(request.POST.get('batch'))
            
            if DAY_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).exists():
                routine_list = DAY_routine.objects.all().filter(Q(dept=dept) & Q(batch=batch)).order_by('exam_date', 'section')
                return render(request, 'day_routine/day_search_schedule.html', {'routine_list': routine_list})
            else:
                messages.warning(request, 'No Record Found.....')
                return redirect('/day_routine.html')

        elif request.method == 'POST' and value == 2:
            date = request.POST.get('date')
            room = int(request.POST.get('room'))

            if DAY_routine.objects.all().filter(Q(exam_date=date) & Q(room=room)).exists():
                routine_list = DAY_routine.objects.all().filter(Q(exam_date=date) & Q(room=room))
                return render(request, 'day_routine/day_search_schedule.html', {'routine_list': routine_list})
            else:
                messages.warning(request, 'No Record Found.....')
                return redirect('/day_routine.html')

    except:
        messages.warning(request, 'No Record Found.....')
        return redirect('/day_routine.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_edit_schedule(request):
    return render(request, 'day_routine/day_edit_schedule.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_get_schedule_info(request, value):
    schedule_info = DAY_routine.objects.filter(id=value)
    return render(request, 'day_routine/day_edit_schedule.html', {'schedule_info': schedule_info})

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_update_schedule_info(request, value):
    info = DAY_routine.objects.get(id=value)
    form = day_routine_form(request.POST, instance=info)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully.....')
        return redirect('/day_routine.html') 
    else:
        messages.warning(request, 'Record Didnot Updated Successfully.....')
        return redirect('/day_routine.html')  

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_delete_schedule_info(request, value):
    if request.method == 'POST':
        if DAY_routine.objects.filter(id=value).exists():
            DAY_routine.objects.filter(id=value).delete()
            messages.success(request, 'Information Successfully Deleted......')
            return redirect('/day_routine.html')
    else:
        messages.warning(request, 'Information Not deleted.....')
        return redirect('/day_routine.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_publish_schedule(request):
    if request.method == 'POST':
        batch = request.POST.get('batch')
        trimister = request.POST.get('trimister')
        term = request.POST.get('term')
        date = request.POST.get('date')

        if publish.objects.filter(batch='Day').exists():
            messages.warning(request, "Schedule Already Published....")
            return redirect('/day_publish_schedule.html')
        else:
            info = publish(batch=batch, trimister=trimister, term=term, pub_date=date)
            info.save()

            messages.success(request, "Exam Schedule Published Successfully.....")
            return redirect('/day_publish_schedule.html')

    return render(request, 'day_routine/day_publish_schedule.html')

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def day_cancel_publish_schedule(request):
    if request.method == 'POST':
        if publish.objects.filter(batch='Day').exists():
            publish.objects.filter(batch='Day').delete()
            messages.success(request, 'Published Schedule Canceled Successfully......')
            return redirect('/day_publish_schedule.html')
        else:
            messages.warning(request, 'No Published Info Exist.....')
            return redirect('/day_publish_schedule.html')
    else:
        return render(request, 'day_routine/day_publish_schedule.html')
    
# ......Extra function for schedule maker....
@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def make_schedule_eve(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time):
    if batch % 2 == 0:             
        if EVE_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).exists():
            count_data = EVE_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).distinct('course_code').count()
                                
            if count_data == 1:
                date = exam_date + timedelta(days=2)
            elif count_data == 2:
                date = exam_date + timedelta(days=4)
            elif count_data == 3:
                date = exam_date + timedelta(days=6)
            elif count_data == 4:
                date = exam_date + timedelta(days=8)
        else:
            date = exam_date

        weekday = date.strftime('%A')

        make_schedule_eve_child(dept, batch, section, total_student, course_code, course_name, date, exam_time, weekday)                    


    if batch % 2 != 0:               
        if EVE_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).exists():
            count_data = EVE_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).distinct('course_code').count()
                            
            if count_data == 1:
                date = exam_date + timedelta(days=3)
            elif count_data == 2:
                date = exam_date + timedelta(days=5)
            elif count_data == 3:
                date = exam_date + timedelta(days=7)
            elif count_data == 4:
                date = exam_date + timedelta(days=9)
        else:
            date = exam_date + timedelta(days=1)

        weekday = date.strftime('%A')
        
        make_schedule_eve_child(dept, batch, section, total_student, course_code, course_name, date, exam_time, weekday)

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def make_schedule_eve_child(dept, batch, section, total_student, course_code, course_name, date, exam_time, weekday):
    st_dist = room_distribution(total_student)
    for i in range(len(st_dist)):
        while 1:
            room = random.choice(list(Rooms.objects.all().values('room_no')))
            if EVE_routine.objects.filter(Q(room=room['room_no']) & Q(exam_date=date) & Q(dept=dept)).exists():
                pass
            elif EVE_routine.objects.filter(Q(room=room['room_no']) & Q(exam_date=date) & ~Q(dept=dept)).exists():
                total_st = EVE_routine.objects.filter(Q(room=room['room_no']) & Q(exam_date=date) & ~Q(dept=dept)).values('st_number')
                st = 0
                for j in total_st.iterator():
                    st = st + j['st_number']
                sit_capasity = Rooms.objects.get(room_no=room['room_no'])
                aveliable = sit_capasity.room_capacity - st

                if aveliable >= st_dist[i]:
                    course_code = course_code
                    course_name = course_name
                    dept = dept
                    batch = batch
                    section = section
                    total_st = total_student
                    st_number = st_dist[i]
                    room = room['room_no']
                    date = date
                    time = exam_time
                    weekday = weekday

                    even_routine = EVE_routine(course_code= course_code, course_name=course_name, dept=dept, batch=batch,
                     section=section, total_st=total_st, st_number=st_number, room=room, exam_date=date, exam_time=time, weekday=weekday)
                    even_routine.save()
                    break
                else:
                    pass
            else:
                course_code = course_code
                course_name = course_name
                dept = dept
                batch = batch
                section = section
                total_st = total_student
                st_number = st_dist[i]
                room = room['room_no']
                date = date
                time = exam_time
                weekday = weekday

                even_routine = EVE_routine(course_code= course_code, course_name=course_name, dept=dept, batch=batch, 
                 section=section, total_st=total_st, st_number=st_number, room=room, exam_date=date, exam_time=time, weekday=weekday)
                even_routine.save()
                break

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def make_schedule_day(dept, batch, section, total_student, course_code, course_name, exam_date, exam_time):
    if batch % 2 == 0:             
        if DAY_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).exists():
            count_data = DAY_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).distinct('course_code').count()
                                
            if count_data == 1:
                date = exam_date + timedelta(days=2)
            elif count_data == 2:
                date = exam_date + timedelta(days=4)
            elif count_data == 3:
                date = exam_date + timedelta(days=6)
            elif count_data == 4:
                date = exam_date + timedelta(days=8)
        else:
            date = exam_date

        weekday = date.strftime('%A')

        make_schedule_day_child(dept, batch, section, total_student, course_code, course_name, date, exam_time, weekday)                    

    if batch % 2 != 0:               
        if DAY_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).exists():
            count_data = DAY_routine.objects.filter(Q(batch = batch) & Q(dept=dept) & Q(section=section)).distinct('course_code').count()
                            
            if count_data == 1:
                date = exam_date + timedelta(days=3)
            elif count_data == 2:
                date = exam_date + timedelta(days=5)
            elif count_data == 3:
                date = exam_date + timedelta(days=7)
            elif count_data == 4:
                date = exam_date + timedelta(days=9)
        else:
            date = exam_date + timedelta(days=1)

        weekday = date.strftime('%A')
        
        make_schedule_day_child(dept, batch, section, total_student, course_code, course_name, date, exam_time, weekday)

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def make_schedule_day_child(dept, batch, section, total_student, course_code, course_name, date, exam_time, weekday):
    st_dist = room_distribution(total_student)
    for i in range(len(st_dist)):
        while 1:
            room = random.choice(list(Rooms.objects.all().values('room_no')))
            if DAY_routine.objects.filter(Q(room=room['room_no']) & Q(exam_date=date) & Q(dept=dept)).exists():
                pass
            elif DAY_routine.objects.filter(Q(room=room['room_no']) & Q(exam_date=date) & ~Q(dept=dept)).exists():
                total_st = DAY_routine.objects.filter(Q(room=room['room_no']) & Q(exam_date=date) & ~Q(dept=dept)).values('st_number')
                st = 0
                for j in total_st.iterator():
                    st = st + j['st_number']
                sit_capasity = Rooms.objects.get(room_no=room['room_no'])
                aveliable = sit_capasity.room_capacity - st

                if aveliable >= st_dist[i]:
                    course_code = course_code
                    course_name = course_name
                    dept = dept
                    batch = batch
                    section = section
                    total_st = total_student
                    st_number = st_dist[i]
                    room = room['room_no']
                    date = date
                    time = exam_time
                    weekday = weekday

                    even_routine = DAY_routine(course_code= course_code, course_name=course_name, dept=dept, batch=batch,
                     section=section, total_st=total_st, st_number=st_number, room=room, exam_date=date, exam_time=time, weekday=weekday)
                    even_routine.save()
                    break
                else:
                    pass
            else:
                course_code = course_code
                course_name = course_name
                dept = dept
                batch = batch
                section = section
                total_st = total_student
                st_number = st_dist[i]
                room = room['room_no']
                date = date
                time = exam_time
                weekday = weekday

                even_routine = DAY_routine(course_code= course_code, course_name=course_name, dept=dept, batch=batch, 
                 section=section, total_st=total_st, st_number=st_number, room=room, exam_date=date, exam_time=time, weekday=weekday)
                even_routine.save()
                break

@login_required(login_url='/login.html')
@user_passes_test(lambda user: user.is_superuser, login_url='error.html')
def room_distribution(st_no):
    st_dist = []
    if st_no <= 30:
        room1 = st_no
        st_dist.append(room1)
    elif (st_no > 30) and (st_no <= 40):
        room1 = 20
        st_dist.append(room1)
        room2 = st_no - 20
        st_dist.append(room2)
    elif (st_no > 40) and (st_no <= 50):
        room1 = 25
        st_dist.append(room1)
        room2 = st_no - 25
        st_dist.append(room2)
    elif (st_no > 50) and (st_no <= 60):
        room1 = 25
        st_dist.append(room1)
        room2 = 20
        st_dist.append(room2)
        room3 = st_no - (room1 + room2)
        st_dist.append(room3)
    elif (st_no > 60) and (st_no <= 75):
        room1 = 25
        st_dist.append(room1)
        room2 = 25
        st_dist.append(room2)
        room3 = st_no - (room1 + room2)
        st_dist.append(room3)
    elif (st_no > 75) and (st_no <= 80):
        room1 = 30
        st_dist.append(room1)
        room2 = 30
        st_dist.append(room2)
        room3 = st_no - (room1 + room2)
        st_dist.append(room3)
    
    return(st_dist)
