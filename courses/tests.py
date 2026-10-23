from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models.deletion import ProtectedError
from django.test import TestCase
from django.utils import timezone
from .models import Course, Assignment, Submission, Enrollment

class LMSModelTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.teacher = User.objects.create_user(username="teacher")
        self.student = User.objects.create_user(username="student")
        self.course = Course.objects.create(
            code="TEST", title="Test", teacher=self.teacher,
        )
        self.task = Assignment.objects.create(
            course=self.course, title="Task",
            deadline=timezone.now(), max_score=100,
        )

    def test_score_cannot_exceed_maximum(self):
        obj = Submission(
            assignment=self.task, student=self.student,
            answer="Answer", score=101,
        )
        with self.assertRaises(ValidationError):
            obj.full_clean()

    def test_enrollment_is_unique(self):
        Enrollment.objects.create(
            course=self.course, student=self.student,
        )
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Enrollment.objects.create(
                    course=self.course, student=self.student,
                )

    def test_teacher_is_protected(self):
        with self.assertRaises(ProtectedError):
            self.teacher.delete()
