from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Incident, Profile, Incident, Comment

# Create your views here.
def index(request):
    incidents = Incident.objects.order_by("-created_at")

    return render(request, "incidents/index.html", {"incidents": incidents})

def register_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        role = request.POST["role"]

        if password != confirmation:
            return render(request, "incidents/register.html", {"message": "Passwords must match."})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)

            Profile.objects.create(user=user,role=role)
            
            login(request, user)
            return redirect('incidents:index')


        except:
            return render(request, "incidents/register.html", {"message": "Username already exists."})



    return render(request, "incidents/register.html")


def login_view(request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('incidents:index')
            else:
                return render(request, "incidents/login.html", {"message": "Invalid username or password."})
                
        return render(request, "incidents/login.html")

def logout_view(request):
    logout(request)
    return redirect('incidents:index')

@login_required
def report_incident(request):

    if request.method == "POST":

        Incident.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            issue_type=request.POST["issue_type"],
            location=request.POST["location"],
            latitude=request.POST.get("latitude"),
            longitude=request.POST.get("longitude"),
            reporter=request.user
        )

        return redirect('incidents:index')

    return render(request, "incidents/report.html")

def incidents_list(request):

    incidents = Incident.objects.order_by("-created_at")

    return render(request, "incidents/incident.html", {"incidents": incidents})

def incident(request, incident_id):
    incident = get_object_or_404(Incident, pk=incident_id)
    
    if request.method == "POST":
        Comment.objects.create(incident=incident, author=request.user, content=request.POST["content"])
        return redirect("incidents:incident", incident_id=incident.id)
    return render(request,"incidents/incident.html", {"incident": incident})


@login_required
def my_incidents(request):
    incidents = Incident.objects.filter(reporter=request.user).order_by("-created_at")

    return render( request, "incidents/my_incidents.html", {"incidents": incidents})

def councillor_dashboard(request):
    incidents = Incident.objects.order_by("-created_at")

    return render(request, "incidents/councillor.html", {"incidents": incidents})

#councillor dashboard
@login_required
def councillor_dashboard(request):

    incidents = Incident.objects.order_by("-created_at")

    context = {
        "incidents": incidents,
        "total_incidents": Incident.objects.count(),
        "open_incidents": Incident.objects.exclude(status="resolved").count(),
        "resolved_incidents": Incident.objects.filter(status="RESOLVED").count()
    }

    return render(request, "incidents/councillor_dashboard.html", context)


@login_required
def update_status(request, incident_id):

    incident = get_object_or_404(Incident, pk=incident_id)

    if request.method == "POST":

        incident.status = request.POST["status"]
        incident.save()

    return redirect("incidents:councillor_dashboard")


@login_required
def edit_comment(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":

        comment.content = request.POST["content"]
        comment.save()

        return redirect("incidents:incident",incident_id=comment.incident.id)

    return render(request, "incidents/edit_comment.html", {"comment": comment})



@login_required
def mayor_dashboard(request):
    incidents = Incident.objects.order_by("-created_at")
    
    context = {
        "incidents": incidents[:10],
        "total_incidents": Incident.objects.count(),
        "reported_incidents": Incident.objects.filter(status="reported").count(),
        "progress_incidents": Incident.objects.filter(status="progress").count(),
         "resolved_incidents": Incident.objects.filter(status="resolved").count(),}
         
    return render(request,"incidents/mayor_dashboard.html",context)

