from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder

grok.templatedir('templates')

class homepage_customview(grok.View):
    grok.context(IATFolder)
    grok.require('zope2.View')
