from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('questions', views.displayQuestions, name='questions'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('incorrectAnswer', views.incorrectAnswer, name='incorrectAnswer'),
    path('correctAnswer', views.correctAnswer, name='correctAnswer'),
    path('indexOfQuestions', views.indexOfQuestions, name='indexOfQuestions'),
    path('correctAnswerIndex', views.correctAnswerIndex, name='correctAnswerIndex'),
    path('incorrectAnswerIndex', views.incorrectAnswerIndex, name='incorrectAnswerIndex'),


]
