import sys
import os
import array
import sqlite3
import json
import posixpath
import subprocess

from math import pi, sin, cos

from multiprocessing import Process, Pipe

import wx
import wx.lib.scrolledpanel
import wx.lib.expando

from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import WindowProperties, AntialiasAttrib
from panda3d.core import loadPrcFileData
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import Texture, GeomNode
from panda3d.core import LVector3, LMatrix4f, Vec3, LVecBase3f, LPlanef, LPoint3f, LVector3f, LVecBase4f
from panda3d.core import TextNode
from panda3d.core import lookAt, Quat
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

from panda3d.core import TransparencyAttrib
from direct.gui.DirectGui import *

global project_path

class PandaViewport(wx.Panel):
    """A special Panel which holds a Panda3d window."""
    def __init__(self, callback=None, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        # See __doc__ of initialize() for this callback
        self.GetTopLevelParent().Bind(wx.EVT_SHOW, self.onShow)

        self.event_callback = callback

    def onShow(self, event):
        if event.IsShown() and self.GetHandle():
            # Windows can't get it right from here. Call it after this function.
            if os.name == "nt":
                wx.CallAfter(self.initialize)
            # All other OSes should be okay with instant init.
            else:
                self.initialize()
        event.Skip()

    def initialize(self):
        """This method requires the top most window to be visible, i.e. you called Show()
        on it. Call initialize() after the whole Panel has been laid out and the UI is mostly done.
        It will spawn a new process with a new Panda3D window and this Panel as parent.
        """
        assert self.GetHandle() != 0
        self.pipe, remote_pipe = Pipe()
        w, h = self.ClientSize.GetWidth(), self.ClientSize.GetHeight()
        self.panda_process = Process(target=Panda3dApp, args=(w, h, self.GetHandle(), remote_pipe))
        self.panda_process.start()

        self.Bind(wx.EVT_SIZE, self.onResize)
        self.Bind(wx.EVT_KILL_FOCUS, self.onDefocus)
        self.Bind(wx.EVT_WINDOW_DESTROY, self.onDestroy)
        self.SetFocus()

        # We need to check the pipe for requests frequently
        self.pipe_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.checkPipe, self.pipe_timer)
        self.pipe_timer.Start(1000.0/60) # 60 times a second

    def onResize(self, event):
        # when the wx-panel is resized, fit the panda3d window into it
        #w, h = event.GetSize().GetWidth(), event.GetSize().GetHeight()
        w = event.EventObject.Parent.GetSize().GetWidth()
        h = event.EventObject.Parent.GetSize().GetHeight()
        self.pipe.send({"msg":"resize", "width":w, "height":h})
    
    def onDefocus(self, event):
        f = wx.Window.FindFocus()
        if f:
            # This makes Panda lose keyboard focus
            f.GetTopLevelParent().Raise()

    def onDestroy(self, event):
        self.pipe.send({'msg':"close"})
        # Give Panda a second to close itself and terminate it if it doesn't
        self.panda_process.join(1)
        if self.panda_process.is_alive():
            self.panda_process.terminate()

    def checkPipe(self, event):
        # Panda requested focus (and probably already has keyboard focus), so make wx
        # set it officially. This prevents other widgets from being rendered focused.
        try:    
            if self.pipe.poll():
                request = self.pipe.recv()
                if( None != request ):
                    if request['msg'] == "focus":
                        self.SetFocus()
                    if( self.event_callback is not None ):
                        self.event_callback(request)
        except BrokenPipeError:
            sys.exit()

    def send_message(self, msg):
        self.pipe.send(msg)

class ProjectNodes():
    def __init__(self, db_file):

        self.selected_node_ids = []

        self.db_file = db_file
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        #Add some viewer-only parameters to the table
        viewer_required_columns = ['tags_json','params_3d_json']
        c.execute("PRAGMA table_info(nodes)")
        table_data = c.fetchall()
        for row in table_data:
            #Remove columns that already exist
            [viewer_required_columns.pop(viewer_required_columns.index(column_name)) 
                for column_name in viewer_required_columns
                if(row[1] == column_name)]
        #Any columns remaining that should be added to the table
        for column in viewer_required_columns:
            new_column_string = "ALTER TABLE nodes ADD COLUMN " + column + " TEXT DEFAULT '{{}}'"
            c.execute(new_column_string)
        conn.commit()
        conn.close()

    def add_node(self):

        #Apply Defaults
        params = ("", "{}", "{}")
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""INSERT INTO nodes (path, tags_json, params_3d_json) VALUES(?,?,?)""", params)
        node_id = c.lastrowid
        c.execute("""UPDATE nodes SET name = ? WHERE id = ?""", ("Node "+str(node_id), node_id))
        conn.commit()
        conn.close()
        return node_id
    
    def get_node_ids(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT id FROM nodes""")
        data = c.fetchall()
        conn.close()

        if( data is not None and len(data) > 0 ):
            return [ row[0] for row in data ]
        return []

    def get_id(self, id):
        node_dict = {}

        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT id,name,path,tags_json,params_3d_json FROM nodes WHERE id = ?""", (id,))
        data = c.fetchone()
        conn.close()

        if( data is not None and len(data) > 0):
            node_dict['id'] = data[0]
            node_dict['name'] = data[1]
            node_dict['path'] = data[2]
            node_dict['tags'] = json.loads(data[3])
            node_dict['params_3d'] = json.loads(data[4])

        return node_dict

    def clear_selected_nodes(self):
        for id in self.selected_node_ids:
            #Remove node highlighting
            self.node_paths[id].hideBounds()

        self.selected_node_ids.clear()

    def select_node(self, id):

        #Check if this node id already exists in the list
        # of selected nodes.
        if( id not in self.selected_node_ids):

            #Add node highlighting
            self.node_paths[id].showTightBounds()

            #Add node to list of selected nodes
            self.selected_node_ids.append(id)

    def number_of_selected_nodes(self):
        return len(self.selected_node_ids)
    
    def get_selected_node_ids(self):
        return self.selected_node_ids

    def get_selected_nodes_human_parameters(self):

        selected_nodes_human_parameters_list = []

        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        for id in self.selected_node_ids:
            c.execute("""SELECT name,path,tags_json,params_3d_json FROM nodes WHERE id = ?""", (id,))
            data = c.fetchone()
            if( data is not None and len(data) > 0 ):
                node_dict = {}
                node_dict['id'] = str(id)
                node_dict['name'] = data[0]
                node_dict['path'] = data[1]
                node_dict['tags'] = json.loads(data[2])
                node_dict['params_3d'] = json.loads(data[3])
                selected_nodes_human_parameters_list.append(node_dict)
        conn.close()
        return selected_nodes_human_parameters_list

    def set_node_param_by_id(self, target_id, key, value):
        params = (value, target_id)

        #Only save keys we know about
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        if( "name" == key ):
            c.execute("""UPDATE nodes SET name = ? WHERE id = ?""", params)
        elif( "path" == key ):
            c.execute("""UPDATE nodes SET path = ? WHERE id = ?""", params)
        conn.commit()
        conn.close()

        #Check if there is any 3D GUI parameter with this name we should update
        try:
            node =  self.node_paths[target_id].find(key).node()
            if( None != key ):
                node.setText(value)
        except AssertionError:
            #Couldn't find anything GUI related
            pass
    
    def delete_node_by_id(self, id):
        #Remove 3d data
        #ToDo: May need a check here in case the ID key doesn't
        # exist in the table. This only occurs if the DB and the GUI
        # have diverged, which indicates a bigger problem. Leaving
        # this crash in so that such issues are brought to light.
        self.node_paths[id].removeNode()
        del self.node_paths[id]

        #Remove from DB
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""DELETE FROM nodes WHERE id = ?""", (id,))
        conn.commit()
        conn.close()

        #Remove from selected nodes list
        if( id in self.selected_node_ids ):
            del self.selected_node_ids[self.selected_node_ids.index(id)]
    
    def set_3d_params_dict(self, id, params_3d):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""UPDATE nodes SET params_3d_json = ? WHERE id = ?""", (json.dumps(params_3d), id))
        conn.commit()
        conn.close()

    def get_3d_params_dict(self, id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT params_3d_json FROM nodes WHERE id = ?""", (id,))
        data = c.fetchone()
        conn.close()

        if( data is not None and len(data) > 0 ):
            return json.loads(data[0])
        else:
            return {}

    def open_node_path(self, id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT path FROM nodes WHERE id = ?""", (id,))
        data = c.fetchone()
        conn.close()

        if( data is not None and len(data) > 0 ):
            try:
                filepath = data[0]
                #Let the system try and open/run this file
                if os.name == 'nt':
                    filepath = filepath.replace(posixpath.sep, os.sep)
                filepath = os.path.abspath(filepath)
                os.startfile(filepath)
            except Exception as e:
                #Couldn't open the file
                print(e)
                pass

class ProjectLinks():
    def __init__(self, db_file):

        self.selected_link_ids = []

        self.db_file = db_file
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        #Add some viewer-only parameters to the table
        viewer_required_columns = ['tags_json','params_3d_json']
        c.execute("PRAGMA table_info(links)")
        table_data = c.fetchall()
        for row in table_data:
            #Remove columns that already exist
            [viewer_required_columns.pop(viewer_required_columns.index(column_name)) 
                for column_name in viewer_required_columns
                if(row[1] == column_name) ]
        #Any columns remaining that should be added to the table
        for column in viewer_required_columns:
            new_column_string = "ALTER TABLE links ADD COLUMN " + column + " TEXT DEFAULT '{{}}'"
            c.execute(new_column_string)
        conn.commit()
        conn.close()
    
    def add_link(self, node_a_id, node_b_id):

        params = (node_a_id, node_b_id, "", json.dumps([]), json.dumps({}))
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""INSERT INTO links (node_id1,node_id2,name,tags_json,params_3d_json) VALUES (?,?,?,?,?)""", params)
        conn.commit()
        conn.close()
        link_id = c.lastrowid

        return link_id
    
    def get_link_ids(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT id FROM links""")
        data = c.fetchall()
        conn.close()

        if( data is not None and len(data) > 0 ):
            return [ row[0] for row in data ]
        return []

    def link_ids_for_node_id(self, node_id):
        link_ids = []

        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT id FROM links WHERE node_id1=? or node_id2=?""", (node_id,node_id))
        data = c.fetchall()
        conn.close()

        if( data is not None and len(data) > 0 ):
            return [ row[0] for row in data ]

        return link_ids

    def get_id(self, id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT id,node_id1,node_id2,name,tags_json,params_3d_json FROM links WHERE id = ?""", (id,))
        data = c.fetchone()
        conn.close()

        if( data is not None and len(data) > 0):
            link_dict = {}
            link_dict['id'] = data[0]
            link_dict['node_id1'] = data[1]
            link_dict['node_id2'] = data[2]
            link_dict['name'] = data[3]
            link_dict['tags'] = json.loads(data[4])
            link_dict['gui_params'] = json.loads(data[5])
            return link_dict
        return None

    def link_exists(self, node_a_id, node_b_id):
        ids = [node_a_id, node_b_id]

        params = (node_a_id, node_b_id, node_b_id, node_a_id)
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT id FROM links WHERE (node_id1=? and node_id2=?) or (node_id1=? and node_id2=?)""", params)
        data = c.fetchone()
        conn.close()

        if( data is not None and len(data) > 0 ):
            return True
        return False

    def select_link(self, id):
        #Check if this id already exists in the list
        # of selected nodes.
        if( id not in self.selected_link_ids):

            #Add node highlighting
            self.node_paths[id].showTightBounds()

            #Add node to list of selected nodes
            self.selected_link_ids.append(id)

    def clear_selected_links(self):
        #Remove highlighting
        for id in self.selected_link_ids:
            self.node_paths[id].hideBounds()
        self.selected_link_ids.clear()

    def get_selected_links_human_parameters(self):
        selected_links_human_parameters_list = []
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        for id in self.selected_link_ids:
            c.execute("""SELECT id,name,tags_json, params_3d_json FROM links WHERE id = ?""", (id,))
            data = c.fetchone()
            if( data is not None and len(data) > 0 ):
                hr_dict = {}
                hr_dict['id'] = str(data[0])
                hr_dict['name'] = data[1]
                hr_dict['tags'] = json.loads(data[2])
                hr_dict['params_3d'] = json.loads(data[3])
                selected_links_human_parameters_list.append(hr_dict)
        conn.close()
        return selected_links_human_parameters_list

    def set_link_param_by_id(self, target_id, key, value):

        params = (value, target_id)

        #Only save keys we know about
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        if( "name" == key ):
            c.execute("""UPDATE links SET name = ? WHERE id = ?""", params)
        conn.commit()
        conn.close()

        #Check if there is any 3D GUI parameter with this name we should update
        node =  self.node_paths[target_id].find(key).node()
        if( None != key ):
            node.setText(value)

    def delete_link_by_id(self, id):

        #Remove 3d data
        #ToDo: May need a check here in case the ID key doesn't
        # exist in the table. This only occurs if the DB and the GUI
        # have diverged, which indicates a bigger problem. Leaving
        # this crash in so that such issues are brought to light.
        self.node_paths[id].removeNode()
        del self.node_paths[id]

        #Remove from DB
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""DELETE FROM links WHERE id = ?""", (id,))
        conn.commit()
        conn.close()

        #Remove from selected links list
        if( id in self.selected_link_ids ):
            del self.selected_link_ids[self.links.index(id)]

    def delete_all_for_node_id(self, node_id):
        """ Delete all links that are associated with the node_id supplied """

        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT id FROM links WHERE node_id1 = ? OR node_id2 = ?""", (node_id, node_id))
        data = c.fetchall()
        conn.close()

        if( data is not None and len(data) > 0 ):
            for row in data:
                id = row[0]
                self.delete_link_by_id(id)
    
    def set_3d_params_dict(self, id, params_3d):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""UPDATE links SET params_3d_json = ? WHERE id = ?""", (json.dumps(params_3d), id))
        conn.commit()
        conn.close()

    def get_3d_params_dict(self, id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""SELECT params_3d_json FROM links WHERE id = ?""", (id,))
        data = c.fetchone()
        conn.close()

        if( data is not None and len(data) > 0 ):
            return json.loads(data[0])
        else:
            return {}

class Panda3dApp(ShowBase):

    def __init__(self, width, height, handle, pipe):
        """Arguments:
        width -- width of the window
        height -- height of the window
        handle -- parent window handle
        pipe -- multiprocessing pipe for communication
        """
        self.pipe = pipe

        loadPrcFileData("", "window-type none")
        loadPrcFileData("", "audio-library-name null")
        #16x multisampling for FSAA
        loadPrcFileData('', 'multisamples 16')

        self.sb = ShowBase()
        wp = WindowProperties()
        wp.setOrigin(0, 0)
        wp.setSize(width, height)
        # This causes warnings on Windows
        #wp.setForeground(True)
        wp.setParentWindow(handle)
        base.openDefaultWindow(props=wp, gsg=None)

        self.load_3d()

        base.taskMgr.add(self.checkPipe, "check pipe")
        base.setBackgroundColor(0,0,0)

        #Look for a ".projectscope" file by recursively going
        # up the file tree
        filename = ".projectscope"
        if( os.path.isfile(filename) ):
            self.db_file = filename
            global project_path
            project_path = filename
            msg_dict = {}
            msg_dict["msg"] = "project_path_set"
            msg_dict["path"] = filename
            self.pipe.send(msg_dict)
        else:
            print("Did not find '.projectscope' file")
            return

        self.conn = sqlite3.connect(self.db_file)
        self.project_nodes = ProjectNodes(self.db_file)
        self.project_links = ProjectLinks(self.db_file)

        #Load camera view
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("""Create TABLE IF NOT EXISTS camera_view (id INTEGER PRIMARY KEY, name TEXT, heading REAL, pitch REAL, x REAL, y REAL, z REAL)""")
        c.execute("""SELECT heading, pitch, x, y, z FROM camera_view WHERE id = 1""")
        data = c.fetchone()
        if( data is None or len(data) < 5):
            #Use defaults if no camera view exists
            data = (0, 0, 0, 0, 0)
            c.execute("""INSERT INTO camera_view (heading, pitch, x, y, z) VALUES (?,?,?,?,?)""", data)
            conn.commit()
            self.camera_pos_id = c.lastrowid
        else:
            self.camera_pos_id = 1
        conn.close()
        self.heading = data[0]
        self.pitch = data[1]
        self.sb.camera.setHpr(self.heading, self.pitch, 0)
        self.sb.camera.setPos(data[2], data[3], data[4])
        self.camera_last_save_time = 0

        #Finally load objects from disk onto the screen
        self.load_objects()

        base.run()

    def load_3d(self):
 
        # Add the spinCameraTask procedure to the task manager.
        self.sb.taskMgr.add(self.controlCamera, "Control Camera")

        #Movement and Camera controls
        self.sb.disableMouse()
        self.mouse_1_pressed = False
        self.shift_held = False
        self.shift_multiplier = 1
        self.click_mouse_coords = []
        self.heading = 0
        self.pitch = 0
        self.mousex = 0
        self.mousey = 0
        self.last_time = 0
        self.accept("escape", sys.exit, [0])
        self.accept("mouse1", self.lmb_press)
        self.accept("shift-mouse1", self.lmb_shift_press)
        self.accept("control-mouse1", self.lmb_ctrl_press)
        self.accept("mouse1-up", self.lmb_release)
        self.accept("mouse2", self.rmb_press)
        self.accept("shift-mouse2", self.rmb_press)
        self.accept("mouse2-up", self.rmb_release)
        self.accept("shift-mouse3", self.rmb_press)
        self.accept("mouse3", self.rmb_press)
        self.accept("mouse3-up", self.rmb_release)
        self.accept("shift", self.shift_push)
        self.accept("shift-up", self.shift_release)
        self.keys = {}
        for key in ['arrow_left', 'arrow_right', 'arrow_up', 'arrow_down',
                    'a', 'd', 'w', 's', 'q', 'e']:
            self.keys[key] = 0
            self.accept(key, self.push_key, [key, 2])
            self.accept('shift-'+key, self.push_key, [key, 2])
            self.accept('%s-up' % key, self.push_key, [key, 0])
        self.last_click_time = globalClock.getLongTime()
        
        #Set up to organize the nodes
        self.clickable_node_paths = self.sb.render.attachNewNode("clickable_node_paths")
        self.sb.render.setAntialias(AntialiasAttrib.MAuto)

        #Set up mouse ray-trace picker so the mouse can interact with the 3d space
        self.picker = CollisionTraverser()  # Make a traverser
        self.pq = CollisionHandlerQueue()  # Make a handler
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = self.sb.camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.pq)

    def load_objects(self):
        self.project_nodes.node_paths = {}
        self.project_links.node_paths = {}

        #Check through the nodes to see what needs to be restored
        for node_id in self.project_nodes.get_node_ids():
            
            #Load the 3D models
            params_3d = self.project_nodes.get_3d_params_dict(node_id)
            node_path = self.makeNode(node_id, params_3d)
            self.project_nodes.node_paths[node_id] = node_path

        for link_id in self.project_links.get_link_ids():
            params_3d = self.project_links.get_3d_params_dict(link_id)
            node_path = self.make_link(link_id, params_3d)
            self.project_links.node_paths[link_id] = node_path

    def shift_push(self):
        self.shift_held = True

    def shift_release(self):
        self.shift_held = False

    def rmb_press(self):
        self.mouse_1_pressed = True
        props = WindowProperties()
        props.setCursorHidden(True)
        self.sb.win.requestProperties(props)
        md = self.sb.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        self.click_mouse_coords = [int(0), int(x), int(y)]

    def rmb_release(self):
        self.mouse_1_pressed = False
        props = WindowProperties()
        props.setCursorHidden(False)
        self.sb.win.requestProperties(props)
    
    def push_key(self, key, value):
        """Stores a value associated with a key."""
        self.keys[key] = value

    def controlCamera(self, task):
        #Camera can be rotated when the mouse
        # button is pressed
        if( self.mouse_1_pressed ):
            md = self.sb.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            if self.sb.win.movePointer(self.click_mouse_coords[0], self.click_mouse_coords[1], self.click_mouse_coords[2]):
                self.heading = self.heading - (x - self.click_mouse_coords[1]) * 0.2
                self.pitch = self.pitch - (y - self.click_mouse_coords[2]) * 0.2
            if self.pitch < -89:
                self.pitch = -89
            if self.pitch > 89:
                self.pitch = 89
            self.sb.camera.setHpr(self.heading, self.pitch, 0)
        #dir = self.sb.camera.getMat().getRow3(1)

        delta = globalClock.getDt()
        DEFAULT_SPEED = 10
        move_x = delta * DEFAULT_SPEED * -self.keys['a'] + delta * DEFAULT_SPEED * self.keys['d']
        move_z = delta * DEFAULT_SPEED * self.keys['s'] + delta * DEFAULT_SPEED * -self.keys['w']
        move_y = delta * DEFAULT_SPEED * self.keys['q'] + delta * DEFAULT_SPEED * -self.keys['e']
        movement_sum = sum([self.keys['a'], self.keys['d'], self.keys['s'], self.keys['q'], self.keys['w'], self.keys['e']])
        if( self.shift_held ):
            self.shift_multiplier *= 1.025
        else:
            self.shift_multiplier *= 0.975
        if( self.shift_multiplier < 1 or movement_sum < 0.5):
            self.shift_multiplier = 1
        move_x *= self.shift_multiplier
        move_z *= self.shift_multiplier
        move_y *= self.shift_multiplier
        self.sb.camera.setPos(self.sb.camera, move_x, -move_z, move_y)

        #Save camera position (might have to limit the save rate)
        now = globalClock.getLongTime()
        if( (now - self.camera_last_save_time) > 5 ):
            camera_pos = self.sb.camera.getPos()
            camera_hpr = self.sb.camera.getHpr()
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()
            params = (camera_hpr[0], camera_hpr[1], camera_pos[0], camera_pos[1], camera_pos[2], self.camera_pos_id)
            c.execute("""UPDATE camera_view SET heading=?, pitch=?, x=?, y=?, z=? WHERE id = ?""", params)
            conn.commit()
            conn.close()
            self.camera_last_save_time = now
        
        return Task.cont

    def getFocus(self):
        """Bring Panda3d to foreground, so that it gets keyboard focus.
        Also send a message to wx, so that it doesn't render a widget focused.
        We also need to say wx that Panda now has focus, so that it can notice when
        to take focus back.
        """
        wp = WindowProperties()
        # This causes warnings on Windows
        #wp.setForeground(True)
        base.win.requestProperties(wp)
        self.pipe.send({"msg":"focus"})

    def resizeWindow(self, width, height):
        old_wp = base.win.getProperties()
        if old_wp.getXSize() == width and old_wp.getYSize() == height:
            return

        wp = WindowProperties()
        wp.setOrigin(0, 0)
        wp.setSize(width, height)
        base.win.requestProperties(wp)

    def move_node(self, node_id, new_x_pos=None, new_y_pos=None, new_z_pos=None):

        #Update position
        params_3d = self.project_nodes.get_3d_params_dict(node_id)
        if( new_x_pos is not None ):
            params_3d['center'][0] = new_x_pos
        if( new_y_pos is not None ):
            params_3d['center'][1] = new_y_pos
        if( new_z_pos is not None ):
            params_3d['center'][2] = new_z_pos
        self.project_nodes.set_3d_params_dict(node_id, params_3d)

        #Remove the old 3D object (maybe just transform it instead?)
        self.project_nodes.node_paths[node_id].removeNode()

        #Make new 3D object
        node_path = self.makeNode(node_id, params_3d)
        self.project_nodes.node_paths[node_id] = node_path

        #Remake all links connecting this node
        for link_id in self.project_links.link_ids_for_node_id(node_id):
            self.project_links.node_paths[link_id].removeNode()
            params_3d = self.project_links.get_3d_params_dict(link_id)
            node_path = self.make_link(link_id, params_3d)
            self.project_links.node_paths[link_id] = node_path

    def size_node(self, node_id, new_x_size=None, new_y_size=None, new_z_size=None):

        #Update size
        params_3d = self.project_nodes.get_3d_params_dict(node_id)
        if( new_x_size is not None ):
            params_3d['size'][0] = new_x_size
        if( new_y_size is not None ):
            params_3d['size'][1] = new_y_size
        if( new_z_size is not None ):
            params_3d['size'][2] = new_z_size
        self.project_nodes.set_3d_params_dict(node_id, params_3d)

        #Remove the old 3D object
        self.project_nodes.node_paths[node_id].removeNode()

        #Make new 3D object
        node_path = self.makeNode(node_id, params_3d)
        self.project_nodes.node_paths[node_id] = node_path

    def colour_node(self, node_id, new_rgb, new_transparency):

        params_3d = self.project_nodes.get_3d_params_dict(node_id)
        params_3d['colour'] = new_rgb
        params_3d['transparency'] = new_transparency
        self.project_nodes.set_3d_params_dict(node_id, params_3d)

        #Remove the old 3D object
        self.project_nodes.node_paths[node_id].removeNode()

        #Make new 3D object
        node_path = self.makeNode(node_id, params_3d)
        self.project_nodes.node_paths[node_id] = node_path

    def radius_link(self, link_id, new_radius):
        params_3d = self.project_links.get_3d_params_dict(link_id)
        params_3d['radius'] = new_radius
        self.project_links.set_3d_params_dict(link_id, params_3d)

        #Remove the old 3D object
        self.project_links.node_paths[link_id].removeNode()

        #Make new 3D object
        node_path = self.make_link(link_id, params_3d)
        self.project_links.node_paths[link_id] = node_path

    def colour_link(self, link_id, new_rgb, new_transparency):
        params_3d = self.project_links.get_3d_params_dict(link_id)
        params_3d['colour'] = new_rgb
        params_3d['transparency'] = new_transparency
        self.project_links.set_3d_params_dict(link_id, params_3d)

        #Remove the old 3D object
        self.project_links.node_paths[link_id].removeNode()

        #Make new 3D object
        node_path = self.make_link(link_id, params_3d)
        self.project_links.node_paths[link_id] = node_path

    def checkPipe(self, task):
        """This task is responsible for executing actions requested by wxWidgets.
        Currently supported requests with params:
        resize, width, height
        close
        """
        # TODO: only use the last request of a type
        #       e.g. from multiple resize requests take only the latest into account
        try:
            while self.pipe.poll():
                request = self.pipe.recv()
                if "resize" == request['msg']:
                    self.resizeWindow(request['width'], request['height'])
                elif "close" == request['msg']:
                    sys.exit()
                elif "node_param_change" == request['msg']:
                    self.project_nodes.set_node_param_by_id(request['id'], request['key'], request['value'])
                elif "node_position_change" == request['msg']:
                    self.move_node(request['id'], new_x_pos=request['x'], new_y_pos=request['y'], new_z_pos=request['z'])
                elif "node_size_change"  == request['msg']:
                    self.size_node(request['id'], new_x_size=request['x'], new_y_size=request['y'], new_z_size=request['z'])
                elif "node_colour_change" == request['msg']:
                    self.colour_node(request['id'], new_rgb=request['rgb'], new_transparency=request['transparency'])
                elif "delete_node" == request['msg']:
                    self.project_nodes.clear_selected_nodes()
                    self.project_nodes.delete_node_by_id(request['id'])
                    msg_dict = {"msg":"nodes_selected"}
                    msg_dict["nodes_details_list"] = self.project_nodes.get_selected_nodes_human_parameters()
                    self.pipe.send(msg_dict)
                    self.project_links.delete_all_for_node_id(request['id'])
                elif "link_param_change" == request['msg']:
                    self.project_links.set_link_param_by_id(request['id'], request['key'], request['value'])
                elif "link_colour_change" == request['msg']:
                    self.colour_link(request['id'], new_rgb=request['rgb'], new_transparency=request['transparency'])
                elif "link_radius_change" == request['msg']:
                    self.radius_link(request['id'], new_radius=request['radius'])
                elif "delete_link" == request['msg']:
                    self.project_links.clear_selected_links()
                    self.project_links.delete_link_by_id(request['id'])
                    msg_dict = {"msg":"links_selected"}
                    msg_dict["links_details_list"] = self.project_links.get_selected_links_human_parameters()
            return Task.cont
        except BrokenPipeError:
            sys.exit()
            return None

    def makeSquare(self, x1, y1, z1, x2, y2, z2, colour, transparency):
        format = GeomVertexFormat.getV3n3cpt2()
        vdata = GeomVertexData('square', format, Geom.UHDynamic)

        vertex = GeomVertexWriter(vdata, 'vertex')
        normal = GeomVertexWriter(vdata, 'normal')
        color = GeomVertexWriter(vdata, 'color')
        texcoord = GeomVertexWriter(vdata, 'texcoord')

        # You can't normalize inline so this is a helper function
        def normalized(*args):
            myVec = LVector3(*args)
            myVec.normalize()
            return myVec

        # make sure we draw the sqaure in the right plane
        if x1 != x2:
            vertex.addData3(x1, y1, z1)
            vertex.addData3(x2, y1, z1)
            vertex.addData3(x2, y2, z2)
            vertex.addData3(x1, y2, z2)


            #Add normals to the vertex data
            p1 = LPoint3f(x1, y1, z1)
            p2 = LPoint3f(x2, y1, z1)
            p3 = LPoint3f(x2, y2, z2)
            norm_vector = LPlanef(p1, p2, p3).getNormal()
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)

        else:
            vertex.addData3(x1, y1, z1)
            vertex.addData3(x2, y2, z1)
            vertex.addData3(x2, y2, z2)
            vertex.addData3(x1, y1, z2)

            #Add normals to the vertex data
            p1 = LPoint3f(x1, y1, z1)
            p2 = LPoint3f(x2, y2, z1)
            p3 = LPoint3f(x2, y2, z2)
            norm_vector = LPlanef(p1, p2, p3).getNormal()
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)

        # adding different colors to the vertex for visibility
        if( colour is None ):
            color.addData4f(1.0, 0.0, 0.0, transparency)
            color.addData4f(0.0, 1.0, 0.0, transparency)
            color.addData4f(0.0, 0.0, 1.0, transparency)
            color.addData4f(1.0, 0.0, 1.0, transparency)
        else:
            color.addData4f(*[1.00 * x for x in colour], transparency)
            color.addData4f(*[0.90 * x for x in colour], transparency)
            color.addData4f(*[0.80 * x for x in colour], transparency)
            color.addData4f(*[0.70 * x for x in colour], transparency)

        texcoord.addData2f(0.0, 1.0)
        texcoord.addData2f(0.0, 0.0)
        texcoord.addData2f(1.0, 0.0)
        texcoord.addData2f(1.0, 1.0)

        # Quads aren't directly supported by the Geom interface
        # you might be interested in the CardMaker class if you are
        # interested in rectangle though
        tris = GeomTriangles(Geom.UHDynamic)
        tris.addVertices(0, 1, 3)
        tris.addVertices(1, 2, 3)

        square = Geom(vdata)
        square.addPrimitive(tris)
        return square

    def makeCube(self, center, size, colour, transparency):

        # Note: it isn't particularly efficient to make every face as a separate Geom.
        # instead, it would be better to create one Geom holding all of the faces.
        #Top (+y) face
        square0 = self.makeSquare(   center[0] - size[0]/2,
                                center[1] + size[1]/2,
                                center[2] - size[2]/2,
                                center[0] + size[0]/2,
                                center[1] + size[1]/2,
                                center[2] + size[2]/2,
                                colour,
                                transparency)
        #Bottom (-y) face
        square1 = self.makeSquare(   center[0] - size[0]/2,
                                center[1] - size[1]/2,
                                center[2] - size[2]/2,
                                center[0] + size[0]/2,
                                center[1] - size[1]/2,
                                center[2] + size[2]/2,
                                colour,
                                transparency)
        #Right (+x) face
        square2 = self.makeSquare(   center[0] + size[0]/2,
                                center[1] - size[1]/2,
                                center[2] - size[2]/2,
                                center[0] + size[0]/2,
                                center[1] + size[1]/2,
                                center[2] + size[2]/2,
                                colour,
                                transparency)
        #Left (-x) face
        square3 = self.makeSquare(   center[0] - size[0]/2,
                                center[1] - size[1]/2,
                                center[2] - size[2]/2,
                                center[0] - size[0]/2,
                                center[1] + size[1]/2,
                                center[2] + size[2]/2,
                                colour,
                                transparency)
        #Front (+z) face
        square4 = self.makeSquare(   center[0] - size[0]/2,
                                center[1] - size[1]/2,
                                center[2] + size[2]/2,
                                center[0] + size[0]/2,
                                center[1] + size[1]/2,
                                center[2] + size[2]/2,
                                colour,
                                transparency)
        #Front (-z) face
        square5 = self.makeSquare(   center[0] - size[0]/2,
                                center[1] - size[1]/2,
                                center[2] - size[2]/2,
                                center[0] + size[0]/2,
                                center[1] + size[1]/2,
                                center[2] - size[2]/2,
                                colour,
                                transparency)

        snode = GeomNode('square')
        snode.addGeom(square0)
        snode.addGeom(square1)
        snode.addGeom(square2)
        snode.addGeom(square3)
        snode.addGeom(square4)
        snode.addGeom(square5)

        return snode

    def create_cylinder(self, p1, p2, radius, colour, transparency):

        #Set up the circular points that will form the end of the cylinder.
        # Later we will transform these points onto the plane that makes
        # the end of the cylinder. Assume we are just working in the x/y
        # plane and centered at (0,0,0) to keep this part simple.
        NUM_CIRCULAR_POINTS = 10
        circle_point_vectors = []
        for i in range(NUM_CIRCULAR_POINTS):
            point_x = radius * cos( i * (2*pi/NUM_CIRCULAR_POINTS) )
            point_y = radius * sin( i * (2*pi/NUM_CIRCULAR_POINTS) )
            circle_point_vectors.append(LVector3f(point_x, point_y, 0))
        #The vector for this circle is in the +z direction
        circle_vector = LVector3f(0,0,1)

        #Get vector from p1 to p2
        p1 = LPoint3f(*p1)
        p2 = LPoint3f(*p2)
        distance_vector = p2 - p1

        #Find the cross product of the two vectors so that we can rotate the circle
        # to match the cylinder end
        rotation_axis = circle_vector.cross(distance_vector.normalized())

        #Find the angle between the two vectors
        rotation_angle = circle_vector.angleRad(distance_vector.normalized())

        #Populate the quaternion
        quat_coef = LVecBase4f(cos(rotation_angle/2), rotation_axis[0]*sin(rotation_angle/2), rotation_axis[1]*sin(rotation_angle/2), rotation_axis[2]*sin(rotation_angle/2))
        rotation_quat = Quat(quat_coef.normalized())

        #Rotate each of the cylinder end points
        for point in circle_point_vectors:
            rotated_point = rotation_quat.xform(point)
            point[0] = rotated_point[0]
            point[1] = rotated_point[1]
            point[2] = rotated_point[2]
            
        #Translate the cylinder points to the location of the cylinder end
        p1_vector = LVector3f(*p1)
        for point in circle_point_vectors:
            point[0] += p1_vector[0]
            point[1] += p1_vector[1]
            point[2] += p1_vector[2]
        
        #Calculate the end circle points
        end_circle_points = []
        for point in circle_point_vectors:
            end_circle_points.append(point + distance_vector)
        
        #Now we have enough information to generate the cylinder vertexes
        snode = GeomNode('cylinder')

        for i in range(len(circle_point_vectors)):
            format = GeomVertexFormat.getV3n3cpt2()
            vdata = GeomVertexData('square', format, Geom.UHDynamic)
            vertex = GeomVertexWriter(vdata, 'vertex')
            normal = GeomVertexWriter(vdata, 'normal')
            color = GeomVertexWriter(vdata, 'color')
            texcoord = GeomVertexWriter(vdata, 'texcoord')

            if( 0 == i ):
                p1 = circle_point_vectors[-1]
                p2 = circle_point_vectors[0]
                p3 = end_circle_points[-1]
                p4 = end_circle_points[0]
            else:
                p1 = circle_point_vectors[i-1]
                p2 = circle_point_vectors[i]
                p3 = end_circle_points[i-1]
                p4 = end_circle_points[i]

            #Add 2 triangles worth of vertex data
            vertex.addData3(p1)
            vertex.addData3(p2)
            vertex.addData3(p3)
            vertex.addData3(p4)

            #Add normals to the vertex data
            norm_vector = LPlanef(p1, p2, p3).getNormal()
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)
            normal.addData3(norm_vector)

            if( colour is None ):
                color.addData4f(1.0, 0.0, 0.0, transparency)
                color.addData4f(0.0, 1.0, 0.0, transparency)
                color.addData4f(0.0, 0.0, 1.0, transparency)
                color.addData4f(1.0, 0.0, 1.0, transparency)
            else:
                color.addData4f(*colour, transparency)
                color.addData4f(*colour, transparency)
                color.addData4f(*colour, transparency)
                color.addData4f(*colour, transparency)

            #ToDo: How to verify this
            texcoord.addData2f(0.0, 1.0)
            texcoord.addData2f(0.0, 0.0)
            texcoord.addData2f(1.0, 0.0)
            texcoord.addData2f(1.0, 1.0)

            #Add 2nd triangle
            tris = GeomTriangles(Geom.UHDynamic)
            tris.addVertices(0, 1, 2)
            tris.addVertices(1, 2, 3)

            square = Geom(vdata)
            square.addPrimitive(tris)
            snode.addGeom(square)

        return snode

    def makeNode(self, node_id, params_3d ):

        shape = 'square' #params_3d['shape']
        center = LVecBase3f(*params_3d['center'])
        size = params_3d['size']

        #Create a cube
        cube = self.makeCube( center, size, params_3d['colour'], params_3d['transparency'] )
        cube = self.clickable_node_paths.attachNewNode(cube)
        
        self.project_nodes.get_id(node_id)['node_path'] = cube
        cube.setTag("NodeId", str(node_id))
        cube.setTag("Type", "node")
        cube.setTwoSided(True)
        cube.setTransparency(TransparencyAttrib.M_dual )
        #cube.setAlphaScale(0.5) #Makes entire node transparent, not just the cube

        #Set the title of the node above the cube
        text = TextNode('name')
        text_node = self.clickable_node_paths.attachNewNode(text)
        text_node.reparentTo(cube)
        text.setWordwrap(15.0)
        text.setAlign(TextNode.ACenter)
        node_title = self.project_nodes.get_id(node_id)["name"]
        text.setText(node_title)
        text_node.setScale(1.0)
        center[2] += (params_3d['size'][2]/2) + 0.5
        text_node.setPos(center)
        text_node.setBillboardPointEye()

        return cube
    
    def make_link(self, link_id, params_3d):

        #Get the node ID's that this link joins
        link_dict = self.project_links.get_id(link_id)
        node_a_id = link_dict['node_id1']
        node_b_id = link_dict['node_id2']

        node_a = self.project_nodes.get_id(node_a_id)
        node_b = self.project_nodes.get_id(node_b_id)
        node_a['node_path'] = self.project_nodes.node_paths[node_a_id]
        node_b['node_path'] = self.project_nodes.node_paths[node_b_id]

        #Generate the cylinder long enough to strech between the nodes
        connection_vector = node_a['node_path'].getBounds().getCenter() - node_b['node_path'].getBounds().getCenter()
        length = connection_vector.length()
        radius = params_3d['radius']
        colour = params_3d['colour']
        transparency = params_3d['transparency']
        p1 = node_a['node_path'].getBounds().getCenter()
        p2 = node_b['node_path'].getBounds().getCenter()
        cylinder = self.create_cylinder(p1, p2, radius, colour, transparency)

        #Add cylinder to the root and format
        cylinder = self.clickable_node_paths.attachNewNode(cylinder)
        cylinder.setTwoSided(True)
        cylinder.setTransparency(TransparencyAttrib.M_dual)

        #Bookkeeping
        cylinder.setTag("Type", "link")
        cylinder.setTag("LinkId", str(link_id))

        #Set the title of the link above the cylinder
        text = TextNode('name')
        text_node = self.clickable_node_paths.attachNewNode(text)
        
        text.setWordwrap(15.0)
        text.setAlign(TextNode.ACenter)
        link_title = self.project_links.get_id(link_id)["name"]
        text.setText(link_title)
        text_node.setScale(1.0)
        center = (node_b['node_path'].getBounds().getCenter() + node_a['node_path'].getBounds().getCenter())/2
        center[2] += radius + .25
        text_node.setPos(center)
        text_node.setBillboardPointEye()
        text_node.reparentTo(cylinder)

        return cylinder

    def check_mouse_collision(self):
        if not self.sb.mouseWatcherNode.hasMouse():
            return

        # Set the position of the ray based on the mouse position
        mpos = self.sb.mouseWatcherNode.getMouse()
        self.pickerRay.setFromLens(self.sb.camNode, mpos.getX(), mpos.getY())
        self.picker.traverse(self.clickable_node_paths)
        if self.pq.getNumEntries() > 0:
            
            #If we have hit something, sort the hits so that the closest
            # is first, and highlight that node
            self.pq.sortEntries()
            type = self.pq.getEntry(0).getIntoNode().getTag('Type')
            if( "node" == type ):
                node_id = int(self.pq.getEntry(0).getIntoNode().getTag('NodeId'))
                self.project_nodes.select_node(node_id)
            elif( "link" == type ):
                link_id = int(self.pq.getEntry(0).getIntoNode().getTag('LinkId'))
                self.project_links.select_link(link_id)
        
        #Send a message out to give the app an update on the state of selected
        # nodes
        msg_dict = {"msg":"nodes_selected"}
        msg_dict["nodes_details_list"] = self.project_nodes.get_selected_nodes_human_parameters()
        self.pipe.send(msg_dict)
        msg_dict = {"msg":"links_selected"}
        msg_dict["links_details_list"] = self.project_links.get_selected_links_human_parameters()
        self.pipe.send(msg_dict)

    def lmb_press(self):

        now = globalClock.getLongTime()

        #Capture pre-click ids
        selected_node_ids = self.project_nodes.get_selected_node_ids()[:]

        self.project_nodes.clear_selected_nodes()
        self.project_links.clear_selected_links()
        self.check_mouse_collision()

        #Now check if we have the same node clicked
        new_selected_node_ids = self.project_nodes.get_selected_node_ids()
        if( (len(new_selected_node_ids) == 1) and 
            (len(selected_node_ids) == 1) and
            (new_selected_node_ids[0] == selected_node_ids[0]) and
            (now - self.last_click_time < 0.3)):
            self.project_nodes.open_node_path(new_selected_node_ids[0])
        
        self.last_click_time = now
        
    def lmb_ctrl_press(self):
        self.check_mouse_collision()

    def lmb_shift_press(self):

        num_selected_nodes = self.project_nodes.number_of_selected_nodes()

        #Make a new node if nothing is selected
        if( 0 == num_selected_nodes ):

            #Create a new node right in front of the camera
            params_3d = {}
            params_3d['center'] = [x for x in (LMatrix4f().translateMat(0.0, 15.0, 0.0) * base.camera.getMat()).getRow3(3)]
            params_3d['size'] = [5,5,5]
            params_3d['colour'] = None
            params_3d['transparency'] = 0.5
            node_id = self.project_nodes.add_node()
            self.project_nodes.set_3d_params_dict(node_id, params_3d)
            node_path = self.makeNode(node_id, params_3d)
            self.project_nodes.node_paths[node_id] = node_path

            #Auto-select this new node and update App
            self.project_nodes.clear_selected_nodes()
            self.project_links.clear_selected_links()
            self.project_nodes.select_node(node_id)
            msg_dict = {"msg":"nodes_selected"}
            msg_dict["nodes_details_list"] = self.project_nodes.get_selected_nodes_human_parameters()
            self.pipe.send(msg_dict)
            msg_dict = {"msg":"links_selected"}
            msg_dict["links_details_list"] = self.project_links.get_selected_links_human_parameters()
            self.pipe.send(msg_dict)

        #If more than 1 node are selected, form a link between them
        elif( num_selected_nodes == 2):
            node_a_id = self.project_nodes.get_selected_node_ids()[0]
            node_b_id = self.project_nodes.get_selected_node_ids()[1]

            #Don't make a link if one already exists between
            # these two nodes
            if( not self.project_links.link_exists(node_a_id, node_b_id) ):
                link_id = self.project_links.add_link(node_a_id, node_b_id)
                params_3d = {}
                params_3d['radius'] = 0.25
                params_3d['colour'] = [1.0,1.0,0]
                params_3d['transparency'] = 0.5
                self.project_links.set_3d_params_dict(link_id, params_3d)
                node_path = self.make_link(link_id, params_3d)
                self.project_links.node_paths[link_id] = node_path

                self.project_nodes.clear_selected_nodes()
                self.project_links.clear_selected_links()
                self.project_links.select_link(link_id)
                msg_dict = {"msg":"nodes_selected"}
                msg_dict["nodes_details_list"] = self.project_nodes.get_selected_nodes_human_parameters()
                self.pipe.send(msg_dict)
                msg_dict = {"msg":"links_selected"}
                msg_dict["links_details_list"] = self.project_links.get_selected_links_human_parameters()
                self.pipe.send(msg_dict)

    def lmb_release(self):
        pass

class ProjectViewer(wx.Frame):
    def __init__(self, *args, **kw):
        super(ProjectViewer, self).__init__(*args, **kw)
        
        self.node_info_panel = wx.lib.scrolledpanel.ScrolledPanel(parent=self)
        self.create_node_info_panel(self.node_info_panel)
        self.node_info_panel.SetupScrolling(scroll_x=False, scroll_y=True)

        self.link_info_panel = wx.lib.scrolledpanel.ScrolledPanel(parent=self)
        self.create_link_info_panel(self.link_info_panel)
        self.link_info_panel.SetupScrolling(scroll_x=False, scroll_y=True)

        self.p = PandaViewport(parent=self, callback=self.panda_frame_callback)

        sizer = wx.FlexGridSizer(3, 1, 0)
        sizer.AddGrowableRow(0) # make first row growable
        sizer.AddGrowableCol(0) # make first column growable
        sizer.SetFlexibleDirection(wx.BOTH)
        sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        sizer.Add(self.p, flag=wx.EXPAND)
        sizer.Add(self.node_info_panel, flag=wx.EXPAND, border=50)
        sizer.Add(self.link_info_panel, flag=wx.EXPAND, border=50)
        self.SetSizer(sizer)

        # Default state for the info panels
        self.node_info_panel.Hide()
        self.link_info_panel.Hide()
    
    def create_node_info_panel(self, panel):
        info_panel = {}
        self.node_info_panel_dict = info_panel
        
        info_panel['delete_button'] = wx.Button(parent=panel, label="Delete")

        info_panel['id_text_label'] = wx.StaticText(parent=panel, label="\nNode ID: ")
        info_panel['id_text'] = wx.TextCtrl(parent=panel)
        info_panel['id_text'].Enable(False)

        info_panel['node_name_text_label'] = wx.StaticText(parent=panel, label="\nNode Name:")
        info_panel['node_name_text'] = wx.TextCtrl(parent=panel)

        info_panel['x_pos_label'] = wx.StaticText(parent=panel, label="\nX-position:")
        info_panel['x_pos'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)
        info_panel['y_pos_label'] = wx.StaticText(parent=panel, label="Y-position:")
        info_panel['y_pos'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)
        info_panel['z_pos_label'] = wx.StaticText(parent=panel, label="Z-position:")
        info_panel['z_pos'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)

        info_panel['x_size_label'] = wx.StaticText(parent=panel, label="\nX-size:")
        info_panel['x_size'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)
        info_panel['y_size_label'] = wx.StaticText(parent=panel, label="Y-size:")
        info_panel['y_size'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)
        info_panel['z_size_label'] = wx.StaticText(parent=panel, label="Z-size:")
        info_panel['z_size'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)

        info_panel['colour_label'] = wx.StaticText(parent=panel, label="\nColour (R,G,B):")
        info_panel['colour'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)
        info_panel['transparency_label'] = wx.StaticText(parent=panel, label="Transparency (0.0 - 1.0):")
        info_panel['transparency'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)

        info_panel['node_path_label'] = wx.StaticText(parent=panel, label="\nNode Path:")
        info_panel['node_path_text'] = wx.lib.expando.ExpandoTextCtrl(parent=panel, style=wx.TE_MULTILINE)

        def update_text(key, evt):
            id = int(self.node_info_panel_dict['id_text'].GetValue())
            value = evt.EventObject.GetValue()
            msg = {"msg":"node_param_change", "id":id, "key":key, "value":value}
            self.p.send_message(msg)
        info_panel['node_name_text'].Bind(wx.EVT_KEY_UP, lambda x: update_text("name", x))

        def update_pos(evt):
            try:
                id = int(self.node_info_panel_dict['id_text'].GetValue())
                x = float(self.node_info_panel_dict['x_pos'].GetValue())
                y = float(self.node_info_panel_dict['y_pos'].GetValue())
                z = float(self.node_info_panel_dict['z_pos'].GetValue())
                msg = {"msg":"node_position_change", "id":id, "x":x, "y":y, "z":z}
                self.p.send_message(msg)
            except ValueError:
                #Problem converting coordinates!
                pass
        info_panel['x_pos'].Bind(wx.EVT_TEXT_ENTER, update_pos)
        info_panel['y_pos'].Bind(wx.EVT_TEXT_ENTER, update_pos)
        info_panel['z_pos'].Bind(wx.EVT_TEXT_ENTER, update_pos)

        def update_size(evt):
            try:
                id = int(self.node_info_panel_dict['id_text'].GetValue())
                x = float(self.node_info_panel_dict['x_size'].GetValue())
                y = float(self.node_info_panel_dict['y_size'].GetValue())
                z = float(self.node_info_panel_dict['z_size'].GetValue())
                msg = {"msg":"node_size_change", "id":id, "x":x, "y":y, "z":z}
                self.p.send_message(msg)
            except ValueError:
                #Problem converting coordinates!
                pass
        info_panel['x_size'].Bind(wx.EVT_TEXT_ENTER, update_size)
        info_panel['y_size'].Bind(wx.EVT_TEXT_ENTER, update_size)
        info_panel['z_size'].Bind(wx.EVT_TEXT_ENTER, update_size)

        def update_colour(evt):
            try:
                id = int(self.node_info_panel_dict['id_text'].GetValue())
                colour_text = self.node_info_panel_dict['colour'].GetValue()
                rgb = None
                if( "None" != colour_text ):
                    rgb = [float(num) for num in self.node_info_panel_dict['colour'].GetValue().split(',')]
                    if( len(rgb) != 3):
                        #There should be exactly 3 colour parts
                        return
                transparency = float(self.node_info_panel_dict['transparency'].GetValue())
                msg = {"msg":"node_colour_change", "id":id, "rgb":rgb, "transparency":transparency}
                self.p.send_message(msg)
            except ValueError:
                #Problem converting colours!
                pass
        info_panel['colour'].Bind(wx.EVT_TEXT_ENTER, update_colour)
        info_panel['transparency'].Bind(wx.EVT_TEXT_ENTER, update_colour)

        def get_project_path():
            return self.project_path

        class DropTarget(wx.DropTarget):
            def __init__(self, textCtrl, *args, **kwargs):
                super(DropTarget, self).__init__(*args, **kwargs)
                self.textCtrl = textCtrl
                self.composite = wx.DataObjectComposite()
                self.fileDropData = wx.FileDataObject()
                self.composite.Add(self.fileDropData)
                self.SetDataObject(self.composite)
            def OnDrop(self, x, y):
                return True
            def OnData(self, x, y, result):
                self.GetData()
                formatType, formatId = self.GetReceivedFormatAndId()
                if formatType == wx.DF_FILENAME:
                    return self.OnFileDrop()
            def GetReceivedFormatAndId(self):
                format = self.composite.GetReceivedFormat()
                formatType = format.GetType()
                try:
                    formatId = format.GetId() # May throw exception on unknown formats
                except:
                    formatId = None
                return formatType, formatId
            def OnFileDrop(self):
                for filename in self.fileDropData.GetFilenames():

                    #Get the relative path to the file from the project
                    # file path
                    relative_path = os.path.relpath(filename, os.path.dirname(os.path.abspath(get_project_path())))
                    if os.name == 'nt':
                        relative_path = relative_path.replace(os.sep, posixpath.sep)

                    self.textCtrl.SetValue(relative_path)
                    class EvtObject(object):
                        pass
                    evt = EvtObject()
                    evt.EventObject = self.textCtrl
                    update_text("path", evt)
                return wx.DragCopy
        info_panel['node_path_text'].SetDropTarget(DropTarget(info_panel['node_path_text']))
        info_panel['node_path_text'].Bind(wx.EVT_KEY_UP, lambda x: update_text("path", x))

        def delete_node(evt):
            id = int(self.node_info_panel_dict['id_text'].GetValue())
            msg = {"msg":"delete_node", "id":id}
            self.p.send_message(msg)
        info_panel['delete_button'].Bind(wx.EVT_BUTTON, delete_node)

        #Put all the widgets in the sizer
        box = wx.BoxSizer(wx.VERTICAL)
        for key in info_panel.keys():
            box.Add(info_panel[key], 0, wx.LEFT | wx.RIGHT, 10)
        panel.SetSizer(box)

    def create_link_info_panel(self, panel):
        
        info_panel = {}
        self.link_info_panel_dict = info_panel

        info_panel['delete_button'] = wx.Button(parent=panel, label="Delete")

        info_panel['id_text_label'] = wx.StaticText(parent=panel, label="Link ID: ")
        info_panel['id_text'] = wx.TextCtrl(parent=panel)
        info_panel['id_text'].Enable(False)

        info_panel['link_name_text_label'] = wx.StaticText(parent=panel, label="\nLink Name: ")
        info_panel['link_name_text'] = wx.TextCtrl(parent=panel)

        info_panel['radius_label'] = wx.StaticText(parent=panel, label="\nRadius:")
        info_panel['radius'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)

        info_panel['colour_label'] = wx.StaticText(parent=panel, label="\nColour (R,G,B):")
        info_panel['colour'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)
        info_panel['transparency_label'] = wx.StaticText(parent=panel, label="Transparency (0.0 - 1.0):")
        info_panel['transparency'] = wx.TextCtrl(parent=panel, style=wx.TE_PROCESS_ENTER)

        def update_text(key, evt):
            id = int(self.link_info_panel_dict['id_text'].GetValue())
            value = evt.EventObject.GetValue()
            msg = {"msg":"link_param_change", "id":id, "key":key, "value":value}
            self.p.send_message(msg)
        info_panel['link_name_text'].Bind(wx.EVT_KEY_UP, lambda x: update_text("name", x))

        def update_radius(evt):
            id = int(self.link_info_panel_dict['id_text'].GetValue())
            try:
                value = float(evt.EventObject.GetValue())
            except ValueError:
                #Problem converting radius!
                pass
            msg = {"msg":"link_radius_change", "id":id, "radius":value}
            self.p.send_message(msg)
        info_panel['radius'].Bind(wx.EVT_TEXT_ENTER, update_radius)

        def update_colour(evt):
            try:
                id = int(self.link_info_panel_dict['id_text'].GetValue())
                colour_text = self.link_info_panel_dict['colour'].GetValue()
                rgb = None
                if( "None" != colour_text ):
                    rgb = [float(num) for num in self.link_info_panel_dict['colour'].GetValue().split(',')]
                    if( len(rgb) != 3):
                        #There should be exactly 3 colour parts
                        return
                transparency = float(self.link_info_panel_dict['transparency'].GetValue())
                msg = {"msg":"link_colour_change", "id":id, "rgb":rgb, "transparency":transparency}
                self.p.send_message(msg)
            except ValueError:
                #Problem converting colours!
                pass
        info_panel['colour'].Bind(wx.EVT_TEXT_ENTER, update_colour)
        info_panel['transparency'].Bind(wx.EVT_TEXT_ENTER, update_colour)

        def delete_link(evt):
            id = int(self.link_info_panel_dict['id_text'].GetValue())
            msg = {"msg":"delete_link", "id":id}
            self.p.send_message(msg)
        info_panel['delete_button'].Bind(wx.EVT_BUTTON, delete_link) 

        #Put all the widgets in the sizer
        box = wx.BoxSizer(wx.VERTICAL)
        for key in info_panel.keys():
            box.Add(info_panel[key], 0, wx.LEFT | wx.RIGHT, 10)
        panel.SetSizer(box)

    def populate_node_info_panel(self, params):
        self.node_info_panel_dict['id_text'].SetValue(params['id'])
        self.node_info_panel_dict['node_name_text'].SetValue(params['name'])
        self.node_info_panel_dict['x_pos'].SetValue(str(round(params['params_3d']['center'][0], 3)))
        self.node_info_panel_dict['y_pos'].SetValue(str(round(params['params_3d']['center'][1], 3)))
        self.node_info_panel_dict['z_pos'].SetValue(str(round(params['params_3d']['center'][2], 3)))
        self.node_info_panel_dict['x_size'].SetValue(str(params['params_3d']['size'][0]))
        self.node_info_panel_dict['y_size'].SetValue(str(params['params_3d']['size'][1]))
        self.node_info_panel_dict['z_size'].SetValue(str(params['params_3d']['size'][2]))
        if( None == params['params_3d']['colour'] ):
            self.node_info_panel_dict['colour'].SetValue("None")
        else:
            self.node_info_panel_dict['colour'].SetValue(",".join([str(round(part,3)) for part in params['params_3d']['colour']]))
        self.node_info_panel_dict['transparency'].SetValue(str(params['params_3d']['transparency']))
        self.node_info_panel_dict['node_path_text'].SetValue(params['path'])

    def populate_link_info_panel(self, params):
        self.link_info_panel_dict['id_text'].SetValue(params['id'])
        self.link_info_panel_dict['link_name_text'].SetValue(params['name'])
        self.link_info_panel_dict['radius'].SetValue(str(round(params['params_3d']['radius'], 3)))
        if( None == params['params_3d']['colour'] ):
            self.link_info_panel_dict['colour'].SetValue("None")
        else:
            self.link_info_panel_dict['colour'].SetValue(",".join([str(round(part,3)) for part in params['params_3d']['colour']]))
        self.link_info_panel_dict['transparency'].SetValue(str(params['params_3d']['transparency']))
    
    def panda_frame_callback(self, event):

        if( "nodes_selected" == event["msg"] ):
            if( 1 == len(event["nodes_details_list"]) ):
                self.node_info_panel.Show()
                #Populate info pane with Node details
                self.populate_node_info_panel(event["nodes_details_list"][0])
                pass
            else:
                self.node_info_panel.Hide()
            self.node_info_panel.GetParent().GetSizer().Layout()
        
        elif( "links_selected" == event["msg"] ):
            if( 1 == len(event["links_details_list"]) ):
                self.link_info_panel.Show()
                #Populate info pane with Node details
                self.populate_link_info_panel(event["links_details_list"][0])
                pass
            else:
                self.link_info_panel.Hide()
            self.link_info_panel.GetParent().GetSizer().Layout()
        
        elif( "project_path_set" == event["msg"] ):
            self.project_path = event["path"]

if __name__ == "__main__":
    app = wx.App(redirect=False)
    app_frame = ProjectViewer(parent=None, size=wx.Size(500,500))
    with open(os.path.join(os.path.dirname(__file__),'version_info.txt'),'r') as version_file:
        app_frame.SetTitle("Project Scope Viewer v"+version_file.readline())
    app_frame.Show()
    app.MainLoop()