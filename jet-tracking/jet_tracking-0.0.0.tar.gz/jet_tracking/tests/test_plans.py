import bluesky
from bluesky.callbacks.best_effort import BestEffortCallback

from databroker import Broker

import pytest
from . import conftest
from .. import plans


@pytest.fixture
def db(request):
    return Broker.named('temp')


@pytest.fixture
def RE(request, db):
    md = dict(scan_id=1000)
    RE = bluesky.RunEngine(md)
    bec = BestEffortCallback()
    RE.subscribe(bec)
    RE.subscribe(db.insert)
    return RE


@pytest.mark.parametrize("use_offaxis", [False, True])
def test_smoke_jet_track(RE, db, questar, parameters, offaxis_parameters,
                         use_offaxis):
    conftest.set_random_image(questar.image)
    conftest.set_random_image(questar.ROI_image)
    questar.ROI.min_xyz.min_x.sim_put(1)
    questar.ROI.min_xyz.min_y.sim_put(1)
    questar.ROI.min_xyz.min_z.sim_put(1)
    questar.ROI.min_xyz.min_x.kind = 'normal'
    questar.ROI.min_xyz.min_y.kind = 'normal'
    questar.ROI.min_xyz.min_z.kind = 'normal'
    if not use_offaxis:
        # _jet_calculate_step(camera=questar, params=parameters)
        RE(plans.jet_track(camera=questar, params=parameters, burst_images=5),
           my_metadata='test')
        print(db[-1])
    # else:
        # _jet_calculate_step_offaxis(camera=questar, params=offaxis_parameters)
