import os
import gerberex
from gerberex.dxf import DxfFile
from gerberex.dxf_path import judge_containment
import gerber
from gerber.render.cairo_backend import GerberCairoContext
from gerberex.utility import is_equal_point, is_equal_value

def merge():
    ctx = gerberex.GerberComposition()
    a = gerberex.read('test.GTL')
    a.to_metric()
    ctx.merge(a)

    b = gerberex.read('test.GTL')
    b.to_metric()
    b.offset(0, 25)
    ctx.merge(b)

    c = gerberex.read('test2.GTL')
    c.to_metric()
    c.offset(0, 60)
    ctx.merge(c)

    c = gerberex.read('test.GML')
    c.to_metric()
    ctx.merge(c)

    ctx.dump('test-merged.GTL')

def merge2():
    ctx = gerberex.DrillComposition()
    a = gerberex.read('test.TXT')
    a.to_metric()
    ctx.merge(a)

    b = gerberex.read('test.TXT')
    b.to_metric()
    b.offset(0, 25)
    ctx.merge(b)

    c = gerberex.read('test2.TXT')
    c.to_metric()
    c.offset(0, 60)
    ctx.merge(c)

    ctx.dump('test-merged.TXT')


os.chdir(os.path.dirname(__file__))

file = gerberex.read('data/outline.dxf')

if True:
    error = 0.001

    inner = file.statements.close_paths[45]
    outer = file.statements.close_paths[51]

    #result = judge_containment(inner, outer, error)

    ostmts = [(i, outer.statements[i])
              for i in range(0, len(outer.statements))]
    loc = (55.4, 15)
    opart = list(filter(
        lambda s: is_equal_point(s[1].start, loc, error) or is_equal_point(s[1].end, loc, error),
        ostmts
    ))
    istmts = [(i, inner.statements[i]) for i in range(0, len(inner.statements))]
    loc = (55.4, 60)
    ipart = list(filter(lambda s: is_equal_point(s[1].end, loc, error), istmts))

    pts1 = opart[0][1].intersections_with_halfline(ipart[0][1].start, ipart[0][1].end, error)
    pts2 = opart[1][1].intersections_with_halfline(ipart[0][1].start, ipart[0][1].end, error)

file.to_metric()
file.width = 0.1
#file.statements.open_paths.clear()
file.write('outputs/outline-line.gml')
file.draw_mode = DxfFile.DM_FILL
file.write('outputs/outline-fill.gml')

ctx = gerberex.GerberComposition()
base = gerberex.rectangle(width=100, height=100, left=0, bottom=0, units='metric')
base.draw_mode = DxfFile.DM_FILL
ctx.merge(base)
file.negate_polarity()
ctx.merge(file)
ctx.dump('outputs/outline-fill-flip.gml')


base = gerberex.rectangle(width=105, height=95,
                          left=-5, bottom=-5, units='metric')
file = gerberex.read('data/complex.dxf')
file.to_metric()
file.draw_mode = DxfFile.DM_FILL
ctx = gerberex.GerberComposition()
ctx.merge(base)
ctx.merge(file)
ctx.dump('outputs/complex-fill.gml')
file.fill_mode = DxfFile.FM_SIMPLE
ctx = gerberex.GerberComposition()
ctx.merge(base)
ctx.merge(file)
ctx.dump('outputs/complex-fill-simple.gml')
file.draw_mode = DxfFile.DM_LINE
file.width = 0.2
ctx = gerberex.GerberComposition()
ctx.merge(base)
ctx.merge(file)
ctx.dump('outputs/complex-line.gml')
file.draw_mode = DxfFile.DM_MOUSE_BITES
file.width = 1.5
file.pitch = 3.5
ctx = gerberex.GerberComposition()
ctx.merge(base)
ctx.merge(file)
ctx.dump('outputs/complex-mouse-bites.gml')
file.draw_mode = DxfFile.DM_LINE
file.width = 0.7
ctx = gerberex.DrillComposition()
ctx.merge(base)
ctx.merge(file)
ctx.dump('outputs/complex-line.txt')

dxf = gerberex.read('data/fill.dxf')
dxf.to_metric()
dxf.rotate(30)
dxf.offset(100, 50)
dxf.width = 0.05
dxf.to_inch()
dxf.draw_mode = DxfFile.DM_LINE
dxf.write('outputs/fill-outline.gml')
dxf.draw_mode = DxfFile.DM_FILL
dxf.write('outputs/fill.gml')

ctx = gerberex.GerberComposition()
base = gerberex.rectangle(width=12, height=12, left=-1, bottom=-1, units='metric')
base.draw_mode = base.DM_FILL
ctx.merge(base)
top = gerberex.read('data/ref_gerber_metric.gtl')
ctx.merge(top)
ctx.dump('outputs/negative.gtl')

ctx = gerberex.GerberComposition()
t1 = gerberex.read('data/ref_gerber_metric.gtl')
t1.rotate(20)
ctx.merge(t1)
t2 = gerberex.read('data/ref_gerber_metric.gtl')
t2.offset(15,0)
ctx.merge(t2)
ctx.dump('outputs/new-merge.gtl')

top = gerberex.read('data/single_quadrant.gtl')
top.write('outputs/single_quadrant.gtl')

top = gerberex.read('data/ref_gerber_metric.gtl')
top.rotate(30)
top.offset(10, 5)
top.write('outputs/newgerber.gtl')
top.to_inch()
top.format = (2, 5)
top.write('outputs/newgerber_inch.gtl')

drill = gerberex.read('data/rout2.txt')
drill.rotate(30, (5, 2))
drill.offset(5,2)
drill.write('outputs/rout.txt')
drill.to_inch()
drill.format = (2, 4)
drill.write('outputs/rout_inch.txt')

ctx = gerberex.DrillComposition()
drill = gerberex.read('data/rout.txt')
ctx.merge(drill)
drill2 = gerberex.read('data/rout.txt')
drill2.rotate(20)
drill2.offset(10, 0)
ctx.merge(drill2)
ctx.dump('outputs/rout.txt')

#merge2()

top = gerberex.read('../tests/data/ref_gerber_metric.gtl')
top = gerber.load_layer('../tests/outputs/RS2724x_rotate.gtl')
ctx = GerberCairoContext(scale=50)
ctx.render_layer(top)
ctx.dump('outputs/test.png')

ctx = gerberex.DrillComposition()
base = gerberex.read('data/base.txt')
dxf = gerberex.read('data/mousebites.dxf')
dxf.draw_mode = DxfFile.DM_MOUSE_BITES
dxf.to_metric()
dxf.width = 0.5
ctx.merge(base)
ctx.merge(dxf)
ctx.dump('outputs/merged.txt')

dxf = gerberex.read('data/mousebite.dxf')
dxf.zero_suppression = 'leading'
dxf.write('outputs/a.gtl')
dxf.draw_mode = DxfFile.DM_MOUSE_BITES
dxf.width = 0.5
dxf.write('outputs/b.gml')
dxf.format = (3,3)
dxf.write('outputs/b.txt', filetype=DxfFile.FT_EXCELLON)
top = gerber.load_layer('outputs/a.gtl')
drill = gerber.load_layer('outputs/b.txt')
ctx = GerberCairoContext(scale=50)
ctx.render_layer(top)
ctx.render_layer(drill)
ctx.dump('outputs/b.png')

file = gerberex.read('data/test.GTL')
file.rotate(45)
file.write('outputs/test_changed.GTL')
file = gerberex.read('data/test.TXT')
file.rotate(45)
file.write('outputs/test_changed.TXT')

copper = gerber.load_layer('test-merged.GTL')
ctx = GerberCairoContext(scale=10)
ctx.render_layer(copper)
outline = gerber.load_layer('test.GML')
outline.cam_source.to_metric()
ctx.render_layer(outline)
drill = gerber.load_layer('test-merged.TXT')
ctx.render_layer(drill)
ctx.dump('test.png')
