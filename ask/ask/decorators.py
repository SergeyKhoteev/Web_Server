from django.urls import reverse

from users.models import Session, MyUser


def returns_user_or_none(func):

	def wraper(request, *args, **kwargs):
		sessid = request.COOKIES.get('sessionid', None)
		if sessid:
			try:
				session = Session.objects.get(session_id=sessid)
				user = session.user
			except:
				user = None
		else:
			user = None

		print(user)
		result = func(request, user, *args, **kwargs)
		return result

	return wraper
