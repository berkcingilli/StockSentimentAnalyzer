from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
import re
from textblob.tokenizers import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
from .models import *
import datetime
from html.parser import HTMLParser
from django.http import JsonResponse
from django.db.models import Q
import pandas as pd
from scipy.stats.stats import pearsonr
from django.core import serializers
import random
# Create your views here.
stopwords = ['her', 'during', 'among', 'thereafter', 'only', 'hers', 'in', 'none', 'with', 'un', 'put', 'hence', 'each',
             'would', 'have', 'to', 'itself', 'that', 'seeming', 'hereupon', 'someone', 'eight', 'she', 'forty', 'much',
             'throughout', 'less', 'was', 'interest', 'elsewhere', 'already', 'whatever', 'or', 'seem', 'fire',
             'however',
             'keep', 'detail', 'both', 'yourselves', 'indeed', 'enough', 'too', 'us', 'wherein', 'himself', 'behind',
             'everything',
             'part', 'made', 'thereupon', 'for', 'nor', 'before', 'front', 'sincere', 'really', 'than', 'alone',
             'doing', 'amongst',
             'across', 'him', 'another', 'some', 'whoever', 'four', 'other', 'latterly', 'off', 'sometime', 'above',
             'often', 'herein',
             'am', 'whereby', 'although', 'who', 'should', 'amount', 'anyway', 'else', 'upon', 'this', 'when', 'we',
             'few', 'anywhere',
             'will', 'though', 'being', 'fill', 'used', 'full', 'thru', 'call', 'whereafter', 'various', 'has', 'same',
             'former', 'whereas',
             'what', 'had', 'mostly', 'onto', 'go', 'could', 'yourself', 'meanwhile', 'beyond', 'beside', 'ours',
             'side', 'our', 'five',
             'nobody', 'herself', 'is', 'ever', 'they', 'here', 'eleven', 'fifty', 'therefore', 'nothing', 'not',
             'mill', 'without',
             'whence', 'get', 'whither', 'then', 'no', 'own', 'many', 'anything', 'etc', 'make', 'from', 'against',
             'ltd', 'next',
             'afterwards', 'unless', 'while', 'thin', 'beforehand', 'by', 'amoungst', 'you', 'third', 'as', 'those',
             'done',
             'becoming', 'say', 'either', 'doesn', 'twenty', 'his', 'yet', 'latter', 'somehow', 'are', 'these', 'mine',
             'under',
             'take', 'whose', 'others', 'over', 'perhaps', 'thence', 'does', 'where', 'two', 'always', 'your',
             'wherever', 'became',
             'which', 'about', 'but', 'towards', 'still', 'rather', 'quite', 'whether', 'somewhere', 'might', 'do',
             'bottom',
             'until', 'km', 'yours', 'serious', 'find', 'please', 'hasnt', 'otherwise', 'six', 'toward', 'sometimes',
             'of',
             'fifteen', 'eg', 'just', 'a', 'me', 'describe', 'why', 'an', 'and', 'may', 'within', 'kg', 'con', 're',
             'nevertheless',
             'through', 'very', 'anyhow', 'down', 'nowhere', 'now', 'it', 'cant', 'de', 'move', 'hereby', 'how',
             'found', 'whom',
             'were', 'together', 'again', 'moreover', 'first', 'never', 'below', 'between', 'computer', 'ten', 'into',
             'see',
             'everywhere', 'there', 'neither', 'every', 'couldnt', 'up', 'several', 'the', 'i', 'becomes', 'don', 'ie',
             'been',
             'whereupon', 'seemed', 'most', 'noone', 'whole', 'must', 'cannot', 'per', 'my', 'thereby', 'so', 'he',
             'name', 'co',
             'its', 'everyone', 'if', 'become', 'thick', 'thus', 'regarding', 'didn', 'give', 'all', 'show', 'any',
             'using', 'on',
             'further', 'around', 'back', 'least', 'since', 'anyone', 'once', 'can', 'bill', 'hereafter', 'be', 'seems',
             'their',
             'myself', 'nine', 'also', 'system', 'at', 'more', 'out', 'twelve', 'therein', 'almost', 'except', 'last',
             'did',
             'something', 'besides', 'via', 'whenever', 'formerly', 'cry', 'one', 'hundred', 'sixty', 'after', 'well',
             'them',
             'namely', 'empty', 'three', 'even', 'along', 'because', 'ourselves', 'such', 'top', 'due', 'inc',
             'themselves']

sp_100 = ["BTC.X", "ETH.X","XRP.X","AAPL", "ABBV", "ABT", "SNDL","AMC", "AIG", "ALL", "AMGN", "AMT", "AMZN", "AXP", "BA", "BAC", "BIIB", "BK",
           "BKNG", "BLK", "BMY", "BRK.B", "C", "CAT", "CHTR", "CL", "CMCSA", "COF", "COP", "COST", "CRM", "CSCO", "CVS",
           "CVX",
           "DD", "DHR", "DIS", "DOW", "DUK", "EMR", "EXC", "F", "FB", "FDX", "GD", "GE", "GILD", "GM", "GOOG", "GOOGL",
           "GS",
           "HD", "HON", "IBM", "INTC",  "KHC", "KMI", "KO",  "LMT", "LOW", "MA", "MCD", "MDLZ",
           "MDT", "MET",
           "MMM", "MO", "MRK", "MS", "MSFT", "NEE", "NFLX", "NKE", "NVDA", "ORCL", "PEP", "PFE",  "PM", "PYPL",
           "QCOM", "RTX",
           "SBUX", "SLB", "SO", "SPG", "T", "TGT", "TMO", "TSLA", "TXN", "UNH", "UNP", "UPS", "USB", "V", "VZ", "WBA",
           "WFC", "WMT", "XOM"]

sp_100_yahoo_finance = ["BTC-USD","AAPL", "ETH-USD","XRP-USD", "ABBV", "ABT", "SNDL", "AMC", "AIG", "ALL", "AMGN", "AMT", "AMZN", "AXP", "BA", "BAC", "BIIB", "BK",
           "BKNG", "BLK", "BMY", "BRK-B", "C", "CAT", "CHTR", "CL", "CMCSA", "COF", "COP", "COST", "CRM", "CSCO", "CVS",
           "CVX",
           "DD", "DHR", "DIS", "DOW", "DUK", "EMR", "EXC", "F", "FB", "FDX", "GD", "GE", "GILD", "GM", "GOOG", "GOOGL",
           "GS",
           "HD", "HON", "IBM", "INTC",  "KHC", "KMI", "KO",  "LMT", "LOW", "MA", "MCD", "MDLZ",
           "MDT", "MET",
           "MMM", "MO", "MRK", "MS", "MSFT", "NEE", "NFLX", "NKE", "NVDA", "ORCL", "PEP", "PFE",  "PM", "PYPL",
           "QCOM", "RTX",
           "SBUX", "SLB", "SO", "SPG", "T", "TGT", "TMO", "TSLA", "TXN", "UNH", "UNP", "UPS", "USB", "V", "VZ", "WBA",
           "WFC", "WMT", "XOM"]

# AIG ,ALL , AMGN , AMT , AXP , BK , BKNG , BLK , CHTR , CL , CMCSA , COF , COP , DD , DHR , DOW , DUK , EMR ,
# EXC , GD , LOW , MDLZ , MDT  , MET  , NEE , SLB ,SO , TMO , TXN , UNP , USB
# 31 less occuring
def contain_num(string):

    return any(character.isdigit() for character in string)

def fetch_graph_data(request):
    print('fetch_graph_block ')
    data = json.loads(request.body)

    res = dict()
    ticker_id = data['ticker_id']
    check = contain_num(str(ticker_id))
    if check == True:
        ticker = Ticker.objects.get(id=int(ticker_id))
    else:
        ticker = Ticker.objects.get(ticker_name=ticker_id)

    #all comments for asked ticker is brought
    all_comments = ticker.comment_set.all()


    res['message'] = 'Deleted'

    # The dates fro x axis of the graph is been prepared
    list_of_all_dates = []
    with_neutral = all_comments.all()
    print('COUNT WITHOUT NATURAL',with_neutral.count())

    for item in with_neutral:
        list_of_all_dates.append(item.comment_date.strftime("%Y-%m-%d"))


    date_df = pd.Series(list_of_all_dates)

    unique_items = date_df.unique()
    unique_items.sort()

    # Comments starting from 1st april is gonna be selected
    first_april_date = 0

    for i in range(len(unique_items)):
        if unique_items[i] == '2021-04-01':
            first_april_date = i

    print('BBBBBBBBBBBBBBBBBBBB',unique_items[first_april_date:])
    unique_items = unique_items[first_april_date:]

    # X-axis for dates on chart is being finalized
    final_categories = []
    for item in unique_items:

        final_categories.append(datetime.datetime.strptime(item, '%Y-%m-%d').strftime('%d-%b-%y'))

    final_categories = final_categories
    print(final_categories[-11:])
    res['categories'] = final_categories
    res['ticker'] = ticker.ticker_name
    curr_day_overall_list = []
    curr_day_pos_list = []
    curr_day_neg_list = []
    total = 0

    # This part selects the comments for each day indivudally
    for item in unique_items:
        today_min = datetime.datetime.combine(datetime.datetime.strptime(item, '%Y-%m-%d'), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.datetime.strptime(item, '%Y-%m-%d'), datetime.time.max)

        curr_day_overall_count = comment.objects.filter(Q(label='pos') | Q(label='neg'), ticker_symbol=ticker.ticker_name,
                                                  comment_date__range=(today_min, today_max)).all().count()
        curr_day_pos_count = comment.objects.filter(label='pos', ticker_symbol=ticker.ticker_name,
                                              comment_date__range=(today_min, today_max)).all().count()
        curr_day_neg_count = comment.objects.filter(label='neg', ticker_symbol=ticker.ticker_name,
                                              comment_date__range=(today_min, today_max)).all().count()

        curr_day_overall = comment.objects.filter(Q(label='pos') | Q(label='neg'),ticker_symbol=ticker.ticker_name,
                                          comment_date__range=(today_min, today_max)).all()
        curr_day_pos = comment.objects.filter(label='pos', ticker_symbol=ticker.ticker_name,
                                                  comment_date__range=(today_min, today_max)).all()
        curr_day_neg = comment.objects.filter(label='neg', ticker_symbol=ticker.ticker_name,
                                                  comment_date__range=(today_min, today_max)).all()

        print('POS COUNT',curr_day_pos_count)
        print('NEG COUNT',curr_day_neg_count)

        # This part caculates the averages of the positive, negative and neutral scores.
        for elem in curr_day_overall:
            total += elem.compound

        if curr_day_overall_count != 0:
            curr_day_overall_list.append(total/curr_day_overall_count)
        else:
            curr_day_overall_list.append(0)

        total = 0

        for elem in curr_day_pos:
            total += elem.compound

        if curr_day_pos_count != 0:
            curr_day_pos_list.append(total / curr_day_pos_count)
        else:
            curr_day_pos_list.append(0)

        total = 0

        for elem in curr_day_neg:
            total += elem.compound

        if curr_day_neg_count != 0:
            curr_day_neg_list.append(total / curr_day_neg_count)
        else:
            curr_day_neg_list.append(0)

        total = 0




    res['pos'] = curr_day_pos_list
    res['neg'] = curr_day_neg_list
    res['overall'] = curr_day_overall_list

    # get stock price data
    today_sentiment_count = comment.objects.filter(ticker_symbol=ticker.ticker_name,
                                                   comment_date__range=[str(datetime.date.today()), str(
                                                       datetime.date.today() + datetime.timedelta(days=1))]).count()

    # Cryptocurrencies returns different number of prices than regular stocks if else conditionals is used to handle this
    # FINHUB API is  consumed
    if ticker.ticker_name == 'BTC.X':
        print('bitcoin block entered')
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[0], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get(
            'https://finnhub.io/api/v1/crypto/candle?symbol={0}&resolution=D&from={1}&to={2}&token=c2059ml37jksha791qog'.format('BINANCE:BTCUSDT',
                int(inital_date), int(end_date)))
        result = r.json()
        result = result['c']

        res['price'] = result
    elif ticker.ticker_name == 'ETH.X':
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[0], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get(
            'https://finnhub.io/api/v1/crypto/candle?symbol={0}&resolution=D&from={1}&to={2}&token=c2059ml37jksha791qog'.format('BINANCE:ETHUSDT',
                int(inital_date), int(end_date)))
        result = r.json()
        result = result['c']
        res['price'] = result
    elif ticker.ticker_name == 'XRP.X':
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[0], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get(
            'https://finnhub.io/api/v1/crypto/candle?symbol={0}&resolution=D&from={1}&to={2}&token=c2059ml37jksha791qog'.format('BINANCE:XRPUSDT',
                int(inital_date), int(end_date)))
        result = r.json()
        result = result['c']
        res['price'] = result
    else:
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[1], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol={0}&resolution=D&from={1}&to={2}&token=c2059ml37jksha791qog'.format(ticker.ticker_name,
                                                                                                                                         int(inital_date),int(end_date)))
        result = r.json()
        inital_prices = result['c']
        inital_dates = result['t']
        final_prices = []
        for i in range(len(inital_prices)):

            final_prices.append(inital_prices[i])
            if i != len(inital_prices)-1:

                diff_days = diff_day_number(str(datetime.datetime.fromtimestamp(inital_dates[i]).date()),str(datetime.datetime.fromtimestamp(inital_dates[i+1]).date()))

                if diff_days == 1:
                    continue
                for j in range(diff_days-1):
                    final_prices.append(inital_prices[i])



        res['price'] = final_prices



    print('categories', final_categories, len(final_categories))
    print('OVERALL', curr_day_overall_list, len(curr_day_overall_list))
    print('stock price', result, len(result))
    print('POS', curr_day_pos_list, len(curr_day_pos_list))
    print('NEG', curr_day_neg_list, len(curr_day_neg_list))

    # HERE counts for Pie Chart is been gathered from database
    positive_count = ticker.comment_set.filter(label='pos').count()
    negative_count = ticker.comment_set.filter(label='neg').count()
    neutral_count = ticker.comment_set.filter(label='neu').count()

    res['pos_count'] = positive_count
    res['neg_count'] = negative_count
    res['neu_count'] = neutral_count


    copy_final_price = res['price']

    derivative_stock_price = []

    # Here daily stock price difference have been derived
    for i in range(len(copy_final_price)):
        if i != len(copy_final_price) - 1:
            derivative_stock_price.append(copy_final_price[i+1]-copy_final_price[i])
        else:
            break



    # Current day is discarded for Correlation graph
    temp_curr_overall = curr_day_overall_list[:-1]
    curr_day_overall_list_normalized = []

    # Equalizing the overall sentiment score and Daily price difference
    temp_final_price = res['price']
    if len(derivative_stock_price) != len(temp_curr_overall):
        still_diff = abs(len(derivative_stock_price)-len(temp_curr_overall))
        for count in range(still_diff):

            derivative_stock_price.append(0.0)
            temp_final_price.append(temp_final_price[-1])

    res['price'] = temp_final_price

    # Min-max normalization for daily price difference and overall sentiment
    dmin, dmax = min(derivative_stock_price), max(derivative_stock_price)
    for i, val in enumerate(derivative_stock_price):
        derivative_stock_price[i] = (val - dmin) / (dmax - dmin)

    omin, omax = min(temp_curr_overall), max(temp_curr_overall)
    for i, val in enumerate(temp_curr_overall):
        curr_day_overall_list_normalized.append((val - omin) / (omax - omin))




    print('OVERALL normalized', curr_day_overall_list_normalized, len(curr_day_overall_list_normalized))
    print('Derivative stock price normalized', derivative_stock_price, len(derivative_stock_price))

    # Adding correlation values to the response object
    res['derivative_norm_price'] = derivative_stock_price
    res['overall_norm_price'] = curr_day_overall_list_normalized

    # Checking if there is an issue on correlation chart and overall strucutre
    try:
        correlation = pearsonr(derivative_stock_price,curr_day_overall_list_normalized)
        res['corr'] = correlation[0]
    except:
        return JsonResponse({'exception':'corr'})


    # Return latest 20 sentiment.

    list_of_all_dates_time = []
    counter = 0
    counter1 = 0
    for item in with_neutral.filter(site_name='Stocktwits').all().order_by('-id')[:25]:
        list_of_all_dates_time.append(item)
        counter += 1
        if counter == 10:
            break

    for item in with_neutral.filter(site_name='Yahoo Finance').all().order_by('-id')[:25]:
        list_of_all_dates_time.append(item)
        counter1 += 1
        if counter1 == 10:
            break

    random.shuffle(list_of_all_dates_time)

    data = serializers.serialize('json', list_of_all_dates_time)

    res['test'] = data


    return JsonResponse(res)


def diff_day_number(day1, day2):
    day1 = datetime.datetime.strptime(day1, "%Y-%m-%d")
    day2 = datetime.datetime.strptime(day2, "%Y-%m-%d")

    return abs((day2 - day1).days)







def index(request):
    tickers = Ticker.objects.all()


    return render(request, "stock_sentiment/index.html",{'ticker':tickers})






def get_sentiment(request):
    vader_analyzer = SentimentIntensityAnalyzer()

    counter = 0

    for ticker in sp_100:
        try:
            example = 'https://api.stocktwits.com/api/2/streams/symbol/{0}.json'.format(ticker)

            response = requests.get(example)

            json_stocktwits = json.loads(response.content)

            for item in json_stocktwits['messages']:



                current_item = HTMLParser().unescape(item['body'])
                if not comment.objects.filter(original_comment=current_item).exists():
                    # removing ticker symbols like $AAPL
                    for i in current_item.split("\n"):
                        example = re.findall(r'[$][A-Za-z][\S]*', str(i))
                        print('QQQQQQQQQQQQQQQQQQQ', example)
                        if example != []:
                            break

                    # print(example)
                    new_current = current_item
                    for elem in example:
                        # print('HERE',elem)
                        new_current = new_current.replace(str(elem), "")

                    # print('HERE',new_current)

                    # remove URL links
                    new_current = re.sub('https?://[A-Za-z0-9./]+', '', new_current)

                    new_current = re.sub('www?\.[A-Za-z0-9./]+', '', new_current)
                    # removing mentions @
                    new_current = re.sub(r'@[A-Za-z0-9]+', '', new_current)

                    # removing hastags
                    new_current = re.sub("/#\w+\s*/", " ", new_current)

                    # removing numbers
                    new_current = re.sub("\d+", " ", new_current)

                    # remove stopwords
                    new_current_tokenized = word_tokenize(new_current)

                    new_current_no_sw = [word for word in new_current_tokenized if not word in stopwords]

                    final_str = ""
                    for element in new_current_no_sw:
                        final_str += " " + element

                    vader_score = vader_analyzer.polarity_scores(final_str)

                    # classify the comment
                    if vader_score['compound'] > -0.05 and vader_score['compound'] < 0.05:
                        label = 'neu'
                    elif vader_score['compound'] > 0.05:
                        label = 'pos'
                    else:
                        label = 'neg'

                    selected_ticker = Ticker.objects.get(ticker_name=ticker)
                    created = comment.objects.create(
                        site_name='Stocktwits',
                        ticker_symbol=ticker,
                        original_comment=current_item,
                        pre_processed_comment=final_str,
                        comment_date=item['created_at'],
                        pos=vader_score['pos'],
                        neu=vader_score['neu'],
                        neg=vader_score['neg'],
                        compound=vader_score['compound'],
                        label=label,
                        ticker=selected_ticker

                    )
                    print(
                        f"{created.site_name}, {created.ticker_symbol}, {created.original_comment}, {created.pre_processed_comment}, {created.pos}, {created.neu}, {created.compound}, {created.label}")




        except Exception as e:
            Exceptions.objects.create(exception=e, extra_info=ticker, time_happened=datetime.datetime.now())




    # Yahoo finance scraping part

    for ticker in sp_100_yahoo_finance:
        try:

            URL = 'https://uk.finance.yahoo.com/quote/{0}/community?p={1}'.format(ticker, ticker)
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, 'html.parser')

            script = soup.find('script', text=re.compile('root\.App\.main'))

            json_text = re.search(r'^\s*root\.App\.main\s*=\s*({.*?})\s*;\s*$',
                                  script.string, flags=re.MULTILINE).group(1)

            data = json.loads(json_text)

            # print(data['context'])

            for messageid in \
                    data['context']['dispatcher']['stores']['CanvassStore']['comments']['canvass-0-CanvassApplet'][
                        'messageList']:
                prid = data['context']['dispatcher']['stores']['BeaconStore']['beaconConfig']['context']['prid']
                try:
                    print(
                        '---------------------------------COMMENTS-----------------------------------------------------\n')

                    message_created_comment = datetime.datetime.fromtimestamp(messageid['meta']['createdAt'])
                    #print(messageid['reactionStats']['upVoteCount'])
                    message_comment = messageid['details']['userText']

                    print(ticker, message_comment)
                    if not comment.objects.filter(original_comment=message_comment).exists():
                        # remove URL links
                        message_comment = re.sub('https?://[A-Za-z0-9./]+', '', message_comment)

                        message_comment = re.sub('www?\.[A-Za-z0-9./]+', '', message_comment)
                        # removing mentions @
                        message_comment = re.sub(r'@[A-Za-z0-9]+', '', message_comment)

                        # removing hastags
                        message_comment = re.sub("/#\w+\s*/", " ", message_comment)

                        # removing numbers
                        message_comment = re.sub("\d+", " ", message_comment)

                        # remove stopwords
                        new_current_tokenized = word_tokenize(message_comment)

                        new_current_no_sw = [word for word in new_current_tokenized if not word in stopwords]

                        final_str = ""
                        for element in new_current_no_sw:
                            final_str += " " + element

                        vader_score = vader_analyzer.polarity_scores(final_str)

                        # classify the comment
                        if vader_score['compound'] > -0.05 and vader_score['compound'] < 0.05:
                            label = 'neu'
                        elif vader_score['compound'] > 0.05:
                            label = 'pos'
                        else:
                            label = 'neg'

                        # make same ticker
                        temp = ''
                        # "BTC-USD", "ETH-USD","XRP-USD", BRK-B
                        if ticker == 'BTC-USD':
                            temp = "BTC.X"
                        elif ticker == 'ETH-USD':
                            temp = "ETH.X"
                        elif ticker == 'XRP-USD':
                            temp = "XRP.X"
                        elif ticker == 'BRK-B':
                            temp = "BRK.B"
                        else:
                            temp = ticker

                        selected_ticker1 = Ticker.objects.get(ticker_name=temp)
                        created = comment.objects.create(
                            site_name='Yahoo Finance',
                            ticker_symbol=temp,
                            original_comment=messageid['details']['userText'],
                            pre_processed_comment=final_str,
                            comment_date=message_created_comment,
                            pos=vader_score['pos'],
                            neu=vader_score['neu'],
                            neg=vader_score['neg'],
                            compound=vader_score['compound'],
                            label=label,
                            ticker=selected_ticker1

                        )
                        print(
                            f"{created.site_name}, {created.ticker_symbol}, {created.original_comment}, {created.pre_processed_comment}, {created.pos}, {created.neu}, {created.compound}, {created.label}")
                        # messageid['messageId'],messageid['reactionStats']['replyCount'])
                    print('---------------------------------REPLIES-----------------------------------------------------\n')
                    if messageid['reactionStats']['replyCount'] != 0:
                        URL2 = 'https://uk.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getReplies_ns;action=showNext;apiVersion=v1;context=' \
                               '{1};count=30;index=null;lang=en-GB;' \
                               'messageId={0};namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;region=GB;' \
                               'sortBy=createdAt;tags={3}?bkt=finance-GB-en-GB-def&device=desktop&ecma=modern&feature=canvassOffnet%2CccOnMute%2CdisableCommentsMessage%2Cdebouncesearch100%2CdeferDarla%2CecmaModern%2CemptyServiceWorker%2CenableCCPAFooter%2CenableCMP%2CenableConsentData%2CenableGuceJs%2CenableGuceJsOverlay%2CenableNavFeatureCue%2CenablePrivacyUpdate%2CenableStreamDebounce%2CenableTheming%2CenableUpgradeLeafPage%2CenableVideoDocking%2CenableVideoURL%2CenableYahooSans%2CenableYodleeErrorMsgCriOS%2CncpListStream%2CncpPortfolioStream%2CncpQspStream%2CncpStream%2CncpStreamIntl%2CncpTopicStream%2CnewContentAttribution%2CnewLogo%2CoathPlayer%2CrelatedVideoFeature%2CvideoNativePlaylist%2CsunsetMotif2%2CenableSingleRail%2CenhanceAddToWL%2Carticle2_csn%2CenableUserPrefAPI%2CenableStageAds%2CsponsoredAds&intl=uk&lang=en-GB' \
                               '&partner=none&prid={2}&region=GB&site=finance&tz=Europe%2FLondon&ver=0.102.4128&returnMeta=true'.format(
                            messageid['messageId'], messageid['contextId'], prid, ticker)
                        time.sleep(0.5)
                        response = requests.get(URL2)
                        current_replies = json.loads(response.content)
                        # print(current_replies)
                        for reply in current_replies['data']:
                            message = reply['details']['userText']
                            #print(reply['reactionStats']['upVoteCount'])

                            if not comment.objects.filter(original_comment=message).exists():
                                message_created = datetime.datetime.fromtimestamp(reply['meta']['createdAt'])

                                # remove URL links
                                message = re.sub('https?://[A-Za-z0-9./]+', '', message)

                                message = re.sub('www?\.[A-Za-z0-9./]+', '', message)
                                # removing mentions @
                                message = re.sub(r'@[A-Za-z0-9]+', '', message)

                                # removing hastags
                                message = re.sub("/#\w+\s*/", " ", message)

                                # removing numbers
                                message = re.sub("\d+", " ", message)

                                # remove stopwords
                                new_current_tokenized = word_tokenize(message)

                                new_current_no_sw = [word for word in new_current_tokenized if not word in stopwords]

                                final_str = ""
                                for element in new_current_no_sw:
                                    final_str += " " + element

                                vader_score = vader_analyzer.polarity_scores(final_str)

                                # classify the comment
                                if vader_score['compound'] > -0.05 and vader_score['compound'] < 0.05:
                                    label = 'neu'
                                elif vader_score['compound'] > 0.05:
                                    label = 'pos'
                                else:
                                    label = 'neg'

                                temp = ''
                                # "BTC-USD", "ETH-USD","XRP-USD", BRK-B
                                if ticker == 'BTC-USD':
                                    temp = "BTC.X"
                                elif ticker == 'ETH-USD':
                                    temp = "ETH.X"
                                elif ticker == 'XRP-USD':
                                    temp = "XRP.X"
                                elif ticker == 'BRK-B':
                                    temp = "BRK.B"
                                else:
                                    temp = ticker

                                selected_ticker2 = Ticker.objects.get(ticker_name=temp)
                                created = comment.objects.create(
                                    site_name='Yahoo Finance',
                                    ticker_symbol=temp,
                                    original_comment=reply['details']['userText'],
                                    pre_processed_comment=final_str,
                                    comment_date=message_created,
                                    pos=vader_score['pos'],
                                    neu=vader_score['neu'],
                                    neg=vader_score['neg'],
                                    compound=vader_score['compound'],
                                    label=label,
                                    ticker=selected_ticker2

                                )
                                print(
                                    f"{created.site_name}, {created.ticker_symbol}, {created.original_comment}, {created.pre_processed_comment}, {created.pos}, {created.neu}, {created.compound}, {created.label}")

                except Exception as e:
                    Exceptions.objects.create(exception=e, extra_info=ticker, time_happened=datetime.datetime.now())
            time.sleep(7)
        except Exception as e:
            Exceptions.objects.create(exception=e, extra_info=ticker, time_happened=datetime.datetime.now())



    return render(request, "stock_sentiment/index.html")


def test_endpoint(request):
    tickers = Ticker.objects.all()
    exception_ticker = []
    for ticker in tickers:
        print(ticker.ticker_name)
        time.sleep(6)
        result = test_fetch_graph_data(ticker.ticker_name)
        if 'exception' in result:
            exception_ticker.append(ticker.ticker_name)



    for item in exception_ticker:
        temp = comment.objects.filter(ticker_symbol=item,comment_date__range=["2021-03-31", "2021-05-01"])
        print(item,temp.count())
        for elem in temp:
            print(elem.comment_date,elem.original_comment,elem.compound,elem.label)

    print(exception_ticker)
    return render(request, "stock_sentiment/index.html",{'ticker':tickers})


def test_fetch_graph_data(ticker_id):
    # This method is almost identical to the fetch_graph_data () except that it is been used for def test_endpoint () only
    res = dict()

    check = contain_num(str(ticker_id))
    if check == True:
        ticker = Ticker.objects.get(id=int(ticker_id))
    else:
        ticker = Ticker.objects.get(ticker_name=ticker_id)

    print(ticker)
    all_comments = ticker.comment_set.all()



    res['message'] = 'Deleted'

    list_of_all_dates = []
    with_neutral = all_comments.all()


    for item in with_neutral:
        list_of_all_dates.append(item.comment_date.strftime("%Y-%m-%d"))

    date_df = pd.Series(list_of_all_dates)

    unique_items = date_df.unique()
    unique_items.sort()

    first_april_date = 0

    for i in range(len(unique_items)):
        if unique_items[i] == '2021-04-01':
            first_april_date = i


    unique_items = unique_items[first_april_date:]

    final_categories = []
    for item in unique_items:
        final_categories.append(datetime.datetime.strptime(item, '%Y-%m-%d').strftime('%d-%b-%y'))

    final_categories = final_categories

    res['categories'] = final_categories
    res['ticker'] = ticker.ticker_name
    curr_day_overall_list = []
    curr_day_pos_list = []
    curr_day_neg_list = []
    total = 0

    for item in unique_items:
        today_min = datetime.datetime.combine(datetime.datetime.strptime(item, '%Y-%m-%d'), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.datetime.strptime(item, '%Y-%m-%d'), datetime.time.max)

        curr_day_overall_count = comment.objects.filter(Q(label='pos') | Q(label='neg'),
                                                        ticker_symbol=ticker.ticker_name,
                                                        comment_date__range=(today_min, today_max)).all().count()
        curr_day_pos_count = comment.objects.filter(label='pos', ticker_symbol=ticker.ticker_name,
                                                    comment_date__range=(today_min, today_max)).all().count()
        curr_day_neg_count = comment.objects.filter(label='neg', ticker_symbol=ticker.ticker_name,
                                                    comment_date__range=(today_min, today_max)).all().count()

        curr_day_overall = comment.objects.filter(Q(label='pos') | Q(label='neg'), ticker_symbol=ticker.ticker_name,
                                                  comment_date__range=(today_min, today_max)).all()
        curr_day_pos = comment.objects.filter(label='pos', ticker_symbol=ticker.ticker_name,
                                              comment_date__range=(today_min, today_max)).all()
        curr_day_neg = comment.objects.filter(label='neg', ticker_symbol=ticker.ticker_name,
                                              comment_date__range=(today_min, today_max)).all()

        print('POS COUNT', curr_day_pos_count)
        print('NEG COUNT', curr_day_neg_count)

        for elem in curr_day_overall:
            total += elem.compound

        if curr_day_overall_count != 0:
            curr_day_overall_list.append(total / curr_day_overall_count)
        else:
            curr_day_overall_list.append(0)

        total = 0

        for elem in curr_day_pos:
            total += elem.compound

        if curr_day_pos_count != 0:
            curr_day_pos_list.append(total / curr_day_pos_count)
        else:
            curr_day_pos_list.append(0)

        total = 0

        for elem in curr_day_neg:
            total += elem.compound

        if curr_day_neg_count != 0:
            curr_day_neg_list.append(total / curr_day_neg_count)
        else:
            curr_day_neg_list.append(0)

        total = 0

    res['pos'] = curr_day_pos_list
    res['neg'] = curr_day_neg_list
    res['overall'] = curr_day_overall_list

    # get stock price data
    today_sentiment_count = comment.objects.filter(ticker_symbol=ticker.ticker_name,
                                                   comment_date__range=[str(datetime.date.today()), str(
                                                       datetime.date.today() + datetime.timedelta(days=1))]).count()

    if ticker.ticker_name == 'BTC.X':
        print('bitcoin block entered')
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[0], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get(
            'https://finnhub.io/api/v1/crypto/candle?symbol={0}&resolution=D&from={1}&to={2}&token=sandbox_c0mrupn48v6tkq13hgog'.format(
                'BINANCE:BTCUSDT',
                int(inital_date), int(end_date)))
        result = r.json()
        result = result['c']

        res['price'] = result
    elif ticker.ticker_name == 'ETH.X':
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[0], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get(
            'https://finnhub.io/api/v1/crypto/candle?symbol={0}&resolution=D&from={1}&to={2}&token=sandbox_c0mrupn48v6tkq13hgog'.format(
                'BINANCE:ETHUSDT',
                int(inital_date), int(end_date)))
        result = r.json()
        result = result['c']
        res['price'] = result
    elif ticker.ticker_name == 'XRP.X':
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[0], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get(
            'https://finnhub.io/api/v1/crypto/candle?symbol={0}&resolution=D&from={1}&to={2}&token=sandbox_c0mrupn48v6tkq13hgog'.format(
                'BINANCE:XRPUSDT',
                int(inital_date), int(end_date)))
        result = r.json()
        result = result['c']
        res['price'] = result
    else:
        inital_date = time.mktime(datetime.datetime.strptime(unique_items[1], "%Y-%m-%d").timetuple())
        if today_sentiment_count == 0:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").timetuple())
        else:
            end_date = time.mktime(datetime.datetime.strptime(str(datetime.date.today() + datetime.timedelta(days=1)),
                                                              "%Y-%m-%d").timetuple())

        r = requests.get(
            'https://finnhub.io/api/v1/stock/candle?symbol={0}&resolution=D&from={1}&to={2}&token=sandbox_c0mrupn48v6tkq13hgog'.format(
                ticker.ticker_name,
                int(inital_date), int(end_date)))
        result = r.json()
        inital_prices = result['c']
        inital_dates = result['t']
        final_prices = []
        for i in range(len(inital_prices)):
            print('Inital block', final_prices)
            final_prices.append(inital_prices[i])
            if i != len(inital_prices) - 1:
                # print(datetime.datetime.fromtimestamp(inital_dates[i]).date(),type(datetime.datetime.fromtimestamp(inital_dates[i])))
                diff_days = diff_day_number(str(datetime.datetime.fromtimestamp(inital_dates[i]).date()),
                                            str(datetime.datetime.fromtimestamp(inital_dates[i + 1]).date()))

                if diff_days == 1:
                    continue
                for j in range(diff_days - 1):
                    final_prices.append(inital_prices[i])



        res['price'] = final_prices



    positive_count = ticker.comment_set.filter(label='pos').count()
    negative_count = ticker.comment_set.filter(label='neg').count()
    neutral_count = ticker.comment_set.filter(label='neu').count()

    res['pos_count'] = positive_count
    res['neg_count'] = negative_count
    res['neu_count'] = neutral_count


    copy_final_price = res['price']

    derivative_stock_price = []

    for i in range(len(copy_final_price)):
        if i != len(copy_final_price) - 1:
            derivative_stock_price.append(copy_final_price[i + 1] - copy_final_price[i])
        else:
            break



    temp_curr_overall = curr_day_overall_list[:-1]
    curr_day_overall_list_normalized = []

    temp_final_price = res['price']
    if len(derivative_stock_price) != len(temp_curr_overall):
        still_diff = abs(len(derivative_stock_price) - len(temp_curr_overall))
        for count in range(still_diff):
            print(1)
            derivative_stock_price.append(0.0)
            temp_final_price.append(temp_final_price[-1])

    res['price'] = temp_final_price

    dmin, dmax = min(derivative_stock_price), max(derivative_stock_price)
    for i, val in enumerate(derivative_stock_price):
        derivative_stock_price[i] = (val - dmin) / (dmax - dmin)

    omin, omax = min(temp_curr_overall), max(temp_curr_overall)
    for i, val in enumerate(temp_curr_overall):
        curr_day_overall_list_normalized.append((val - omin) / (omax - omin))


    print('OVERALL', temp_curr_overall, len(temp_curr_overall))
    print('OVERALL normalized', curr_day_overall_list_normalized, len(curr_day_overall_list_normalized))
    print('DERIVATIVE stock price', derivative_stock_price, len(derivative_stock_price))
    print('Derivative stock price normalized', derivative_stock_price, len(derivative_stock_price))


    res['derivative_norm_price'] = derivative_stock_price
    res['overall_norm_price'] = curr_day_overall_list_normalized

    try:
        correlation = pearsonr(derivative_stock_price, curr_day_overall_list_normalized)

        res['corr'] = correlation[0]
    except:
        res['exception'] = 'corr'

    # Return latest 20 sentiment.

    list_of_all_dates_time = []
    counter = 0
    counter1 = 0
    for item in with_neutral.filter(site_name='Stocktwits').all().order_by('-id')[:25]:
        list_of_all_dates_time.append(item)
        counter += 1
        if counter == 10:
            break

    for item in with_neutral.filter(site_name='Yahoo Finance').all().order_by('-id')[:25]:
        list_of_all_dates_time.append(item)
        counter1 += 1
        if counter1 == 10:
            break

    random.shuffle(list_of_all_dates_time)
    # print('lankirr',type(list_of_all_dates_time))
    data = serializers.serialize('json', list_of_all_dates_time)
    # print('lankirr',type(data),data)
    res['test'] = data

    return res


