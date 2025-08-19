from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SchoolClassForm, TeacherForm, PeriodForm
from .models import SchoolClass, Teacher, Period

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("class_list")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("class_list")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def class_list(request):
    classes = SchoolClass.objects.all()
    return render(request, "class_list.html", {"classes": classes})

@login_required
def add_class(request):
    if request.method == "POST":
        form = SchoolClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("class_list")
    else:
        form = SchoolClassForm()
    return render(request, "add_class.html", {"form": form})

@login_required
def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("class_list")
    else:
        form = TeacherForm()
    return render(request, "add_teacher.html", {"form": form})

@login_required
def add_period(request):
    if request.method == "POST":
        form = PeriodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("class_list")
    else:
        form = PeriodForm()
    return render(request, "add_period.html", {"form": form})

@login_required
def view_timetable(request, class_id):
    school_class = get_object_or_404(SchoolClass, id=class_id)
    periods = Period.objects.filter(school_class=school_class).order_by("day", "start_time")
    return render(request, "timetable.html", {"class": school_class, "periods": periods})
