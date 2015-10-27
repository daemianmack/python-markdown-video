#!/usr/bin/env python

"""
Embeds web videos using URLs.  For instance, if a URL to an youtube video is
found in the text submitted to markdown and it isn't enclosed in parenthesis
like a normal link in markdown, then the URL will be swapped with a embedded
youtube video.

All resulting HTML is XHTML Strict compatible.

>>> from __future__ import unicode_literals
>>> import markdown

Test Markdown Escaping

# >>> s = "\\http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/"
# >>> markdown.markdown(s, ['video'])
# '<p>http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/</p>'
>>> s = "`http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/`"
>>> markdown.markdown(s, ['video'])
'<p><code>http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/</code></p>'

Test Markdown Link

>>> s = "[Metacafe link](http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/)"
>>> markdown.markdown(s, ['video'])
'<p><a href="http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/">Metacafe link</a></p>'

Test HTML Link

>>> s = '<a href="http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/">Metacafe link</a>'
>>> markdown.markdown(s, ['video'])
'<p><a href="http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/">Metacafe link</a></p>'


Test Dailymotion

>>> s = "http://www.dailymotion.com/video/x3b3ec0_wingsuit-slalom-racing-8-000-feet-above-the-ground_sport"
>>> markdown.markdown(s, ['video'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="270" mozallowfullscreen="true" src="http://www.dailymotion.com/embed/video/x3b3ec0" webkitallowfullscreen="true" width="480"></iframe>\\n</p>'


# Test Gametrailers

# >>> s = "http://www.gametrailers.com/video/console-comparison-borderlands/58079"
# >>> markdown.markdown(s, ['video'])
# '<p><object data="http://www.gametrailers.com/remote_wrap.php?mid=58079" height="392" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://www.gametrailers.com/remote_wrap.php?mid=58079" /><param name="allowfullscreen" value="true" /></object></p>'


Test Metacafe

>>> s = "http://www.metacafe.com/watch/11419683/killing_luke_skywalker_battlefront/"
>>> markdown.markdown(s, ['video'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="248" mozallowfullscreen="true" src="http://www.metacafe.com/embed/11419683/" webkitallowfullscreen="true" width="440"></iframe>\\n</p>'


Test Metacafe with arguments

>>> markdown.markdown(s, ['video(metacafe_width=500,metacafe_height=425)'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="425" mozallowfullscreen="true" src="http://www.metacafe.com/embed/11419683/" webkitallowfullscreen="true" width="500"></iframe>\\n</p>'


Test Veoh Video

>>> s = "http://www.veoh.com/watch/v95981404eQdfjw2E"
>>> markdown.markdown(s, ['video'])
'<p><object height="341" width="410"><param name="movie" value="http://www.veoh.com/swf/webplayer/WebPlayer.swf?version=AFrontend.5.7.0.1509&amp;permalinkId=v95981404eQdfjw2E&amp;player=videodetailsembedded&amp;videoAutoPlay=0&amp;id=anonymous"></param><param name="allowfullscreen" value="true"></param><embed allowfullscreen="true" height="341" name="veohFlashPlayerEmbed" src="http://www.veoh.com/swf/webplayer/WebPlayer.swf?version=AFrontend.5.7.0.1509&amp;permalinkId=v95981404eQdfjw2E&amp;player=videodetailsembedded&amp;videoAutoPlay=0&amp;id=anonymous" type="application/x-shockwave-flash" width="410"></embed></object></p>'


Test Vimeo Video

>>> s = "http://www.vimeo.com/1496152"
>>> markdown.markdown(s, ['video'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="321" mozallowfullscreen="true" src="https://player.vimeo.com/video/1496152" webkitallowfullscreen="true" width="500"></iframe>\\n</p>'

Test Vimeo Video with some GET values

>>> s = "http://vimeo.com/1496152?test=test"
>>> markdown.markdown(s, ['video'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="321" mozallowfullscreen="true" src="https://player.vimeo.com/video/1496152" webkitallowfullscreen="true" width="500"></iframe>\\n</p>'


Test Yahoo! Video

# >>> s = "http://video.yahoo.com/watch/1981791/4769603"
# >>> markdown.markdown(s, ['video'])
# '<p><object data="http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40" height="322" type="application/x-shockwave-flash" width="512"><param name="movie" value="http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40" /><param name="allowfullscreen" value="true" /><param name="flashVars" value="id=4769603&amp;vid=1981791" /></object></p>'

Test Yahoo! screen

>>> s = 'https://screen.yahoo.com/popular/leto-nicholson-ledger-hamill-play-231207869.html'
>>> markdown.markdown(s, ['video'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="360" mozallowfullscreen="true" scrolling="no" src="https://screen.yahoo.com/popular/leto-nicholson-ledger-hamill-play-231207869.html?format=embed" webkitallowfullscreen="true" width="640"></iframe>\\n</p>'


Test Youtube

>>> s = "http://www.youtube.com/watch?v=u1mA-0w8XPo&hd=1&fs=1&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1"
>>> markdown.markdown(s, ['video'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="315" mozallowfullscreen="true" src="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" webkitallowfullscreen="true" width="420"></iframe>\\n</p>'


Test Youtube with argument

>>> markdown.markdown(s, ['video(youtube_width=200,youtube_height=100)'])
'<p>\\n<iframe allowfullscreen="true" frameborder="0" height="100" mozallowfullscreen="true" src="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" webkitallowfullscreen="true" width="200"></iframe>\\n</p>'


Test Youtube Link

>>> s = "[Youtube link](http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1)"
>>> markdown.markdown(s, ['video'])
'<p><a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1">Youtube link</a></p>'


Test HTML Youtube Link

>>> s = 'Here is a link to <a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1">a YouTube movie</a>.'
>>> markdown.markdown(s, ['video'])
'<p>Here is a link to <a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1">a YouTube movie</a>.</p>'
"""

import markdown
try:
    from markdown.util import etree
except:
    from markdown import etree

version = "0.1.6"


class VideoExtension(markdown.Extension):
    def __init__(self, **configs):
        self.config = {
            'dailymotion_width': ['480', 'Width for Dailymotion videos'],
            'dailymotion_height': ['270', 'Height for Dailymotion videos'],
            'gametrailers_width': ['512', 'Width for Gametrailers videos'],
            'gametrailers_height': ['288', 'Height for Gametrailers videos'],
            'metacafe_width': ['440', 'Width for Metacafe videos'],
            'metacafe_height': ['248', 'Height for Metacafe videos'],
            'veoh_width': ['410', 'Width for Veoh videos'],
            'veoh_height': ['341', 'Height for Veoh videos'],
            'vimeo_width': ['500', 'Width for Vimeo videos'],
            'vimeo_height': ['321', 'Height for Vimeo videos'],
            'yahoo_width': ['640', 'Width for Yahoo! videos'],
            'yahoo_height': ['360', 'Height for Yahoo! videos'],
            'youtube_width': ['420', 'Width for Youtube videos'],
            'youtube_height': ['315', 'Height for Youtube videos'],
        }

        # Override defaults with user settings
        if configs is not None:
            for key, value in configs.items():
                self.setConfig(key, value)

    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(
            md, 'dailymotion', Dailymotion,
            r'([^("]|^)https?://www\.dailymotion\.com/video/(?P<dailymotionid>[^_]+)_\S+')
        self.add_inline(
            md, 'gametrailers', Gametrailers,
            r'([^("]|^)https?://www.gametrailers.com/video/[a-z0-9-]+/(?P<gametrailersid>\d+)')
        self.add_inline(
            md, 'metacafe', Metacafe,
            r'([^("]|^)https?://www\.metacafe\.com/watch/(?P<metacafeid>[-\w]+)/\S+')
        self.add_inline(
            md, 'veoh', Veoh,
            r'([^("]|^)https?://www\.veoh\.com/\S*(#watch%3D|watch/)(?P<veohid>\w+)')
        self.add_inline(
            md, 'vimeo', Vimeo,
            r'([^("]|^)https?://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
        self.add_inline(
            md, 'yahoo', Yahoo,
            r'([^("]|^)https?://video\.yahoo\.com/watch/(?P<yahoovid>\d+)/(?P<yahooid>\d+)')
        self.add_inline(
            md, 'yahooscreen', YahooScreen,
            r'([^("]|^)https?://screen.yahoo.com/(?P<yahooscreenid>[-\w/]+).html')
        # http://www.youtube.com/watch?v=R2fwHjLvvk4&feature=rec-LGOUT-exp_stronger_r2-2r-1-HM
        # http://www.youtube.com/v/0Xfh5iBBh4Y?fs=1&hl=en_US
        self.add_inline(
            md, 'youtube', Youtube,
            r'([^("\']|^)https?://www\.youtube\.com/(?:watch\?\S*v=|v\/)(?P<youtubeargs>[A-Za-z0-9_&=-]+)\S*')
        self.add_inline(
            md, 'youtubeshort', YoutubeShort,
            r'([^("\']|^)https?://youtu\.be/(?P<youtubeargs>.*)\S*')


class Dailymotion(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.dailymotion.com/embed/video/{}'.format(m.group('dailymotionid'))
        width = self.ext.config['dailymotion_width'][0]
        height = self.ext.config['dailymotion_height'][0]
        return iframe_object(url, width, height)


class Gametrailers(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.gametrailers.com/remote_wrap.php?mid={}'.format(
            m.group('gametrailersid')).split('/')[-1]
        width = self.ext.config['gametrailers_width'][0]
        height = self.ext.config['gametrailers_height'][0]
        return flash_object(url, width, height)


class Metacafe(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        if m.group(1) == '\\':
            pass
        url = 'http://www.metacafe.com/embed/{}/'.format(m.group('metacafeid'))
        width = self.ext.config['metacafe_width'][0]
        height = self.ext.config['metacafe_height'][0]
        return iframe_object(url, width, height)


class Veoh(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.veoh.com/swf/webplayer/WebPlayer.swf?version=AFrontend.5.7.0.1509&permalinkId={}&player=videodetailsembedded&videoAutoPlay=0&id=anonymous'.format(m.group('veohid'))
        width = self.ext.config['veoh_width'][0]
        height = self.ext.config['veoh_height'][0]
        obj = flash_object(url, width, height)
        param = etree.Element('embed')
        param.set('src', url)
        param.set('type', 'application/x-shockwave-flash')
        param.set('allowfullscreen', 'true')
        param.set('width', str(width))
        param.set('height', str(height))
        param.set('name', 'veohFlashPlayerEmbed')
        obj.append(param)
        return obj


class Vimeo(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'https://player.vimeo.com/video/{}'.format(m.group('vimeoid'))
        width = self.ext.config['vimeo_width'][0]
        height = self.ext.config['vimeo_height'][0]
        return iframe_object(url, width, height)


class Yahoo(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = "http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40"
        width = self.ext.config['yahoo_width'][0]
        height = self.ext.config['yahoo_height'][0]
        obj = flash_object(url, width, height)
        param = etree.Element('param')
        param.set('name', 'flashVars')
        param.set('value', "id={}&vid={}".format((m.group('yahooid'),
                                                  m.group('yahoovid'))))
        obj.append(param)
        return obj


class YahooScreen(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = "https://screen.yahoo.com/{}.html?format=embed".format(m.group('yahooscreenid'))
        width = self.ext.config['yahoo_width'][0]
        height = self.ext.config['yahoo_height'][0]
        obj = iframe_object(url, width, height)
        obj.set('scrolling', 'no')
        return obj


class Youtube(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.youtube.com/v/{}'.format(m.group('youtubeargs'))
        width = self.ext.config['youtube_width'][0]
        height = self.ext.config['youtube_height'][0]
        return iframe_object(url, width, height)


class YoutubeShort(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.youtube.com/v/{}'.format(m.group('youtubeargs'))
        width = self.ext.config['youtube_width'][0]
        height = self.ext.config['youtube_height'][0]
        return iframe_object(url, width, height)


def iframe_object(url, width, height):
    obj = etree.Element('iframe')
    obj.set('width', str(width))
    obj.set('height', str(height))
    obj.set('src', url)
    obj.set('frameborder', "0")
    obj.set('webkitallowfullscreen', 'true')
    obj.set('mozallowfullscreen', 'true')
    obj.set('allowfullscreen', 'true')
    return obj


def flash_object(url, width, height):
    obj = etree.Element('object')
    obj.set('width', str(width))
    obj.set('height', str(height))
    param = etree.Element('param')
    param.set('name', 'movie')
    param.set('value', url)
    obj.append(param)
    param = etree.Element('param')
    param.set('name', 'allowfullscreen')
    param.set('value', 'true')
    obj.append(param)
    return obj


def makeExtension(**kwargs):
    return VideoExtension(**kwargs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
