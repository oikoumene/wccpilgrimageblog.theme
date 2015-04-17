from zope.interface import implements
from zope import schema
from wccpilgrimageblog.theme import MessageFactory as _
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.users.browser.personalpreferences import UserDataPanel
from plone.z3cform.fieldsets import extensible
from z3c.form.field import Fields
from plone.app.users.browser.register import RegistrationForm
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider





class IEnhancedUserDataSchema(IUserDataSchema):
    # ...
    twitter_username = schema.TextLine(
        title=_(u'label_twitter', default=u'Twitter'),
        description=_(u'desc_twitter_username',
                      default=u"Enter your Twitter Account"),
        required=False,
        )
    
class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema
    
    
@adapter(Interface, IDefaultBrowserLayer, UserDataPanel)
class UserDataPanelExtender(extensible.FormExtender):
    def update(self):
        fields = Fields(
            IEnhancedUserDataSchema,
            prefix="IEnhancedUserDataSchema")
        self.add(fields)
        
@adapter(Interface, IDefaultBrowserLayer, RegistrationForm)
class RegistrationPanelExtender(extensible.FormExtender):
    def update(self):
        fields = Fields(IEnhancedUserDataSchema)
        #NB: Not omitting the accept field this time, we want people to check it
        self.add(fields)