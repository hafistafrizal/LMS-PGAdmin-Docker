from django.contrib import admin
from .models import (
    Course, Lesson, Assignment, Enrollment, Submission,
)

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ("order", "title", "content")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "code", "title", "teacher", "is_published", "created_at",
    )
    list_filter = ("is_published",)
    search_fields = ("code", "title", "teacher__username")
    ordering = ("code",)
    list_select_related = ("teacher",)
    inlines = [LessonInline]

admin.site.register([Lesson, Assignment, Enrollment, Submission])
