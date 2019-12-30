import ioc

from aorta.model.cqrs import CommandHandler


@ioc.inject('publisher', 'EventPublisher')
@ioc.inject('service', 'iam.RegisterUserService')
@CommandHandler.register_for('unimatrix.iam.RegisterUser')
class RegisterUserCommandHandler(CommandHandler):

    def handle(self, dto):
        pass
