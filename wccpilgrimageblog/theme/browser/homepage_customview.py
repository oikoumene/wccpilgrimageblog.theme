from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from Products.CMFCore.interfaces import ISiteRoot
from plone.app.discussion.interfaces import IConversation, IComment
import datetime

grok.templatedir('templates')

class homepage_customview(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def contents(self):
        # results = []
        brains = self.catalog.searchResults(portal_type='News Item',
                                            sort_on='created',
                                            sort_order='reverse',)[:4]
        # for brain in brains:
        #     effective_date = brain.effective
        #     if effective_date <= self.time():
        #         results.append(brain)
        #         if len(results) == 4:
        #             break;
        return brains
        
    def totalComments(self, context=None):
        comments = IConversation(context)
        return len(comments)
    # def time(self):
    #     return datetime.datetime.now().strftime("%m/%d/%Y %H:%M")
