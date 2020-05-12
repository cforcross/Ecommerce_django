from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model


def home_page(request):
    # print(request.session.get("first_name", "unknown"))
    context = {
        "title": "Hello world",
        "content": "Welcome to the homepage",
    }
    if request.user.is_authenticated:
        context["premuim_content"] = "YEEEAAHHHHHHH"
    return render(request, 'home_page.html', context=context)


def about_page(request):
    context = {
        "title": "About page"
    }
    return render(request, 'about_page.html', context=context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        'content': "Contact form",
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, 'contact/view.html', context=context)


def login_page(request):
    form = LoginForm(request.POST, None)
    context = {
        'form': form,
    }

    print("user logged in")
    # print(request.user.is_authenticated)

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            print(user)
            # print(request.user.is_authenticated)
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect('/login')
        else:
            # Return an 'invalid login' error message.
            print('Error')
    return render(request, "auth/login.html", context=context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST, None)

    context = {
        'form': form,
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context=context)
