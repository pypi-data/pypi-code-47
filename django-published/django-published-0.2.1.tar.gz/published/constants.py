NEVER_AVAILABLE = -1
AVAILABLE = 1
AVAILABLE_AFTER = 0

PUBLISH_CHOICES = (
    (NEVER_AVAILABLE, 'Never Available'),
    (AVAILABLE, 'Available Now'),
    (AVAILABLE_AFTER, 'Available after "Publish Date"'),
)

__all__ = ['PUBLISH_CHOICES', 'NEVER_AVAILABLE', 'AVAILABLE_AFTER', 'AVAILABLE']
