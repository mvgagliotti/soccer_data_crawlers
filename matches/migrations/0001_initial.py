# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'matches_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'matches', ['Team'])

        # Adding model 'Season'
        db.create_table(u'matches_season', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_year', self.gf('django.db.models.fields.IntegerField')()),
            ('end_year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'matches', ['Season'])

        # Adding model 'ConcreteTeam'
        db.create_table(u'matches_concreteteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Season'])),
        ))
        db.send_create_signal(u'matches', ['ConcreteTeam'])

        # Adding model 'Championship'
        db.create_table(u'matches_championship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'matches', ['Championship'])

        # Adding model 'ConcreteChampionship'
        db.create_table(u'matches_concretechampionship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('championship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Championship'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Season'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('champion', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='champion', null=True, to=orm['matches.Team'])),
        ))
        db.send_create_signal(u'matches', ['ConcreteChampionship'])

        # Adding M2M table for field participants on 'ConcreteChampionship'
        m2m_table_name = db.shorten_name(u'matches_concretechampionship_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('concretechampionship', models.ForeignKey(orm[u'matches.concretechampionship'], null=False)),
            ('team', models.ForeignKey(orm[u'matches.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['concretechampionship_id', 'team_id'])

        # Adding model 'ChampionshipPhase'
        db.create_table(u'matches_championshipphase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('championship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ConcreteChampionship'])),
            ('rounds', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('groups', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phase_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'matches', ['ChampionshipPhase'])

        # Adding model 'PhaseGroup'
        db.create_table(u'matches_phasegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ChampionshipPhase'])),
        ))
        db.send_create_signal(u'matches', ['PhaseGroup'])

        # Adding M2M table for field participants on 'PhaseGroup'
        m2m_table_name = db.shorten_name(u'matches_phasegroup_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('phasegroup', models.ForeignKey(orm[u'matches.phasegroup'], null=False)),
            ('team', models.ForeignKey(orm[u'matches.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['phasegroup_id', 'team_id'])

        # Adding model 'ChampionshipTable'
        db.create_table(u'matches_championshiptable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team'])),
            ('phase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ChampionshipPhase'])),
            ('round', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('matches_played', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('matches_won', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('matches_drawn', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('matches_lost', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('goals_scored', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('goals_against', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'matches', ['ChampionshipTable'])

        # Adding model 'Player'
        db.create_table(u'matches_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('current_team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('birth_city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities.City'], null=True, blank=True)),
        ))
        db.send_create_signal(u'matches', ['Player'])

        # Adding model 'PlayerHistory'
        db.create_table(u'matches_playerhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Team'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'matches', ['PlayerHistory'])

        # Adding model 'TeamPlayer'
        db.create_table(u'matches_teamplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('concrete_team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ConcreteTeam'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Player'])),
            ('t_shirt', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('substitute', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'matches', ['TeamPlayer'])

        # Adding model 'Stadium'
        db.create_table(u'matches_stadium', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities.City'])),
        ))
        db.send_create_signal(u'matches', ['Stadium'])

        # Adding model 'Match'
        db.create_table(u'matches_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('stadium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Stadium'], null=True, blank=True)),
            ('championship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ConcreteChampionship'])),
            ('championshipPhase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ChampionshipPhase'], null=True, blank=True)),
            ('phaseGroup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.PhaseGroup'], null=True, blank=True)),
            ('round_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('home_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_team', to=orm['matches.ConcreteTeam'])),
            ('away_team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ConcreteTeam'])),
            ('home_team_goals', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True)),
            ('away_team_goals', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'matches', ['Match'])

        # Adding model 'MatchPlayer'
        db.create_table(u'matches_matchplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Match'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.TeamPlayer'])),
            ('from_home_team', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ConcreteTeam'])),
            ('t_shirt', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('substitute', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('first_yellow_card', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('first_yellow_card_minute', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('second_yellow_card', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('red_card', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('second_card_or_red_card_minute', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'matches', ['MatchPlayer'])

        # Adding model 'Goal'
        db.create_table(u'matches_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Match'])),
            ('scored_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.TeamPlayer'])),
            ('in_favor_of', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.ConcreteTeam'])),
            ('in_favor_of_home_team', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('auto_gol', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('minute', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'matches', ['Goal'])

        # Adding model 'MatchSubstitution'
        db.create_table(u'matches_matchsubstitution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Match'])),
            ('player_in', self.gf('django.db.models.fields.related.ForeignKey')(related_name='player_in', to=orm['matches.MatchPlayer'])),
            ('player_out', self.gf('django.db.models.fields.related.ForeignKey')(related_name='player_out', to=orm['matches.MatchPlayer'])),
            ('minute', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'matches', ['MatchSubstitution'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'matches_team')

        # Deleting model 'Season'
        db.delete_table(u'matches_season')

        # Deleting model 'ConcreteTeam'
        db.delete_table(u'matches_concreteteam')

        # Deleting model 'Championship'
        db.delete_table(u'matches_championship')

        # Deleting model 'ConcreteChampionship'
        db.delete_table(u'matches_concretechampionship')

        # Removing M2M table for field participants on 'ConcreteChampionship'
        db.delete_table(db.shorten_name(u'matches_concretechampionship_participants'))

        # Deleting model 'ChampionshipPhase'
        db.delete_table(u'matches_championshipphase')

        # Deleting model 'PhaseGroup'
        db.delete_table(u'matches_phasegroup')

        # Removing M2M table for field participants on 'PhaseGroup'
        db.delete_table(db.shorten_name(u'matches_phasegroup_participants'))

        # Deleting model 'ChampionshipTable'
        db.delete_table(u'matches_championshiptable')

        # Deleting model 'Player'
        db.delete_table(u'matches_player')

        # Deleting model 'PlayerHistory'
        db.delete_table(u'matches_playerhistory')

        # Deleting model 'TeamPlayer'
        db.delete_table(u'matches_teamplayer')

        # Deleting model 'Stadium'
        db.delete_table(u'matches_stadium')

        # Deleting model 'Match'
        db.delete_table(u'matches_match')

        # Deleting model 'MatchPlayer'
        db.delete_table(u'matches_matchplayer')

        # Deleting model 'Goal'
        db.delete_table(u'matches_goal')

        # Deleting model 'MatchSubstitution'
        db.delete_table(u'matches_matchsubstitution')


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
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Team']"})
        },
        u'matches.concretechampionship': {
            'Meta': {'object_name': 'ConcreteChampionship'},
            'champion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'champion'", 'null': 'True', 'to': u"orm['matches.Team']"}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Championship']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['matches.Team']", 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Season']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'matches.concreteteam': {
            'Meta': {'object_name': 'ConcreteTeam'},
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
            'scored_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.TeamPlayer']"})
        },
        u'matches.match': {
            'Meta': {'object_name': 'Match'},
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"}),
            'away_team_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteChampionship']"}),
            'championshipPhase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ChampionshipPhase']", 'null': 'True', 'blank': 'True'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_team'", 'to': u"orm['matches.ConcreteTeam']"}),
            'home_team_goals': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'phaseGroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.PhaseGroup']", 'null': 'True', 'blank': 'True'}),
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
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.TeamPlayer']"}),
            'red_card': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'second_card_or_red_card_minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'second_yellow_card': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'substitute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            't_shirt': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ConcreteTeam']"})
        },
        u'matches.matchsubstitution': {
            'Meta': {'object_name': 'MatchSubstitution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Match']"}),
            'minute': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_in': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_in'", 'to': u"orm['matches.MatchPlayer']"}),
            'player_out': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_out'", 'to': u"orm['matches.MatchPlayer']"})
        },
        u'matches.phasegroup': {
            'Meta': {'object_name': 'PhaseGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['matches.Team']", 'null': 'True', 'blank': 'True'}),
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.ChampionshipPhase']"})
        },
        u'matches.player': {
            'Meta': {'object_name': 'Player'},
            'birth_city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities.City']", 'null': 'True', 'blank': 'True'}),
            'current_team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Team']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'matches.playerhistory': {
            'Meta': {'object_name': 'PlayerHistory'},
            'from_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matches.Team']"}),
            'to_date': ('django.db.models.fields.DateField', [], {})
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