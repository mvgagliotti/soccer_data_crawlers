# coding=UTF-8
from django.contrib import admin
from matches.models import ConcreteTeam, TeamPlayer, Team, Player, Season, Match,\
    MatchPlayer, Stadium, Championship, Goal, ConcreteChampionship, Coach,\
    Referee, MatchSubstitution, ChampionshipPhase, PhaseGroup
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline
from ajax_select import make_ajax_form


'''
Estádio
'''

class StadiumAdmin(AjaxSelectAdmin):
    model = Stadium
    form = make_ajax_form(Stadium, {"city":"city"})

'''
Jogador
'''
class PlayerAdmin(AjaxSelectAdmin):
    model = Player
    form = make_ajax_form(Player,
      {
        "birth_city":"city",
        "current_team":"concreteteam",
        "country_of_birth":"country",
        "second_nationality":"country",
    })

'''
Técnico
'''
class CoachAdmin(AjaxSelectAdmin):
    model = Coach
    form = make_ajax_form(Coach, {"country_of_birth":"country"})

'''
Árbitro
'''
class RefereeAdmin(AjaxSelectAdmin):
    model = Referee
    form = make_ajax_form(Coach, {"country_of_birth":"country"})

'''
Equipes
'''

class PlayerInLine(AjaxSelectAdminTabularInline):
    model = TeamPlayer
    extra = 11
    form = make_ajax_form(TeamPlayer, {"player":"player"})

class TitularesPlayersInLine(PlayerInLine):
    verbose_name_plural = "Titulares"

    def get_queryset(self, request):
        return PlayerInLine.get_queryset(self, request).filter(substitute=False)

    def get_formset(self, request, obj=None, **kwargs):
        fs =  PlayerInLine.get_formset(self, request, obj=obj, **kwargs)
        fs.form.base_fields['substitute'].initial = False
        return fs


class ReservasPlayersInLine(PlayerInLine):
    verbose_name_plural = "Reservas"

    def get_queryset(self, request):
        return PlayerInLine.get_queryset(self, request).filter(substitute=True)

    def get_formset(self, request, obj=None, **kwargs):
        '''
        sobrescrevendo para setar atributos iniciais do formulário
        '''
        fs = super(ReservasPlayersInLine, self).get_formset(request, obj, **kwargs)
        fs.form.base_fields['substitute'].initial = True
        return fs;

class ConcreteTeamAdmin(AjaxSelectAdmin):
    inlines = [TitularesPlayersInLine, ReservasPlayersInLine]
    form = make_ajax_form(ConcreteTeam,
        {"team":"team",
         "coach" : "coach",
        }
    )
    verbose_name = 'Equipe'
    verbose_name_plural = 'Equipes'

'''
 ***************************************** Campeonatos **********************************************
'''

class PhaseInline(AjaxSelectAdminTabularInline):
    '''
    Inline de fases de um campeonato
    '''
    model = ChampionshipPhase
    extra = 0

class ConcreteChampAdmin(AjaxSelectAdmin):
    model = ConcreteChampionship
    form = make_ajax_form(ConcreteChampionship, {
         "participants" : "concreteteam",
         "champion" : "concreteteam",
    })
    inlines = [PhaseInline]


class PhaseGroupInline(AjaxSelectAdminTabularInline):
    '''
    Grupos de uma fase
    '''
    model = PhaseGroup
    verbose_name_plural = "grupos"
    form = make_ajax_form(PhaseGroup, {"participants" : "concreteteam"})
    extra = 0

class ChampPhase(AjaxSelectAdmin):
    '''
    Fases de um campeonato
    '''
    model = ChampionshipPhase
    form = make_ajax_form(ChampionshipPhase,
                          {"championship":"concretechampionship"})

    inlines = [PhaseGroupInline]

'''
Partidas
'''
class GoalsInline(AjaxSelectAdminTabularInline):
    verbose_name_plural = "Gols marcados"
    model = Goal
    fields = ("scored_by", "in_favor_of_home_team", "auto_gol", "minute")
    extra = 0
    form = make_ajax_form(Goal, {"scored_by":"player"})

class MatchPlayerInline(AjaxSelectAdminTabularInline):
    fields = ("player","t_shirt", "substitute",
              "from_home_team", "first_yellow_card", "first_yellow_card_minute",
              "second_yellow_card", "red_card", "second_card_or_red_card_minute") #TODO: completar com outros campos
    model = MatchPlayer
    extra = 0
    form = make_ajax_form(MatchPlayer, {"player":"player"})

class SubstitutePlayerInLine(MatchPlayerInline):
    def get_formset(self, request, obj=None, **kwargs):
        '''
        sobrescrevendo para setar atributos iniciais do formulário
        '''
        fs = super(MatchPlayerInline, self).get_formset(request, obj, **kwargs)
        fs.form.base_fields['substitute'].initial = True
        return fs;

    def get_queryset(self, request):
        '''
        Filtrando os reservas
        '''
        return MatchPlayerInline.get_queryset(self, request).filter(substitute=True)

class HomeTeamMatchPlayerInline(MatchPlayerInline):
    verbose_name_plural = "Titulares do time mandante"
    def get_queryset(self, request):
        return MatchPlayerInline.get_queryset(self, request).filter(from_home_team=True, substitute=False)

class HomeTeamSubstituteMatchPlayerInline(SubstitutePlayerInLine):
    verbose_name_plural = "Reservas do time mandante"
    def get_queryset(self, request):
        return SubstitutePlayerInLine.get_queryset(self, request).filter(from_home_team=True)

class AwayTeamMatchPlayerInline(MatchPlayerInline):
    verbose_name_plural = "Titulares do time visitante"
    def get_queryset(self, request):
        return MatchPlayerInline.get_queryset(self, request).filter(from_home_team=False, substitute=False)

    def get_formset(self, request, obj=None, **kwargs):
        fs =  MatchPlayerInline.get_formset(self, request, obj=obj, **kwargs)
        fs.form.base_fields['from_home_team'].initial = False
        return fs

class AwayTeamSubstituteMatchPlayerInline(SubstitutePlayerInLine):
    verbose_name_plural = "Reservas do time visitante"
    def get_queryset(self, request):
        return SubstitutePlayerInLine.get_queryset(self, request).filter(from_home_team=False)

    def get_formset(self, request, obj=None, **kwargs):
        fs =  MatchPlayerInline.get_formset(self, request, obj=obj, **kwargs)
        fs.form.base_fields['from_home_team'].initial = False
        return fs

'''
Substituições
'''
class MatchSubstitutionInLine(AjaxSelectAdminTabularInline):
    model = MatchSubstitution
    extra = 0
    form = make_ajax_form(MatchSubstitution, {"player_in":"player", "player_out":"player"})

    def get_queryset(self, request):
        qs =  AjaxSelectAdminTabularInline.get_queryset(self, request)
        return qs;

class MatchSubstitutionFromHomeTeamInline(MatchSubstitutionInLine):
    verbose_name_plural = "Substituições do time mandante"

    def get_formset(self, request, obj=None, **kwargs):
        fs =  AjaxSelectAdminTabularInline.get_formset(self, request, obj=obj, **kwargs);
        fs.form.base_fields['from_home_team'].initial = True
        return fs;

    def get_queryset(self, request):
        return MatchSubstitutionInLine.get_queryset(self, request).filter(from_home_team=True)

class MatchSubstitutionFromAwayTeamInline(MatchSubstitutionInLine):
    verbose_name_plural = "Substituições do time visitante"

    def get_formset(self, request, obj=None, **kwargs):
        fs =  AjaxSelectAdminTabularInline.get_formset(self, request, obj=obj, **kwargs);
        fs.form.base_fields['from_home_team'].initial = False
        return fs;

    def get_queryset(self, request):
        return MatchSubstitutionInLine.get_queryset(self, request).filter(from_home_team=False)

'''
Partida
'''
class MatchAdmin(AjaxSelectAdmin):
    inlines = [GoalsInline, HomeTeamMatchPlayerInline,HomeTeamSubstituteMatchPlayerInline,
               AwayTeamMatchPlayerInline,AwayTeamSubstituteMatchPlayerInline,
               MatchSubstitutionFromHomeTeamInline,
               MatchSubstitutionFromAwayTeamInline]

    form = make_ajax_form(Match, {
       "stadium":"stadium",
       "home_team":"concreteteam",
       "away_team":"concreteteam",
       "championship" : "concretechampionship",
       "championshipPhase":"champphase",
       "phaseGroup":"phasegroup",
       "referee" : "referee",
       "home_team_coach" : "coach",
       "away_team_coach" : "coach",
    })

    def save_related(self, request, form, formsets, change):
        result = AjaxSelectAdmin.save_related(self, request, form, formsets, change)

        match = form.instance
        if (match.matchplayer_set.all().count() == 0):
            match.fill_players_from_home_team()
            match.fill_players_from_away_team()

        return result;

    def save_model(self, request, obj, form, change):
        saved = AjaxSelectAdmin.save_model(self, request, obj, form, change)
        return saved

    def save_formset(self, request, form, formset, change):

        instances = formset.save(commit=False)
        current_match = form.instance

        '''
        Precisei fazer este workaround, pra skipar o save_formset do AjaxSelectAdmin,
        pois ao remover gol ou jogador, ocorria um erro de validação meio sem sentido. Na falta
        de uma solução melhor, optei por não chamar o método da super-classe, visto que o objeto já é salvo mesmo nos outros casos.
        '''
        skip_superclass_save = formset.model == Goal or formset.model == MatchPlayer

        for instance in instances:

            '''
            setando a equipe dos MatchPlayers
            '''
            if isinstance(instance, MatchPlayer):

                if instance.from_home_team:
                    instance.team = current_match.home_team
                else:
                    instance.team = current_match.away_team

                instance.save()

            '''
            setando o ConcreteTeam em que foi atribuído o gol
            '''
            if isinstance(instance, Goal):

                instance.match = current_match

                if instance.in_favor_of_home_team:
                    instance.in_favor_of = form.instance.home_team
                else:
                    instance.in_favor_of = form.instance.away_team

                instance.save()
                skip_superclass_save = True

            '''
            Substituições
            '''
            if isinstance(instance, MatchSubstitution):
                pass
                        
        if not skip_superclass_save:                        
            return AjaxSelectAdmin.save_formset(self, request, form, formset, change)
        else:
            return

admin.site.register(ConcreteTeam, ConcreteTeamAdmin)
admin.site.register(Team)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Season)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Championship)
admin.site.register(ConcreteChampionship, ConcreteChampAdmin)
admin.site.register(ChampionshipPhase, ChampPhase)