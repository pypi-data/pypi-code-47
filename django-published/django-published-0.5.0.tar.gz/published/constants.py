NEVER_AVAILABLE = 0
AVAILABLE = 1
AVAILABLE_AFTER = 2

PUBLISH_CHOICES = (
    (NEVER_AVAILABLE, 'Never Available'),
    (AVAILABLE, 'Available Now'),
    (AVAILABLE_AFTER, 'Available after "Publish Date"'),
)

__all__ = ['PUBLISH_CHOICES', 'NEVER_AVAILABLE', 'AVAILABLE_AFTER', 'AVAILABLE']
