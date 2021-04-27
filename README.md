# Tool-for-Sentiment-Analysis

This is a tool to check a twitter user's home timeline (tweets) to get and separate them into three categories so that the user can read whichever he wants on the basis of his mood.

<img src="https://github.com/Dibyakanti/Tool-for-Sentiment-Analysis-EE390-course-project/blob/main/img/preview.png">

## How to run

#### Intial preparation before running the codes :

1. Clone this repository to your local computer.
2. Register yourself on twitter developer platform and get access and consumer token.
3. Put the keys that you obtained in the `keys.py` file.

#### Get the tweets :

To get the tweets you need to run `get_tweet.py`.

'''
python get_tweet.py --count 100       # put the number of tweets you want to fetch (default 50)
'''

#### Run `index.html`

Point your localhost to the cloned root directory. Browse to `http://localhost/index.html`

Note - you can copy the whole repo to `/var/www/html/` address
