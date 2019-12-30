""" demos of the OrthMesh class (see fc_hypermesh.OrthMesh module)

Usage information
=================
There are eigth available functions:

    1. demo01: [-1,1]x[-1,1]x[-1,1] meshing by orthotopes
    2. demo02: [-1,1]x[-1,1] meshing by orthotopes
    3. demo03: [-1,1]x[0,1]x[0,2] meshing by orthotopes
    4. demo04: [-1,1]x[0,1] meshing by simplices
    5. demo05: [0,1]x[0,1] mapped by (x,y)->(2*x,y) and meshed by simplices
    6. demo06: [0,1]x[0,1] mapped by (x,y)->(20*x,2*(2*y-1+cos(2*pi*x))) 
       and meshed by simplices
    7. demo07: [0,1]x[0,1]x[0,1] mapped by 
       (x,y,z)->(x+sin(4*pi*y),10*y-1,z+cos(4*pi*y)) 
       and meshed by simplices
    8. demo08: plot Khun decomposition of [0,1]^d with k-order d-simplex 
       for d in 1..3 and k in 1..3
    
Example 1
---------
>>>   import fc_hypermesh.demos
>>>   demos.demo03()

"""
from __future__ import print_function
from fc_tools.colors import str2rgb
from fc_tools.others import isModuleFound
from fc_tools.Matplotlib import DisplayFigures,SaveAllFigsAsFiles
from fc_hypermesh.OrthMesh import OrthMesh

if isModuleFound('matplotlib'):
  import matplotlib.pyplot as plt
  from fc_tools.Matplotlib import DisplayFigures,set_axes_equal,SaveAllFigsAsFiles

  def savefigs(basename,**kwargs):
    savedir=kwargs.get('dir', None )
    if savedir is not None:
      SaveAllFigsAsFiles(basename,**kwargs)
      
Show=isModuleFound('matplotlib')

def alldemos(show=Show,**kwargs):
  runbenchs=kwargs.pop('runbenchs', True )
  ListOfDemos=['demo01','demo02','demo03','demo04','demo05','demo06','demo07']
  for demo in ListOfDemos:
    rundemo(demo,show,**kwargs)
    rundemo(demo,show,order=3,**kwargs)
  rundemo('demo08',show,order=4,**kwargs)
  savedir=kwargs.get('dir', None )
  if savedir is not None:  
    print('  -> All figures save in %s'%savedir)
  if runbenchs:
    from fc_hypermesh.benchs import allbenchs_small
    allbenchs_small()
    
def rundemo(demo,show,**kwargs):
  order=kwargs.pop('order', 1 )
  print('[fc_hypermesh] Running %s (order=%d)'%(demo,order))
  eval(demo+'(show=show,order=order)',globals(),locals())
  if show:
    plt.show()
    seedemo(show)
    savefigs(demo+'_order%d'%order,**kwargs)
    plt.close('all')
  
def seedemo(show):
  if show:
    DisplayFigures()
    plt.show()
    #import time
    print('    Waiting 3s before closing ...')
    plt.pause(3)
    #time.sleep(3)

def demo01(show=Show,stop=False,order=1):
  """ OrthMesh  """
  print('------ demo01 --------')
  print("oTh=OrthMesh(3,[10,5,10],type='orthotope', box=[[-1,1],[0,1],[0,2]],order=%d)"%order)
  print('----------------------')
  oTh=OrthMesh(3,[10,5,10],type='orthotope', box=[[-1,1],[0,1],[0,2]],order=order)
  print(oTh)
  
  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
  
    plt.close('all')
    plt.ion()
    fig=plt.figure(1)
    oTh.plotmesh(legend=True)
    set_axes_equal()
    plt.figure(2)
    oTh.plotmesh(m=2,legend=True,edgecolor=[0,0,0])
    set_axes_equal()
    plt.axis('off')

    plt.figure(3)
    oTh.plotmesh(m=2,facecolor=None,edgecolor=str2rgb('LightGray'))
    oTh.plotmesh(m=1,legend=True,linewidth=2)
    set_axes_equal()
    plt.axis('off')

    plt.figure(4)
    oTh.plotmesh(m=1,color='black')
    oTh.plotmesh(m=0,legend=True,s=55) # see matplotlib.pyplot.scatter options
    set_axes_equal()
    plt.axis('off')
    
    if order>1:
      fig=plt.figure(5)
      oTh.plotmesh()
      oTh.plotnodes(vsize=15,nsize=10)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(6)
      oTh.plotmesh(m=2)
      oTh.plotnodes(m=2)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(7)
      #oTh.plotmesh(m=2,color='LightGray',facecolor=None)
      oTh.plotmesh(m=1,color='LightGray')
      oTh.plotnodes(m=1,vcolor='m')
      set_axes_equal()
      plt.axis('off')
      
    plt.show(block=stop)
  
def demo02(show=Show,stop=False,order=1):
  print('------ demo02 --------')
  print("oTh=OrthMesh(2,[12,5],type='orthotope',box=[[-1,1],[0,1]],order=%d)"%order)
  print('----------------------')
  oTh=OrthMesh(2,[12,5],type='orthotope',box=[[-1,1],[0,1]],order=order)
  print(oTh)
  
  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
  
    plt.close('all')
    plt.ion()
    plt.figure(1)
    oTh.plotmesh(legend=True)
    set_axes_equal()

    plt.figure(2)
    oTh.plotmesh(m=1,legend=True,linewidth=3)
    set_axes_equal()
    plt.axis('off')

    plt.figure(3)
    oTh.plotmesh(m=1,color='black')
    oTh.plotmesh(m=0,legend=True,s=105) # see matplotlib.pyplot.scatter options
    set_axes_equal()
    plt.axis('off')  
    #plt.show(block=stop)
    
    if order>1:
      fig=plt.figure(4)
      oTh.plotmesh()
      oTh.plotnodes(vsize=15,nsize=10)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(5)
      oTh.plotmesh(m=2)
      oTh.plotnodes(m=2)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(6)
      oTh.plotmesh(m=1,color='LightGray')
      oTh.plotnodes(m=1,vcolor='m')
      set_axes_equal()
      plt.axis('off')
    
    DisplayFigures()
    plt.show(block=stop)
  
def demo03(show=Show,stop=False,order=1):
  print('------ demo03 --------')
  print("oTh=OrthMesh(3,[10,5,10],box=[[-1,1],[0,1],[0,2]],order=%d)"%order)
  print('----------------------')
  oTh=OrthMesh(3,[10,5,10],box=[[-1,1],[0,1],[0,2]],order=order)
  print(oTh)
  
  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
  
    plt.close('all')
    plt.ion()
    plt.figure(1)
    oTh.plotmesh(legend=True,linewidth=0.5)
    set_axes_equal()

    plt.figure(2)
    oTh.plotmesh(m=2,legend=True,edgecolor=[0,0,0])
    set_axes_equal()
    plt.axis('off')

    plt.figure(3)
    oTh.plotmesh(m=2,edgecolor=[0,0,0],color='none')
    oTh.plotmesh(m=1,legend=True,linewidth=2,alpha=0.3)
    set_axes_equal()
    plt.axis('off')

    plt.figure(4)
    oTh.plotmesh(m=1,color='black',alpha=0.3)
    oTh.plotmesh(m=0,legend=True,s=55)
    set_axes_equal()
    plt.axis('off')
    
    if order>1:
      fig=plt.figure(5)
      oTh.plotmesh()
      oTh.plotnodes(vsize=15,nsize=10)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(6)
      oTh.plotmesh(m=2)
      oTh.plotnodes(m=2)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(7)
      #oTh.plotmesh(m=2,color='LightGray',facecolor=None)
      #oTh.plotmesh(m=1,color='LightGray')
      oTh.plotnodes(m=1,vcolor='m',vsize=15,nsize=10)
      set_axes_equal()
      plt.axis('off')
    
    DisplayFigures()
    plt.show(block=stop)
    
    

def demo04(show=Show,stop=False,order=4):
  print('------ demo04 --------')
  print("oTh=OrthMesh(2,[12,5],type='simplex',box=[[-1,1],[0,1]],order=%d)"%order)
  print('----------------------')
  oTh=OrthMesh(2,[12,5],type='simplex',box=[[-1,1],[0,1]],order=order)
  print(oTh)
  
  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
  
    plt.close('all')
    plt.ion()
    plt.figure(1)
    oTh.plotmesh(legend=True)
    set_axes_equal()

    plt.figure(2)
    oTh.plotmesh(m=1,legend=True,linewidth=3)
    plt.axis('off')
    set_axes_equal()

    plt.figure(3)
    oTh.plotmesh(m=1,color='black')
    oTh.plotmesh(m=0,legend=True,s=105) # see matplotlib.pyplot.scatter options
    plt.axis('off')
    set_axes_equal()
    
    if order>1:
      fig=plt.figure(4)
      oTh.plotmesh()
      oTh.plotnodes(vsize=15,nsize=10)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(5)
      oTh.plotmesh(m=1,color='LightGray')
      oTh.plotnodes(m=1,vcolor='m')
      set_axes_equal()
      plt.axis('off')
      
    DisplayFigures()
    plt.show(block=stop)
    
def demo05(show=Show,stop=False,order=1):
  import numpy as np
  print('------ demo05 --------')
  print('trans=lambda q: np.array([2*q[0],q[1]])')
  print("oTh=OrthMesh(2,5,type='simplex',mapping=trans,order=%d)"%order)
  print('----------------------')
  trans=lambda q: np.array([2*q[0],q[1]])
  oTh=OrthMesh(2,5,type='simplex',mapping=trans,order=order)
  print(oTh)
  
  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
  
    plt.close('all')
    plt.ion()
    plt.figure(1)
    oTh.plotmesh(legend=True)
    set_axes_equal()

    plt.figure(2)
    oTh.plotmesh(color='lightgray')
    oTh.plotmesh(m=1,legend=True,linewidth=3)
    plt.axis('equal')
    plt.axis('off')

    plt.figure(3)
    oTh.plotmesh(color='lightgray')
    oTh.plotmesh(m=1,color='black')
    oTh.plotmesh(m=0,legend=True,s=105) # see matplotlib.pyplot.scatter options
    plt.axis('equal')
    plt.axis('off')
    
    if order>1:
      fig=plt.figure(4)
      oTh.plotmesh()
      oTh.plotnodes()
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(5)
      oTh.plotmesh(m=1,color='LightGray')
      oTh.plotnodes(m=1,vcolor='m')
      set_axes_equal()
      plt.axis('off')

    DisplayFigures()
    plt.show(block=stop)
      
def demo06(show=Show,stop=False,order=1):
  import numpy as np
  print('------ demo06 --------')
  print('trans=lambda q: np.array([20*q[0],2*(2*q[1]-1+np.cos(2*np.pi*q[0]))])')
  print("oTh=OrthMesh(2,[100,20],type='simplex',mapping=trans,order=%d)"%order)
  print('----------------------')
  trans=lambda q: np.array([20*q[0],2*(2*q[1]-1+np.cos(2*np.pi*q[0]))])
  oTh=OrthMesh(2,[20,4],type='simplex',mapping=trans,order=order)
  print(oTh)

  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
  
    plt.close('all')
    plt.ion()
    plt.figure(1)
    oTh.plotmesh(legend=True)
    plt.axis('equal')

    plt.figure(2)
    oTh.plotmesh(color='lightgray')
    oTh.plotmesh(m=1,legend=True,linewidth=3)
    plt.axis('equal')
    plt.axis('off')

    plt.figure(3)
    oTh.plotmesh(color='lightgray')
    oTh.plotmesh(m=1,color='black')
    oTh.plotmesh(m=0,legend=True,s=105) # see matplotlib.pyplot.scatter options
    plt.axis('equal')
    plt.axis('off')
    
    if order>1:
      fig=plt.figure(4)
      oTh.plotmesh()
      oTh.plotnodes(vsize=15,nsize=10)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(5)
      oTh.plotmesh(m=1,color='LightGray')
      oTh.plotnodes(m=1,vcolor='m')
      set_axes_equal()
      plt.axis('off')

    DisplayFigures()
    plt.show(block=stop)

def demo07(show=Show,stop=False,order=1):
  import numpy as np
  print('------ demo07 --------')
  print('trans=lambda q: np.array([q[0]+np.sin(4*np.pi*q[1]), 10*q[1]-1, q[2]+np.cos(4*np.pi*q[1])])')
  print("oTh=OrthMesh(3,[3,25,3],type='simplex',mapping=trans,order=%d)"%order)
  print('----------------------')
  trans=lambda q: np.array([q[0]+np.sin(4*np.pi*q[1]), 10*q[1]-1, q[2]+np.cos(4*np.pi*q[1])])
  oTh=OrthMesh(3,[3,25,3],type='simplex',mapping=trans,order=order)
  print(oTh)
  
  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
  
    plt.close('all')
    plt.ion()
    plt.figure(1)
    oTh.plotmesh(legend=True)
    set_axes_equal()

    plt.figure(2)
    oTh.plotmesh(m=2,legend=True,edgecolor=[0,0,0])
    set_axes_equal()

    plt.figure(3)
    oTh.plotmesh(m=2,edgecolor='lightgray',facecolor=None,alpha=0.3)
    oTh.plotmesh(m=1,legend=True,linewidth=2)
    set_axes_equal()

    plt.figure(4)
    oTh.plotmesh(m=1,color='black')
    oTh.plotmesh(m=0,legend=True,s=55)
    set_axes_equal()
    
    if order>1:
      fig=plt.figure(5)
      oTh.plotmesh()
      oTh.plotnodes()
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(6)
      oTh.plotmesh(m=2)
      oTh.plotnodes(m=2)
      set_axes_equal()
      plt.axis('off')
      
      fig=plt.figure(7)
      oTh.plotmesh(m=1,color='LightGray')
      oTh.plotnodes(m=1,vcolor='m')
      set_axes_equal()
      plt.axis('off')
      
    DisplayFigures()
    plt.show(block=stop)
    
def demo08(show=Show,stop=False,order=3):
  import numpy as np
  print('------ demo08 --------')
  print('Kuhn decomposition')
  print('----------------------')
  
  if show:
    if not isModuleFound('matplotlib'):
      print('[fc-hypermesh] Needs matplotlib package to be installed for graphics')
      return
    from .Matplotlib import plotKuhnOrder
    plt.close('all')
    plt.ion()
    fig=1
    for d in np.arange(1,4):
      for order in np.arange(1,order+1):
        plt.figure(fig)
        plotKuhnOrder(d,order)
        fig+=1
      
    DisplayFigures()
    plt.show(block=stop)  
