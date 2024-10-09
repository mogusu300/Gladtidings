# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Course, Topic, Enrollment, Certificate
from .forms import CustomUserCreationForm, CourseForm, TopicForm, EnrollmentForm, CertificateForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my_courses')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def list_courses(request):
    courses = Course.objects.filter(public=True)
    return render(request, 'courses.html', {'courses': courses})

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    courses = [enrollment.course for enrollment in enrollments]
    return render(request, 'my_courses.html', {'courses': courses})

@login_required
def enroll(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.user = request.user
            enrollment.save()
            return redirect('my_courses')
    else:
        form = EnrollmentForm()
    return render(request, 'enroll.html', {'form': form})

@login_required
def my_certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'certificates.html', {'certificates': certificates})

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        if request.user.check_password(old_password):
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Important!
            messages.success(request, 'Password changed successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Old password is incorrect.')
    return render(request, 'change_password.html')

@login_required
def create_course(request):
    if request.user.role != 'admin':
        messages.error(request, 'Only admins can create courses.')
        return redirect('home')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            course.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

@login_required
def list_topics(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    topics = Topic.objects.filter(course=course)

    for topic in topics:
        print(f"Topic: {topic.title}, ID: {topic.id}")

    return render(request, 'list_topics.html', {'course': course, 'topics': topics})


@login_required
def get_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'topic.html', {'topic': topic})

@login_required
def create_topic(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user.role != 'admin' or course.creator != request.user:
        messages.error(request, 'Only the course creator can add topics.')
        return redirect('list_courses')
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.course = course
            topic.save()
            return redirect('list_topics', course_id=course_id)
    else:
        form = TopicForm()
    return render(request, 'create_topic.html', {'form': form})

@login_required
def update_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user.role != 'admin' or topic.course.creator != request.user:
        messages.error(request, 'Only the course creator can update topics.')
        return redirect('list_courses')
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('get_topic', topic_id=topic_id)
    else:
        form = TopicForm(instance=topic)
    return render(request, 'update_topic.html', {'form': form})

@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user.role != 'admin' or topic.course.creator != request.user:
        messages.error(request, 'Only the course creator can delete topics.')
        return redirect('list_courses')
    if request.method == 'POST':
        topic.delete()
        return redirect('list_topics', course_id=topic.course.id)
    return render(request, 'delete_topic.html', {'topic': topic})



def index(request):
    return render(request, 'index.html')
