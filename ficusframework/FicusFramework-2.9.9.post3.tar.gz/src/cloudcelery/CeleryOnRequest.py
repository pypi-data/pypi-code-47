from cloudcelery import celery
from schedule import TriggerActor
from munch import Munch
import json


@celery.task(name='tasks.on_request', bind=True, max_retries=2, default_retry_delay=1 * 6)
def on_request(self, protocol):
    """
    从celery接收协议
    :param self:
    :param protocol:
    :return:
    """
    print(f'protocol:{protocol}')

    body = Munch(json.loads(protocol))

    try:
        result = TriggerActor.handle_trigger(body, True)        # ResultVO
    except:
        pass

    try:
        return {'status': True,
                'data': 'asdfasdnfvasdfoiasjdofiasjdfoasnvcasodifjasodifjasonvasoidjfaosidjfasonfvsaoidjfasoidnvs'}
    finally:
        pass
