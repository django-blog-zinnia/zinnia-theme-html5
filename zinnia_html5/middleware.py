"""Middlewares for zinnia_html5"""
import re
from bs4 import BeautifulSoup

from django.utils.encoding import smart_str

INVALID_A_RELS = re.compile(r'(shortlink|archives|trackback)')


class DraftHTML5ValidatorCleaner(object):
    """
    This Middleware only exists for providing
    a strict compliance with HTML5 validators.

    The problem is that HTML5 is still in draft,
    and some microformats are not already allowed
    by the on-line validators.

    Instead of rewriting all the Zinnia's templates,
    it's easier to add this middleware and disable it
    when the HTML5 specifications will be completed
    and the on-line HTML5 validators up-to-date.

    So the HTML response will be cleaned of the
    unsupported attributes provided by Zinnia and
    expected for a Weblog app.
    """

    def remove_a_rel(self, soup):
        tags = soup.find_all('a', rel=INVALID_A_RELS)
        for t in tags:
            del t['rel']
            self.update_content = True

    def change_a_rel_tag_category(self, soup):
        tags = soup.find_all('a', rel='tag category')
        for t in tags:
            t['rel'] = 'tag'
            self.update_content = True

    def change_link_archives(self, soup):
        tags = soup.find_all('link', rel='archives')
        for t in tags:
            t['rel'] = 'alternate'
            self.update_content = True

    def remove_pubdate(self, soup):
        tags = soup.find_all(pubdate=True)
        for t in tags:
            del t['pubdate']
            self.update_content = True

    def process_response(self, request, response):
        if (not response.status_code == 200 or
                not '<html' in response.content):
            return response

        self.update_content = False
        soup = BeautifulSoup(smart_str(response.content), "html5lib")

        self.remove_pubdate(soup)
        self.remove_a_rel(soup)
        self.change_link_archives(soup)
        self.change_a_rel_tag_category(soup)

        if self.update_content:
            response.content = str(soup)

        return response
