# -*- coding: utf-8 -*-

import scrapy
import json


class BwinSpider(scrapy.Spider):
    name = 'bwin'
    start_urls = ['https://cds-api.bwin.com/bettingoffer/fixtures?x-bwin-accessid=NTZiMjk3OGMtNjU5Mi00NjA5LWI2MWItZmU4MDRhN2QxZmEz&lang=en&country=RU&userCountry=RU&fixtureTypes=Standard&state=Latest&offerMapping=Filtered&offerCategories=Gridable&fixtureCategories=Gridable,NonGridable,Other&sportIds=4&regionIds=']


    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        all_games = jsonresponse.get('fixtures')
        for x in all_games:
            league = x.get('competition').get('name').get('value')
            home = x.get('games')[0].get('results')[0].get('name').get('value')
            away = x.get('games')[0].get('results')[2].get('name').get('value')
            _1 = x.get('games')[0].get('results')[0].get('odds')
            _x = x.get('games')[0].get('results')[1].get('odds')
            _2 = x.get('games')[0].get('results')[2].get('odds')

            yield {
                'league': league,
                'home': home,
                'away': away,
                '_1': _1,
                '_x': _x,
                '_2': _2
            }