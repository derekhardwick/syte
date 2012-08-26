
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.4'


#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'derekhardwick.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'jWWbvne8fjK6hkFcYoJhb9T0K2YunzbvKzs9abbB3f0sOrsogT'

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = '1RPyMGHphUFVbPk6SnV4w'
TWITTER_CONSUMER_SECRET = 'Vw41wEuV3hVUSnCztqQ3mc5O2aD14TWHHTDyfe28I'
TWITTER_USER_KEY = '18453325-lJcfCS9Eqpt5iMN8jKrIe1a4xEANt2k7nXBtiKccD'
TWITTER_USER_SECRET = 'pX2qIPyk3WABSrN5dMTY1EENPd3tNFtVyeQboruYM'


#Github Integration
GITHUB_INTEGRATION_ENABLED = False
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '[ENTER GITHUB ACCESS TOKEN HERE, SEE GITHUB SETUP INSTRUCTIONS]'

GITHUB_OAUTH_ENABLED = False
GITHUB_CLIENT_ID = '[ENTER GITHUB CLIENT ID HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_CLIENT_SECRET = '[ENTER GITHUB CLIENT SECRET HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '16863442.ce391b6.3c59d0c469634a049f90c7c2e5c43b3b'
INSTAGRAM_USER_ID = '16863442'

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = 'ce391b6e4a9c4e3f8b1567abfe30c64c'
INSTAGRAM_CLIENT_SECRET = '73dae3f198e449bdb8e848a9785e8d33'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'

#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = False
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = '[ENTER FOURSQUARE ACCESS TOKEN HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = True
FOURSQUARE_CLIENT_ID = '[ENTER FOURSQUARE CLIENT_ID HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_CLIENT_SECRET = '[ENTER FOURSQUARE CLIENT_SECRET HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = True
DISQUS_SHORTNAME = 'derekhardwick'


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = False
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '[ENTER LASTFM API_KEY HERE, SEE LASTFM SETUP INSTRUCTIONS]'
LASTFM_USERNAME = '[ENTER LASTFM username HERE, SEE LASTFM SETUP INSTRUCTIONS]'


#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = False
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = '[ENTER SOUNDCLOUD APPLICATION CLIENT_ID HERE]'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = False
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False



if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://derekhardwick.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
