from collective.grok import gs
from wccpilgrimageblog.theme import MessageFactory as _

@gs.importstep(
    name=u'wccpilgrimageblog.theme', 
    title=_('wccpilgrimageblog.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wccpilgrimageblog.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
