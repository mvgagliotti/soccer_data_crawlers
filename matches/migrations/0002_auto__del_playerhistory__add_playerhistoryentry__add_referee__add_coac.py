# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PlayerHistory'
        db.delete_table(u'matches_playerhistory')

        # Adding model 'PlayerHistoryEntry'
        db.create_table(u'matches_playerhistoryentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'matches', ['PlayerHistoryEntry'])

        # Adding model 'Referee'
        db.create_table(u'matches_referee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country_of_birth', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities.Country'], null=True, blank=True)),
        ))
        db.send_create_signal(u'matches', ['Referee'])

        # Adding model 'Coach'
        db.create_table(u'matches_coach', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country_of_birth', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities.Country'], null=True, blank=True)),
        ))
        db.send_create_signal(u'matches', ['Coach'])

        # Deleting field 'Player.from_date'
        db.delete_column(u'matches_player', 'from_date')

        # Adding field 'Player.country_of_birth'
        db.add_column(u'matches_player', 'country_of_birth',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='country_of_birth', null=True, to=orm['cities.Country']),
                      keep_default=False)

        # Adding field 'Player.second_nationality'
        db.add_column(u'matches_player', 'second_nationality',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='second_nationality', null=True, to=orm['cities.Country']),
                      keep_default=False)


        # Changing field 'Player.current_team'
        db.alter_column(u'matches_player', 'current_team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team'], null=True))
        # Adding field 'Match.referee'
        db.add_column(u'matches_match', 'referee',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Referee'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Match.home_team_coach'
        db.add_column(u'matches_match', 'home_team_coach',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='home_team_coach', null=True, to=orm['matches.Coach']),
                      keep_default=False)

        # Adding field 'Match.away_team_coach'
        db.add_column(u'matches_match', 'away_team_coach',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='away_team_coach', null=True, to=orm['matches.Coach']),
                      keep_default=False)

        # Adding field 'Team.is_national_team'
        db.add_column(u'matches_team', 'is_national_team',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'PhaseGroup.name'
        db.add_column(u'matches_phasegroup', 'name',
                      self.gf('django.db.models.fields.CharField')(default='fill_my_name', max_length=25),
                      keep_default=False)


        # Changing field 'Goal.scored_by'
        db.alter_column(u'matches_goal', 'scored_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player']))
        # Adding field 'MatchSubstitution.from_home_team'
        db.add_column(u'matches_matchsubstitution', 'from_home_team',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'MatchSubstitution.player_in'
        db.alter_column(u'matches_matchsubstitution', 'player_in_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player']))

        # Changing field 'MatchSubstitution.player_out'
        db.alter_column(u'matches_matchsubstitution', 'player_out_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player']))
        # Adding field 'ConcreteTeam.coach'
        db.add_column(u'matches_concreteteam', 'coach',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Coach'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'ConcreteChampionship.champion'
        db.alter_column(u'matches_concretechampionship', 'champion_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['matches.ConcreteTeam']))

        # Changing field 'MatchPlayer.player'
        db.alter_column(u'matches_matchplayer', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player']))

        # Changing field 'ChampionshipTable.team'
        db.alter_column(u'matches_championshiptable', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ConcreteTeam']))

    def backwards(self, orm):
        # Adding model 'PlayerHistory'
        db.create_table(u'matches_playerhistory', (
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'matches', ['PlayerHistory'])

        # Deleting model 'PlayerHistoryEntry'
        db.delete_table(u'matches_playerhistoryentry')

        # Deleting model 'Referee'
        db.delete_table(u'matches_referee')

        # Deleting model 'Coach'
        db.delete_table(u'matches_coach')


        # User chose to not deal with backwards NULL issues for 'Player.from_date'
        raise RuntimeError("Cannot reverse this migration. 'Player.from_date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Player.from_date'
        db.add_column(u'matches_player', 'from_date',
                      self.gf('django.db.models.fields.DateField')(),
                      keep_default=False)

        # Deleting field 'Player.country_of_birth'
        db.delete_column(u'matches_player', 'country_of_birth_id')

        # Deleting field 'Player.second_nationality'
        db.delete_column(u'matches_player', 'second_nationality_id')


        # User chose to not deal with backwards NULL issues for 'Player.current_team'
        raise RuntimeError("Cannot reverse this migration. 'Player.current_team' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Player.current_team'
        db.alter_column(u'matches_player', 'current_team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team']))
        # Deleting field 'Match.referee'
        db.delete_column(u'matches_match', 'referee_id')

        # Deleting field 'Match.home_team_coach'
        db.delete_column(u'matches_match', 'home_team_coach_id')

        # Deleting field 'Match.away_team_coach'
        db.delete_column(u'matches_match', 'away_team_coach_id')

        # Deleting field 'Team.is_national_team'
        db.delete_column(u'matches_team', 'is_national_team')

        # Deleting field 'PhaseGroup.name'
        db.delete_column(u'matches_phasegroup', 'name')


        # Changing field 'Goal.scored_by'
        db.alter_column(u'matches_goal', 'scored_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.TeamPlayer']))
        # Deleting field 'MatchSubstitution.from_home_team'
        db.delete_column(u'matches_matchsubstitution', 'from_home_team')


        # Changing field 'MatchSubstitution.player_in'
        db.alter_column(u'matches_matchsubstitution', 'player_in_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.MatchPlayer']))

        # Changing field 'MatchSubstitution.player_out'
        db.alter_column(u'matches_matchsubstitution', 'player_out_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.MatchPlayer']))
        # Deleting field 'ConcreteTeam.coach'
        db.delete_column(u'matches_concreteteam', 'coach_id')


        # Changing field 'ConcreteChampionship.champion'
        db.alter_column(u'matches_concretechampionship', 'champion_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['matches.Team']))

        # Changing field 'MatchPlayer.player'
        db.alter_column(u'matches_matchplayer', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.TeamPlayer']))

        # Changing field 'ChampionshipTable.team'
        db.alter_column(u'matches_championshiptable', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team']))

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
            'minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scored_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Player']"})
        },
        u'matches.match': {
            'Meta': {'object_name': 'Match'},
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"}),
            'away_team_coach': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'away_team_coach'", 'null': 'True', 'to': u"orm['matches.Coach']"}),
            'away_team_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteChampionship']"}),
            'championshipPhase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ChampionshipPhase']", 'null': 'True', 'blank': 'True'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_team'", 'to': u"orm['matches.ConcreteTeam']"}),
            'home_team_coach': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home_team_coach'", 'null': 'True', 'to': u"orm['matches.Coach']"}),
            'home_team_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'phaseGroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.PhaseGroup']", 'null': 'True', 'blank': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Referee']", 'null': 'True', 'blank': 'True'}),
            'round_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Stadium']", 'null': 'True', 'blank': 'True'})
        },
        u'matches.matchplayer': {
            'Meta': {'object_name': 'MatchPlayer'},
            'first_yellow_card': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'first_yellow_card_minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_home_team': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Player']"}),
            'red_card': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'second_card_or_red_card_minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'country_of_birth': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.Country']", 'null': 'True', 'blank': 'True'}),
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
            'substitute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            't_shirt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['matches']