from typing import List
from ninja import NinjaAPI, Router
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .models import CustomUser, Course, Topic, Enrollment, Certificate
from .scheme import (
    UserCreateSchema, UserSchema, LoginSchema, ChangePasswordSchema,
    CourseSchema, TopicSchema, EnrollmentSchema, CertificateSchema
)

# Initialize NinjaAPI
api = NinjaAPI()

# Initialize Router
router = Router()

# Register a new user
@router.post("/register", response=UserSchema)
def register(request, data: UserCreateSchema):
    """
    Register a new user with the provided data.
    Schema: UserCreateSchema, UserSchema
    """
    user = CustomUser.objects.create_user(
        username=data.username,
        email=data.email,
        password=data.password,
        role=data.role
    )
    return user

# Login an existing user
@router.post("/login")
def login_view(request, data: LoginSchema):
    """
    Authenticate and log in a user with the provided credentials.
    Schema: LoginSchema
    """
    user = authenticate(request, username=data.username, password=data.password)
    if user is not None:
        login(request, user)
        return {"success": True}
    return {"success": False}

# List all public courses
@router.get("/courses", response=List[CourseSchema])
def list_courses(request):
    """
    Retrieve a list of all public courses.
    Schema: CourseSchema
    """
    courses = Course.objects.filter(public=True)
    return courses

# List courses enrolled by the current user
@router.get("/my-courses", response=List[CourseSchema])
def my_courses(request):
    """
    Retrieve a list of courses that the current user is enrolled in.
    Schema: CourseSchema
    """
    user = request.user
    enrollments = Enrollment.objects.filter(user=user)
    courses = [enrollment.course for enrollment in enrollments]
    return courses

# Enroll the current user in a course
@router.post("/enroll", response=EnrollmentSchema)
def enroll(request, data: EnrollmentSchema):
    """
    Enroll the current user in a specified course.
    Schema: EnrollmentSchema
    """
    user = request.user
    course = get_object_or_404(Course, id=data.course_id)
    enrollment, created = Enrollment.objects.get_or_create(user=user, course=course)
    return enrollment

# List certificates of the current user
@router.get("/certificates", response=List[CertificateSchema])
def my_certificates(request):
    """
    Retrieve a list of certificates for the current user.
    Schema: CertificateSchema
    """
    user = request.user
    certificates = Certificate.objects.filter(user=user)
    return certificates

# Change password for the current user
@router.post("/change-password")
def change_password(request, data: ChangePasswordSchema):
    """
    Change the password for the current user.
    Schema: ChangePasswordSchema
    """
    user = request.user
    if user.check_password(data.old_password):
        user.set_password(data.new_password)
        user.save()
        return {"success": True}
    return {"success": False}

# Create a new course (admin only)
@router.post("/courses", response=CourseSchema)
def create_course(request, data: CourseSchema):
    """
    Create a new course (admin only).
    Schema: CourseSchema
    """
    user = request.user
    if user.role != 'admin':
        return {"error": "Only admins can create courses"}
    course = Course.objects.create(
        title=data.title,
        description=data.description,
        public=data.public,
        creator=user
    )
    return course

# List topics of a specific course
@router.get("/courses/{course_id}/topics", response=List[TopicSchema])
def list_topics(request, course_id: int):
    """
    Retrieve a list of topics for a specified course.
    Schema: TopicSchema
    """
    topics = Topic.objects.filter(course_id=course_id)
    return topics

# Get details of a specific topic
@router.get("/topics/{topic_id}", response=TopicSchema)
def get_topic(request, topic_id: int):
    """
    Retrieve details of a specified topic.
    Schema: TopicSchema
    """
    topic = get_object_or_404(Topic, id=topic_id)
    return topic

# Create a new topic within a course (course creator only)
@router.post("/courses/{course_id}/topics", response=TopicSchema)
def create_topic(request, course_id: int, data: TopicSchema):
    """
    Create a new topic within a specified course (course creator only).
    Schema: TopicSchema
    """
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    if user.role != 'admin' or course.creator != user:
        return {"error": "Only the course creator can add topics"}
    topic = Topic.objects.create(course=course, title=data.title, content=data.content)
    return topic

# Update an existing topic (course creator only)
@router.put("/topics/{topic_id}", response=TopicSchema)
def update_topic(request, topic_id: int, data: TopicSchema):
    """
    Update a specified topic (course creator only).
    Schema: TopicSchema
    """
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user.role != 'admin' or topic.course.creator != request.user:
        return {"error": "Only the course creator can update topics"}
    topic.title = data.title
    topic.content = data.content
    topic.save()
    return topic

# Delete an existing topic (course creator only)
@router.delete("/topics/{topic_id}")
def delete_topic(request, topic_id: int):
    """
    Delete a specified topic (course creator only).
    """
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user.role != 'admin' or topic.course.creator != request.user:
        return {"error": "Only the course creator can delete topics"}
    topic.delete()
    return {"success": True}

# Add the router to the API
api.add_router("/", router)


