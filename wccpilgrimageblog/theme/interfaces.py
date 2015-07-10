from zope.interface import Interface
#from quintagroup.z3cform.captcha import Captcha, CaptchaWidgetFactory
from wccpilgrimageblog.theme import MessageFactory as _
from quintagroup.formlib.captcha import Captcha

class IProductSpecific(Interface):
    pass


class IExtendRegistrationForm(Interface):
    """Marker interface for my custom registration form
    """

class ICaptchaSchema(Interface):
    captcha = Captcha(
        title=_(u'Type the code'),
        description=_(u'Type the code from the picture shown below.'))
