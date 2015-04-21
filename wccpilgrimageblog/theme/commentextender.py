
from plone.app.discussion.browser.comments import CommentForm
from plone.directives import form
from zope import schema
from plone.app.discussion.interfaces import IComment

class defaultUserNotification(CommentForm):
    def __init__(self, context, request):
        super(defaultUserNotification, self).__init__(context, request)
        

@form.default_value(field=IComment['user_notification'])
def defaultValue(self):
    return True