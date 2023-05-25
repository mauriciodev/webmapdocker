from moderation import moderation
from moderation.moderator import GenericModerator

from mdmanager.models import metadata


class MetadataModerator(GenericModerator):
    # Add your moderator settings for AnotherModel here
    notify_user = False
    auto_approve_for_superusers = False
    auto_approve_for_staff = False
    visible_until_rejected = False


#moderation.register(metadata)  # Uses default moderation settings
moderation.register(metadata, MetadataModerator)  # Uses custom moderation settings
