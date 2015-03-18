from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from plone.app.discussion.interfaces import IConversation, IComment

grok.templatedir('templates')

class pages_listing_customview(grok.View):
    grok.context(IATFolder)
    grok.require('zope2.View')
    
    def totalComments(self, context=None):
        comments = IConversation(context)
        return len(comments)
    
