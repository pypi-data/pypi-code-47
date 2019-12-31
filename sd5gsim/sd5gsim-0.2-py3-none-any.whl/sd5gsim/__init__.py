
# coding: utf-8

# In[2]:


import uuid
class channel:
    def __init__(self, **kwargs):
        self.ch_id = "ch_" + str(uuid.uuid4())
        self.power = None
        self.availability = None
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.allocations = []

    def add_node_to_alloc(self, **kwargs): # kwargs = {"alloc_node": alloc_node,"alloc_time": alloc_time,"alloc_power": alloc_power}
        alloc = allocation(**kwargs)
        self.alloc_res_list.append(alloc)


# In[3]:


import uuid
class allocation:
    def __init__(self, **kwargs):
        self.alloc_id = "alloc_" + str(uuid.uuid4())
        self.alloc_node = None
        self.alloc_time = None
        self.alloc_power = None
        for key, value in kwargs.items():
            setattr(self, key, value)


# In[4]:


import uuid
class antenna:
    def __init__(self, **kwargs):
        self.ant_id = "a_" + str(uuid.uuid4())
        self.active = None
        self.power = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.power = 0.0
        self.active = False


# In[5]:


import uuid
class resource:
    def __init__(self, **kwargs):
        self.res_id = "r_" + str(uuid.uuid4())
        self.alloc_ch = None
        self.alloc_ant = None
        self.alloc_time = None
        self.alloc_power = None
        for key, value in kwargs.items():
            setattr(self, key, value)


# In[6]:


import uuid
class v_node:
    def __init__(self, **kwargs):
        self.v_node_id = "v_" + str(uuid.uuid4())
        self.active = False
        self.alloc_res_list = []
        self.parent_nd = None
        self.parent_bs = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def add_res(self, **kwargs): # kwargs = {"channel": channel,"ant": ant, "power": power, "time": time}
        res = resource(**kwargs)
        self.alloc_res_list.append(res)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def request_res(self):
        pass

    def vacate_res(self):
        pass



# In[7]:


import uuid
class connection:
    def __init__(self, **kwargs):
        self.connection_id = "c_" + str(uuid.uuid4())
        self.src_node = None
        self.src_vnode = None
        self.src_ant = None
        self.src_ch = None
        self.des_node = None
        self.des_vnode = None
        self.des_ant = None
        for key, value in kwargs.items():
            setattr(self, key, value)


# In[8]:


import uuid
from pprint import pprint
from random import randrange

class node:
    def __init__(self, **kwargs):
        self.node_id = "n_" + str(uuid.uuid4())
        self.vn_count = 6
        self.ant_count = 6
        self.ch_count = 0
        self.coordinates = {"x": randrange(1, 1125), "y": randrange(1, 950)}
        self.parent_bs = None
        self.local_channels = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.local_antennas = [antenna(**{"active": False, "power": 0.0}) for i in range(0, self.ant_count)]
        self.local_v_nodes = [v_node(**{"parent_nd": self, "parent_bs": self.parent_bs}) for i in range(0, self.vn_count)]

    def add_to_local_channels(self, **kwargs):
        pass

    def get_channel_from_LP(self, des_nd):
        pass

    def activate_v_node(self):
        found_vn = None
        for vn in self.local_v_nodes:
            if vn.active == False:
                vn.activate()
                found_vn = vn
        return found_vn

    def deactivate_v_node(self, v_node):
        v_node.deactivate()

    def activate_ant(self):
        found_ant = None
        for ant in self.local_antennas:
            if ant.active == False:
                ant.activate()
                found_ant = ant
        return found_ant

    def deactivate_ant(self, ant):
        ant.deactivate()

    def set_local_channels(self):
        chs = {}
        for i in range(0, self.ch_count):
            ch = channel()
            chs[ch.ch_id] = {"availability": True, "power": 12000}
        return chs

    def set_local_antennas(self):
        ants = {}
        for i in range(0, self.ant_count):
            ant = antenna()
            ants[ant.ant_id] = {"availability": True, "power": 12000}
        return ants

    def request_ch(self, rec_node):
        pass

    def print_info(self):
        pprint(vars(self))


# In[9]:


import uuid
from random import randrange
import matplotlib.pyplot as plt

class basestation:
    def __init__(self, **kwargs):
        self.bs_id = "b_" + str(uuid.uuid4())
        self.n_count = 6
        self.all_ch_count = 6

        self.coordinates = {"x": randrange(540, 590), "y": randrange(450, 500)}
        self.dimensions = {"x": 1000, "y": 1000}

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.bs_nodes = [node(**{"parent_bs": self}) for i in range(0, self.n_count)]
        self.global_pool = [channel(**{"availability": True, "power": 12000}) for i in range(0, self.all_ch_count)]

        self.ch_allocations = {}

        # Calculating Network Metrics
        self.channel_capacity = 5000
        self.num_of_reqs = 0
        self.num_of_blocked_reqs = 0
        self.num_of_transmitted_pkts = 0
        self.total_bandwidth = self.channel_capacity * self.all_ch_count
        self.utilized_channels = 0
        self.num_control_msg = 0
        self.packet_size = 500
        self.control_msg_size = 50



        self.throughput = 0.0
        self.blocking_rate = 0.0
        self.channel_utilization = 0.0

    def calculate_metrics(self, sim_time):
        try:
            thpt = (self.num_of_transmitted_pkts * self.packet_size) / sim_time
        except Exception as e:
            thpt = 0.0
        try:
            overhead = (self.num_control_msg * self.control_msg_size) / (self.num_of_transmitted_pkts * self.packet_size)
        except Exception as e:
            overhead = 0.0
        try:
            block_rate = self.num_of_blocked_reqs / self.num_of_reqs
        except Exception as e:
            block_rate = 0.0
        try:
            utilization = self.utilized_channels / (self.total_bandwidth)
        except Exception as e:
            utilization = 0.0

        return(thpt, overhead, block_rate, utilization)

    def assing_ch_to_node(self, **kwargs):
        ch_to_assign = None
        for ch in self.global_pool:
            if ch.availability:
                ch.availability = False
                kwargs["src_ch"] = ch
                self.establish_connection(**kwargs)
                return ch
        return ch_to_assign

    def establish_connection(self, **kwargs):
        # kwargs = {"src_node": src_node, "src_vnode": src_vnode, "src_ant": src_ant, "src_ch": src_ch, "des_node": des_node, "des_vnode": des_vnode, "des_ant": des_ant}
        cnt = connection(**kwargs)
        self.ch_allocations[cnt.src_ch.ch_id] = cnt.src_node

    def terminate_connection(self, **kwargs):
        src_node = kwargs["src_node"]
        src_vnode = kwargs["src_vnode"]
        src_ant = kwargs["src_ant"]
        des_node = kwargs["des_node"]
        des_vnode = kwargs["des_vnode"]
        des_ant = kwargs["des_ant"]
        src_ch = kwargs["src_ch"]
        num_of_pkts = kwargs["num_of_pkts"]

        self.num_of_transmitted_pkts += num_of_pkts
        src_node.deactivate_v_node(src_vnode)
        des_node.deactivate_v_node(des_vnode)
        src_node.deactivate_ant(src_ant)
        des_node.deactivate_ant(des_ant)
        src_ch.availability = True

        self.ch_allocations[src_ch.ch_id] = None
    def calculate_tx_time(self, num_pckts):
        return (num_pckts*self.packet_size)/self.channel_capacity

    def plot_network(self):
        x_coordinates = []
        y_coordinates = []
        for nd in self.bs_nodes:
            x_coordinates.append(nd.coordinates["x"])
            y_coordinates.append(nd.coordinates["y"])
        plt.scatter(x_coordinates, y_coordinates)
        plt.show()


# # GUI

# In[10]:


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# In[11]:


from tkinter import *
from PIL import Image, ImageTk
import time
from tkinter import ttk
from collections import defaultdict
import random
from statistics import mean

class SD5GSim_GUI:
    def __init__(self, root):
        self.root = root
        self.root.wm_title("Network Simulator")
        self.root.geometry("1500x1000")
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.submenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.submenu)
        self.submenu.add_command(label="New Project")
        self.submenu.add_separator()
        self.submenu.add_command(label="Exit", command=self.root.destroy)

        self.run_menu = Menu(self.menu)
        self.menu.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Generate Environment", command=lambda: self.generate_environment_2(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()))
        self.run_menu.add_command(label="Start Simulation", command=lambda: self.get_sim_args(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()))

        self.about_menu = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.about_menu)
        self.about_menu.add_command(label="About", command=self.doNothing)
        #############################

        self.left_frame = Frame(self.root, bg='#20B2AA')
        self.left_frame.place(relx=0, rely=0.05, relwidth=0.25, relheight=0.95)

        self.right_frame = LabelFrame(self.root, highlightbackground="black", highlightthickness=1, text="Simulation Environment")
        self.right_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.95)

        ###################

        self.box1 = LabelFrame(self.left_frame, borderwidth=1, relief="solid", text="Simulation Parameters", bg='#20B2AA')
        self.box2 = LabelFrame(self.left_frame, borderwidth=1, relief="solid", text="Simulation Results", bg='#20B2AA')
        self.box1.pack(expand=True, fill="both", padx=5, pady=5)
        self.box2.pack(expand=True, fill="both", padx=5, pady=5)

        ###################

        self.label1 = Label(self.box1,  text="Number of cells", bg='#20B2AA')
        self.label1.grid(row= 1, column=0, sticky=E)
        self.entry1 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry1.grid(row=1,column=1)
        self.label2 = Label(self.box1,  text="Number of channels/cell", bg='#20B2AA')
        self.label2.grid(row= 2, column=0, sticky=E)
        self.entry2 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry2.grid(row=2,column=1)
        self.label3 = Label(self.box1,  text="Number of PNs/cell", bg='#20B2AA')
        self.label3.grid(row= 3, column=0, sticky=E)
        self.entry3 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry3.grid(row=3,column=1)
        self.label4 = Label(self.box1,  text="Number of VNs/PN", bg='#20B2AA')
        self.label4.grid(row= 4, column=0, sticky=E)
        self.entry4 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry4.grid(row=4,column=1)
        self.label5 = Label(self.box1,  text="Number of RIs/PN", bg='#20B2AA')
        self.label5.grid(row= 5, column=0, sticky=E)
        self.entry5 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry5.grid(row=5,column=1)
        self.label6 = Label(self.box1,  text="Simulation Time", bg='#20B2AA')
        self.label6.grid(row= 6, column=0, sticky=E)
        self.entry6 = Entry(self.box1, bg='white', relief=SUNKEN, width=6)
        self.entry6.grid(row=6,column=1)

        self.label7 = Label(self.box2, text="Average Network Throughput", bg='#20B2AA')
        self.label7.grid(row= 11, column=0, sticky=E)
        self.label8 = Label(self.box2, bg='white', text='', relief=SUNKEN, width=6)
        self.label8.grid(row=11,column=1)

        self.label9 = Label(self.box2, text="Average Network Blocking Rate", bg='#20B2AA')
        self.label9.grid(row= 12, column=0, sticky=E)
        self.label10 = Label(self.box2, bg='white', text='', relief=SUNKEN, width=6)
        self.label10.grid(row=12,column=1)

        self.label13 = Label(self.box2, text="Average Network Overhead", bg='#20B2AA')
        self.label13.grid(row= 14, column=0, sticky=E)
        self.label14 = Label(self.box2, bg='white', text='', relief=SUNKEN, width=6)
        self.label14.grid(row=14,column=1)

        #############################
        self.toolbar = Frame(self.root, bd=4, bg='#20B2AA')

        self.run_img = Image.open("run.png")
        # self.run_img = self.run_img.resize((25, 23), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.render2 = ImageTk.PhotoImage(self.run_img)

        self.gen_img = Image.open("gen.png")
        # self.gen_img = self.gen_img.resize((25, 28), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.render3 = ImageTk.PhotoImage(self.gen_img)

        self.exit_img = Image.open("exit.png")
        self.render4 = ImageTk.PhotoImage(self.exit_img)

        self.clear_img = Image.open("clear.png")
        self.render5 = ImageTk.PhotoImage(self.clear_img)
        ##############################################################


        self.gen_butt = Button(self.toolbar, image= self.render3, text = "Generate Envirnment", command=lambda: self.generate_environment_2(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()), bg='#008080')
        self.gen_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.gen_butt, text = 'Generate Envirnment')
        self.run_butt = Button(self.toolbar, image=self.render2, text = "Start Simulation", command=lambda: self.get_sim_args(self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()), bg='#008080')
        self.run_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.run_butt, text = 'Start Simulation')
        self.clear_butt = Button(self.toolbar, image=self.render5, text = "Clear Environment", command=lambda: self.clear_frame(self.right_frame), bg='#008080')
        self.clear_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.clear_butt, text = 'Clear Environment')

        self.exit_butt = Button(self.toolbar, image=self.render4, text = "Exit", command=self.root.destroy, bg='#008080')
        self.exit_butt.pack(side=LEFT, padx=2, pady=2)
        CreateToolTip(self.exit_butt, text = 'Exit Simulator')

        self.toolbar.pack(side=TOP, fill=X)
        ############################
        self.status = Label(self.root, text=" ", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
    def doNothing():
        print("Works!!")

    def clear_frame(self,frame):
        for widget in frame.winfo_children():
            if widget != self.toolbar:
                widget.destroy()

    def generate_environment_2(self, cell_count, ch_count, node_count, vn_count, ant_count, sim_time):
        global bss
        ####################
        tabControl = ttk.Notebook(self.right_frame)          # Create Tab Control
        ####################
        ss_img = Image.open("icon3.png")
        ss_img = ss_img.resize((20, 20), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        render = ImageTk.PhotoImage(ss_img)

        ss1_img = Image.open("icon2.png")
        ss1_img = ss1_img.resize((20, 20), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        render3 = ImageTk.PhotoImage(ss1_img)

        ss2_img = Image.open("icon5.png")
        ss2_img = ss2_img.resize((20, 20), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        render5 = ImageTk.PhotoImage(ss2_img)

        ss_icon_list = [render, render3, render5]

        bs_img = Image.open("icon4.png")
        bs_img = bs_img.resize((50, 50), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        render1 = ImageTk.PhotoImage(bs_img)

        ####################
        bs_args = {
            "n_count": int(node_count),
            "all_ch_count": int(ch_count),
            "dimensions": {
                "x": 2000,
                "y": 2000
            }
        }
        bss = [basestation(**bs_args) for i in range(0, int(cell_count))]
        cell_num = 0
        for bs in bss:
            cell_num+=1
            tab1 = ttk.Frame(tabControl)            # Create a tab
            cell_name = 'Cell ' + str(cell_num)
            tabControl.add(tab1, text=cell_name)      # Add the tab
            tabControl.pack(expand=1, fill="both")  # Pack to make visible
            img0 = Label(tab1, image=render1)
            img0.image = render1
            img0.place(x=bs.coordinates['x'], y=bs.coordinates['y'])
            for node in bs.bs_nodes:
                temp_render = random.choice(ss_icon_list)
                img = Label(tab1, image=temp_render)
                img.image = temp_render
                img.place(x=node.coordinates['x'], y=node.coordinates['y'])

    def get_sim_args(self, cell_count, ch_count, node_count, vn_count, ant_count, sim_time):
        global bss

        max_time = int(sim_time)
        start_time = time.time()  # remember when we started
        while (time.time() - start_time) < max_time:
            run_io_tasks_in_parallel([
                lambda: start_simulation(bss[0]),
                lambda: start_simulation(bss[1]),
                lambda: start_simulation(bss[2]),
                lambda: start_simulation(bss[3]),
                lambda: start_simulation(bss[4]),
            ])


        metrics = defaultdict(list)

        for bs in bss:
            (thpt, overhead, block_rate, utilization) = bs.calculate_metrics(int(sim_time))
            metrics['throughput'].append(thpt)
            metrics['overhead'].append(overhead)
            metrics['blocking'].append(block_rate)

        avg_throughput = round(mean(metrics['throughput']), 2)
        avg_blocking_rate = round(mean(metrics['blocking']), 2)
        avg_overhead = round(mean(metrics['overhead']), 2)

        self.label8['text'] = str(avg_throughput)
        self.label10['text'] = str(avg_blocking_rate)
        self.label14['text'] = str(avg_overhead)


# In[ ]:


from concurrent.futures import ThreadPoolExecutor
import threading
from random import randrange
import random

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()
def start_simulation(bs):
    MIN_PACKET_COUNT = 100
    MAX_PACKET_COUNT = 500
    REQUEST_PROBABILITY = 0.85

    req_prob = random.uniform(0, 1)
    if req_prob < REQUEST_PROBABILITY:
        (sen_nd, rec_nd) = random.choices(bs.bs_nodes, k=2)
        sen_vn = sen_nd.activate_v_node()
        rec_vn = rec_nd.activate_v_node()
        src_ant = sen_nd.activate_ant()
        des_ant = rec_nd.activate_ant()
        num_of_pkts = randrange(MIN_PACKET_COUNT, MAX_PACKET_COUNT)
        bs.num_control_msg += 1

        if all(instance is not None for instance in [sen_vn, rec_vn, src_ant, des_ant]):
            req_attrs = {
                "src_node": sen_nd,
                "src_vnode": sen_vn,
                "src_ant": src_ant,
                "des_node": rec_nd,
                "des_vnode": rec_vn,
                "des_ant": des_ant
            }
            bs.num_of_reqs += 1
            src_ch = bs.assing_ch_to_node(**req_attrs)
            req_attrs["src_ch"] = src_ch
            req_attrs["num_of_pkts"] = num_of_pkts
            if src_ch != None:
                bs.utilized_channels += 1
                curr_attrs = req_attrs
                tx_time = bs.calculate_tx_time(num_of_pkts)
                timer = threading.Timer(tx_time, lambda: bs.terminate_connection(**curr_attrs))
                timer.start()
            else:
                bs.num_of_blocked_reqs += 1
                pass
def main():
    root = Tk()
    my_gui = SD5GSim_GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

