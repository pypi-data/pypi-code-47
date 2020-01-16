import sys
import os
import shutil

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk

#printsq = sg.Print
#sg.ChangeLookAndFeel('GreenTan')

import som_selector

def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas
    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = Tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo


def show_figure(fig, som_model_path):
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds    
    print(figure_x, figure_y, figure_w, figure_h)
    # define the window layout      
    layout = [[sg.Text('Plot test')],      
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.InputText(key='_save_input_', visible=False, change_submits=True, disabled=True)],
              [sg.SaveAs('Save Model', enable_events=True, file_types=(("Text Files", "*.txt"),), 
                        key='_save_model_path_', target='_save_input_'), sg.Cancel(key='_cancel_')]]      

    # create the window and show it without the plot      
    fig_window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI').Layout(layout).Finalize()      


    # add the plot to the window      
    fig_photo = draw_figure(fig_window.FindElement('canvas').TKCanvas, fig)      

    # show it all again and get buttons
    while True:
        fig_event, fig_values = fig_window.Read()      
        
        print(fig_event)
        if fig_event == '_save_input_':
            # Save the model to their place of choosing
            shutil.copy(som_model_path, fig_values['_save_input_'])
            break
        if fig_event == '_cancel_':
            break
        if event is None:      
            break

    fig_window.Close()
            
#root = Tkinter.Tk()
#defaultbg = root.cget('bg')
#print(defaultbg)

validated = False

layout = [[sg.Text('SOM Selector Tool', size=(30, 1), font=("Helvetica", 14))],      
[sg.Text('_'  * 100, size=(70, 1))],
[sg.Text('Workspace:', size=(25, 1), auto_size_text=True, justification='right'), 
    #sg.InputText(default_text='Y:/EPSCoR/My-Project/Data/som_selector_wkspace', do_not_clear=True, key='_output_dir_path_'),
    sg.InputText(do_not_clear=True, key="_output_dir_path_"),
    sg.FolderBrowse()],
[sg.Text('_'  * 100, size=(70, 1))],    
[sg.Text('SOM Input Features:', size=(25, 1), auto_size_text=True, justification='right'), 
    sg.InputText(default_text='Y:/EPSCoR/My-Project/Data/Kristen/SedRegDataV2g-Copy.csv', do_not_clear=True, key="_som_input_path_"),
    sg.FileBrowse()],
[sg.Text('SOM Parameters:', size=(25, 1), auto_size_text=True, justification='right'), 
    sg.InputText(default_text='Y:/EPSCoR/My-Project/Data/test_sample_data/som_classified_clusters.csv', do_not_clear=True, key='_som_params_path_'),
    sg.FileBrowse()],
[sg.Text('SOM Columns:', size=(25, 1), auto_size_text=True, justification='right'), sg.InputText(do_not_clear=True, key='_columns_')],
[sg.Text('SOM Rows:', size=(25, 1), auto_size_text=True, justification='right'), sg.InputText(do_not_clear=True, key='_rows_')],
[sg.Text('SOM Iterations:', size=(25, 1), auto_size_text=True, justification='right'), sg.InputText(default_text='500', do_not_clear=True, key='_iterations_')],
[sg.Text('SOM Grid Type:', size=(25, 1), auto_size_text=True, justification='right'), sg.InputCombo(['hex', 'square'], default_value=0, key='_grid_type_')],
[sg.Text('Number of Clusters:', size=(25, 1), auto_size_text=True, justification='right'), sg.InputText(do_not_clear=True, key='_number_clusters_')],

[sg.Text('', text_color=None, background_color=None, size=(70, 1), key='_success_message_')],
[sg.Submit(), sg.Cancel(key='_cancel_')]]

window = sg.Window('SOM Selector Tool', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

# Event Loop      
while True:      
    event, values = window.Read()      
    print(event)
    if event is None:      
        break
    if event == '_cancel_':
        break
    if event == 'Submit':
        try:
            # TODO: Should try to validate file inputs first           
            results = som_selector.execute(values)
            som_fig = results['som_figure']
            som_model_path = results['model_weights_path']
            show_figure(som_fig, som_model_path)
            #print(values)
            pass
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        window.FindElement('_success_message_').Update(text_color="#24b73d")
        window.FindElement('_success_message_').Update('The Model Completed Successfully')
        window.FindElement('_cancel_').Update('Close')

print("Done.")

