from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from Products.CMFCore.interfaces import ISiteRoot
from plone.app.discussion.interfaces import IConversation, IComment

grok.templatedir('templates')

class posts_by_author_view(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def contents(self):
        results = []
        author = self.authorValue()
        brains = self.catalog.searchResults(portal_type='News Item',
                                                  sort_on='created',
                                                  sort_order='reverse',
                                                  review_state='published')
        for brain in brains:
            if author in brain.listCreators or author == '':
                results.append(brain)
        return results
    
    def authorValue(self):
        tag = ''
        request = self.request
        if request.form:
            if 'name' in request.form:
                tag = request.form['name']
        return tag
    
    def totalComments(self, context=None):
        comments = IConversation(context)
        return len(comments)
    