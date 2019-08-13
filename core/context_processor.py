from core.models import (
	Movie,
	Person,
	Vote
)

def user_vote_movie(request):
	if request.user.is_authenticated:
		movies = Vote.objects.filter(user = request.user)
		return {'user_vote_movies': movies}
	else:
		return {'user_vote_movies': None}

