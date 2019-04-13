# install needed Packages
import warnings
warnings.filterwarnings('ignore')
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import textstat
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')
from nltk.probability import FreqDist
from nltk.corpus import stopwords
#nltk.download('stopwords')
import re
import spacy
from spacy import displacy  

# Functions 

# Functions below takes string as a input:

def get_article_features(title, text, nlp):
    '''
    The Above Function Returns Json Object for the String Input.
    Takes two Parameter
    '''
    def preprocess(sentence):
         sentence = sentence.lower()
         tokenizer = RegexpTokenizer(r'\w+')
         tokens = tokenizer.tokenize(sentence)
         return " ".join(tokens)
    def lexical_diversity(text):
        '''
        Returns the diversity of the string.
        '''
        tokens = word_tokenize(text)
        word_count = len(tokens)
        vocab_size = len(set(tokens))
        diversity_score = vocab_size / word_count
        return (diversity_score * 100)


    def freq_dist_sentence(text,stop_flag = False):
        '''
        Returns word count for Each Sentence
        '''
        text = preprocess(text)
        tokenized_word = word_tokenize(text)
        # with Stop Flag enabled
        if stop_flag:
            stop_words=set(stopwords.words("english"))
            tokenized_word = [x for x in tokenized_word if (x not in stop_words and x.isalpha())]
        fdist = FreqDist(tokenized_word)
        return fdist

    def polarity_sc(text):
        # Returns dictionary of Polarity Score. Vader Intensity Analyzer
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(text)
        return scores

    def reading_standard(text):
        x = textstat.text_standard(text)
        match = re.search(r'(.?\d+)th(\s\w{3}\s((.?\d+)))?',x)
        r_stan = []
        if match:
            r_stan.append(match.group(1))
            r_stan.append(match.group(3))
        return r_stan

    def spacy_vizualizer(title,text, nlp):
        '''
        Returns Graphs of NER and Dependency Parse.
        Return Format is HTML
        '''
        text = nlp(text)
        title = nlp(title)
        html_dep = displacy.render(title, style = 'dep', page = True)
        html_ent = displacy.render(text, style = 'ent', minify = True)
        dep = html_dep
        ent = html_ent
        print(dep)
        return (dep, ent)   
   
    result = {}
    #Result = []
    Text = preprocess(text)
    Title = preprocess(title)
    result['difficult_words'] = textstat.difficult_words(Text)
    result['word_count'] = len(word_tokenize(Text))
    result['lexical_diversity'] = lexical_diversity(Text)
    result['word_dist'] = dict(freq_dist_sentence(Text).most_common())
    result['word_dist_without_stopwords'] = dict(freq_dist_sentence(Text,stop_flag=True).most_common())
    result['polarity_title_pos'] = polarity_sc(Title)['pos'] * 100
    result['polarity_title_neg'] = polarity_sc(Title)['neg'] * 100 
    result['polarity_title_neu'] = polarity_sc(Title)['neu'] * 100
    result['reading_standard'] = reading_standard(text)
    result['dependency_html'], result['ner_html'] = spacy_vizualizer(title, text, nlp)

    return result
    