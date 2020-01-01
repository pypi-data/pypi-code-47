
demo1='''
import wpkit
from wpkit import node as n
from wpkit.node import components
from wpkit.web import bps,utils,request
from wpkit.web.bps import pan
app=wpkit.web.get_default_app(__name__)
bp_pan=pan.BluePan(__name__)
@bp_pan.route('/home',methods=['get'])
def f1():
    p=wpkit.basic.DirTree('./data')
    from wpkit.web.bps.pan import pages
    return pages.panpage.to_string()
@bp_pan.route('/data',methods=['post'])
@utils.parse_json
def f2(cmd):
    print(cmd)
    return 'testing'
app.add_blueprint(bp_pan)
app.sitemap['PanHome']='/pan/home'
print(app.sitemap)

'''
