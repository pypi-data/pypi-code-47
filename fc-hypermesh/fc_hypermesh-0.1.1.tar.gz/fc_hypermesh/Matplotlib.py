import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Patch
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as a3
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
from fc_tools.others import LabelBaseName
import fc_hypermesh.CartesianGrid as CG
from fc_hypermesh.OrthMesh import OrthMesh
from fc_tools.Matplotlib import set_axes_equal,SetGeometry,DisplayFigures
from fc_tools.colors import check_color

def plotmesh(Th,**kwargs):
    color=kwargs.pop('color',Th.color)
    if Th.type==0:
      return eval("PlotmeshSubTh"+str(Th.m)+"simp"+str(Th.d)+"D(Th,color,**kwargs)")
    else:
      return eval("PlotmeshSubQh"+str(Th.m)+"orth"+str(Th.d)+"D(Th,color,**kwargs)")

def PlotmeshSubTh2simp2D(Th,color,**kwargs):
  from matplotlib.patches import Polygon
  from matplotlib.collections import PolyCollection
  Name=LabelBaseName(2,2)
  Poly2D=Th.q[:,Th.me[Th.ivertex]].swapaxes(0,2)
  p = PolyCollection(Poly2D, facecolor="none",edgecolor = color)
  ax=plt.gca()
  ax.add_collection(p)
  ax.autoscale()
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  return legend_handle,label
  
def PlotmeshSubQh2orth2D(Th,color,**kwargs):
  from matplotlib.patches import Polygon
  from matplotlib.collections import PolyCollection
  Name=LabelBaseName(2,2)
  Poly2D=Th.q[:,Th.me[Th.ivertex[[0,1,3,2]]]].swapaxes(0,2)
  p = PolyCollection(Poly2D, facecolor="none",edgecolor = color)
  ax=plt.gca()
  legend_handle=ax.add_collection(p)
  ax.autoscale()
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  return legend_handle,label

def PlotmeshSubTh1simp1D(Th,color,**kwargs):
  ive=range(Th.m+1)
  ANone=np.array([None]*Th.nme)
  Name=LabelBaseName(1,1)
  X=np.array([Th.q[0,Th.me[Th.ivertex[0]]],Th.q[0,Th.me[Th.ivertex[1]]],ANone]).T.reshape((Th.nme*3,))
  Y=np.zeros(X.shape)
  fig = plt.gcf()
  ax = fig.gca()
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  legend_handle,=ax.plot(X,Y,color=color,picker=5,**kwargs)
  # legend_handle.aname=label # The aname attribute was deprecated in Matplotlib 3.1 and will be removed in 3.3.
  return legend_handle,label
  
def PlotmeshSubTh1simp2D(Th,color,**kwargs):
  ive=range(Th.m+1)
  ANone=np.array([None]*Th.nme)
  Name=LabelBaseName(2,1)
  X=np.array([Th.q[0,Th.me[Th.ivertex[0]]],Th.q[0,Th.me[Th.ivertex[1]]],ANone]).T.reshape((Th.nme*3,))
  Y=np.array([Th.q[1,Th.me[Th.ivertex[0]]],Th.q[1,Th.me[Th.ivertex[1]]],ANone]).T.reshape((Th.nme*3,))
  fig = plt.gcf()
  ax = fig.gca()
  #plt.rc('text', usetex=True)
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  legend_handle,=ax.plot(X,Y,color=color,picker=5,**kwargs)
  # legend_handle.aname=label # The aname attribute was deprecated in Matplotlib 3.1 and will be removed in 3.3.
  #legend_handle=plt.Line2D([0, 1],[0,1],color=color,**kwargs)
  #label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  return legend_handle,label

def PlotmeshSubQh1orth2D(Th,color,**kwargs):
  return PlotmeshSubTh1simp2D(Th,color,**kwargs)

def PlotmeshSubQh1orth1D(Th,color,**kwargs):
  return PlotmeshSubTh1simp1D(Th,color,**kwargs)

def PlotmeshSubTh0simp2D(Th,color,**kwargs):
  s=kwargs.get('s', 20 );kwargs.pop('s',None)
  marker=kwargs.get('marker', 'o' );kwargs.pop('marker',None)
  Name=LabelBaseName(2,0)
  fig = plt.gcf()
  ax = fig.gca()
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  color=np.array(color).reshape((1,3))
  #legend_handle,=ax.plot(Th.q[0,0],Th.q[1,0],color=color,linestyle='',marker='o',picker=5,**kwargs)
  legend_handle=ax.scatter(Th.q[0,0],Th.q[1,0],c=color,marker=marker,s=s,**kwargs)
  # legend_handle.aname=label # The aname attribute was deprecated in Matplotlib 3.1 and will be removed in 3.3.
  return legend_handle,label

def PlotmeshSubQh0orth2D(Th,color,**kwargs):
  return PlotmeshSubTh0simp2D(Th,color,**kwargs)

def PlotmeshSubTh0simp3D(Th,color,**kwargs):
  s=kwargs.get('s', 5 );kwargs.pop('s',None)
  marker=kwargs.get('marker', 'o' );kwargs.pop('marker',None)
  Name=LabelBaseName(3,0)
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  #legend_handle=ax.scatter(Th.q[0,0],Th.q[1,0],Th.q[2,0],c=color,marker=marker,picker=picker,**kwargs)
  color=np.array(color).reshape((1,3))
  legend_handle=ax.scatter(Th.q[0,0],Th.q[1,0],Th.q[2,0],c=color,marker=marker,s=s,**kwargs)
  #legend_handle.aname=label # The aname attribute was deprecated in Matplotlib 3.1 and will be removed in 3.3.
  return legend_handle,label

def PlotmeshSubQh0orth3D(Th,color,**kwargs):
  return PlotmeshSubTh0simp3D(Th,color,**kwargs)
    
def PlotmeshSubTh1simp3D(Th,color,**kwargs):
  Name=LabelBaseName(3,1)
  Line3D=Th.q[:,Th.me[Th.ivertex]].swapaxes(0,2)
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  ax.add_collection3d(Line3DCollection(Line3D,colors=color, **kwargs))
  legend_handle=plt.Line2D([0, 1],[0,1],color=color,**kwargs)
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  return legend_handle,label

def PlotmeshSubQh1orth3D(Th,color,**kwargs):
  return PlotmeshSubTh1simp3D(Th,color,**kwargs)
  
def PlotmeshSubTh2simp3D(Th,color,**kwargs): 
  return PlotmeshSubGen2orth3D(Th,color,**kwargs)


def PlotmeshSubQh2orth3D(Th,color,**kwargs):  
  return PlotmeshSubGen2orth3D(Th,color,**kwargs)

def PlotmeshSubGen2orth3D(Th,color,**kwargs):
  Name=LabelBaseName(3,2)
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  #alpha=kwargs.pop('facealpha',0.1)
  edgecolor=kwargs.pop('edgecolor',None)
  facecolor=kwargs.pop('facecolor',color)
  if facecolor is None and edgecolor is None:
    if color is None:
      edgecolor=Th.color
    else:
      edgecolor=color
  #if 'facecolor' in kwargs:
    #color=kwargs.pop('facecolor',None)
  if edgecolor is None:
    edgecolor='black'
  if facecolor is None:
    Line3D=Th.q[:,Th.me].swapaxes(0,2)
    if Th.type==0:
      C=Th.ivertex[np.array([[0,1],[1,2],[2,0]])]
    else:
      C=Th.ivertex[np.array([[0,1],[2,3],[0,2],[1,3]])]
    Poly3D=np.zeros((0,2,3))
    if edgecolor is None:
      edgecolor=Th.color
    for edge in C:
      Poly3D=np.concatenate((Poly3D,Th.q[:,Th.me[edge]].T))
    p = Line3DCollection(Poly3D,color=edgecolor,**kwargs)  
    legend_handle=Patch(color=edgecolor,**kwargs)
  else:
    if Th.type==0:
      Poly3D=Th.q[:,Th.me[Th.ivertex]].swapaxes(0,2)
    else:  
      Poly3D=Th.q[:,Th.me[Th.ivertex[[0,1,3,2]]]].swapaxes(0,2)
    p = Poly3DCollection(Poly3D, facecolor=facecolor,edgecolor = edgecolor,**kwargs)
    alpha=kwargs.pop('alpha',1)
    legend_handle=Patch(color=color,**kwargs)
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  ax.add_collection3d(p)
  ax.autoscale()
  return legend_handle,label  
  
def PlotmeshSubGen2orth3Dold(Th,color,**kwargs):  
  Name=LabelBaseName(3,2)
  #alpha=kwargs.pop('facealpha',0.1)
  edgecolor=kwargs.pop('edgecolor',None)
  if color is None:
    color=Th.color
  if 'facecolor' in kwargs:
    color=kwargs.pop('facecolor',None)
  if color is None: 
    Line3D=Th.q[:,Th.me].swapaxes(0,2)
    if Th.type==0:
      C=Th.ivertex[np.array([[0,1],[1,2],[2,0]])]
    else:
      C=Th.ivertex[np.array([[0,1],[2,3],[0,2],[1,3]])]
    Poly3D=np.zeros((0,2,3))
    if edgecolor is None:
      edgecolor=Th.color
    for edge in C:
      Poly3D=np.concatenate((Poly3D,Th.q[:,Th.me[edge]].T))
    p = Line3DCollection(Poly3D,color=edgecolor,**kwargs)  
    legend_handle=Patch(color=edgecolor,**kwargs)
  else:  
    if Th.type==0:
      Poly3D=Th.q[:,Th.me[Th.ivertex]].swapaxes(0,2)
    else:  
      Poly3D=Th.q[:,Th.me[Th.ivertex[[0,1,3,2]]]].swapaxes(0,2)
    p = Poly3DCollection(Poly3D, facecolor=color,edgecolor = edgecolor,**kwargs)
    alpha=kwargs.pop('alpha',1)
    legend_handle=Patch(color=color,**kwargs)
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  ax.add_collection3d(p)
  ax.autoscale()
  return legend_handle,label
  
def PlotmeshSubTh3simp3D(Th,color,**kwargs):
  Name=LabelBaseName(3,3)
  Poly3D=[]
  C=CG.combs(np.arange(4),2)
  for i in range(6):
     A=Th.q[:,Th.me[Th.ivertex[C[i]]]].T
     Poly3D+= A.tolist()
      
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d')
  
  ax.add_collection3d(Line3DCollection(Poly3D,colors=color,**kwargs))#linewidths=0.4, linestyles=':')) # linewidths=0.4, linestyles=':')
  #legend_handle,=plt.plot([0, 1],[0,1],color=color,visible=False,**kwargs)
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  return legend_handle,label

def PlotmeshSubQh3orth3D(Th,color,**kwargs):
  Name=LabelBaseName(3,3)
  Poly3D=[]
  C=[[0,1],[0,4],[1,5],[4,5],[2,3],[2,6],[3,7],[6,7],[1,3],[5,7],[4,6],[0,2]]
  Poly3D=np.zeros((0,2,3))
  for edge in C:
     A=Th.q[:,Th.me[Th.ivertex[edge]]].T
     Poly3D=np.concatenate((Poly3D,A))
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    ax = fig.gca( projection='3d') 
  ax.add_collection3d(Line3DCollection(Poly3D,colors=color,**kwargs))#linewidths=0.4, linestyles=':')) # linewidths=0.4, linestyles=':')
  ax.autoscale()
  #legend_handle,=plt.plot([0, 1],[0,1],color=color,visible=False,**kwargs)
  legend_handle=Patch(color=color,**kwargs) # to improve
  label=r"$%s_{"%(Name)+str(int(Th.label))+"}$"
  return legend_handle,label

def plotElementsNumber(Th,**kwargs):
  Ba=Th.barycenters()
  fig = plt.gcf()
  ax = fig.axes[0]
  if Th.d==2:
    for k in range(Th.nme):
      ax.annotate(str(k),(Ba[0,k],Ba[1,k]),verticalalignment='center', horizontalalignment='center',clip_on=True,
                  bbox=dict(boxstyle="round",fc=(1.0, 0.7, 0.7),ec=(1., .5, .5)))
  if Th.d==3:
    for i in range(len(Th.ivertex)):  
      Line3D=np.array([Th.q[:,Th.me[Th.ivertex[i]]],Ba]).swapaxes(0,2).swapaxes(1,2)
      ax.add_collection3d(Line3DCollection(Line3D,colors='red',linestyles='dotted'))
    for k in range(Th.nme):
      ax.text(Ba[0,k],Ba[1,k],Ba[2,k],str(k),verticalalignment='center', horizontalalignment='center',clip_on=True,color='black',
                  bbox=dict(boxstyle="round",fc=(1.0, 0.7, 0.7),ec=(1., .5, .5)))
      
def setcolor(color,colorauto):
  if color=='auto':
    return colorauto
  return check_color(color)
      
def ploteltsNumber(Th,**kwargs):
  vLineColor=setcolor(kwargs.pop('vLineColor',None),Th.color)
  vLineStyle=kwargs.pop('vLineStyle',':')
  vLineWidth=kwargs.pop('vLineWidth',0.5)
  color=check_color(kwargs.pop('color',Th.color))
  boxstyle=kwargs.pop('boxstyle','round')
  fc=setcolor(kwargs.pop('fc','white'),Th.color)
  ec=setcolor(kwargs.pop('ec','white'),Th.color)
  bbox=kwargs.pop('bbox',dict(boxstyle=boxstyle,fc=fc,ec=ec))
  Idx=kwargs.pop('indices',None)
  if Idx is None:
    Idx=np.arange(Th.nme)
  Ba=Th.barycenters()[:,Idx]
  fig = plt.gcf()
  ax = fig.axes[0]
  if Th.d==1:
    if vLineColor is not None:
      ax.annotate('0',(Ba[0,0],1/20),verticalalignment='center', horizontalalignment='center',clip_on=True,
                  bbox=bbox,color=color,**kwargs)
  if Th.d==2:
    if vLineColor is not None:
      ANone=np.array([None]*len(Idx))
      for i in range(len(Th.ivertex)):  
        X=np.array([Th.q[0,Th.me[Th.ivertex[i],Idx]],Ba[0],ANone])#.T.reshape((Th.nme*3,))
        Y=np.array([Th.q[1,Th.me[Th.ivertex[i],Idx]],Ba[1],ANone])#.T.reshape((Th.nme*3,))
        ax.plot(X,Y,color=vLineColor,linestyle=vLineStyle,linewidth=vLineWidth)
      
    for k in range(Ba.shape[1]):
      ax.annotate(str(k),(Ba[0,k],Ba[1,k]),verticalalignment='center', horizontalalignment='center',clip_on=True,
                  bbox=bbox,color=color,**kwargs)
    return
  if Th.d==3:
    if vLineColor is not None:
      for i in range(len(Th.ivertex)):  
        Line3D=np.array([Th.q[:,Th.me[Th.ivertex[i],Idx]],Ba]).swapaxes(0,2).swapaxes(1,2)
        ax.add_collection3d(Line3DCollection(Line3D,colors=vLineColor,linestyles=vLineStyle,linewidths=vLineWidth)) #linewidths
    for k in range(Ba.shape[1]):
      ax.text(Ba[0,k],Ba[1,k],Ba[2,k],str(k),verticalalignment='center', horizontalalignment='center',clip_on=True,
              bbox=bbox,color=color,**kwargs) 
    

def plotnodesNumber(Th,**kwargs):
  #print(q.shape)
  D=kwargs.pop('D',None)
  color=check_color(kwargs.pop('color',Th.color))
  boxstyle=kwargs.pop('boxstyle','round')
  fc=setcolor(kwargs.pop('fc','white'),Th.color)
  ec=setcolor(kwargs.pop('ec','white'),Th.color)
  bbox=kwargs.pop('bbox',dict(boxstyle=boxstyle,fc=fc,ec=ec))
  indices=kwargs.pop('indices',None)
  elt_indices=kwargs.pop('elt_indices',None)
  #if elt_indices is not None:
  if D is None:
    if Th.dim<=2:
      D=np.zeros((2,1))
    if Th.dim==3:
      D=np.zeros((3,1))
  
  fig = plt.gcf()
  #if len(fig.axes)>0:
  ax=fig.axes[0]
  #else:
    #if Th.d==3:
      #ax = fig.gca( projection='3d')
    #else:
      #ax = fig.gca()
      
  if Th.d==1:
    for k in range(Th.nq):
      ax.annotate(str(k),(Th.q[0,k]+D[0],D[1]),verticalalignment='center', horizontalalignment='center',clip_on=True,
                  bbox=bbox,color=color,**kwargs)
  if Th.d==2:
    for k in range(Th.nq):
      ax.annotate(str(k),(Th.q[0,k]+D[0],Th.q[1,k]+D[1]),verticalalignment='center', horizontalalignment='center',clip_on=True,
                  bbox=bbox,color=color,**kwargs)
  if Th.d==3:
    for k in range(Th.nq):
      #ax.text(Th.q[0,k]+D[0],Th.q[1,k]+D[1],Th.q[2,k]+D[2],str(k),verticalalignment='center', horizontalalignment='center',clip_on=True,
      ax.text(Th.q[0,k]+D[0],Th.q[1,k]+D[1],Th.q[2,k]+D[2],str(k),verticalalignment='center', horizontalalignment='center',clip_on=True,
              bbox=bbox,color=color,**kwargs)

         
def plotnodes(Th,**kwargs):
  vcolor=check_color(kwargs.pop('vcolor','k'))
  vsize=kwargs.pop('vsize',40)
  ncolor=check_color(kwargs.pop('ncolor','DarkSlateGray'))
  nsize=kwargs.pop('nsize',20)
  idx=np.unique(Th.me[Th.ivertex]) # vertices index
  idxc=np.setdiff1d(np.arange(Th.nq),idx) # 
  fig = plt.gcf()
  if len(fig.axes)>0:
    ax=fig.axes[0]
  else:
    if Th.d==3:
      ax = fig.gca( projection='3d')
    else:
      ax = fig.gca()
  if Th.d==3:
    a=1
    ax.scatter(Th.q[0,idx],Th.q[1,idx],Th.q[2,idx],color=vcolor,s=vsize,clip_on=True)
    ax.scatter(Th.q[0,idxc],Th.q[1,idxc],Th.q[2,idxc],color=ncolor,s=nsize,clip_on=True)
  if Th.d==2:
    ax.scatter(Th.q[0,idx],Th.q[1,idx],color=vcolor,s=vsize)
    ax.scatter(Th.q[0,idxc],Th.q[1,idxc],color=ncolor,s=nsize)
  if Th.d==1:
    ax.scatter(Th.q[0,idx],0*Th.q[0,idx],color=vcolor,s=vsize)
    ax.scatter(Th.q[0,idxc],np.zeros((len(idxc),)),color=ncolor,s=nsize)
    
def plotKuhnOrder(d,order,**kwargs):
  vcolor=check_color(kwargs.get('vcolor','k')) # vertices color
  vsize=kwargs.get('vsize',70) 
  ncolor=check_color(kwargs.get('ncolor','DarkSlateGray')) # nodes color
  nsize=kwargs.get('nsize',30) 
  #FontSize=kwargs.get('FontSize',10)
  #linewidths=kwargs.get('linewidths',1.5)
  EltNum=kwargs.get('EltNum',[]) # Element numbers 
  EltFaceColor=check_color(kwargs.get('EltFaceColor','m'))
  EltFaceAlpha=kwargs.get('EltFaceAlpha',0.2)
  Th=OrthMesh(d,np.ones((1,d)),order=order,type='simplex')
  plt.clf()
  Th.plotmesh()#linewidths=linewidths)
  Th.Mesh.plotnodes(vcolor=vcolor,vsize=vsize,ncolor=ncolor,nsize=nsize)
  c=1./20
  if d==3:
    D=np.array([-c,-c,-c])/2
  if d==2:
    D=np.array([-c,-c])
  if d==1:
    D=np.array([0,-c])
  Th.Mesh.plotnodesNumber(D=D,color='k',bbox=dict(fc='w',ec='k'))
  Th.Mesh.ploteltsNumber(vLineColor='b')
  set_axes_equal()
  plt.title('Kuhn decomposition: dim=%d, order=%d'%(d,order))
  plt.show() 
  
def plotRefElement(d,order,**kwargs):
  from fc_hypermesh.EltMesh import EltMesh
  EltType=kwargs.pop('type','simplex')
  assert(EltType in ['simplex','orthotope'])
  vcolor=kwargs.pop('vcolor','k') # vertices color
  vsize=kwargs.pop('vsize',70) 
  ncolor=kwargs.pop('ncolor','DarkSlateGray') # nodes color
  nsize=kwargs.pop('nsize',30)
  scale=kwargs.pop('scale',1.)
  azimuth=kwargs.pop('azimuth',22.)
  elevation=kwargs.pop('elevation',18.)
  fontsize=kwargs.pop('fontsize',0)
  
  q,me=CG.RefElement(d,order,type=EltType)
  K=EltMesh(d,d,q,me,order=order)
  K.plotmesh()
  K.plotnodes(vcolor=vcolor,vsize=vsize,ncolor=ncolor,nsize=nsize)
  c=1./20
  if d==3:
    D=np.array([-c,-c,c])#.reshape((3,1))
  elif d==2:
    D=np.array([c,c])#.reshape((2,1))
  else: # d==1
    D=np.array([c,c])#.reshape((1,1))
  if fontsize>0:
    K.plotnodesNumber(bbox=dict(fc='w',ec='k'),fontsize=fontsize,D=D)
  set_axes_equal()
  ax=plt.gca()
  ax.set_xlabel('x'),ax.set_ylabel('y')
  if d==3:
    ax.set_zlabel('z')
    ax.view_init(elevation, azimuth)
  fig=plt.gcf()
  fig.set_figheight(scale*fig.get_figheight())
  fig.set_figwidth(scale*fig.get_figwidth())
  #SetGeometry(0,0,800,800)
  plt.show() 
  
def plotOrder3DMesh(p,**kwargs):
  EltType=kwargs.pop('type','simplex')
  assert(EltType in ['simplex','orthotope'])
  N=kwargs.pop('N',[3,4,2]);
  Th=OrthMesh(3,N,order=p,type=EltType)
  plt.ion()
  plt.close('all')
  DisplayFigures(nfig=4)
  plt.figure(1)
  Th.plotmesh()
  Th.plotnodes()
  set_axes_equal()
  plt.figure(2)
  Th.plotmesh(m=2,legend=True,facecolor=None)#,alpha=0.2)#,FaceAlpha=0.2)
  Th.plotnodes(m=2,nsize=60)
  set_axes_equal()
  plt.figure(3)
  Th.plotmesh(m=1,legend=True)
  Th.plotnodes(m=1)
  set_axes_equal()
  plt.figure(4)
  Th.plotmesh(m=1,color='b',linewidth=0.5)
  Th.plotmesh(m=0,legend=True)
  set_axes_equal()
  #Th.plotnodes(m=0)
  #plt.show()
  return Th

def plotOrder2DMesh(p,**kwargs):
  EltType=kwargs.pop('type','simplex')
  assert(EltType in ['simplex','orthotope'])
  N=kwargs.pop('N',[3,4]);
  Th=OrthMesh(2,N,order=p,type=EltType)
  plt.ion()
  plt.close('all')
  DisplayFigures(nfig=3)
  plt.figure(1)
  Th.plotmesh()
  Th.plotnodes()
  set_axes_equal()
  plt.figure(2)
  Th.plotmesh(m=1,legend=True)#,FaceAlpha=0.2)
  Th.plotnodes(m=1)
  set_axes_equal()
  plt.figure(3)
  Th.plotmesh(m=0,legend=True)
  Th.plotmesh(m=1,color='b',linewidth=0.5)
  set_axes_equal()
  #Th.plotnodes(m=0)
  #plt.show()
  return Th
  
