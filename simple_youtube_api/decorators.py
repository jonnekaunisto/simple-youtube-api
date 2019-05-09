"""
    All the decorators used in Simple YouTube API go here
"""
import decorator

@decorator.decorator
def video_snippet_set(f, video, *a, **k):
    video.snippet_set = True
    return f(video, *a, **k)

@decorator.decorator
def video_status_set(f, video, *a, **k):
    video.status_set = True
    return f(video, *a, **k)
