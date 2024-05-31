
from ninja import NinjaAPI, Router
from .models import Course, Institution
from .schemas import CourseCreateSchema, CourseSchema
from django.shortcuts import get_object_or_404

api = NinjaAPI()

router = Router()

@router.post("/courses/create", response=CourseSchema)
def create_course(request, data: CourseCreateSchema):
    institution = get_object_or_404(Institution, id=data.institution_id) if data.institution_id else None
    course = Course.objects.create(
        title=data.title,
        description=data.description,
        public=data.public,
        institution=institution
    )
    return course

@router.get("/courses", response=list[CourseSchema])
def list_courses(request):
    courses = Course.objects.all()
    return courses

@router.get("/courses/{course_id}", response=CourseSchema)
def get_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    return course

@router.put("/courses/{course_id}", response=CourseSchema)
def update_course(request, course_id: int, data: CourseCreateSchema):
    course = get_object_or_404(Course, id=course_id)
    institution = get_object_or_404(Institution, id=data.institution_id) if data.institution_id else None
    course.title = data.title
    course.description = data.description
    course.public = data.public
    course.institution = institution
    course.save()
    return course

@router.delete("/courses/{course_id}", response=dict)
def delete_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return {"success": True}

api.add_router("/", router)  # Add the router to the API instance
