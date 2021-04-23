from django.urls import path, re_path
from stock_sentiment import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    #re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('test/',views.test , name='test'),
    path('delete_pic/',views.delete_profile_pic , name='delete_pic'),
    path('fetch_graph_data/',views.fetch_graph_data , name='fetch_graph_data'),
    path('search/',views.search_result , name='search_result'),

]