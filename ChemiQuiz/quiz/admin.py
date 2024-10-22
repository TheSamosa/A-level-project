from django.contrib import admin
from .models import UserProfile,QuestionProfile,QuestionsAnsweredWrong



class UserProfileAdmin(admin.ModelAdmin):
    list_display=("user","NextQuestionToAnswer","questionsAttempted","countDownToDisplayWrongAnswer")
admin.site.register(UserProfile,UserProfileAdmin)

class QuestionProfileAdmin(admin.ModelAdmin):
    list_display=("question","answer","questionNumber")
admin.site.register(QuestionProfile,QuestionProfileAdmin)

class QuestionsAnsweredWrongAdmin(admin.ModelAdmin):
    list_display=("user","questionNumber","creationTime")
admin.site.register(QuestionsAnsweredWrong,QuestionsAnsweredWrongAdmin)
    