import sentiment_analysis  # imports sentiment_analysis file to use the function

keyword_file = 'keywords.txt'  # these two files are for the test cases of the program.
tweets_file = 'tweets.txt'

results = sentiment_analysis.compute_tweets(tweets_file, keyword_file)  # calls the compute_tweet function.
print("%-10s%10s%15s%18s\n"   # places the values in the output.
      "%-10s%10.4f%15d%15d\n"
      "%-10s%10.4f%15d%15d\n"
      "%-10s%10.4f%15d%15d\n"
      "%-10s%10.4f%15d%15d" % ("REGION", "AVERAGE/MEAN", "KEYWORDS", "TOTAL TWEETS",
                               "Eastern", results[0][0], results[0][1], results[0][2],
                               "Central", results[1][0], results[1][1], results[1][2],
                               "Mountain", results[2][0], results[2][1], results[2][2],
                               "Pacific", results[3][0], results[3][1], results[3][2]))