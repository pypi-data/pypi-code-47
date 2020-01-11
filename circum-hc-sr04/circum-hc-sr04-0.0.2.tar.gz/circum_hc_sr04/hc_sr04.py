import click
import circum.endpoint
import copy
import logging

from threading import Semaphore, Thread
from Bluetin_Echo import Echo


logger = logging.getLogger(__name__)
tracking_semaphore = None
tracking_info = {"objects": []}
vector_info = []
updated = False
max_seen = 0


def _get_targets(echo: Echo, samples: int, threshold: int) -> [int]:
    global max_seen
    result = echo.read('cm', samples)
    max_seen = max(result, max_seen)
    if result < max_seen - threshold:
        return [result]
    return []


def _update_thread(echo: Echo, samples: int):
    global tracking_info
    global vector_info
    global updated

    while True:
        targets = _get_targets(echo, samples)

        tracking_semaphore.acquire()

        if targets and targets is not None:
            tracking_info["objects"] = \
                [{"x": 0, "y": 0, "z": target / 100} for target in targets]
            for i, target in enumerate(targets):
                logger.debug('Target distance: {}\n'.format(target))
        else:
            tracking_info["objects"] = []

        updated = True

        tracking_semaphore.release()
        # time.sleep(update_interval)


def run_hc_sr04(hc_sr04_args: {}) -> {}:
    global updated
    ret = None
    tracking_semaphore.acquire()
    if updated:
        ret = copy.deepcopy(tracking_info)
        updated = False
    tracking_semaphore.release()
    return ret


@click.command()
@click.option('--num-samples',
              required=False,
              default=5,
              type=int,
              help='The number of samples to average per reading.')
@click.option('--trigger-pin',
              required=True,
              type=int,
              help='The pin used to trigger the HC-SR04.')
@click.option('--echo-pin',
              required=True,
              type=int,
              help='The pin the HC-SR04 will signal the echo on.')
@click.option('--speed-of-sound',
              required=False,
              default=343,
              type=int,
              help='Override the speed of sound to a calibrated value in m/s.')
@click.option('--threshold',
              required=False,
              default=20,
              type=int,
              help='Only register an object if it is at least threshold cm closer than the furthest distance '
                   'returned so far. This accounts for unmoving objects in the sensors range at the cost of '
                   'missing moving objects that are present when the sensor starts.')
@click.pass_context
def hc_sr04(ctx,
            num_samples: int,
            trigger_pin: int,
            echo_pin: int,
            speed_of_sound: int,
            threshold: int):
    global tracking_semaphore
    tracking_semaphore = Semaphore()

    echo = Echo(trigger_pin, echo_pin, speed_of_sound)

    tracker_thread = Thread(target=_update_thread, args=[echo, num_samples, threshold])
    tracker_thread.daemon = True
    tracker_thread.start()
    circum.endpoint.start_endpoint(ctx, "cam", run_hc_sr04)
