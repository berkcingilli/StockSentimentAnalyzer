
## check readme.md uncomment this out only if you're in linux enviroment and to run background tasks.

# from bs4 import BeautifulSoup
# import requests
# import json
# import re
# from textblob.tokenizers import word_tokenize
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# import time
# from .models import *
# import datetime
# from html.parser import HTMLParser
#
# # Create your views here.
# stopwords = ['her', 'during', 'among', 'thereafter', 'only', 'hers', 'in', 'none', 'with', 'un', 'put', 'hence', 'each',
#              'would', 'have', 'to', 'itself', 'that', 'seeming', 'hereupon', 'someone', 'eight', 'she', 'forty', 'much',
#              'throughout', 'less', 'was', 'interest', 'elsewhere', 'already', 'whatever', 'or', 'seem', 'fire',
#              'however',
#              'keep', 'detail', 'both', 'yourselves', 'indeed', 'enough', 'too', 'us', 'wherein', 'himself', 'behind',
#              'everything',
#              'part', 'made', 'thereupon', 'for', 'nor', 'before', 'front', 'sincere', 'really', 'than', 'alone',
#              'doing', 'amongst',
#              'across', 'him', 'another', 'some', 'whoever', 'four', 'other', 'latterly', 'off', 'sometime', 'above',
#              'often', 'herein',
#              'am', 'whereby', 'although', 'who', 'should', 'amount', 'anyway', 'else', 'upon', 'this', 'when', 'we',
#              'few', 'anywhere',
#              'will', 'though', 'being', 'fill', 'used', 'full', 'thru', 'call', 'whereafter', 'various', 'has', 'same',
#              'former', 'whereas',
#              'what', 'had', 'mostly', 'onto', 'go', 'could', 'yourself', 'meanwhile', 'beyond', 'beside', 'ours',
#              'side', 'our', 'five',
#              'nobody', 'herself', 'is', 'ever', 'they', 'here', 'eleven', 'fifty', 'therefore', 'nothing', 'not',
#              'mill', 'without',
#              'whence', 'get', 'whither', 'then', 'no', 'own', 'many', 'anything', 'etc', 'make', 'from', 'against',
#              'ltd', 'next',
#              'afterwards', 'unless', 'while', 'thin', 'beforehand', 'by', 'amoungst', 'you', 'third', 'as', 'those',
#              'done',
#              'becoming', 'say', 'either', 'doesn', 'twenty', 'his', 'yet', 'latter', 'somehow', 'are', 'these', 'mine',
#              'under',
#              'take', 'whose', 'others', 'over', 'perhaps', 'thence', 'does', 'where', 'two', 'always', 'your',
#              'wherever', 'became',
#              'which', 'about', 'but', 'towards', 'still', 'rather', 'quite', 'whether', 'somewhere', 'might', 'do',
#              'bottom',
#              'until', 'km', 'yours', 'serious', 'find', 'please', 'hasnt', 'otherwise', 'six', 'toward', 'sometimes',
#              'of',
#              'fifteen', 'eg', 'just', 'a', 'me', 'describe', 'why', 'an', 'and', 'may', 'within', 'kg', 'con', 're',
#              'nevertheless',
#              'through', 'very', 'anyhow', 'down', 'nowhere', 'now', 'it', 'cant', 'de', 'move', 'hereby', 'how',
#              'found', 'whom',
#              'were', 'together', 'again', 'moreover', 'first', 'never', 'below', 'between', 'computer', 'ten', 'into',
#              'see',
#              'everywhere', 'there', 'neither', 'every', 'couldnt', 'up', 'several', 'the', 'i', 'becomes', 'don', 'ie',
#              'been',
#              'whereupon', 'seemed', 'most', 'noone', 'whole', 'must', 'cannot', 'per', 'my', 'thereby', 'so', 'he',
#              'name', 'co',
#              'its', 'everyone', 'if', 'become', 'thick', 'thus', 'regarding', 'didn', 'give', 'all', 'show', 'any',
#              'using', 'on',
#              'further', 'around', 'back', 'least', 'since', 'anyone', 'once', 'can', 'bill', 'hereafter', 'be', 'seems',
#              'their',
#              'myself', 'nine', 'also', 'system', 'at', 'more', 'out', 'twelve', 'therein', 'almost', 'except', 'last',
#              'did',
#              'something', 'besides', 'via', 'whenever', 'formerly', 'cry', 'one', 'hundred', 'sixty', 'after', 'well',
#              'them',
#              'namely', 'empty', 'three', 'even', 'along', 'because', 'ourselves', 'such', 'top', 'due', 'inc',
#              'themselves']
#
# sp_100 = ["BTC.X", "ETH.X","XRP.X","AAPL", "ABBV", "ABT", "SNDL","AMC", "AIG", "ALL", "AMGN", "AMT", "AMZN", "AXP", "BA", "BAC", "BIIB", "BK",
#            "BKNG", "BLK", "BMY", "BRK.B", "C", "CAT", "CHTR", "CL", "CMCSA", "COF", "COP", "COST", "CRM", "CSCO", "CVS",
#            "CVX",
#            "DD", "DHR", "DIS", "DOW", "DUK", "EMR", "EXC", "F", "FB", "FDX", "GD", "GE", "GILD", "GM", "GOOG", "GOOGL",
#            "GS",
#            "HD", "HON", "IBM", "INTC",  "KHC", "KMI", "KO",  "LMT", "LOW", "MA", "MCD", "MDLZ",
#            "MDT", "MET",
#            "MMM", "MO", "MRK", "MS", "MSFT", "NEE", "NFLX", "NKE", "NVDA", "ORCL", "PEP", "PFE",  "PM", "PYPL",
#            "QCOM", "RTX",
#            "SBUX", "SLB", "SO", "SPG", "T", "TGT", "TMO", "TSLA", "TXN", "UNH", "UNP", "UPS", "USB", "V", "VZ", "WBA",
#            "WFC", "WMT", "XOM"]
#
# sp_100_yahoo_finance = ["BTC-USD","AAPL", "ETH-USD","XRP-USD", "ABBV", "ABT", "SNDL", "AMC", "AIG", "ALL", "AMGN", "AMT", "AMZN", "AXP", "BA", "BAC", "BIIB", "BK",
#            "BKNG", "BLK", "BMY", "BRK-B", "C", "CAT", "CHTR", "CL", "CMCSA", "COF", "COP", "COST", "CRM", "CSCO", "CVS",
#            "CVX",
#            "DD", "DHR", "DIS", "DOW", "DUK", "EMR", "EXC", "F", "FB", "FDX", "GD", "GE", "GILD", "GM", "GOOG", "GOOGL",
#            "GS",
#            "HD", "HON", "IBM", "INTC",  "KHC", "KMI", "KO",  "LMT", "LOW", "MA", "MCD", "MDLZ",
#            "MDT", "MET",
#            "MMM", "MO", "MRK", "MS", "MSFT", "NEE", "NFLX", "NKE", "NVDA", "ORCL", "PEP", "PFE",  "PM", "PYPL",
#            "QCOM", "RTX",
#            "SBUX", "SLB", "SO", "SPG", "T", "TGT", "TMO", "TSLA", "TXN", "UNH", "UNP", "UPS", "USB", "V", "VZ", "WBA",
#            "WFC", "WMT", "XOM"]
#
#
#
# def get_sentiment():
#     vader_analyzer = SentimentIntensityAnalyzer()
#
#     for ticker in sp_100:
#         try:
#             example = 'https://api.stocktwits.com/api/2/streams/symbol/{0}.json'.format(ticker)
#
#             response = requests.get(example)
#
#             json_stocktwits = json.loads(response.content)
#
#             for item in json_stocktwits['messages']:
#                 if "likes" in item:
#                     likes = int(item['likes']['total'])
#                 else:
#                     likes = 0
#
#                 current_item = HTMLParser().unescape(item['body'])
#                 if not comment.objects.filter(original_comment=current_item).exists():
#                     # removing ticker symbols like $AAPL
#                     for i in current_item.split("\n"):
#                         example = re.findall(r'[$][A-Za-z][\S]*', str(i))
#                         print('QQQQQQQQQQQQQQQQQQQ', example)
#                         if example != []:
#                             break
#
#                     # print(example)
#                     new_current = current_item
#                     for elem in example:
#                         # print('HERE',elem)
#                         new_current = new_current.replace(str(elem), "")
#
#                     # print('HERE',new_current)
#
#                     # remove URL links
#                     new_current = re.sub('https?://[A-Za-z0-9./]+', '', new_current)
#
#                     new_current = re.sub('www?\.[A-Za-z0-9./]+', '', new_current)
#                     # removing mentions @
#                     new_current = re.sub(r'@[A-Za-z0-9]+', '', new_current)
#
#                     # removing hastags
#                     new_current = re.sub("/#\w+\s*/", " ", new_current)
#
#                     # removing numbers
#                     new_current = re.sub("\d+", " ", new_current)
#
#                     # remove stopwords
#                     new_current_tokenized = word_tokenize(new_current)
#
#                     new_current_no_sw = [word for word in new_current_tokenized if not word in stopwords]
#
#                     final_str = ""
#                     for element in new_current_no_sw:
#                         final_str += " " + element
#
#                     vader_score = vader_analyzer.polarity_scores(final_str)
#
#                     # classify the comment
#                     if vader_score['compound'] > -0.05 and vader_score['compound'] < 0.05:
#                         label = 'neu'
#                     elif vader_score['compound'] > 0.05:
#                         label = 'pos'
#                     else:
#                         label = 'neg'
#
#                     selected_ticker = Ticker.objects.get(ticker_name=ticker)
#                     created = comment.objects.create(
#                         site_name='Stocktwits',
#                         ticker_symbol=ticker,
#                         original_comment=current_item,
#                         pre_processed_comment=final_str,
#                         comment_like_count=likes,
#                         comment_date=item['created_at'],
#                         pos=vader_score['pos'],
#                         neu=vader_score['neu'],
#                         neg=vader_score['neg'],
#                         compound=vader_score['compound'],
#                         label=label,
#                         ticker=selected_ticker
#
#                     )
#                     print(
#                         f"{created.site_name}, {created.ticker_symbol}, {created.original_comment}, {created.pre_processed_comment}, {created.pos}, {created.neu}, {created.compound}, {created.label}")
#                     # print('OLD', item['body'], 'SCORE : ', vader_analyzer.polarity_scores(item['body']))
#                     # print('NEW ', new_current, 'SCORE : ', vader_analyzer.polarity_scores(new_current))
#                     # print('NO SW', new_current_no_sw)
#                     # print('FINAL STRING : ', final_str, 'SCORE : ', vader_analyzer.polarity_scores(final_str))
#                     # print("-------------------------------------------------------------------------------------")
#
#             # counter += 1
#             # if counter == 50:
#             #     break
#
#         except Exception as e:
#             Exceptions.objects.create(exception=e, extra_info=ticker, time_happened=datetime.datetime.now())
#
#     # Yahoo finance scraping part
#
#     for ticker in sp_100_yahoo_finance:
#         try:
#
#             URL = 'https://uk.finance.yahoo.com/quote/{0}/community?p={1}'.format(ticker, ticker)
#             page = requests.get(URL)
#
#             soup = BeautifulSoup(page.content, 'html.parser')
#
#             script = soup.find('script', text=re.compile('root\.App\.main'))
#
#             json_text = re.search(r'^\s*root\.App\.main\s*=\s*({.*?})\s*;\s*$',
#                                   script.string, flags=re.MULTILINE).group(1)
#
#             data = json.loads(json_text)
#
#             # print(data['context'])
#
#             for messageid in \
#                     data['context']['dispatcher']['stores']['CanvassStore']['comments']['canvass-0-CanvassApplet'][
#                         'messageList']:
#                 prid = data['context']['dispatcher']['stores']['BeaconStore']['beaconConfig']['context']['prid']
#                 try:
#                     print(
#                         '---------------------------------COMMENTS-----------------------------------------------------\n')
#
#                     message_created_comment = datetime.datetime.fromtimestamp(messageid['meta']['createdAt'])
#                     # print(messageid['reactionStats']['upVoteCount'])
#                     message_comment = messageid['details']['userText']
#
#                     print(ticker, message_comment)
#                     if not comment.objects.filter(original_comment=message_comment).exists():
#                         # remove URL links
#                         message_comment = re.sub('https?://[A-Za-z0-9./]+', '', message_comment)
#
#                         message_comment = re.sub('www?\.[A-Za-z0-9./]+', '', message_comment)
#                         # removing mentions @
#                         message_comment = re.sub(r'@[A-Za-z0-9]+', '', message_comment)
#
#                         # removing hastags
#                         message_comment = re.sub("/#\w+\s*/", " ", message_comment)
#
#                         # removing numbers
#                         message_comment = re.sub("\d+", " ", message_comment)
#
#                         # remove stopwords
#                         new_current_tokenized = word_tokenize(message_comment)
#
#                         new_current_no_sw = [word for word in new_current_tokenized if not word in stopwords]
#
#                         final_str = ""
#                         for element in new_current_no_sw:
#                             final_str += " " + element
#
#                         vader_score = vader_analyzer.polarity_scores(final_str)
#
#                         # classify the comment
#                         if vader_score['compound'] > -0.05 and vader_score['compound'] < 0.05:
#                             label = 'neu'
#                         elif vader_score['compound'] > 0.05:
#                             label = 'pos'
#                         else:
#                             label = 'neg'
#
#                         # make same ticker
#                         temp = ''
#                         # "BTC-USD", "ETH-USD","XRP-USD", BRK-B
#                         if ticker == 'BTC-USD':
#                             temp = "BTC.X"
#                         elif ticker == 'ETH-USD':
#                             temp = "ETH.X"
#                         elif ticker == 'XRP-USD':
#                             temp = "XRP.X"
#                         elif ticker == 'BRK-B':
#                             temp = "BRK.B"
#                         else:
#                             temp = ticker
#
#                         selected_ticker1 = Ticker.objects.get(ticker_name=temp)
#                         created = comment.objects.create(
#                             site_name='Yahoo Finance',
#                             ticker_symbol=temp,
#                             original_comment=messageid['details']['userText'],
#                             pre_processed_comment=final_str,
#                             comment_date=message_created_comment,
#                             comment_like_count=int(messageid['reactionStats']['upVoteCount']),
#                             pos=vader_score['pos'],
#                             neu=vader_score['neu'],
#                             neg=vader_score['neg'],
#                             compound=vader_score['compound'],
#                             label=label,
#                             ticker=selected_ticker1
#
#                         )
#                         print(
#                             f"{created.site_name}, {created.ticker_symbol}, {created.original_comment}, {created.pre_processed_comment}, {created.pos}, {created.neu}, {created.compound}, {created.label}")
#                         # messageid['messageId'],messageid['reactionStats']['replyCount'])
#                     print(
#                         '---------------------------------REPLIES-----------------------------------------------------\n')
#                     if messageid['reactionStats']['replyCount'] != 0:
#                         URL2 = 'https://uk.finance.yahoo.com/_finance_doubledown/api/resource/canvass.getReplies_ns;action=showNext;apiVersion=v1;context=' \
#                                '{1};count=30;index=null;lang=en-GB;' \
#                                'messageId={0};namespace=yahoo_finance;oauthConsumerKey=finance.oauth.client.canvass.prod.consumerKey;oauthConsumerSecret=finance.oauth.client.canvass.prod.consumerSecret;region=GB;' \
#                                'sortBy=createdAt;tags={3}?bkt=finance-GB-en-GB-def&device=desktop&ecma=modern&feature=canvassOffnet%2CccOnMute%2CdisableCommentsMessage%2Cdebouncesearch100%2CdeferDarla%2CecmaModern%2CemptyServiceWorker%2CenableCCPAFooter%2CenableCMP%2CenableConsentData%2CenableGuceJs%2CenableGuceJsOverlay%2CenableNavFeatureCue%2CenablePrivacyUpdate%2CenableStreamDebounce%2CenableTheming%2CenableUpgradeLeafPage%2CenableVideoDocking%2CenableVideoURL%2CenableYahooSans%2CenableYodleeErrorMsgCriOS%2CncpListStream%2CncpPortfolioStream%2CncpQspStream%2CncpStream%2CncpStreamIntl%2CncpTopicStream%2CnewContentAttribution%2CnewLogo%2CoathPlayer%2CrelatedVideoFeature%2CvideoNativePlaylist%2CsunsetMotif2%2CenableSingleRail%2CenhanceAddToWL%2Carticle2_csn%2CenableUserPrefAPI%2CenableStageAds%2CsponsoredAds&intl=uk&lang=en-GB' \
#                                '&partner=none&prid={2}&region=GB&site=finance&tz=Europe%2FLondon&ver=0.102.4128&returnMeta=true'.format(
#                             messageid['messageId'], messageid['contextId'], prid, ticker)
#                         time.sleep(0.5)
#                         response = requests.get(URL2)
#                         current_replies = json.loads(response.content)
#                         # print(current_replies)
#                         for reply in current_replies['data']:
#                             message = reply['details']['userText']
#                             # print(reply['reactionStats']['upVoteCount'])
#
#                             if not comment.objects.filter(original_comment=message).exists():
#                                 message_created = datetime.datetime.fromtimestamp(reply['meta']['createdAt'])
#
#                                 # remove URL links
#                                 message = re.sub('https?://[A-Za-z0-9./]+', '', message)
#
#                                 message = re.sub('www?\.[A-Za-z0-9./]+', '', message)
#                                 # removing mentions @
#                                 message = re.sub(r'@[A-Za-z0-9]+', '', message)
#
#                                 # removing hastags
#                                 message = re.sub("/#\w+\s*/", " ", message)
#
#                                 # removing numbers
#                                 message = re.sub("\d+", " ", message)
#
#                                 # remove stopwords
#                                 new_current_tokenized = word_tokenize(message)
#
#                                 new_current_no_sw = [word for word in new_current_tokenized if not word in stopwords]
#
#                                 final_str = ""
#                                 for element in new_current_no_sw:
#                                     final_str += " " + element
#
#                                 vader_score = vader_analyzer.polarity_scores(final_str)
#
#                                 # classify the comment
#                                 if vader_score['compound'] > -0.05 and vader_score['compound'] < 0.05:
#                                     label = 'neu'
#                                 elif vader_score['compound'] > 0.05:
#                                     label = 'pos'
#                                 else:
#                                     label = 'neg'
#
#                                 temp = ''
#                                 # "BTC-USD", "ETH-USD","XRP-USD", BRK-B
#                                 if ticker == 'BTC-USD':
#                                     temp = "BTC.X"
#                                 elif ticker == 'ETH-USD':
#                                     temp = "ETH.X"
#                                 elif ticker == 'XRP-USD':
#                                     temp = "XRP.X"
#                                 elif ticker == 'BRK-B':
#                                     temp = "BRK.B"
#                                 else:
#                                     temp = ticker
#
#                                 selected_ticker2 = Ticker.objects.get(ticker_name=temp)
#                                 created = comment.objects.create(
#                                     site_name='Yahoo Finance',
#                                     ticker_symbol=temp,
#                                     original_comment=reply['details']['userText'],
#                                     pre_processed_comment=final_str,
#                                     comment_date=message_created,
#                                     comment_like_count=int(reply['reactionStats']['upVoteCount']),
#                                     pos=vader_score['pos'],
#                                     neu=vader_score['neu'],
#                                     neg=vader_score['neg'],
#                                     compound=vader_score['compound'],
#                                     label=label,
#                                     ticker=selected_ticker2
#
#                                 )
#                                 print(
#                                     f"{created.site_name}, {created.ticker_symbol}, {created.original_comment}, {created.pre_processed_comment}, {created.pos}, {created.neu}, {created.compound}, {created.label}")
#                                 # print(f"UserName: {reply['meta']['author']['nickname']}\n")
#                                 # print(f"'Vader Score : {vader_analysis1['compound']}  TextBlob Score : {analysis1.sentiment.polarity}   {reply['details']['userText']}\n")
#                                 # for word in analysis1.words:
#                                 # print(word ,'  :    ' ,vader_analyzer.polarity_scores(word))
#                 except Exception as e:
#                     Exceptions.objects.create(exception=e, extra_info=ticker, time_happened=datetime.datetime.now())
#             time.sleep(7)
#         except Exception as e:
#             Exceptions.objects.create(exception=e, extra_info=ticker, time_happened=datetime.datetime.now())
#
#     t1 = time.time() - t0
#     print("Time elapsed: ", t1)  # CPU seconds elapsed (floating point)
#     try:
#         print('Final time passed in minutes: ', str(datetime.timedelta(seconds=t1)))
#     except Exception as e:
#         print(e)