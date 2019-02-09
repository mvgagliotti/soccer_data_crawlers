# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from matches.models import *
from django.contrib.contenttypes.models import ContentType
from django.db.models.aggregates import Count
import json
from django.db.models import Q
from django.db import connection
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
import logging
import os

from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Q
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from fut_friends import settings
from matches.form.upload_form import UploadFileForm
from matches.models import *
from fut_friends.common import JsonHelper
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from datetime import date, datetime


@staff_member_required
def importer(request):
    """
    Serve a tela de importação
    """    
    return render(request, 'matches/match_importer/importer.html')


@staff_member_required
def import_status(request):
    """
    Retorna o status da importação
    """
    _id = request.GET.get('id')
    
    importer_entry = MatchImporter.objects.filter(id=_id)[0]        
    json_result = {'id' : _id, 
                   'importedMatches' : importer_entry.imported_matches, 
                   'matchesToImport' : importer_entry.matchs_to_import,
                   'started' : not (importer_entry.start_time is None)
                   }    
    
    data = JsonHelper().to_json(json_result)    
    return HttpResponse(data, 'application/json')                        
    

@staff_member_required
def upload_zip(request):
    """
    Faz o upload do arquivo e gera uma entrada em MatchImporter
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            '''
            Salva entrada em MatchImporter
            '''
            import_entry = MatchImporter(filename=unicode(request.FILES['file'].name))
            import_entry.save()
            
            '''
            Salva o arquivo no caminho especificado no settings
            '''
            handle_uploaded_file(request.FILES['file'], settings.IMPORTER_PATH)
            
            '''
            Retornando json com importer_entry
            '''            
            json_result = {'id' : import_entry.id}
            data = JsonHelper().to_json(json_result)
            
            return HttpResponse(data, 'application/json')                        
            
        else:
            print "form inválido"
    else:
        #TODO: 
        form = UploadFileForm()


def handle_uploaded_file(f, path):
    '''
    Salva o arquivo "f" no caminho "path"
    '''
    with open(os.path.join(path, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def search_form(request):
    return render(request, 'matches/search_form.html')


def search_component_year(request):
    year = int(request.POST.get("q"))

    #Compreende todas as partidas a partir de 1900
    if year >= 190:
        response_data = []

        if year <= date.today().year:
            years = Match.objects.dates('match_date', 'year', order='DESC').filter(match_date__icontains=year, match_date__lt=datetime.now())

            x = 0
            for y in years:
                object_dir = {}
                object_dir['id'] = str(y.year)
                object_dir['text'] = str(y.year)
                response_data.insert(x, object_dir)
                x += 1

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return HttpResponse("Erro na solicitacao")


def search_component_team(request):
    team = str(request.POST.get("q"))

    if len(team) >= 3:

        teams = Team.objects.filter(short_name__icontains=str(team))

        response_data = []
        x = 0
        for t in teams:
            object_dir = {}
            object_dir['id'] = str(t.id)
            object_dir['text'] = u"" + t.short_name
            response_data.insert(x, object_dir)
            x += 1

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return HttpResponse("Erro na solicitacao")


def search_component_championship(request):
    championship = str(request.POST.get("q"))

    if len(championship) >= 3:

        championships = Championship.objects.filter(name__icontains=str(championship))

        response_data = []
        x = 0
        for t in championships:
            object_dir = {}
            object_dir['id'] = str(t.id)
            object_dir['text'] = u"" + t.name
            response_data.insert(x, object_dir)
            x += 1

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return HttpResponse("Erro na solicitacao")


def search(request, page=1):

    #request.session['matches_search'] = {}
    '''
    request.session['matches_search_search_year'] = 0
    request.session['matches_search_search_team'] = 0
    request.session['matches_search_search_championship'] = 0
    request.session['matches_search_search_team_name'] = ""
    request.session['matches_search_search_championship_name'] = ""
    '''


    if request.method == 'POST':
        if request.POST.get("match_date_year"):
            request.session['matches_search_search_year'] = int(request.POST.get("match_date_year"))
        else:
            request.session['matches_search_search_year'] = 0

        if request.POST.get("match_team"):
            request.session['matches_search_search_team'] = int(request.POST.get("match_team"))

            team = Team.objects.get(id=request.session['matches_search_search_team'])
            request.session['matches_search_search_team_name'] = team.short_name
        else:
            request.session['matches_search_search_team'] = 0
            request.session['matches_search_search_team_name'] = ""

        if request.POST.get("match_championship"):
            request.session['matches_search_search_championship'] = int(request.POST.get("match_championship"))

            championship = Championship.objects.get(id=request.session['matches_search_search_championship'])
            request.session['matches_search_search_championship_name'] = championship.name
        else:
            request.session['matches_search_search_championship'] = 0
            request.session['matches_search_search_championship_name'] = ""

    else:
        if request.GET.get("page"):
            page = int(request.GET.get("page"))

        if page <= 0:
            page = 1

    if request.session['matches_search_search_year'] > 0 or request.session['matches_search_search_team'] > 0 or request.session['matches_search_search_championship'] > 0:
        matches = Match.objects.select_related('championship', 'championship__championship', 'championship__season', 'home_team', 'home_team__team', 'away_team', 'away_team__team', 'stadium')
        matches = matches.order_by('-match_date')

        if request.session['matches_search_search_year'] > 0:
            matches = matches.filter(match_date__year=request.session['matches_search_search_year'])

        if request.session['matches_search_search_team'] > 0:
            matches = matches.filter(Q(home_team__team__id=request.session['matches_search_search_team']) | Q(away_team__team__id=request.session['matches_search_search_team']))

        if request.session['matches_search_search_championship'] > 0:
            matches = matches.filter(championship__championship=request.session['matches_search_search_championship'])

        matches.filter(match_date__lt=datetime.now())

        paginator = Paginator(matches, 20)

        matches = paginator.page(page)

        return render(request, 'matches/search_results.html',
                      {
                          'matches': matches,
                          'search_year': request.session['matches_search_search_year'],
                          'team_name': request.session['matches_search_search_team_name'],
                          'championship_name': request.session['matches_search_search_championship_name'],
                          'resultTotal': matches.paginator.count,
                          'paginator': paginator
                      }
        )

    return HttpResponse("No data")


def details(request, match_id):
    from profile.models import Friend

    if match_id > 0:

        match = Match.objects.filter(id=match_id)
        if len(match) == 1:
            match = match[0]
            if match.public_thread_id == 0:
                thread = Thread()
                thread.save()
                match.public_thread = thread
                match.save()

        match = get_object_or_404(Match.objects.select_related('championship', 'championship__championship', 'championship__season', 'home_team', 'home_team__team', 'away_team', 'away_team__team', 'stadium', 'public_thread'), id=match_id)
        existing_friends = Friend.objects.filter(user=request.user)

        friends_threads = UserThread.objects.filter(match=match, user_id__in=[x.friend.id for x in existing_friends])

        user_private_thread = UserThread.objects.filter(match=match, user=request.user).select_related('thread')
        if len(user_private_thread) == 0:
            ut = Thread()
            ut.save()

            user_private_thread = UserThread(match=match, thread=ut, user=request.user)
            user_private_thread.save()
        else:
            user_private_thread = user_private_thread[0]

        players = MatchPlayer.objects.filter(match=match).order_by('position', 'player__name')
        goals = Goal.objects.filter(match=match)
        substitutions = MatchSubstitution.objects.filter(match=match)

        return render(request, 'matches/match_detail.html', {
            'match': match,
            'players': players,
            'substitutions': substitutions,
            'goals': goals,
            'friends_threads': friends_threads,
            'user_private_thread': user_private_thread,
        })

    return HttpResponse("No data")


def stadiums_nearby(request):
    lat = float(request.POST.get("lat"))
    lng = float(request.POST.get("lng"))

    if lat == 0.0 or lng == 0.0:
        #Pega a lat/lng pelo IP

        '''
        from django.contrib.gis.geoip import GeoIP
        g = GeoIP()
        g.city(IP)
        '''



    stadiums = Stadium.objects.raw('''
    SELECT
        matches_stadium.*,
        (6371 * acos(cos(radians(%s)) * cos(radians(lat)) * cos(radians(lng) - radians(%s)) + sin(radians(%s)) * sin(radians(lat)))) AS distance
    FROM
        matches_stadium
    HAVING distance < 250
    ORDER BY distance
    LIMIT 0,15''', [str(lat), str(lng), str(lat)])

    response = {}
    stadiumsJson = []
    for s in stadiums:
        st = {}
        st['id'] = s.id
        st['short_name'] = s.short_name
        st['distance'] = str(int(s.distance))

        stadiumsJson.append(st)

    response['stadiums'] = stadiumsJson

    return HttpResponse(json.dumps(response), content_type="application/json")


def stadium_matches(request):
    stadium_id = int(request.POST.get("id"))

    if stadium_id > 0:

        #Pesquisa por data desabilitada para pesquisar todas as partidas
        matches = Match.objects.filter(stadium_id=stadium_id)[:10]


        response = {}
        matchesJson = []
        for m in matches:
            mt = {}
            mt['id'] = m.id
            mt['home_team'] = m.home_team.team.short_name
            mt['away_team'] = m.away_team.team.short_name
            mt['championship'] = m.championship.championship.name
            mt['season'] = m.championship.season.start_year

            matchesJson.append(mt)

        response['matches'] = matchesJson

        return HttpResponse(json.dumps(response), content_type="application/json")

    return HttpResponse("No data")
