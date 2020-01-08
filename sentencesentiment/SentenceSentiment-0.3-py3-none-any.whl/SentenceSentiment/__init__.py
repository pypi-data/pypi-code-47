from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Sent:
    def __init__(self):
        print("Mathematical Problem")

    def Mathfunc(self, number):
        print("Math Implication of square formula")
        return number*number

    # import SentimentIntensityAnalyzer class
    # from vaderSentiment.vaderSentiment module.
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    # function to print sentiments
    # of the sentence.
    def sentiment_scores(self, sentence):

        # Create a SentimentIntensityAnalyzer object.
        sid_obj = SentimentIntensityAnalyzer()

        # polarity_scores method of SentimentIntensityAnalyzer
        # oject gives a sentiment dictionary.
        # which contains pos, neg, neu, and compound scores.
        sentiment_dict = sid_obj.polarity_scores(sentence)

        print("Overall sentiment dictionary is : ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

        print("Sentence Overall Rated As", end=" ")

        # decide sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05:
            print("Positive")

        elif sentiment_dict['compound'] <= - 0.05:
            print("Negative")

        else:
            print("Neutral")

