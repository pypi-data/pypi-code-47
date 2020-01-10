import pandas as pd
import seaborn as sn
import datetime
import us
import os
import matplotlib
import matplotlib.pyplot as plt
from . import peer_explorer, peer_finder

dirname, filename = os.path.split(os.path.abspath(__file__))
matplotlib.use("MacOSX", warn=False, force=True)
STATE_MAPPING = us.states.mapping('fips', 'abbr')


def _code2name(df_data, area):
    name = list(df_data[df_data["AREA"] == area].AREA_NAME)[0]
    if ',' in name:
        area = name.split(",")[0]
        state = name.split(",")[1]
        area = area.split("-")[0]
        state = state.split("-")[0]
        name = area.strip() + " (" + state.strip() + ")"
    else:
        state = STATE_MAPPING[str(area).zfill(5)[:2]]
        name = f"{state}, {name}"

    return name


def _add_state(x):
    fips = x.AREA
    county = x.AREA_NAME
    state = STATE_MAPPING[str(fips).zfill(5)[:2]]
    return f"{state}, {county}"


def _fm_string(fm):
    fm = fm.split("-")[0]
    fm = " ".join([x.capitalize() for x in fm.split("_")])
    return fm


def _time_string():
    now = datetime.datetime.now()
    return "_".join([str(x) for x in [now.month, now.day, now.hour, now.minute]])


def add_mean_row(df_data, subset_area=None, col_dim="AREA"):
    df_data = df_data.set_index(col_dim).T
    df_data["mean"] = df_data.mean(axis=1)
    df_data = (df_data.T).reset_index()
    return df_data


def bar_all_fm(df_data, area, peers, cols, year,
               limit_fms=10, save_fig=None, show=False):
    plt.clf()
    cols = cols[:limit_fms]
    for i, c in enumerate(cols):
        if 'LQ' in c:
            cols[i] = c.split('-')[0]+'-PC_EMPL'
    df_data = df_data[df_data['YEAR'] == year]
    df_data = df_data.dropna(subset=cols, how="any")
    name = _code2name(df_data, area)
    fm = [_fm_string(col) for col in cols]

    def group(x):
        if x in peers:
            return 'Peer group average'
        elif x == area:
            return name
        else:
            return 'All other average'
    df_data["Peer"] = df_data['AREA'].apply(group)
    df_data["NAME"] = df_data["AREA_NAME"].apply(
        lambda x: x.split(",")[0][:12])
    df_peers = df_data[df_data["AREA"].isin(peers)]
    df_others = df_data[~df_data["AREA"].isin(peers)]

    # sn.set(rc={'figure.figsize':(30,8.27)})
    df_data = df_data.groupby('Peer')[cols].mean()
    df_data = df_data.stack().reset_index()
    df_data.columns = ['Areas', 'Industry', 'Concentration']
    df_data['Concentration'] = df_data['Concentration'].apply(lambda x: 100*x)
    df_data['Industry'] = df_data['Industry'].apply(_fm_string)

    fig = sn.barplot(x='Industry', y='Concentration', data=df_data, hue='Areas',
                     hue_order=[name, 'Peer group average',
                                'All other average'],
                     palette="viridis")
    fig.set_ylabel('Concentration of industry (in %)')
    fig.set_xticklabels(labels=df_data['Industry'], rotation=20,
                        horizontalalignment='right', fontsize='medium')
    plt.tight_layout()

    if save_fig is not None:
        plt.savefig(save_fig)
    if show:
        plt.show()


def duo_fm_viz(df_data, area, peers, col, year,
               save_fig=None, show=False):
    plt.clf()

    if 'LQ' in col:
        col = col.split('-')[0]+'-PC_EMPL'
    df_data = df_data[df_data['YEAR'] == year]
    df_data = df_data.dropna(subset=[col], how="any")
    if not os.path.exists(os.path.join(dirname, "../results/")):
        os.mkdir(os.path.join(dirname, "../results/"))
    name = _code2name(df_data, area)
    fm = _fm_string(col)
    df_data[col] = df_data[col].apply(lambda x: 100*x)
    df_data["Peer"] = df_data.apply(
        lambda x: "Peers" if (x.AREA) in peers else "Others", axis=1
    )

    fig, axes = plt.subplots(figsize=(12, 6), ncols=2)
    if ',' not in df_data["AREA_NAME"].iloc[0]:
        df_data['AREA_NAME'] = df_data.apply(_add_state, axis=1)

    df_data["NAME"] = df_data["AREA_NAME"].apply(lambda x: x[:20])
    subdata = df_data[df_data["AREA"].isin(peers)]
    subdata.sort_values(by=col, inplace=True)
    y = df_data[col].median()
    q1 = df_data[col].quantile(0.25)
    q3 = df_data[col].quantile(0.75)
    sn.barplot(x=col, y="NAME", palette=sn.color_palette("Blues",
                                                         n_colors=len(peers)+1),
               data=subdata,
               ax=axes[0])
    axes[0].axvline(x=y, c="#ef8d22ff", label='National Median')
    axes[0].axvline(x=q1, ls="--", lw=0.5, c="#ef8d22ff", label='1st quantile')
    axes[0].axvline(x=q3, ls="--", lw=0.5, c="#ef8d22ff", label='3rd quantile')
    axes[0].set_xlabel(f"")
    axes[0].set_ylabel(f"")
    axes[0].text(1.01*q1, 0, "1st quantile", rotation=90,
                 color='#ef8d22ff', va='top',
                 fontsize='large')
    axes[0].text(1.01*q3, 0, "3rd quantile", rotation=90,
                 color='#ef8d22ff', va='top',
                 fontsize='large')
    axes[0].text(1.01*y, 0, "National median", rotation=90,
                 color='#ef8d22ff', va='top',
                 fontsize='large',
                 fontweight='bold')

    # for tick in axes[0][0].get_xticklabels():
    #     tick.set_rotation(30)
    bin = df_data[col].std()/3
    sn.kdeplot(
        list(df_data[col]),
        # color="blue",
        bw=bin,
        shade=True,
        ax=axes[1],
        color='#ef8d22ff',
        label=f'National distribution'
    )
    for i, p in enumerate(list(subdata['AREA'])):
        val = df_data[df_data['AREA'] == p][col].iloc[0]
        axes[1].axvline(x=val, lw=1,
                        c=sn.color_palette("Blues",
                                           n_colors=subdata.shape[0]).as_hex()[i],
                        )

    axes[1].set_ylabel("% of all areas")
    axes[1].set_xlabel(f"")
    axes[1].set_xlim(0)
    plt.legend(loc='upper right')
    fig.text(0.5, 0.04, f"Concentration of {fm} (in %)", ha='center')

    fig.suptitle(f"{name} and its peers - {fm} ", fontsize=16)
    plt.tight_layout(rect=[0, 0.1, 1, 0.95])
    if save_fig is not None:
        plt.savefig(save_fig)
    if show:
        plt.show()


if __name__ == "__main__":
    dirname, filename = os.path.split(os.path.abspath(__file__))
    df_data = pd.read_csv(
        os.path.join(dirname, "../data/processed/county_metrics_outcomes.csv")
    )
    # df_data = df_data[df_data["YEAR"] == 2015]
    # peers, fms = peer_finder.get_top_n_fms_peers(
    #     df_data, area=53033, year=2016, n_peers=5, n_fms=5
    # )
    peers, fms = peer_finder.get_distinguishing_features_peers(
        df_data, area=53033, year=2016, n_peers=5, n_feat=5
    )

    area = 53033
    bar_all_fm(df_data, area, [53033] + peers, fms, year=2016,
               save_fig=None, show=True)
    # for f in fms:
    duo_fm_viz(df_data, area, [53033] + peers,
               col=fms[0], year=2016, save_fig=None, show=True)
