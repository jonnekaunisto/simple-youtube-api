"""
    All the decorators used in Simple YouTube API go here
"""
import decorator


@decorator.decorator
def video_snippet_set(func, video, *a, **k):
    ''' Sets the snippet_set to true '''
    video.snippet_set = True
    return func(video, *a, **k)


@decorator.decorator
def video_status_set(func, video, *a, **k):
    ''' Sets the status_set to true '''
    video.status_set = True
    return func(video, *a, **k)


@decorator.decorator
def require_channel_auth(func, video, *a, **k):
    ''' Checks that channel auth exists '''
    if video.channel is not None:
        return func(video, *a, **k)

    raise Exception(
        "Setting channel authentication is required before calling "
        + func.__name__
    )


@decorator.decorator
def require_youtube_auth(func, video, *a, **k):
    ''' Checks that youtube auth exists '''
    if video.youtube is not None:
        return func(video, *a, **k)

    raise Exception(
        "Setting youtube authentication is required before calling "
        + func.__name__
    )


@decorator.decorator
def require_channel_or_youtube_auth(func, video, *a, **k):
    ''' Checks that youtube or channel auth exists '''
    if video.youtube is not None or video.channel is not None:
        return func(video, *a, **k)

    raise Exception(
        "Setting youtube or channel authentication is required before calling "
        + func.__name__
    )
