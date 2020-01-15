import argparse
import pystk
from time import time
from copy import deepcopy


def benchmark(cfg):
    pystk.init(cfg)
    race = pystk.Race(pystk.RaceConfig(track=args.track))
    race.start()
    race.step()
    t0 = time()
    for it in range(args.steps):
        race.step()
    race_time = time() - t0
    race.stop()
    del race
    pystk.clean()
    return race_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--track', default='lighthouse')
    parser.add_argument('-s', '--steps', default=500, type=int)
    args = parser.parse_args()

    cfg = pystk.GraphicsConfig.ld()


    timings = {}

    for cfg in [pystk.GraphicsConfig.ld(), pystk.GraphicsConfig.sd(), pystk.GraphicsConfig.hd()]:
        cfg.screen_width = 200
        cfg.screen_height = 150
        cfg_dict = {k: getattr(cfg, k) for k in dir(cfg) if k[0] != '_' and not callable(getattr(cfg, k))}
        del cfg_dict['render_window']
        del cfg_dict['screen_width']
        del cfg_dict['screen_height']

        cfg_time = benchmark(cfg)

        for o in cfg_dict:
            new_cfg = deepcopy(cfg)
            setattr(new_cfg, o, not cfg_dict[o])
            new_time = benchmark(new_cfg)
            if o not in timings:
                timings[o] = []
            if cfg_dict[o]:
                timings[o].append(cfg_time - new_time)
            else:
                timings[o].append(new_time - cfg_time)

    for o, v in timings.items():
        print(o, sum(v) / len(v))



    #
    # for config in [pystk.GraphicsConfig.ld(), pystk.GraphicsConfig.sd(), pystk.GraphicsConfig.hd(), None]:
    #     print(config)
    #     t0 = time()
    #     render = True
    #     if config is None:
    #         config = pystk.GraphicsConfig.ld()
    #         render = False
    #     config.screen_width = 320
    #     config.screen_height = 240
    #     pystk.init(config)
    #     init_time, t0 = time() - t0, time()
    #
    #     config = pystk.RaceConfig(render=render)
    #     if args.kart != '':
    #         config.players[0].kart = args.kart
    #     if args.track is not None:
    #         config.track = args.track
    #     if args.step_size is not None:
    #         config.step_size = args.step_size
    #     for i in range(1, args.num_player):
    #         config.players.append(pystk.PlayerConfig(args.kart, pystk.PlayerConfig.Controller.AI_CONTROL))
    #
    #     race = pystk.Race(config)
    #     race_time, t0 = time() - t0, time()
    #
    #     race.start()
    #     start_time, t0 = time() - t0, time()
    #
    #     for it in range(500):
    #         race.step()
    #     step_time, t0 = time() - t0, time()
    #     for it in range(5):
    #         race.restart()
    #     restart_time, t0 = time() - t0, time()
    #
    #     print('  graphics', init_time)
    #     print('  race config', race_time)
    #     print('  start', start_time)
    #     print('  restart', restart_time / 5.)
    #     print('  step FPS', 500. / step_time)
    #
    #     race.stop()
    #     del race
    #     pystk.clean()
