from django.conf.urls import patterns, url

from matches import views

urlpatterns = patterns('',
    url(r'searchForm/?$', views.search_form, name='search_form'),
    url(r'searchComponent/year/?$', views.search_component_year, name='search_component_year'),
    url(r'searchComponent/team/?$', views.search_component_team, name='search_component_team'),
    url(r'searchComponent/championship/?$', views.search_component_championship, name='search_component_championship'),
    url(r'search/?$', views.search, name='search'),
    url(r'search/(?P<page>[0-9]*)?/?$', views.search, name='search_pagination'),
    url(r'details/([0-9]+)/?$', views.details, name='details'),
    url(r'stadiums_nearby/?$', views.stadiums_nearby, name='stadiums_nearby'),
    url(r'stadium_matches/?$', views.stadium_matches, name='stadium_matches'),
    url(r'importer/?$', views.importer, name='importer'),
    url(r'importer/upload?$', views.upload_zip, name='upload_zip'),
    url(r'importer/status?$', views.import_status, name='importer_status')    
        
)
