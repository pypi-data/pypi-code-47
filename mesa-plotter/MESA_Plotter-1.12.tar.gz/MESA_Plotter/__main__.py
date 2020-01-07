import matplotlib.pyplot as plt
import sys
import argparse
import MESA_Plotter._MESA_Plotter.MESA_Plotter as mp

plt.rcParams.update({'font.size': 20, 'axes.labelsize': 'large','xtick.labelsize': 'large','ytick.labelsize': 'large', 'xtick.major.size': 10,'xtick.major.width': 2,'ytick.major.size': 10,'ytick.major.width': 2,'ytick.minor.size': 5,'ytick.minor.width': 1,})


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument("x_axis", help="Variable to plot on x-axis. Use built_in to acces the built in plots like color magnitude diagramms.", type=str)
    parser.add_argument("y_axis", help="Variable to plot on y-axis. If x_axis==built_in, choose built in plot to generate (color_mag, color_mag_r_b)",  type=str)
    parser.add_argument("-z", "--z_axis", help="If this option is set, this variable is plotted as color code.", type=str, default= ' ')
    parser.add_argument("-fs", "--figsize",
                        help="Optional parameter to control the size of the plot.",
                        type=str, default="16,9")

    parser.add_argument("-c", "--colorLog", help="If this option is set, the color code will be log scaled", action='store_true')

    parser.add_argument("-min", "--minMass",
                        help="Defines the lowest mass of evolutionary tracks that will be plotted."
                        "Note: it takes the track which mass value is closest to this.", type=float, default=0.2)

    parser.add_argument("-max", "--maxMass",
                        help="Defines the highest mass of evolutionary tracks that will be plotted."
                        "Note: it takes the track which mass value is closest to this.", type=float, default=10.0)
    parser.add_argument("-ic", "--isochrones",
                        help="For each age in this list (age in Myrs), an isochron will be plotted", nargs='+', default=[])
    parser.add_argument("-si", "--specialIsochrone",
                        help="Choose which isochrones should be Plotted in a specific color. First Isochrone has ID 0.", nargs='+', default=[])
    parser.add_argument("-sc", "--specialColor",
                        help="Choose the color for the specific isochrones", nargs='+', default=[])
    parser.add_argument("-hms", "--highmainsequence",
                        help="If this option is set, the evolutionary tracks for high mass stars include the main sequence", action='store_true')
    parser.add_argument("-iz", "--initial_Z",
                        help="The metallicity to use for the plots", type=str, default= '0.02')


    args = parser.parse_args(args)

    f_x = None if args.figsize.split(",")[0] == 'None' else float(args.figsize.split(",")[0])
    f_y = None if args.figsize.split(",")[1] == 'None' else float(args.figsize.split(",")[1])

    fig, ax = plt.subplots(1, figsize = (f_x, f_y))
    mp.plot_diagram(args.x_axis, args.y_axis, ax, fig, z_name=args.z_axis, mass_min=args.minMass, mass_max=args.maxMass, color_log=args.colorLog, isochrones =args.isochrones,
                    specialIsoschrones= args.specialIsochrone, specialColor = args.specialColor , highmainsequence = args.highmainsequence, initial_z = args.initial_Z)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

