# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ConcreteChampionship.rounds'
        db.delete_column(u'matches_concretechampionship', 'rounds')

        # Adding field 'ConcreteChampionship.match_count'
        db.add_column(u'matches_concretechampionship', 'match_count',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ConcreteChampionship.rounds'
        db.add_column(u'matches_concretechampionship', 'rounds',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ConcreteChampionship.match_count'
        db.delete_column(u'matches_concretechampionship', 'match_count')


    models = {
        u'cities.city': {
            'Meta': {'object_name': 'City'},
            'city_en': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'city_pt-br': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Region']"})
        },
        u'cities.country': {
            'Meta': {'object_name': 'Country'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'country_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country_pt-br': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cities.region': {
            'Meta': {'object_name': 'Region'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_en': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'region_pt-br': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'matches.championship': {
            'Meta': {'object_name': 'Championship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'matches.championshipphase': {
            'Meta': {'object_name': 'ChampionshipPhase'},
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteChampionship']"}),
            'groups': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phase_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'rounds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'matches.championshiptable': {
            'Meta': {'object_name': 'ChampionshipTable'},
            'goals_against': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'goals_scored': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matches_drawn': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'matches_lost': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'matches_played': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'matches_won': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ChampionshipPhase']"}),
            'points': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"})
        },
        u'matches.coach': {
            'Meta': {'object_name': 'Coach'},
            'country_of_birth': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Country']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'matches.concretechampionship': {
            'Meta': {'object_name': 'ConcreteChampionship'},
            'champion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'champion'", 'null': 'True', 'to': u"orm['matches.ConcreteTeam']"}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Championship']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['matches.ConcreteTeam']", 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Season']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'matches.concreteteam': {
            'Meta': {'object_name': 'ConcreteTeam'},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Coach']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Season']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Team']"})
        },
        u'matches.goal': {
            'Meta': {'object_name': 'Goal'},
            'auto_gol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_favor_of': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"}),
            'in_favor_of_home_team': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Match']"}),
            'match_time': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scored_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Player']"})
        },
        u'matches.match': {
            'Meta': {'object_name': 'Match'},
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"}),
            'away_team_coach': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'away_team_coach'", 'null': 'True', 'to': u"orm['matches.Coach']"}),
            'away_team_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'away_team_penalty_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteChampionship']"}),
            'championshipPhase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ChampionshipPhase']", 'null': 'True', 'blank': 'True'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_team'", 'to': u"orm['matches.ConcreteTeam']"}),
            'home_team_coach': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home_team_coach'", 'null': 'True', 'to': u"orm['matches.Coach']"}),
            'home_team_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'home_team_penalty_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'match_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'phaseGroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.PhaseGroup']", 'null': 'True', 'blank': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Referee']", 'null': 'True', 'blank': 'True'}),
            'referee_ass1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ref_aux1'", 'null': 'True', 'to': u"orm['matches.Referee']"}),
            'referee_ass2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ref_aux2'", 'null': 'True', 'to': u"orm['matches.Referee']"}),
            'round_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Stadium']", 'null': 'True', 'blank': 'True'})
        },
        u'matches.matchplayer': {
            'Meta': {'object_name': 'MatchPlayer'},
            'first_yellow_card': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'first_yellow_card_minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_yellow_card_time': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'from_home_team': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Player']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'red_card': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'second_card_or_red_card_minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'second_card_or_red_card_time': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'second_yellow_card': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'substitute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            't_shirt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"})
        },
        u'matches.matchsubstitution': {
            'Meta': {'object_name': 'MatchSubstitution'},
            'from_home_team': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Match']"}),
            'match_time': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_in': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_in'", 'to': u"orm['matches.Player']"}),
            'player_out': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_out'", 'to': u"orm['matches.Player']"})
        },
        u'matches.phasegroup': {
            'Meta': {'object_name': 'PhaseGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['matches.ConcreteTeam']", 'null': 'True', 'blank': 'True'}),
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ChampionshipPhase']"})
        },
        u'matches.player': {
            'Meta': {'object_name': 'Player'},
            'birth_city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.City']", 'null': 'True', 'blank': 'True'}),
            'country_of_birth': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'country_of_birth'", 'null': 'True', 'to': u"orm['cities.Country']"}),
            'current_team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Team']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'second_nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'second_nationality'", 'null': 'True', 'to': u"orm['cities.Country']"})
        },
        u'matches.playerhistoryentry': {
            'Meta': {'object_name': 'PlayerHistoryEntry'},
            'from_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Team']"}),
            'to_date': ('django.db.models.fields.DateField', [], {})
        },
        u'matches.referee': {
            'Meta': {'object_name': 'Referee'},
            'birth_data': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'country_of_birth': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Country']", 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'matches.season': {
            'Meta': {'object_name': 'Season'},
            'end_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'matches.stadium': {
            'Meta': {'object_name': 'Stadium'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.City']"}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'matches.team': {
            'Meta': {'object_name': 'Team'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_national_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'matches.teamplayer': {
            'Meta': {'object_name': 'TeamPlayer'},
            'concrete_team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Player']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'substitute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            't_shirt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['matches']