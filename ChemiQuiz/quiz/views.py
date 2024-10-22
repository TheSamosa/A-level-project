from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . import functions
from .models import QuestionProfile, QuestionsAnsweredWrong, UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]
        if functions.detailsValidation(username,password,confirmPassword):
            myuser = User.objects.create_user(username = username,password = password)
            myUserProfile = UserProfile(user = myuser)
            myUserProfile.save()
            myuser.save()
            return redirect("signin")
    return render(request,"signup.html")

def home(request):
    if "registered" in request.POST:
        return redirect("signin")

    if "register" in request.POST: 
        return redirect("signup")

    return render(request,"home.html")

def signin(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("questions")

        else:
            return redirect("signin")

    return render(request,"signin.html")

def displayQuestions(request):
    user = request.user
    if user.is_authenticated: 
        currentQuestion = functions.checkIfUserShouldAnswerWrongQuestion(user)

        if request.method == 'POST':
            userAnswer = []
            userAnswer = request.POST
            print(userAnswer)
            correctAnswer = currentQuestion.answer
            print(correctAnswer)
            if "answer" in userAnswer:
                if functions.validateAnswer(user,userAnswer,correctAnswer,currentQuestion):
                   return redirect("correctAnswer")
                else:
                    return redirect("incorrectAnswer")
                # return redirect("questions")
        
        print(f"answer to the question {currentQuestion.questionNumber} is {currentQuestion.answer}")
        print(f"wrong answer countdown is {user.userprofile.countDownToDisplayWrongAnswer}")
        context = {}
        context["currentQuestion"] = currentQuestion

    else:
        return redirect("signin")

    return render(request,"questions.html",context)



def logoutUser(request):
    logout(request)
    return redirect("home")
    

@login_required
def leaderboard(request):
    leaderboardData = UserProfile.objects.all().order_by("-questionsAttempted")
    print(leaderboardData)
    context = {}
    context["leaderboardData"] = leaderboardData
    
    return render(request,"leaderboard.html",context)




@login_required
def incorrectAnswer(request):
    return render(request,"incorrectAnswer.html")

@login_required
def correctAnswer(request):
    return render(request,"correctAnswer.html")

@login_required
def incorrectAnswerIndex(request):
    return render(request,"incorrectAnswerIndex.html")

@login_required
def correctAnswerIndex(request):
    return render(request,"correctAnswerIndex.html")

@login_required
def indexOfQuestions(request):
    user = request.user
    questionCount = QuestionProfile.objects.count()
    print(questionCount)
    context = {}
    context["questionCount"] = questionCount
    #currentQuestion = QuestionProfile.objects.get(questionNumber =  )

    if request.method == 'POST':
            user.userprofile.questionsAttempted += 1
            user.save()
            post = []
            post = request.POST
            userAnswer = post["answer"]
            currentQuestion = QuestionProfile.objects.get(questionNumber = post["button"])
            if userAnswer == currentQuestion.answer:
                return redirect("correctAnswerIndex")
            else:
                return redirect("incorrectAnswerIndex")

            
            # i need to check answer compared to the actual answer of the question which i will get from button.
            # i need to increment the questionAttempted
            # then i need to send it to a page which says if the answer was wrong or correct#
            # try and make it so that you can reuse the already existing html pages for it by changing the url using context
                # return redirect("questions")
            # also you need to fix the fact that the nave bar does not work for any page except home page
            
    
    return render(request,"indexOfQuestions.html",context)


