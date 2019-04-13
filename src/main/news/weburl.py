from newspaper import Article
from newsapi import NewsApiClient
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import datetime
from datetime import date, timedelta

bow = joblib.load('media/News/ques_bow.joblib')
tfidf = joblib.load('media/News/ques_tfidf.joblib')
# for mapping
feature_names=bow.get_feature_names()
print('BOW AND TFIDF LOADED!!!')

def headline_text(url = '', summary = False):
    '''
    Returns headline text of news.. 
    Just makes call to the newspaper class.
    '''
    article = Article(url)
    # Download the article and parse it.
    article.download()
    article.parse()
    #authors = article.authors
    headline = article.title
    text = article.text
    if summary:
        article.nlp()
        summary = article.summary
        return url, headline, text, summary
    return url, headline, text

    #### NEWS FETCH #####
apikey = 'a02e87f91bc0476f9b239cc7022a6850'
newsapi = NewsApiClient(api_key=apikey)

def get_news(q, everything = False):
    today = str(datetime.date.today())
    yesterday = date.today() - timedelta(5)
    yesterday = yesterday.strftime('2019-%m-%d')
    list_news = []
    all_news = {}
    
    top_news = []
    top_head = {}
    news = {}

    # top_headlines = newsapi.get_top_headlines(q,
    #                                       sources='the-telegraph,the-times-of-india',
    #                                       language='en')
    
    all_articles = newsapi.get_everything(q=q,
                                      sources='the-telegraph, the-times-of-india, bbc-news, the-verge, the-hindu',
                                      from_param=yesterday,
                                      to=today,
                                      language='en',
                                      sort_by='popularity',
                                      page=1)

    # print(str(top_headlines))

    print(str(all_articles))


    # for i in range(top_headlines['totalResults']):

    #     top_head['Url'], top_head['Headline'], top_head['Text']= headline_text(top_headlines['articles'][i]['url'])
    #     top_news.append(top_head)
    for i in range(10):
        try:
            news = {}
            news['Url'], news['Headline'], news['Text']= all_articles['articles'][i]['url'], all_articles['articles'][i]['title'], all_articles['articles'][i]['description']
        except Exception as e:
            pass
        if news != {}:
            list_news.append(news)
    
    # all_news['TOP'] = top_news
    all_news['ALL'] = list_news

    print(all_articles['articles'][0])
    print(all_articles['articles'][1])
    return all_news

def get_allnews(text):
    '''
    Returns: dict type having signature
    x[<keyword>][<type TOP | ALL >][< index >][< keys Url| Headline | Text ]
    example :-
    >>> x['update']['ALL'][0].keys()
    dict_keys(['Url', 'Headline', 'Text'])
    '''
    keywords = get_keywords(text)
    print(keywords)
    tdic = {}
    for word in keywords[:1]:
        tdic[word] = get_news(word)
    return tdic

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
 
def extract_topn_from_vector(feature_names, sorted_items, topn=5):
    """get the feature names and tf-idf score of top n items"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]
 
    score_vals = []
    feature_vals = []
    
    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])
 
    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results 

def get_keywords(text):

    tf_idf_vector=tfidf.transform(bow.transform([text]))
    #sort the tf-idf vectors by descending order of scores
    sorted_items=sort_coo(tf_idf_vector.tocoo())
    #extract only the top n; n here is 3
    keywords=extract_topn_from_vector(feature_names,sorted_items,3)
    print("\n=====Ques=====")
    print(text)
    print("\n===Keywords===")
    for k in keywords:
        print(k,keywords[k])
    return list(keywords.keys())