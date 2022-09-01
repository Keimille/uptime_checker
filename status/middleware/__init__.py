from django.utils.deprecation import MiddlewareMixin
from stronghold.middleware import LoginRequiredMiddleware
from django.contrib.auth.decorators import login_required
#TO_DO: Fix login required
class LoginRequiredShimMiddleware(MiddlewareMixin):
     pass