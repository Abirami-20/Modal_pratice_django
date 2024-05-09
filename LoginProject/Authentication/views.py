from django.shortcuts import render
from django.shortcuts import render, redirect
dummy_users = {
    'abi': '123',
    'user2': 'password2',
}

def login(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username in dummy_users and dummy_users[username] == password:
            # Successful login, redirect to home page
            return redirect('home')
        else:
            # Invalid credentials, display error message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')