# coding=UTF-8
from django.test import TestCase
from matches.models import Team, Match, Championship, Season
from django.utils import timezone

# Create your tests here.
class MyTest(TestCase):
    def testMatchLogics(self):
        team1 = Team(short_name="SP", full_name="São Paulo FC")
        team2 = Team(short_name="Palmeiras", full_name="Palmeiras FC")
        team1.save();
        team2.save();
        
        season = Season(start_year=2012, end_year=2012)
        season.save();
        
        cp = Championship(name="Brasileirao", start_date=timezone.now())
        cp.season = season;
        cp.save();
                
        match1 = Match()
        
        match1.championship = cp;
        match1.home_team = team1;
        match1.away_team = team2;
        match1.match_date = timezone.now();
        
        match1.save();