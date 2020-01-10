import bluesky
from bluesky import preprocessors as bpp
from bluesky import plan_stubs as bps

from . import cam_utils


def jet_track(camera, params, *, burst_images=20, md=None):
    if md is None:
        md = {}

    @bpp.run_decorator(md=md)
    def inner():
        roi_start = camera.ROI.min_xyz

        for i in range(5):
            yield from bps.checkpoint()

            roi_image = cam_utils.get_burst_avg(burst_images, camera.ROI_image)
            rho, theta = cam_utils.jet_detect(roi_image)

            info = yield from bps.trigger_and_read([params, roi_start],
                                                   name='primary')
            beam_x = info[params.beam_x.name]['value']
            beam_y = info[params.beam_y.name]['value']
            beam_x_px = info[params.beam_x_px.name]['value']
            beam_y_px = info[params.beam_y_px.name]['value']
            cam_roll = info[params.cam_roll.name]['value']
            pxsize = info[params.pxsize.name]['value']
            roi_x = info[roi_start.min_x.name]['value']
            roi_y = info[roi_start.min_y.name]['value']

            # check x-ray beam position
            cam_x, cam_y = cam_utils.get_cam_coords(
                beam_x_px, beam_y_px, cam_roll=cam_roll, pxsize=pxsize)

            # find distance from jet to x-rays
            jet_x = cam_utils.get_jet_x(rho, theta, roi_x, roi_y, pxsize=pxsize,
                                        cam_x=cam_x, cam_y=cam_y, beam_x=beam_x,
                                        beam_y=beam_y, cam_roll=cam_roll)
            yield from bps.mv(params.cam_x, cam_x)
            yield from bps.mv(params.cam_y, cam_y)
            yield from bps.mv(params.jet_x, jet_x)

    return (yield from inner())
    # return bpp.rewindable_wrapper(inner, rewindable=True)


if __name__ == '__main__':
    from bluesky.utils import install_kicker
    install_kicker()
