from plone.app.users.browser.account import AccountPanelSchemaAdapter
from wccpilgrimageblog.theme.userdataschema import IEnhancedUserDataSchema
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataSchemaAdapter(UserDataPanelAdapter):
    #schema = IEnhancedUserDataSchema
    
    def get_twitter_username(self):
        return self.context.getProperty('twitter_username', '')
    def set_twitter_username(self, value):
        return self.context.setMemberProperties({'twitter_username': value})
    twitter_username = property(get_twitter_username, set_twitter_username)