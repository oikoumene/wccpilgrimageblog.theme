from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder

grok.templatedir('templates')

class homepage_customview(grok.View):
    grok.context(IATFolder)
    grok.require('zope2.View')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def contents(self):
        return self.catalog.unrestrictedSearchResults({'query':'/'.join(self.context.getPhysicalPath()), 'depth':1},
                                                        portal_type='News Item',
                                                        sort_on='created',
                                                        sort_order='reverse')[:4]
    
        
    