import ioc
from aorta.model.cqrs import CommandHandler

from iam.ext.django.models import Subject


@ioc.inject('publisher', 'EventPublisher')
@CommandHandler.register_for('unimatrix.iam.EnableSubject')
class EnableSubjectCommandHandler(CommandHandler):

    def handle(self, dto):
        """Enable a subject by its :attr:`~iam.ext.django.models.Subject.id`
        attribute.
        """
        Subject.objects.enable(id=dto.subject.id)
        self.publisher.observe('unimatrix.iam.SubjectEnabled', {
            'subject': dict(dto.subject)
        })

