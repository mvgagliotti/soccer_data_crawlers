from django import template
from django.db.models import Q
from matches.models import Match
import datetime

register = template.Library()


@register.inclusion_tag('matches/matches_search_component.html', takes_context=True)
def matches_search_component(context):
    return {'user': context['request'].user, "request":context['request']}

@register.inclusion_tag('matches/user_next_matches_widget.html', takes_context=True)
def user_next_matches_widget(context, profile):

    user_matches = Match.objects.filter(
        Q(match_date__gt=datetime.datetime.today()),
        Q(home_team__team_id=profile.team_primary_id) | Q(home_team__team_id=profile.team_secondary_id)
        | Q(away_team__team_id=profile.team_primary_id) | Q(away_team__team_id=profile.team_secondary_id)
    ).order_by('match_date')[:3]

    more_matches = []

    matchesCount = user_matches.count()
    if matchesCount < 3:
        more_matches = Match.objects.filter(Q(match_date__gt=datetime.datetime.today())).order_by('match_date')[:(3-matchesCount)]


    return {
            'user_matches': user_matches,
            'more_matches': more_matches
            }
