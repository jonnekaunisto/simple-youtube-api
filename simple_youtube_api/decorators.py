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


@decorator.decorator
def require_channel_auth(f, video, *a, **k):
    if(video.channel is not None):
        return f(video, *a, **k)
    else:
        raise Exception("Setting channel authentication is required before calling " + f.__name__)


@decorator.decorator
def require_youtube_auth(f, video, *a, **k):
    if(video.youtube is not None):
        return f(video, *a, **k)
    else:
        raise Exception("Setting youtube authentication is required before calling " + f.__name__)


@decorator.decorator
def require_channel_or_youtube_auth(f, video, *a, **k):
    if(video.youtube is not None or video.channel != None):
        return f(video, *a, **k)
    else:
        raise Exception("Setting youtube or channel authentication is required before calling " + f.__name__)





