from collective.grok import gs
from wcc.pilgrimagetheme import MessageFactory as _

@gs.importstep(
    name=u'wcc.pilgrimagetheme', 
    title=_('wcc.pilgrimagetheme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.pilgrimagetheme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
