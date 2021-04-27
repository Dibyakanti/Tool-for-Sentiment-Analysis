<?php
require_once('TwitterAPIExchange.php');
// $hashtag = $_GET["q"];

$settings = array(
    'oauth_access_token' => "put access token here ",
    'oauth_access_token_secret' => "put access token secret here",
    'consumer_key' => "put consumer token here",
    'consumer_secret' => "put consumer token secret here"
);

$url = 'https://api.twitter.com/1.1/statuses/home_timeline.json';
// $getfield = '?q=#'.$hashtag.' AND -filter:retweets AND -filter:replies&lang=en&count=20&tweet_mode=extended';
$getfield = '?q=-filter:retweets AND -filter:replies&lang=en&count=50&tweet_mode=extended';
$requestMethod = 'GET';

$twitter = new TwitterAPIExchange($settings);
$response = $twitter->setGetfield($getfield)
     ->buildOauth($url, $requestMethod)
     ->performRequest();

echo $response;
?>
