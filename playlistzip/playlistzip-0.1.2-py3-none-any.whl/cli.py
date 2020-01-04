import re
import argparse
import json
import pycurl
from jsonpath_rw import jsonpath, parse
from io import BytesIO

def combine_episodes(episode_dicts):
    combo = {}
    for ep, v in episode_dicts[0].items():
        matching = [ d[ep][1] if ep in d else None for d in episode_dicts[1:] ]
        if any(matching):
            combo[ep] = ( v[0], [ v[1] ] + matching )
    return combo;

def pick_json_element(body, regex):
    m = regex.search(body)
    return m.group(1)

def get_episode(text, regs):
    m = first_true(map(lambda v:v.search(text), regs), bool)
    return m.group(1) if m else False

def first_true(iterable, pred=None, default=False):
    return next(filter(pred, iterable), default)

def get_episodes(pl_json, compiled_regs, index_start=0):
    fvideo = parse('$..playlistVideoRenderer')
    out_dict = {}

    for i, m in enumerate( fvideo.find(pl_json) ):
        title = m.value['title']['runs'][0]['text']
        vid = m.value['videoId']

        episode = ( i+1+index_start ) if compiled_regs is None else get_episode(title, compiled_regs)
        if episode:
            out_dict[episode] = (title, vid)
    return out_dict

def get_next_token(pl_json):
    ftoken = parse('$..nextContinuationData.continuation')
    found = ftoken.find(pl_json)
    return found[0].value if len(found) > 0 else False

def fetch(url, agent, headers):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.USERAGENT, agent)
    c.setopt(c.HTTPHEADER, headers)
    c.perform()
    c.close()
    return buffer.getvalue()

def collect_eps(eps, token, agent, headers, compiled_regs):
    while bool( token ):
        url = "https://m.youtube.com/playlist?ctoken={}&pbj=1".format(token)
        body = fetch(url, agent, headers)
        njson = json.loads(body)
        token = get_next_token(njson)
        eps.update(get_episodes(njson, compiled_regs, len(eps) ))
    return eps

def fetch_eps( playlist_id, find_json_regex, compiled_regs ):
    agent = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    headers = [
            "X-YouTube-Client-Name: 2",
            "X-YouTube-Client-Version: 2.20191115.05.00"
            ]
    url = "https://m.youtube.com/playlist?list={}".format(playlist_id)
    body = fetch(url, agent, headers)
    pl_json = json.loads(pick_json_element(body.decode('utf-8'), find_json_regex))
    eps = get_episodes(pl_json, compiled_regs)
    next_token = get_next_token(pl_json)
    if bool( next_token ):
        eps = collect_eps(eps, next_token, agent, headers, compiled_regs)
    return eps

def compile_regs(first, second, third, fourth):
    default_regs = [ r'Episode ([0-9]{1,3})', r'#([0-9]{1,3})', r'([0-9]{1,3})' ]
    dregs_compiled = [ re.compile(reg) for reg in default_regs ]
    return [
        compile_reg_list(first) if first else dregs_compiled,
        compile_reg_list(second) if second else dregs_compiled,
        compile_reg_list(third) if third else dregs_compiled,
        compile_reg_list(fourth) if fourth else dregs_compiled,
    ]

def compile_reg_list(regs):
    return [ re.compile(r) for r in regs ]

def getLink(vids):
    params = '&t=0&v='.join([vid for vid in vids if vid is not None]) + '&t=0'
    return f'https://viewsync.net/watch?v={params}'

def run( playlists, 
        first_regex=[], second_regex=[], third_regex=[], fourth_regex=[],
        join_by_index=False
        ):

    # json finder
    jf = re.compile(r'initial-data"><!-- (.*?) -->')

    if join_by_index:
        cregs = None
    else:
        cregs = compile_regs(first_regex, second_regex, third_regex, fourth_regex)
    episode_dicts = [ fetch_eps(pl, jf, cregs[i] if cregs else None) for i, pl in enumerate(playlists) ]

    combined = combine_episodes(episode_dicts)
    if join_by_index is False:
        csorted = sorted(combined.items(), key=lambda v:int(v[0]))
    else:
        csorted = combined.items()

    final_list = []
    for episode_num, groupTuple in csorted:
        title, vids = groupTuple
        link = getLink(vids)
        ep_dict = {
            'episode': episode_num,
            'title': title,
            'url': link
        }
        final_list.append(ep_dict)
    return final_list

def main():
    parser = argparse.ArgumentParser(description='Join two to four youtube playlists into viewsync links')
    parser.add_argument('playlists', nargs='+')
    parser.add_argument('--first-regex', action='append')
    parser.add_argument('--second-regex', action='append')
    parser.add_argument('--third-regex', action='append')
    parser.add_argument('--fourth-regex', action='append')
    parser.add_argument('--join-by-index', action='store_true')

    parser.add_argument('--omit-title', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()

    ep_dicts = run(args.playlists,
            args.first_regex, 
            args.second_regex, 
            args.third_regex, 
            args.fourth_regex,
            args.join_by_index)

    if args.json:
        print(json.dumps(ep_dicts))
    else:
        for ep in ep_dicts:
            print( ep["url"] if args.omit_title else ' '.join([ep["title"], ep["url"]]) )

