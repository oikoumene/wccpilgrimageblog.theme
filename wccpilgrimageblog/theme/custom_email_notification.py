import logging
from zope.component import queryUtility
from Products.CMFCore.utils import getToolByName
from smtplib import SMTPException
from plone.app.discussion.interfaces import IDiscussionSettings
from plone.registry.interfaces import IRegistry
from zope.i18n import translate
from plone.app.discussion import PloneAppDiscussionMessageFactory as _
from Acquisition import aq_parent, aq_base, Implicit
from zope.i18nmessageid import Message
from Products.CMFPlone.utils import safe_unicode

MAIL_NOTIFICATION_MESSAGE = _(
    u"mail_notification_message",
    default=u"A comment on '${title}' "
            u"has been posted here: ${link}\n\n"
            u"---\n"
            u"${text}\n"
            u"---\n")

logger = logging.getLogger("plone.app.discussion")

def notify_user(obj, event):
    """Tell users when a comment has been added.

       This method composes and sends emails to all users that have added a
       comment to this conversation and enabled user notification.

       This requires the user_notification setting to be enabled in the
       discussion control panel.
    """

    # Check if user notification is enabled
    registry = queryUtility(IRegistry)
    settings = registry.forInterface(IDiscussionSettings, check=False)
    if not settings.user_notification_enabled:
        #return
        pass

    # Get informations that are necessary to send an email
    mail_host = getToolByName(obj, 'MailHost')
    portal_url = getToolByName(obj, 'portal_url')
    portal = portal_url.getPortalObject()
    sender = portal.getProperty('email_from_address')

    # Check if a sender address is available
    if not sender:
        return

    # Compose and send emails to all users that have add a comment to this
    # conversation and enabled user_notification.
    conversation = aq_parent(obj)
    content_object = aq_parent(conversation)

    # Avoid sending multiple notification emails to the same person
    # when he has commented multiple times.
    emails = set()
    for comment in conversation.getComments():
        obj_is_not_the_comment = obj != comment
        valid_user_email = comment.author_email
        if valid_user_email:
            emails.add(comment.author_email)
    
    if not emails:
        return

    subject = translate(_(u"A comment has been posted."),
                        context=obj.REQUEST)
    message = translate(
        Message(
            MAIL_NOTIFICATION_MESSAGE,
            mapping={
                'title': safe_unicode(content_object.title),
                'link': content_object.absolute_url() + '/view#' + obj.id,
                'text': obj.text
            }
        ),
        context=obj.REQUEST
    )
    for email in emails:
        # Send email
        try:
            mail_host.send(message,
                           email,
                           sender,
                           subject,
                           charset='utf-8')
        except SMTPException:
            logger.error('SMTP exception while trying to send an ' +
                         'email from %s to %s',
                         sender,
                         email)