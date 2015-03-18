from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from Products.CMFCore.interfaces import ISiteRoot

grok.templatedir('templates')

class posts_by_author_view(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def contents(self):
        results = []
        request = self.request
        author = None
        if request.form:
            if 'name' in request.form:
                author = request.form['name']
                results = self.catalog.unrestrictedSearchResults(portal_type='News Item',
                                                                      sort_on='created',
                                                                      sort_order='reverse',
                                                                      review_state='published',
                                                                      Creator=author)
        
    
        return results
    