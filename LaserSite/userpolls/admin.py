from django.contrib import admin

from .models import Question, Choice


admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')  #  changes on Admin portal to show text and publication date
    list_filter = ['pub_date']  # allows to filter by publication date
    search_fields = ['question_text']  # adds search bar functionality

admin.site.register(Question, QuestionAdmin)

