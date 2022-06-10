from django.utils import timezone

from users.models import Session


class FirstMiddleWare():

	def __init__(self, get_response):
		self._get_response = get_response

	def __call__(self, request, *args, **kwargs):

		sessid = request.COOKIES.get('sessionid', None)
		if sessid:
			try:
				session = Session.objects.get(session_id=sessid, expire_date__gt=timezone.now())
				request._session = session
				request._user = session.user
			except Session.DoesNotExist:
				request._session = None
				request._user = None
		else:
			request._session = None
			request._user = None

		response = self._get_response(request)
		return response