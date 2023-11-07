from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def home(request):
    sections_url = reverse("sections")
    return HttpResponse(f"<h1>Welcome to my course notes!</h1> <p><a href='{sections_url}'>Click the list of the sections</a></p>")

def sections(request):
    home_url = reverse("home")
    sections = ["Web Frameworks", "Setting up Django", "URL Mapping"]
    section_links = [f"<li><a href='/notes/{section}'>{section}</a></li>" for section in sections]
    return HttpResponse(f"<h1>Browse my notes by section</h1><ul>{''.join(section_links)}</ul><p><a href='{home_url}'>Back to home</a></p>")
