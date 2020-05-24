import codecs
import shutil

with codecs.open("CollatedTweets.csv", encoding="utf-16") as input_file:
    with codecs.open(
            "CollatedTweetsNDC.csv", "w", encoding="utf-8") as output_file:
        shutil.copyfileobj(input_file, output_file)
