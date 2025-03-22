from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from other.models.job import Job
from other.serializers.job_serializers import JobViewSerializer


class JobServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        jobs = Job.objects.all().order_by("-created_at")
        if data.get("keyword"):
            jobs = jobs.filter(title__icontains=data.get("keyword"))
        return self.ok(JobViewSerializer(jobs, many=True).data, StatusCodes().SUCCESS)

    def post_service(self, request, data):
        job = Job.objects.create(
            title=data.get("title"),
            department=data.get("department"),
            location=data.get("location"),
            type=data.get("type"),
            description=data.get("description"),
        )
        return self.ok(JobViewSerializer(job).data, StatusCodes().CREATED)