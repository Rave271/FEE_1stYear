

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegistrationForm
from django.http import JsonResponse
from .models import Score
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .models import LeaderboardEntry
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ScoreHistory

def index_view(request):
    # Add your logic here, this view is responsible for rendering the home page
    return render(request, 'index.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('guide')
#         else:
#             error_message = 'Invalid username or password.'
#             return render(request, 'login.html', {'error_message': error_message})
#     return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or any other page
                return redirect('home')  # Change 'home' to your desired URL name
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('guide')  # Redirect to guide page after successful registration and login
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})





# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             UserProfile.objects.create(user=user)
#             login(request, user)
#             return redirect('guide')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})











def leaderboard(request):
    # Retrieve user profiles ordered by score
    users = UserProfile.objects.order_by('-score')

    # Render the leaderboard template with the user profiles
    return render(request, 'leaderboard.html', {'users': users})
@login_required
def quiz_submission(request):
    if request.method == 'POST':
        # Process the quiz submission and calculate the score
        score = calculate_score(request.POST)  # Your logic to calculate the score
        
        # Update the user's profile with the score
        leaderboard_entry, created = LeaderboardEntry.objects.get_or_create(user=request.user)
        if score > user_profile.high_score:
            user_profile.high_score = score
            user_profile.save()
        
         # Pass the score to the template context to display it on the page
        context = {'score': score}
        return render(request, 'quiz_result.html', context)
    else:
        return redirect('quiz_page')
def guide_view(request):
    # Your logic for rendering the guide.html template goes here
    return render(request, 'guide.html')   



def complete_quiz(request, quiz_id):
    if request.method == 'POST':
        # Get the quiz based on the quiz_id
        quiz = Quiz.objects.get(id=quiz_id)

        # Get the user's answers from the POST data
        user_answers = request.POST

        # Get the correct answers from the quiz
        correct_answers = quiz.correct_answers  # This depends on how your Quiz model is set up

        # Calculate the score
        score = 0
        for question, correct_answer in correct_answers.items():
            user_answer = user_answers.get(question)
            if user_answer == correct_answer:
                score += 1

        # Update the leaderboard
        entry, created = LeaderboardEntry.objects.get_or_create(user=request.user)
        entry.score += score
        entry.save()

        # Redirect to a success page
        return redirect('quiz_success')
    else:
        # If the request method is not POST, redirect to the quiz page
        return redirect('quiz_page')


def quizselection_view(request):
    # Logic for rendering the next page template
    return render(request, 'quizselection.html')
def f1_view(request):
    # Logic for rendering the next page template
    return render(request, 'f1.html')
def home_view(request):
    # Logic for rendering the next page template
    return render(request, 'home.html')
def reset_view(request):
    # Logic for rendering the next page template
    return render(request, 'reset.html')
def f1home_view(request):
    # Logic for rendering the next page template
    return render(request, 'f1home.html')
from django.shortcuts import render

def end(request):
    score = request.GET.get('score', 0)
    questions = request.GET.get('questions', 0)
    return render(request, 'end.html', {'score': score, 'questions': questions})
def ecology_view(request):
    # Logic for rendering the next page template
    return render(request, 'ecology.html')
def ecologyhome_view(request):
    # Logic for rendering the next page template
    return render(request, 'ecologyhome.html')

def astronomy_view(request):
    # Logic for rendering the next page template
    return render(request, 'astronomy.html')
def astronomyhome_view(request):
    # Logic for rendering the next page template
    return render(request, 'astronomyhome.html')
def deca_view(request):
    # Logic for rendering the next page template
    return render(request, 'deca.html')
def decahome_view(request):
    # Logic for rendering the next page template
    return render(request, 'decahome.html')

def economics_view(request):
    # Logic for rendering the next page template
    return render(request, 'economics.html')
def economicshome_view(request):
    # Logic for rendering the next page template
    return render(request, 'economicshome.html')


def fee_view(request):
    # Logic for rendering the next page template
    return render(request, 'fee.html')
def feehome_view(request):
    # Logic for rendering the next page template
    return render(request, 'feehome.html')
def reset_view(request):
    # Logic for rendering the next page template
    return render(request, 'reset.html')


def history_view(request):
    # Logic for rendering the next page template
    return render(request, 'history.html')



def record_score(request, score):
    if request.user.is_authenticated:
        user_score = Score(user=request.user, score=score)
        user_score.save()
# views.py
def leaderboard(request):
    top_scores = LeaderboardEntry.objects.order_by('-score')[:5]
    return render(request, 'leaderboard.html', {'leaderboard': top_scores})
def quiz_submission(request):
    if request.method == 'POST':
        # Process the quiz submission and calculate the score
        score = calculate_score(request.POST)  # Your logic to calculate the score
        
        # Record the score in the ScoreHistory table
        quiz_name = "Your Quiz Name"  # Replace this with the actual quiz name
        user = request.user
        score_history = ScoreHistory.objects.create(user=user, quiz_name=quiz_name, score=score)
        
        # Pass the score to the template context to display it on the page
        context = {'score': score}
        return render(request, 'quiz_result.html', context)
    else:
        return redirect('quiz_page')
    
def score_history(request):
    top_scores = ScoreHistory.objects.order_by('-score')[:5]
    return render(request, 'score_history.html', {'score_history': top_scores})
@csrf_exempt
def update_score(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        user = request.user

        # Update the leaderboard
        entry, created = LeaderboardEntry.objects.get_or_create(user=user)
        entry.score = score
        entry.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})