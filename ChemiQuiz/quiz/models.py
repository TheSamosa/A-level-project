from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    NextQuestionToAnswer = models.IntegerField(default=1)
    questionsAttempted = models.IntegerField(default=0)
    countDownToDisplayWrongAnswer = models.IntegerField(default=4)


class QuestionProfile(models.Model):
    question = models.ImageField(upload_to="images/",null= True, blank = True )
    answer = models.CharField(max_length = 1)
    questionNumber = models.IntegerField(primary_key=True)


class QuestionsAnsweredWrong(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    questionNumber = models.IntegerField()
    creationTime = models.DateTimeField(auto_now=True)


"settings.AUTH_USER_MODEL"