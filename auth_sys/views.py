from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'auth_sys/login.html'
    success_url = 'restaran'


class CustomLogoutView(LogoutView):
    next_page = 'login'


# class RegisterView(CreateView):
#     model = User
#     template_name = "task_tracker/register.html"
#     form = UserCreationForm
#     # success_url = reverse_lazy('task-list')

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)

#         return redirect('task-list')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("restaran")
    else:
        form = UserCreationForm()

    return render(
        request,           
        "auth_sys/register_form.html", 
        {"form": form}
    )