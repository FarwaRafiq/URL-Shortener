from django.shortcuts import render, redirect
import pyshorteners
from django.contrib import messages

def urlshort(request):
    short_url = ""
    url = ""
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            try:
                s = pyshorteners.Shortener()
                short_url = s.tinyurl.short(url)
                messages.success(request, 'url short is generated')
                # print(f"Shortened URL: {short_url}")
            except Exception as e:
                # print(f"Error shortening URL: {e}")
                 short_url = f"Error: {str(e)}"
    context = {
        'short_url' : short_url,
        'url': url
    }
    
    return render(request, 'url_short/index.html', context)
