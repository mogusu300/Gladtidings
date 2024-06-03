# core/api.py
from ninja import NinjaAPI, Router
from .models import Course, Enrollment
from .scheme import EnrollmentSchema, CourseSchema

api = NinjaAPI()

router = Router()

@router.post("/enrollments/", response=EnrollmentSchema)
def enroll_user_in_course(request, data: EnrollmentSchema):
    try:
        course = Course.objects.get(id=data.course_id)
        enrollment = Enrollment.objects.create(user=request.user, course=course)
        return enrollment
    except Course.DoesNotExist:
        return {"error": "Course not found"}

api.add_router("/api/v1/", router) 





