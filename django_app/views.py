from django.shortcuts import render
from .tasks import process_video


def process_video_view(request):
    if request.method == 'POST':
        process_video.delay()
        return render(request, 'success.html')
    return render(request, 'index.html')
