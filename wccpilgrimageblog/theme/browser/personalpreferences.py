from plone.app.users.browser.personalpreferences import PersonalPreferencesPanel
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from zope.formlib import form
from wccpilgrimageblog.theme.userdataschema import IEnhancedUserDataSchema

class CustomPersonalPreferencesPanel(UserDataPanelAdapter):
    
    form_fields = form.FormFields(IEnhancedUserDataSchema)
    # Apply same widget overrides as in the base class
    