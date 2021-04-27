<?php
require_once('TwitterAPIExchange.php');
// $hashtag = $_GET["q"];

$settings = array(
    'oauth_access_token' => 1289826632903979008-R3qr2tVshwnAiHONMmcwJuRpGPpVGd,
    'oauth_access_token_secret' => NM021bBrjwVBlag3UO8KLx7biTDwjTMXG5F1NYMz9E8DJ,
    'consumer_key' => NrF5bt4MhnGzdKyehnwiwtXbo,
    'consumer_secret' => ne3HRfxehhmtlQsVLKxz4zupOXUu9VHUMYbKV07tMeJsdiR39w
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
