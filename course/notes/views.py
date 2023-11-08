from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Import notes from models.py
from .models import Note, notes


def home(request):
    sections_url = reverse("sections")
    html_content = f"<h1>Welcome to my course notes!</h1> <p><a href='{sections_url}'>Click here to browse the list of sections</a></p>"
    return HttpResponse(html_content)


def sections(request):
    home_url = reverse("home")
    sections = ["Web-frameworks", "Setting-up-django", "Url-mapping"]
    section_links = [f"<li><a href='/notes/{section}'>{section}</a></li>" for section in sections]
    html_content = f"<h1>Browse my notes by section</h1><ol>{''.join(section_links)}</ol>"
    html_content += f"<p><a href='{home_url}'>Back to home</a></p>"
    return HttpResponse(html_content)


def sections_detail(request, text_passed):
    if text_passed in ("Web-frameworks", "Setting-up-django", "Url-mapping"):
        section_title = f"Notes about {text_passed}"

        # Conditional text based on section
        section_notes = [note['text'] for note in notes if note['section'] == text_passed]

        html_content = f"<h1>{section_title}</h1><ol>"
        for note in section_notes:
            html_content += f"<li>{note}</li>"
        html_content += "</ol>"

        sections_url = reverse("sections")
        html_content += f"<p><a href='{sections_url}'>Back to sections</a></p>"

        return HttpResponse(html_content)
    else:
        html_content = f"<h1>Section not found</h1><p>Please choose a valid section from the list below:</p><ul><li><a href='/notes/web-frameworks'>Web Frameworks</a></li><li><a href='/notes/setting-up-django'>Setting up Django</a></li><li><a href='/notes/url-mapping'>URL Mapping</a></li></ul>"
        return HttpResponse(html_content)
    
def search_notes(request, search_term):
    # Check if the search term is non-numeric
    if not search_term.isdigit():
        filtered_notes = [note for note in notes if search_term.lower() in note['text'].lower()]

        if filtered_notes:
            html_content = f"<h1>Search Results for '{search_term}'</h1><ol>"
            for note in filtered_notes:
                html_content += f"<li>{note['text']}</li>"
            html_content += "</ol>"
            html_content += f"<p><a href='{reverse('home')}'>Back to home</a></p>"

            return HttpResponse(html_content)
        else:
            html_content = f"<h1>No notes found for '{search_term}'</h1><p>Please try a different search term.</p>"
            html_content += f"<p><a href='{reverse('home')}'>Back to home</a></p>"

            return HttpResponse(html_content)
    else:
        error_message = f"Search term '{search_term}' is not valid. Please enter a non-numeric search term."
        html_content = f"<h1>Invalid Search Term</h1><p>{error_message}</p>"
        html_content += f"<p><a href='{reverse('home')}'>Back to home</a></p>"

        return HttpResponse(html_content)

def non_numeric_notes(request, non_numeric_string):
    filtered_notes = [note for note in notes if non_numeric_string.lower() in note['text'].lower()]

    if filtered_notes:
        html_content = f"<h1>Search Results for '{non_numeric_string}'</h1><ol>"
        for note in filtered_notes:
            html_content += f"<li>{note['text']}</li>"
        html_content += "</ol>"
        html_content += f"<p><a href='{reverse('home')}'>Back to home</a></p>"

        return HttpResponse(html_content)
    else:
        html_content = f"<h1>No notes found for '{non_numeric_string}'</h1><p>Please try a different search term.</p>"
        html_content += f"<p><a href='{reverse('home')}'>Back to home</a></p>"

        return HttpResponse(html_content)

def redirect_to_section_list(request):
    return HttpResponseRedirect("/notes/")
