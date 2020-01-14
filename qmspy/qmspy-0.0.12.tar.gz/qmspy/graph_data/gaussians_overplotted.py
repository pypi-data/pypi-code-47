from ..config import *

def gaussians_overplotted(data, savedir):
    """
    """
    df = check_data_type(data)

    #split DataFrame into actual data and gaussian data
    actual = df.loc[:, [ev, amu, sem, std, pks]]
    gaussi = df.loc[:, [apk, gfx, gfy]]

    i = 0
    for label, df in actual.groupby(ev):
        fig, ax = plt.subplots(figsize=(12,12))

        df.plot(amu, sem, label=str(label)+'eV', ax=ax)

        for j in range(int(df[pks].sum())):
            temp = gaussi.iloc[ (i+j)*120 : (i+j+1)*120 ]

            temp.plot(gfx, gfy, ax=ax,
                      label=str(temp.iloc[0][apk])+'amu',
                      alpha=0.5)

        plt.title('Overplotted Gaussians for '+str(label)+'eV Scan')
        plt.xlabel('Mass amu')
        plt.ylabel('Ion Current')
        plt.legend(ncol=2, bbox_to_anchor=(1.25, 1.0))
        plt.tight_layout()
        plt.savefig(savedir + str(label) + '.png')
        plt.close()
        i += j +1
