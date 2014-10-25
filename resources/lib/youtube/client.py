import json
import requests

__author__ = 'bromix'


class Client(object):
    KEY = 'AIzaSyAd-YEOqZz9nXVzGtn3KWzYLbLaajhqIDA' #TV

    def __init__(self, key='', language='en-US'):
        self._key = self.KEY
        if key:
            self._key = key
            pass

        self._language = language
        self._country = language.split('-')[1]
        pass

    def get_channel_sections_v3(self, channel_id):
        params = {'part': 'snippet,contentDetails,id',
                  'channelId': channel_id}
        return self._perform_v3_request(method='GET', path='channelSections', params=params)

    def get_channels_v3(self, channel_id):
        """
        :param channel_id: list or comma-separated list of the YouTube channel ID(s)
        :return:
        """
        if isinstance(channel_id, list):
            channel_id = ','.join(channel_id)
            pass

        params = {'part': 'snippet,contentDetails,brandingSettings',
                  'id': channel_id}
        return self._perform_v3_request(method='GET', path='channels', params=params)

    def get_guide_v3(self):
        params = {'part': 'snippet',
                  'regionCode': self._country,
                  'hl': self._language}
        return self._perform_v3_request(method='GET', path='guideCategories', params=params)

    def get_guide_tv(self):
        return self._perform_tv_request(method='POST', path='guide')

    def _perform_v3_request(self, method='GET', headers=None, path=None, post_data=None, params=None,
                            allow_redirects=True):
        # params
        if not params:
            params = {}
            pass
        _params = {'key': self._key}
        _params.update(params)

        # headers
        if not headers:
            headers = {}
            pass
        _headers = {'Host': 'www.googleapis.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.36 Safari/537.36',
                    'X-JavaScript-User-Agent': 'Google APIs Explorer'}

        # postdata - IS ALWAYS JSON!
        if not post_data:
            post_data = {}
            pass
        _post_data = {}
        _post_data.update(post_data)

        _headers.update(headers)

        # url
        _url = 'https://www.googleapis.com/youtube/v3/%s' % path.strip('/')

        result = None
        if method == 'GET':
            result = requests.get(_url, params=_params, headers=_headers, verify=False, allow_redirects=allow_redirects)
        elif method == 'POST':
            result = requests.post(_url, data=json.dumps(_post_data), params=_params, headers=_headers, verify=False,
                                   allow_redirects=allow_redirects)
        elif method == 'PUT':
            result = requests.put(_url, data=json.dumps(_post_data), params=_params, headers=_headers, verify=False,
                                  allow_redirects=allow_redirects)
        elif method == 'DELETE':
            result = requests.delete(_url, data=json.dumps(_post_data), params=_params, headers=_headers, verify=False,
                                     allow_redirects=allow_redirects)
            pass

        if result is None:
            return {}

        return result.json()

    def _perform_tv_request(self, method='GET', headers=None, path=None, post_data=None, params=None,
                            allow_redirects=True):
        """
        This is part of the YouTube TV API for TVs
        :param method:
        :param headers:
        :param path:
        :param post_data:
        :param params:
        :param allow_redirects:
        :return:
        """

        # params
        if not params:
            params = {}
            pass
        _params = {'key': self._key}
        _params.update(params)

        # headers
        if not headers:
            headers = {}
            pass
        _headers = {'Host': 'www.googleapis.com',
                    'Connection': 'keep-alive',
                    'Origin': 'https://www.youtube.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.36 Safari/537.36',
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'DNT': '1',
                    'Referer': 'https://www.youtube.com/tv',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.8,de;q=0.6'}

        # postdata - IS ALWAYS JSON!
        if not post_data:
            post_data = {}
            pass
        _post_data = {'context': {'client': {'acceptLanguage': self._language,
                                             'acceptRegion': self._country,
                                             'clientName': 'TVHTML5',
                                             'clientVersion': '4'}}}
        if isinstance(post_data, dict):
            _post_data.update(post_data)
            pass

        _headers.update(headers)

        # url
        _url = 'https://www.googleapis.com/youtubei/v1/%s' % path.strip('/')

        result = None
        if method == 'GET':
            result = requests.get(_url, params=_params, headers=_headers, verify=False, allow_redirects=allow_redirects)
        elif method == 'POST':
            result = requests.post(_url, data=json.dumps(_post_data), params=_params, headers=_headers, verify=False,
                                   allow_redirects=allow_redirects)
        elif method == 'PUT':
            result = requests.put(_url, data=json.dumps(_post_data), params=_params, headers=_headers, verify=False,
                                  allow_redirects=allow_redirects)
        elif method == 'DELETE':
            result = requests.delete(_url, data=json.dumps(_post_data), params=_params, headers=_headers, verify=False,
                                     allow_redirects=allow_redirects)
            pass

        if result is None:
            return {}

        return result.json()

    pass