# Coordinates given for the regions.
p1 = (49.189787, -67.444574)
p2 = (24.660845, -67.444574)
p3 = (49.189787, -87.518395)
p4 = (24.660845, -87.518395)
p5 = (49.189787, -101.998892)
p6 = (24.660845, -101.998892)
p7 = (49.189787, -115.236428)
p8 = (24.660845, -115.236428)
p9 = (49.189787, -125.242264)
p10 = (24.660845, -125.242264)
#               SENTIMENT ANALYSIS OF TWEET FILES BY USING SOME SPECIFIC KEYWORDS
'This program can analyse tweet files based on their regions and content of tweets. '
'The program will output an average of sentiment value based on the keywords and their values on prompted keyword file.'
'The program also will output the total words counted in tweets and the total keywords counted out of those tweets.'
'This values and numbers will be outputted according to their regional areas such as Eastern.'


def compute_tweets(tweets_file, keyword_file):
    try:
        o_tweets_file = open(tweets_file, 'r', encoding='utf-8')  # opens tweet files.
        o_tweets_file2 = open(tweets_file, 'r', encoding='utf-8')  # opens tweet files.
        o_keyword_file = open(keyword_file, 'r', encoding='utf-8')  # opens keyword files.

        word_list = list_of_word(o_tweets_file)  # make use word function coded below.
        list_of_lat_long = lat_long_all_list(o_tweets_file2)  # make use list of latitude and longitude function below.
        keyword_dict = dict_of_keywords(o_keyword_file)  # make use keyword dictionary below.
        sentiment_score_list = sentiment_score_function(word_list, keyword_dict)  # make use sentiment values list below

        # Analyse the file for four major regions(North America).
        regional_analysis_eastern = regional_analysis(list_of_lat_long, "Eastern", sentiment_score_list)
        regional_analysis_central = regional_analysis(list_of_lat_long, "Central", sentiment_score_list)
        regional_analysis_mountain = regional_analysis(list_of_lat_long, "Mountain", sentiment_score_list)
        regional_analysis_pacific = regional_analysis(list_of_lat_long, "Pacific", sentiment_score_list)
        regional_analysis_all = [regional_analysis_eastern, regional_analysis_central,  # Combines all four analyses.
                                 regional_analysis_mountain, regional_analysis_pacific]
        return regional_analysis_all  # returns the function to main file to be proceeded.
    except IOError:
        result = []  # Checks if the file works or not. If it doesnt, instead of returning python in-built error,
        return result  # it returns an empty list.


def lat_long_all_list(tweet_file):  # We are taking the latitude and longitude points in a list to locate the tweets.
    list_of_lat_long = []
    for line in tweet_file:
        line = line.split()
        lat = line[0]
        lat = lat.replace('[', '')  # removes '[' after we get the list for latitude.
        lat = float(lat.replace(',', ''))  # removes ',' after we get the list for latitude.
        long = line[1]
        long = float(long.replace(']', ''))  # removes ']' after we get the list for longitude.
        list_of_lat_long.append([lat, long])  # creates a list with two values.
    return list_of_lat_long


def list_of_word(tweet_file):  # We are taking all tweet file in a list by splitting, making all the numbers lower case.
    word_list = []
    for words in tweet_file:
        punc_signs = ".,;:`~_?!'-=+*&^%$#@()[]{}\"/\\><"
        words = words.split()
        word_list_detail = []
        for column in words:
            column2 = column.strip(punc_signs)
            word_list_detail.append(column2.lower())
        word_list.append(list(word_list_detail))
    return word_list


def dict_of_keywords(tweet_file):  # We are creating a dictionary for values in keyword file.
    keyword_dict = dict()  # We need a dictionary because we will need to assign some keys to their values.
    import csv  # this helps with comma separated values.
    listing = csv.reader(tweet_file)
    for row in listing:
        key = row[0]
        value = float(row[1])
        keyword_dict.update({key: value})  # appending new keys and values to dictionary each time by updating dict.
    return keyword_dict


def sentiment_score_function(word_list, keyword_dict):  # calculates sentiment values of each tweets while finding them,
    sentiment_score_list = []                           # by using set.intersection.
    for i in range(len(word_list)):
        intersection_of_keywords = list((set(word_list[i])).intersection(set(keyword_dict)))  # the key point of func.
        if len(intersection_of_keywords) > 0:
            score = 0
            for key in intersection_of_keywords:
                score += float(keyword_dict.get(key))  # goes to dictionary and find the 'number'.
            sentiment_score = float(score/len(intersection_of_keywords))  # Finds the sentiment value for each tweet.
        else:
            sentiment_score = 0
        sentiment_score_list.append(sentiment_score)  # list of all sentiment values.
    return sentiment_score_list


# makes the analysis according to each region while determining the regions based on their coordinates.
def regional_analysis(list_of_lat_long, region, sentiment_score_list):
    left_longitude = 0
    right_longitude = 0
    lower_latitude = 0
    upper_latitude = 0
    if region == "Eastern":           # determines the Eastern region based on given coordinates.
        right_longitude = p1[1]
        left_longitude = p3[1]
        lower_latitude = p2[0]
        upper_latitude = p1[0]
    if region == "Central":          # determines the Central region based on given coordinates.
        right_longitude = p3[1]
        left_longitude = p5[1]
        lower_latitude = p6[0]
        upper_latitude = p5[0]
    if region == "Mountain":         # determines the Mountain region based on given coordinates.
        right_longitude = p5[1]
        left_longitude = p7[1]
        lower_latitude = p8[0]
        upper_latitude = p7[0]
    if region == "Pacific":          # determines the Pacific region based on given coordinates.
        right_longitude = p7[1]
        left_longitude = p9[1]
        lower_latitude = p10[0]
        upper_latitude = p9[0]

    tweets_counted = 0
    keyword_tweets_counted = 0
    total_sentiment_score = 0

    for i in range(len(list_of_lat_long)):
        # checks every latitude and longitude in their list(lat-long) according to their list positions and determines,
        # their region. Also calculates the average sentiment values for each regions.
        if (lower_latitude < (list_of_lat_long[i][0]) < upper_latitude) and \
                (left_longitude <= list_of_lat_long[i][1] <= right_longitude):
            tweets_counted += 1  # count all tweets.
            total_sentiment_score += sentiment_score_list[i]  # for loop helps us to use it also for calculation,
            if sentiment_score_list[i] > 0:                   # of sentiment values.
                keyword_tweets_counted += 1  # count tweets that have keywords in keyword file.
    if total_sentiment_score > 0:
        average = total_sentiment_score/keyword_tweets_counted  # takes the mean/average.
        regional_tuple = (average, keyword_tweets_counted, tweets_counted)  # stores wanted values in a tuple
    else:                                                      # so it cannot be changed. (because that is what we need)
        regional_tuple = (0, 0, 0)
    return regional_tuple
