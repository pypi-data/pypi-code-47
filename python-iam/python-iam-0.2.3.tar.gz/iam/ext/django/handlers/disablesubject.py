import ioc
from aorta.model.cqrs import CommandHandler

from iam.ext.django.models import Subject


@ioc.inject('publisher', 'EventPublisher')
@CommandHandler.register_for('unimatrix.iam.DisableSubject')
class DisableSubjectCommandHandler(CommandHandler):

    def handle(self, dto):
        """Disable a subject by its :attr:`~iam.ext.django.models.Subject.id`
        attribute.
        """
        Subject.objects.disable(id=dto.subject.id)
        self.publisher.observe('unimatrix.iam.SubjectDisabled', {
            'subject': dict(dto.subject)
        })
