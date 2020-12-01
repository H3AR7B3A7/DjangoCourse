from django.http import HttpResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    my_context = {"my_text": "Some text ...",
                  "my_number": 123,
                  "my_list": [5, 6, 7, 8]}

    return render(request, "index.html", my_context)


def contact(request, *args, **kwargs):
    return HttpResponse(
        """
        <h1>Contact</h1>
        <a href="/">Back</a>
        """
    )
