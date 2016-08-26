from django.conf import settings

def dev_context_processor(request):
    env_state = {
        'dev': settings.DEBUG,
        'prod': not settings.DEBUG
    }
    return env_state
