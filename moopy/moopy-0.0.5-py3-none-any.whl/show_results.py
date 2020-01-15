import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize.optimize import OptimizeResult, vecnorm
import copy
# import parameters as pa
# import general as gene
# import objectives as obj


# Analysis Tools

def nondominated_filter(ds):

    ds = sorted(ds, key=lambda x: x.f[0], reverse=False)

    size = len(ds)
    ind = 0
    i = 0
    num_dom = 0
    ds_dom = []

    while ind < size:
        dp = ds[ind]
        while i < size:
            if i != ind and np.all(np.asarray((dp.f) < ds[i].f)):
                ds_dom.append(copy.copy(ds[i]))
                del ds[i]
                num_dom += 1
                size -= 1
                i -= 1
            i += 1
        i = 0
        ind += 1

    return ds, ds_dom


def Uniformcheck(ds):

    ds = sorted(ds, key=lambda x: x.f[0], reverse=False)

    d = []
    for i, dpi in enumerate(ds):
        if i != 0:
            d.append(vecnorm(dpi.f - ds[i - 1].f))

    # d = []
    # for i, dpi in enumerate(ds):
    #     di = 10
    #     for j, dpj in enumerate(ds):
    #         if i != j:
    #             dt = vecnorm(dpi.f - dpj.f)
    #             if dt < di:
    #                 di = dt
    #     d.append(di)

    sum = 0
    for di in d:
        sum += di
    td = sum/len(ds)

    sum2 = 0
    for di in d:
        sum2 += (di / td) ** 2

    return np.sqrt(sum2/(len(ds)-1))


def Eveness2(ds):

    ds = sorted(ds, key=lambda x: x.f[0], reverse=False)

    d = []
    for i, dpi in enumerate(ds):
        if i != 0:
            d.append(vecnorm(dpi.f - ds[i - 1].f))

    sum = 0
    for di in d:
        sum += di
    mu = sum/len(d)

    sum2 = 0
    for i, di in enumerate(d):
        if i != 0:
            sum2 += (di - d[i-1]) ** 2

    si = np.sqrt(sum2 / (len(d) - 1))

    ol = mu - si
    i = 0
    while i < len(d)-1:
        if d[i] < ol:
            d[i+1] += d[i]
            del d[i]
        else:
            i += 1

    mu = sum / len(d)

    sum2 = 0
    for i, di in enumerate(d):
        if i != 0:
            sum2 += (di - d[i-1]) ** 2

    si = np.sqrt(sum2 / (len(d) - 1))

    return si / mu


def Eveness(ds):

    ds = sorted(ds, key=lambda x: x.f[0], reverse=False)

    d = []
    for i, dpi in enumerate(ds):
        if i != 0:
            d.append(vecnorm(dpi.f - ds[i - 1].f))

    sum = 0
    for di in d:
        sum += di
    mu = sum/len(d)

    sum2 = 0
    for i, di in enumerate(d):
        if i != 0:
            sum2 += (di - mu) ** 2

    si = np.sqrt(sum2 / (len(d) - 1))

    # return si / mu

    ol = mu - si
    i = 0
    while i < len(d)-1:
        if d[i] < ol:
            d[i+1] += d[i]
            del d[i]
        else:
            i += 1

    mu = sum / len(d)

    sum2 = 0
    for i, di in enumerate(d):
        if i != 0:
            sum2 += (di - mu) ** 2
            sum2 += (d[i-1] - mu) ** 2

    si = np.sqrt(sum2 / (2*len(d) - 1))

    return si / mu


def Extension(ds, ds_ini):

    list = []
    for dpi in ds_ini:
        num = 10
        for dp in ds:
            d = vecnorm(dp.f - dpi)
            if d < num:
                num = d
        list.append(num)
    dd = 0
    for l in list:
        dd += l**2
    EX = np.sqrt(dd)/len(ds_ini)


def displ_ds(ds):
    if (type(ds[0]) == list):
        dsn = []
        for dp in ds:
            dsn += dp
        ds = dsn
    for i, dp in enumerate(ds):
        displ_dp(dp, i)


def displ_ds2(ds):
    if not ds:
        print("no Pf and Px")
        return
    if (type(ds[0]) == list):
        dsn = []
        for dp in ds:
            dsn += dp
        ds = dsn
    print("Pf")
    for i, dp in enumerate(ds):
        displ_dp2(dp.f)
    print("Px")
    for i, dp in enumerate(ds):
        displ_x(dp.x)

def print_Pf(ds):
    if not ds:
        print("no Pf")
        return
    if (type(ds[0]) == list):
        dsn = []
        for dp in ds:
            dsn += dp
        ds = dsn
    print("Pf")
    for i, dp in enumerate(ds):
        displ_dp2(dp.f)

def print_Px(ds):
    if not ds:
        print("no Px")
        return
    if (type(ds[0]) == list):
        dsn = []
        for dp in ds:
            dsn += dp
        ds = dsn
    print("Px")
    for i, dp in enumerate(ds):
        displ_x(dp.x)


def displ_Pf(ds):
    if (type(ds[0]) == list):
        dsn = []
        for dp in ds:
            dsn += dp
        ds = dsn
    print("f")
    for i, dp in enumerate(ds):
        displ_dp2(dp.f)

def displ_Pf_reve(ds):
    if (type(ds[0]) == list):
        dsn = []
        for dp in ds:
            dsn += dp
        ds = dsn
    print("f")
    for i, dp in enumerate(ds):
        displ_dp2(np.flip(dp.f, axis=0))


def reverse_info(ds):
    dsn = []
    for dp in ds:
        dsn.append(OptimizeResult(f=np.flipud(dp.f), x=np.flipud(dp.x), g = np.flipud(dp.g)))
    return dsn


def displ_dp2(f):
    if len(f) == 1:
        print('(',f[0],')')
    elif len(f) == 2:
        print('(',f[0],',',f[1],')')
    elif len(f) == 3:
        print('(', f[0], ',', f[1], ',', f[2], ')')
    elif len(f) == 4:
        print('(', f[0], ',', f[1], ',', f[2],',', f[3],')')
    elif len(f) == 5:
        print('(', f[0], ',', f[1], ',', f[2],',', f[3], ',', f[4],')')
    elif len(f) == 6:
        print('(', f[0], ',', f[1], ',', f[2],',', f[3], ',', f[4], ',', f[5],')')
    else:
        print('(', f[0], ',', f[1], ',', f[2],',', f[3], ')')


def displ_x(x):
    if len(x) == 1:
        print('(', x[0], ',', 0.0, ')')
    elif len(x) == 2:
        print('(', x[0], ',', x[1], ')')
    else:
        print('(', x[0], ',', x[1], ',', x[2], ')')

def dptostring(x):
    if len(x) == 1:
        return '( ' + str(x[0])+ ','+ str(0.0)+ ' )'
    elif len(x) == 2:
        return '( ' + str(x[0]) + ',' + str(x[1]) + ' )'
    else:
        return '( ' + str(x[0]) + ',' + str(x[1]) +','+ str(x[2])+' )'



def displ_dp(dp, i=0):
    if hasattr(dp, 'minf'):
        # print('{:10}'.format('test'))
        print('index =', i, ',f =', dp.f, ',x =', dp.x, ',minf =', dp.minf)
    else:
        print('index =', i, ',f =', dp.f, ',x =', dp.x,)

def fun1(x):
    return ((x[0] - 1)*x[1]**2)/3
def fun2(x):
    return x[1]

def objfuncs(x):
    f1 = ((x[0] - 1)*x[1]**2)/3
    f2 = x[1]
    f = np.array([f1, f2])
    return f




def unpackdata(data):

    unpacked_data = []

    for i in range(len(data[0].f)):
        f = []
        for j in range(len(data)):
            f.append(data[j].f[i])

        unpacked_data.append(f)

    return unpacked_data

def unpackdatax(data):

    unpacked_data = []

    for i in range(len(data[0].x)):
        x = []
        for j in range(len(data)):
            x.append(data[j].x[i])

        unpacked_data.append(x)

    return unpacked_data

# def createObSp():
#
#     x_ana = np.arange(0.0, 1.0, (1/49))
#
#     ObSp = []
#
#     for i in range(len(x_ana)):
#         for j in range(len(x_ana)):
#             ObSp.append(list(objfuncs([x_ana[i], x_ana[j]])))
#
#     ObSp = [list(x) for x in zip(*ObSp)]
#
#     return ObSp

class ShowPareto(object):

    def displ_ds(self, ds):
        if (type(ds[0]) == list):
            dsn = []
            for dp in ds:
                dsn += dp
            ds = dsn
        for i, dp in enumerate(ds):
            self.displ_dp(dp, i)

    def displ_dp(self, dp, i=0):
        if hasattr(dp, 'minf'):
            # print('{:10}'.format('test'))
            print('index =', i, ',f =', dp.f, ',x =', dp.x, ',lamb =', dp.lamb, ',minf =', dp.minf)
        else:
            print('index =', i, ',f =', dp.f, ',x =', dp.x, ',lamb =', dp.lamb)

    def list_objfuncs(self, objfuncs):
        def objfuncs_list(x):
            return np.asarray([obj(x) for obj in objfuncs])
        return objfuncs_list

    def __init__(self):
        self.ObSp = None
        self.CrSp = None
        # self.ObSp = createObSp(self.list_objfuncs(objfuncs), bounds[0][0], bounds[0][1])
        # self.CrSp = createCrSp(bounds[0][0], bounds[0][1])


    def output(self, data_par, opt=1, I=1, x=None, *args, **kwargs):

        reve = kwargs.pop('reve', False)
        # Unpack data
        par = unpackdata(data_par)

        if reve:
            par = list(reversed(par))

        # Open figure
        fig = plt.figure(I, figsize=(20, 20))
        ax = fig.add_subplot(111)

        # Scatter plot the objective space
        # ax.scatter(self.ObSp[0], self.ObSp[1], s=10)

        # Scatter plot of received data
        c = np.linspace(0, 10, num=len(par[0]))
        ax.scatter(par[0], par[1], s=40, c=c)

        # ax.scatter(par[0], par[1], s=40, color='red')


        if x is not None:
            ax.scatter(x[0], x[1], s=30, color='green')

        # Plot settings
        plt.xlabel('$f_1$', fontsize=20)
        plt.ylabel('$f_2$', fontsize=20)
        plt.title('Objective space', fontsize=20)

        if opt == 1:
            plt.show(block=I)
        elif opt == 2:
            fig.savefig('TestImg/plot_par_' + str(I) + '.png')
            plt.close(fig)
        elif opt == 3:
            from matplotlib2tikz import save as tikz_save
            tikz_save('TikzImg/plot_par_' + str(I) + '.tikz',
                      figureheight='\\figureheight',
                      figurewidth='\\figurewidth')
        else:
            print('No plot option is given.')

    def input(self, data_par, opt=1, I=1, x=None, *args, **kwargs):

        # Unpack data
        par = unpackdatax(data_par)

        # Open figure
        fig = plt.figure(I, figsize=(20, 20))
        ax = fig.add_subplot(111)

        # # Scatter plot the objective space
        # ax.scatter(self.CrSp[0], self.CrSp[1], s=10)

        # Scatter plot of received data
        c = np.linspace(0, 10, num=len(par[0]))
        if len(par) == 1:
            ax.scatter(par[0], np.zeros(len(par[0])), s=40, c=c)
        else:
            ax.scatter(par[0], par[1], s=40, c=c)
        # elif len(par) == 2:
        #     ax.scatter(par[0], par[1], s=40, c=c)
        # else:
        #     ax.scatter(par[0], par[1], par[3], s=40, c=c)

        # # Scatter plot of received data
        # ax.scatter(par[0], par[1], s=40, color='red')

        if x is not None:
            ax.scatter(x[0], x[1], s=30, color='green')

        # Plot settings
        plt.xlabel('$x_1$', fontsize=20)
        plt.ylabel('$x_2$', fontsize=20)
        plt.title('Crateria space', fontsize=20)

        if opt == 1:
            plt.show(block=I)
        elif opt == 2:
            fig.savefig('TestImg/plot_input_par_' + str(I) + '.png')
            plt.close(fig)
        elif opt == 3:
            from matplotlib2tikz import save as tikz_save
            tikz_save('TikzImg/plot_input_par_' + str(I) + '.tikz',
                      figureheight='\\figureheight',
                      figurewidth='\\figurewidth')
        else:
            print('No plot option is given.')



def createObSp(objfunc, lob, upb):
    # Loading parameters

    x_ana = np.arange(lob, upb, (upb-lob)/20)

    ObSp = []

    for i in range(len(x_ana)):
        for j in range(len(x_ana)):
            for k in range(len(x_ana)):
            # for k in range(1):
                ObSp.append(list(objfunc([x_ana[i], x_ana[j], x_ana[k]])))

    ObSp = [list(x) for x in zip(*ObSp)]

    return ObSp

def createCrSp(lob, upb):
    # Loading parameters
    # para =([0, 5], [0, 5], [0, 5])

    x_ana = np.arange(lob, upb, (upb-lob)/20)

    CrSp = []

    for i in range(len(x_ana)):
        for j in range(len(x_ana)):
            CrSp.append(list(np.array([x_ana[i], x_ana[j]])))

    CrSp = [list(x) for x in zip(*CrSp)]

    return CrSp

# def createCrSp():
#     # Loading parameters
#     para = pa.load_parameters()
#
#     x_ana = np.arange(para.lob, para.upb, para.dana)
#
#     CrSp = []
#
#     for i in range(len(x_ana)):
#         for j in range(len(x_ana)):
#             CrSp.append(list(np.array([x_ana[i], x_ana[j]])))
#
#     CrSp = [list(x) for x in zip(*CrSp)]
#
#     return CrSp


def plt_data(data_ini, data_ana, data_par, opt = 1, I = 1):
    # Create objective space
    ObSp = createObSp()

    # Unpack data
    par = unpackdata(data_par)
    ana = unpackdata(data_ana)
    ini = unpackdata(data_ini)

    # Open figure
    fig = plt.figure(I, figsize=(20, 20))
    ax = fig.add_subplot(111)

    # Scatter plot the objective space
    ax.scatter(ObSp[0], ObSp[1], s=10)

    # Scatter plot of received data
    ax.scatter(ana[0], ana[1], s=30, color='orange')
    ax.scatter(ini[0], ini[1], s=30, color='red')
    ax.scatter(par[0], par[1], s=30, color='green')
    # ax.scatter(par[0][0], par[1][0], s=30, color='red')

    # Plot settings
    plt.xlabel('$f_1$',fontsize=20)
    plt.ylabel('$f_2$',fontsize=20)
    plt.title('Objective space',fontsize=20)

    if opt == 1:
        plt.show(block=I)
    elif opt == 2:
        fig.savefig('TestImg/plot_data_' + str(I) + '.png')
        plt.close(fig)
    elif opt == 3:
        from matplotlib2tikz import save as tikz_save
        tikz_save('TikzImg/plot_data_' + str(I) + '.tikz',
               figureheight = '\\figureheight',
               figurewidth = '\\figurewidth')
    else:
        print('No plot option is given.')

def plt_par(data_par, opt = 1, I = 1):
    # Create objective space
    # ObSp = createObSp(objfunc, lob, upb)

    # Unpack data
    par = unpackdata(data_par)

    # Open figure
    fig = plt.figure(I, figsize=(20, 20))
    ax = fig.add_subplot(111)

    # Scatter plot the objective space
    ax.scatter(ObSp[0], ObSp[1], s=10)

    # Scatter plot of received data
    ax.scatter(par[0], par[1], s=40, color='red')
    # ax.scatter(par[0], par[1], s=30, color='green')

    # Plot settings
    plt.xlabel('$f_1$', fontsize=20)
    plt.ylabel('$f_2$', fontsize=20)
    plt.title('Objective space', fontsize=20)

    if opt == 1:
        plt.show(block=I)
    elif opt == 2:
        fig.savefig('TestImg/plot_par_' + str(I) + '.png')
        plt.close(fig)
    elif opt == 3:
        from matplotlib2tikz import save as tikz_save
        tikz_save('TikzImg/plot_par_' + str(I) + '.tikz',
                  figureheight='\\figureheight',
                  figurewidth='\\figurewidth')
    else:
        print('No plot option is given.')

def plt_input_data(data_ini, data_ana, data_par, opt = 1, I = 1):
    # Create objective space
    CrSp = createCrSp()

    # Unpack data
    par = unpackdatax(data_par)
    ana = unpackdatax(data_ana)
    ini = unpackdatax(data_ini)

    # Open figure
    fig = plt.figure(I, figsize=(20, 20))
    ax = fig.add_subplot(111)

    # Scatter plot the objective space
    ax.scatter(CrSp[0], CrSp[1], s=10)

    # Scatter plot of received data
    ax.scatter(ana[0], ana[1], s=30, color='orange')
    ax.scatter(ini[0], ini[1], s=30, color='red')
    ax.scatter(par[0], par[1], s=30, color='green')
    # ax.scatter(par[0][0], par[1][0], s=30, color='red')

    # Plot settings
    plt.xlabel('$x_1$',fontsize=20)
    plt.ylabel('$x_2$',fontsize=20)
    plt.title('Crateria space',fontsize=20)

    if opt == 1:
        plt.show(block=I)
    elif opt == 2:
        fig.savefig('TestImg/plot_input_data_' + str(I) + '.png')
        plt.close(fig)
    elif opt == 3:
        from matplotlib2tikz import save as tikz_save
        tikz_save('TikzImg/plot_input_data_' + str(I) + '.tikz',
               figureheight = '\\figureheight',
               figurewidth = '\\figurewidth')
    else:
        print('No plot option is given.')

def plt_input_par(data_par, opt = 1, I = 1):
    # Create objective space
    CrSp = createCrSp()

    # Unpack data
    par = unpackdatax(data_par)

    # Open figure
    fig = plt.figure(I, figsize=(20, 20))
    ax = fig.add_subplot(111)

    # Scatter plot the objective space
    ax.scatter(CrSp[0], CrSp[1], s=10)

    # Scatter plot of received data
    ax.scatter(par[0], par[1], s=40, color='red')
    # ax.scatter(par[0], par[1], s=30, color='green')

    # Plot settings
    plt.xlabel('$x_1$',fontsize=20)
    plt.ylabel('$x_2$',fontsize=20)
    plt.title('Crateria space',fontsize=20)

    if opt == 1:
        plt.show(block=I)
    elif opt == 2:
        fig.savefig('TestImg/plot_input_par_' + str(I) + '.png')
        plt.close(fig)
    elif opt == 3:
        from matplotlib2tikz import save as tikz_save
        tikz_save('TikzImg/plot_input_par_' + str(I) + '.tikz',
               figureheight = '\\figureheight',
               figurewidth = '\\figurewidth')
    else:
        print('No plot option is given.')


