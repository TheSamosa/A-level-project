from django.contrib.auth.models import User
from .models import QuestionProfile, QuestionsAnsweredWrong,UserProfile
from random import randint


def detailsValidation(username,password,confirmPassword):
    if User.objects.filter(username=username).exists():
        return False
    if password != confirmPassword:
        return False
    
    return True

def validateAnswer(user,userAnswer,correctAnswer,currentQuestion):
    user.userprofile.questionsAttempted += 1 
    questionAnsweredCorrectly = True   
    if resetWrongAnswerCountdown(user) and QuestionsAnsweredWrong.objects.filter(user=user).exists():
        deleteWrongAnswerObjects(user,currentQuestion)       
    else:
        decrementWrongAnswerCountdown(user)
        incrementNextQuestionToAnswer(user,currentQuestion)
    if userAnswer["answer"] != correctAnswer:
        isWrongAnswer(user,currentQuestion)
        questionAnsweredCorrectly = False
    user.userprofile.save()
    return questionAnsweredCorrectly

def isWrongAnswer(user,currentQuestion):
    questionAnsweredWrong = QuestionsAnsweredWrong(user = user,questionNumber= currentQuestion.questionNumber)
    questionAnsweredWrong.save()

def resetWrongAnswerCountdown(user):
    if user.userprofile.countDownToDisplayWrongAnswer <= 0:
        user.userprofile.countDownToDisplayWrongAnswer = randint(3,4)
        user.userprofile.save()
        return True
    return False

 
def decrementWrongAnswerCountdown(user):
    user.userprofile.countDownToDisplayWrongAnswer -= 1

def deleteWrongAnswerObjects(user,currentQuestion):
    objectsToDelete = QuestionsAnsweredWrong.objects.filter(questionNumber = currentQuestion.questionNumber,user = user)
    for i in objectsToDelete:
        i.delete()

def incrementNextQuestionToAnswer(user,currentQuestion):
    totalQuestions = QuestionProfile.objects.count()

    if currentQuestion.questionNumber == totalQuestions:
        user.userprofile.NextQuestionToAnswer = 1
    else:
        user.userprofile.NextQuestionToAnswer = currentQuestion.questionNumber + 1
        print(user.userprofile.NextQuestionToAnswer)
        

def checkIfUserShouldAnswerWrongQuestion(user):
    if user.userprofile.countDownToDisplayWrongAnswer == 0 and QuestionsAnsweredWrong.objects.filter(user=user).exists():
        wrongItems = QuestionsAnsweredWrong.objects.filter(user=user).order_by("creationTime").first()
        currentQuestion = QuestionProfile.objects.get(questionNumber = wrongItems.questionNumber)
    else:  
        currentQuestion = QuestionProfile.objects.get(questionNumber = user.userprofile.NextQuestionToAnswer)
    return currentQuestion

    