from django.db import models


class Note(models.Model):
    section = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.section}: {self.text}"


notes = [
    {"section": "Web-frameworks",
        "text": "Web frameworks are a way to improve our productivity and make complex things look easy."},
    {"section": "Web-frameworks",
        "text": "Django is a web framework written with Python that offers a 'batteries included' approach, as    opposed to Flask, that aims at minimizing the initial features to reduce the footprint."},
    {"section": "Web-frameworks",
        "text": "Most web frameworks use the MVC design pattern that states that logic, data and visualization should be kept in different places."},


    {"section": "Setting-up-django",
        "text": "Setting up Django is very simple. It requires installing Django, starting a project and an app."},
    {"section": "Setting-up-django",
        "text": "The startproject command lets us specify the directory where the project will be created."},
    {"section": "Setting-up-django",
        "text": "Django comes with a development web server that makes it very simple to install and start working."},


    {"section": "Url-mapping",
        "text": "URL Mapping can be very easy at the beginning but it may become extremely complex in some cases."},
    {"section": "Url-mapping",
        "text": "URL Mapping is the process of mapping URLs to views."},
    {"section": "Url-mapping",
        "text": "URL endpoints may be defined with literals and parameters, which will be passed on to the view."},

    {"section": "URL Mapping",
        "text": "Parameters passed with the <b><</b> and <b>></b> will be passed as keyword arguments."},

]
