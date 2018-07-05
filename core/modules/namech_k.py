#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:Get info on a specific person with his username.

from core.lib import colors
from core.lib import completer
import readline
import json

#requirements
import requests

#colors
C = colors.Palette()


class module_element(object):

    def __init__(self):
        self.title = "Namech_k\n"
        self.require = {
            'username':{'value':'', 'required':'yes'}
        }

        self.export = []

        #completer
        comp = completer.Module(self.require)
        readline.parse_and_bind("tab: complete")
        readline.set_completer(comp.complete)

        self.service = """Facebook YouTube Twitter Instagram Blogger GooglePlus
        Twitch Reddit Ebay Wordpress Pinterest Yelp Slack Github Basecamp Tumblr
        Flickr Pandora ProductHunt Steam MySpace Foursquare OkCupid Vimeo UStream
        Etsy SoundCloud BitBucket Meetup CashMe DailyMotion Aboutme Disqus Medium
        Behance Photobucket Bitly CafeMom coderwall Fanpop deviantART GoodReads
        Instructables Keybase Kongregate LiveJournal StumbleUpon AngelList LastFM
        Slideshare Tripit Fotolog Vine PayPal Dribbble Imgur Tracky Flipboard Vk
        kik Codecademy Roblox Gravatar Trip Pastebin Coinbase BlipFM Wikipedia
        Ello StreamMe IFTTT WebCredit CodeMentor Soupio Fiverr Trakt Hackernews
        five00px Spotify POF Houzz Contently BuzzFeed TripAdvisor HubPages Scribd
        Venmo Canva CreativeMarket Bandcamp Wikia ReverbNation foodspotting Wattpad
        Designspiration ColourLovers eyeem Miiverse KanoWorld AskFM Smashcast Badoo
        Newgrounds younow Patreon Mixcloud Gumroad Quora"""

    def get_options(self, name):
        if name in self.require:
            return self.require[name]['value']
        else:
            return False


    def main(self):
        print "{}{} Running module: {}{}".format(C.OK, C.GREEN, self.title, C.END)
        username = self.get_options('username')
        server = 'https://namechk.com/'
        data = [ ('q', '{}'.format(username)) ]
        try:
            print "{} Try loading username: {}".format(C.WAR, username)
            req = requests.post(server, data=data)
            token = json.loads(req.content)
            token = token['valid']
            flag = True
        except:
            print "{} Can't open URL".format(C.ERROR)
            flag = False

        if flag == True:
            self.service = self.service.split()
            for item in self.service:
                try:
                    data = [
                        ('service', item),
                        ('token', token),
                        ('fat', 'xwSgxU58x1nAwVbP6+mYSFLsa8zkcl2q6NcKwc8uFm+TvFbN8LaOzmLOBDKza0ShvREINUhbwwljVe30LbKcQw==')
                    ]
                    req = requests.post(server + 'services/check', data=data)
                    verify = json.loads(req.content)
                    if verify['status'] == 'unavailable':
                        result = '{:15} : {}{}{}'.format(item, C.GREEN, verify['callback_url'], C.END)
                        print " - " + result
                        self.export.append(result)
                except KeyboardInterrupt:
                    print "[STOP]"
                    break
