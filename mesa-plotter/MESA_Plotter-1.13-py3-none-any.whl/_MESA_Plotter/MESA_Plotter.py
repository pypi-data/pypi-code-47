import matplotlib.colors as col
import numpy as np
import os
import json
import subprocess

def check_sshfs(path):
    if os.path.exists(os.path.join(path,"1","log_Teff.txt")):
        return

    command = f"sshfs endurance:/mnt/data/MESA_Plotter {path}"
    subprocess.check_call(command.split())

    if not os.path.exists(os.path.join(path,"1","log_Teff.txt")):
        raise IOError(f"Issue with sshfs, can't mount tracks to {path}")


def folder(mass):
    masses = np.linspace(np.log10(0.2),np.log10(10), 60)
    masses = 10**masses
    delta = np.inf
    out = 0
    for i in range(len(masses)):
        if abs(mass-masses[i]) < delta:
            delta = abs(mass-masses[i])
            out = i+1
    return out

def color_mag(path,c_1='B',c_2='V'):
    bc_v = np.genfromtxt(path + f'/bc_V.txt')
    log_L = np.genfromtxt(path + f'/log_L.txt')
    if c_1 =='BP' and c_2 =='RP':
        mag_1 = np.genfromtxt(path + f'/abs_mag_V.txt')
        mag_2 = np.genfromtxt(path + f'/abs_mag_I.txt')
        v_i = mag_1 - mag_2
        bp_rp = -0.04212 + 1.286*v_i - 0.009494*v_i**2
        abs_mag = -0.01746 + 0.008092*(mag_1-mag_2)-0.2810*(mag_1-mag_2)**2+0.03655*(mag_1-mag_2)**3 + (4.8 - 2.5 * log_L - bc_v)
        return (bp_rp, abs_mag, rf'$({c_1} - {c_2})_0$', r'$M_G$')
    else:
        mag_1 = np.genfromtxt(path + f'/abs_mag_{c_1}.txt')
        mag_2 = np.genfromtxt(path + f'/abs_mag_{c_2}.txt')
        return (mag_1 - mag_2, 4.8 - 2.5 * log_L - bc_v, rf'$({c_1} - {c_2})_0$', r'$M_v$')


def get_path():
    conf_file = os.path.join(os.path.expanduser("~"), ".MESAPlotter", "MESAPlotter.json")
    if os.path.exists(conf_file):
        with open(conf_file, 'r')as f:
            data_dict = json.load(f)
        return data_dict['sshfs_path']
    else:
        path = input("Please enter the full path for the MESA tracks:\n")
        while not os.path.exists(path):
            path = input("Path doesn't exist. Please enter the full path for the MESA tracks:\n")

        os.makedirs(os.path.join(os.path.expanduser("~"), ".MESAPlotter"))
        data_dict = {'sshfs_path': path}
        with open(conf_file, 'w') as f:
            json.dump(data_dict, f)
        return path


def plot_diagram(x_name, y_name, ax, fig, z_name = ' ', mass_min = 0.5, mass_max = 6.0, color_log = False, isochrones = [], specialIsoschrones = [], specialColor = [], highmainsequence = False, initial_z = '0.02'):
    masses = np.linspace(np.log10(0.2),np.log10(10), 60)
    masses = 10**masses
    path = get_path()
    path = path + '/Z' + initial_z
    start = folder(mass_min)
    end = np.min([folder(mass_max),60])
    labels= {'log_Teff': r'log$(T_\mathrm{eff})$', 'log_L': r'log$(L/L_\odot)$', 'log_g': r'log$(g)$', 'pp': 'log energy production by PP chain', 'cno': 'log energy production by CNO cycle',
             'star_age': 'age in years', 'abs_mag_B': 'absolute Magnitude B',  'abs_mag_R': 'absolute Magnitude R',  'abs_mag_H': 'absolute Magnitude H',  'abs_mag_I': 'absolute Magnitude I',
             'abs_mag_J': 'absolute magnitude J',  'abs_mag_K': 'absolute magnitude K',  'abs_mag_L': 'absolute magnitude L',  'abs_mag_Lprime': r'absolute magnitude $L_\mathrm{prime}$',
             'abs_mag_M': 'absolute magnitude M',  'abs_mag_U': 'absolute magnitude U',  'abs_mag_V': 'absolute magnitude V',  'bc_B': 'bolometric correction B', 'bc_H': 'bolometric correction H',
             'bc_I': 'bolometric correction I', 'bc_J': 'bolometric correction J', 'bc_K': 'bolometric correction K', 'bc_L': 'bolometric correction L', 'bc_Lprime': r'bolometric correction $L_\mathrm{prime}$',
             'bc_M': 'bolometric correction M', 'bc_R': 'bolometric correction R', 'bc_U': 'bolometric correction U', 'bc_V': 'bolometric correction V', 'center_h1': r'central hydrogen abundance X_H',
             'conv_mx1_bot': 'mass coordinate of bottom of largest convective zone', 'conv_mx2_bot': 'mass coordinate of bottom of second largest convective zone',
             'conv_mx1_top': 'mass coordinate of top of largest convective zone', 'conv_mx2_top': 'mass coordinate of top of second largest convective zone',
             'log_R': r'log$(R/R_\odot)$', 'model_number': 'MESA model number', 'num_backups': 'number of backups up to this model number', 'num_iters': 'number of newton iterations at this step',
             'num_retries': 'number of MESA retries up to this model', 'num_zones': 'number of zones inside the stellar model', 'star_mass': r'stellar mass $M/M_\odot$','star_mdot': r'mass loss $\dot{M}/M_\odot$',
             'time_step': 'timestep in years', 'total_internal_energy': 'thermodynamic internal energy u',
             }
    built_ins = {'color_mag':[color_mag,'B','V']}
    colors = ['B','H','I','J','K','L','Lprime','M','R','U','V']
    for c_1 in colors:
        for c_2 in colors:
            if c_1 == c_2:
                continue
            else:
                built_ins[f'color_mag_{c_1}_{c_2}'] = [color_mag,c_1,c_2]
    built_ins['color_mag_BP_RP'] = [color_mag,'BP','RP']

    x_sign = 1
    y_sign = 1
    if x_name in ['log_Teff']:
        x_sign = -1
    if y_name in ['log_g']+list(built_ins.keys()):
        y_sign = -1
    if y_name in ['color_mag', 'color_mag_r_b']:
        x_sign = -1

    if isochrones != []:
        steps= []
        for i in range(start, end+1):
            if i >52 and highmainsequence:
                age = np.genfromtxt(path + f'/TAMS/{i}/star_age.txt')
            else:
                age = np.genfromtxt(path + f'/ZAMS/{i}/star_age.txt')
            stepslist = []
            for isos in range(len(isochrones)):
                isostep = -1
                for k in range(len(age)):
                    if age[k]>float(isochrones[isos])*10**6:
                        isostep = k
                        break
                stepslist.append(isostep)
            steps.append(stepslist)

    if z_name != ' ':
        all_x = []
        all_y = []
        all_z = []

    if isochrones != []:
        iso_data = {f'iso{isochrones[0]}': []}
        for k in range(1, len(isochrones)):
            iso_data[f'iso{isochrones[k]}'] = []

    for i in range(start, end+1):
        if x_name == 'built_in':
            if i > 52 and highmainsequence:
                x_value, y_value, xlabel, ylabel = built_ins[y_name][0](path + f'/TAMS/{i}', built_ins[y_name][1],
                                                                        built_ins[y_name][2])
            else:
                x_value, y_value, xlabel, ylabel = built_ins[y_name][0](path + f'/ZAMS/{i}', built_ins[y_name][1],
                                                                        built_ins[y_name][2])
        else:
            if i >52 and highmainsequence:
                x_value = np.genfromtxt(path + f'/TAMS/{i}/{x_name}.txt')
                y_value = np.genfromtxt(path + f'/TAMS/{i}/{y_name}.txt')
            else:
                x_value = np.genfromtxt(path + f'/ZAMS/{i}/{x_name}.txt')
                y_value = np.genfromtxt(path + f'/ZAMS/{i}/{y_name}.txt')

        if isochrones != []:
            for k in range(len(isochrones)):
                if steps[i-start][k] != -1:
                    iso_data[f'iso{isochrones[k]}'].append(x_value[steps[i-start][k]])
                    iso_data[f'iso{isochrones[k]}'].append(y_value[steps[i-start][k]])

        if z_name != ' ':
            if i >52 and highmainsequence:
                z_value = np.genfromtxt(path + f'/TAMS/{i}/{z_name}.txt')
            else:
                z_value = np.genfromtxt(path + f'/ZAMS/{i}/{z_name}.txt')
            for k in range(len(z_value)):
                all_z.append(z_value[k])
                all_x.append(x_value[k])
                all_y.append(y_value[k])
        else:
            ax.plot(x_value, y_value, 'k-', lw = 0.7)
            pass

    if z_name != ' ':
        if color_log:
            scat = ax.scatter(all_x, all_y, c=all_z, s=10, cmap='jet', zorder=1, alpha=0.4, norm=col.LogNorm())
        else:
            scat = ax.scatter(all_x, all_y, c=all_z, s=10, cmap='jet', zorder=1, alpha=0.4)
        cbar = fig.colorbar(scat, ax=ax)
        try:
            cbar.set_label(labels[z_name])
        except:
            cbar.set_label(z_name)
    if isochrones != []:
        for k in range(len(isochrones)):
            if str(k) in specialIsoschrones:
                color = -1
                for ic in range(len(specialIsoschrones)):
                    if str(k) == specialIsoschrones[ic]:
                        color = ic
                ax.plot(iso_data[f'iso{isochrones[k]}'][::2], iso_data[f'iso{isochrones[k]}'][1::2], linestyle = '--', color = specialColor[color],lw = 1.5)#,  alpha = 0.7)
            else:
                ax.plot(iso_data[f'iso{isochrones[k]}'][::2], iso_data[f'iso{isochrones[k]}'][1::2], 'k--',lw = 1.5,  alpha = 0.7)
            ax.text(iso_data[f'iso{isochrones[k]}'][0]+x_sign*0.01*np.std(ax.set_xlim()), iso_data[f'iso{isochrones[k]}'][1], f'{isochrones[k]} Myr', fontsize = 'xx-small')

    else:
        pass
    if x_name in ['log_Teff']:
        ax.invert_xaxis()
    if y_name in ['log_g']+list(built_ins.keys()):
        ax.invert_yaxis()
    if y_name in ['color_mag_r_b']:
        ax.invert_xaxis()

    if x_name == 'built_in':
        ax.set_xlabel(xlabel)
    else:
        try:
            ax.set_xlabel(labels[x_name])
        except:
            ax.set_xlabel(x_name)
    if x_name == 'built_in':
        ax.set_ylabel(ylabel)
    else:
        try:
            ax.set_ylabel(labels[y_name])
        except:
            ax.set_ylabel(y_name)