from moderation import moderation
from moderation.moderator import GenericModerator

from mdmanager.models import product


class ProductModerator(GenericModerator):
    # Add your moderator settings for AnotherModel here
    notify_user = False
    auto_approve_for_superusers = False
    auto_approve_for_staff = False
    visible_until_rejected = True


#moderation.register(product)  # Uses default moderation settings
moderation.register(product, ProductModerator)  # Uses custom moderation settings
