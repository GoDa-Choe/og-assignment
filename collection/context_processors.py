def is_artist(request):
    return {'is_artist': hasattr(request.user, 'artist')}
