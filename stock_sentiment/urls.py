from django.urls import path
from stock_sentiment import views

urlpatterns = [

    # you can check views.py for which view is going to be run
    path('', views.index, name='home'),
    path('get_sentiment/',views.get_sentiment, name='get_sentiment'),
    path('fetch_graph_data/',views.fetch_graph_data , name='fetch_graph_data'),
    path('test_endpoint/',views.test_endpoint , name='test_endpoint'),

]