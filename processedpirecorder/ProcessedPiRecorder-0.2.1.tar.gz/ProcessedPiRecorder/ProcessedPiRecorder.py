#!/usr/bin/env/python3

import time
import multiprocessing as mp
import picamera
import tifffile
import imageio as iio
import numpy as np
import cv2
import datetime as dt
import logging
import collections

# Class of raspberrypi video recorder based on Picamera and multiprocessing.
# Outputs into a big tiff appropriate for downstream use in Deep Lab Cut or other whatever.
# Supports the stereopi.


#OK, meat and potatoes time
class ProcessedPiRecorder:
    #initialize 
    def __init__(self,
                 tif_path='', x_resolution=0, y_resolution=0, scale_factor=1, framerate=0, 
                 rec_length=0, display=True, display_proc='camera_reader', stereo=False,
                 timestamp=False, report_Hz=False, monitor_qs= False,
                 callback=None, cb_type=None, blocking=True, 
                 write_vid=True, tif_compression=6, buffer_length=1, Hz_buffer=10,
                 log_file=None):      
        
        #Set up logging
        i_logger = logging.getLogger('init_logger')
        self.log_file = log_file
                     
        #Stereo or mono
        self.stereo = stereo
        
        #Camera sensor and downscaling
        if stereo: self.cam_width  = int((x_resolution+31)/32)*32 #must be factor of 32
        else:      self.cam_width  = int((x_resolution+15)/16)*16 #must be factor of 16
        self.cam_height            = int((y_resolution+15)/16)*16 #must be factor of 16
        
        self.img_width  = int(self.cam_width  * scale_factor)
        self.img_height = int(self.cam_height * scale_factor)
        self.tif_compression = tif_compression
        
        #Camera recording
        self.framerate  = framerate
        self.rec_length = rec_length
        self.video_path = tif_path
        self.timestamp  = timestamp
        self.reportHz   = report_Hz
        
        #init the numpy array
        self.capture = np.zeros((self.img_height, self.img_width, 4), dtype=np.uint8)

        #Callbacks
        self.display       = display
        self.display_proc  = display_proc
        self.blocking      = blocking
        self.callback      = callback
        self.cb_type       = cb_type
        self.monitor_qs    = monitor_qs
        self.buffer_length = buffer_length
        self.Hz_buffer     = Hz_buffer
        self.write_vid     = write_vid
        
        if (callback is not None) and (cb_type not in ['2Proc','3Proc']):
            i_logger.exception('Callback type "%s" is unsupported try "2Proc" or "3Proc"' % (self.cb_type,))                

        
    #Reads in the video stream, timestamps, monitors framerate and passes frames
    def camera_reader(self, queue, queue_list):        

        #Set up logging
        c_logger = logging.getLogger('camera_logger')
        
        #set up the camera
        if self.stereo:
            camera = picamera.PiCamera(stereo_mode='side-by-side',stereo_decimate=False)
            camera.hflip = True
        else:
            camera = picamera.PiCamera()

        camera.resolution = (self.cam_width, self.cam_height)
        camera.framerate  = self.framerate
        time.sleep(0.1) #let camera warm up
        
        #Get the start time for latency and prep the counter variable
        t0 = dt.datetime.now()
        t1 = t0
        per=collections.deque(maxlen=self.Hz_buffer)
        counter=0
        if self.timestamp: camera.annotate_text = '0'

        #Read frames
        for frame in camera.capture_continuous(self.capture, format='bgra', use_video_port=True,
                                                    resize=(self.img_width, self.img_height)):
            #Track performance
            #Framerate
            counter = counter + 1
            t2=dt.datetime.now() 
            per.append((t2-t1).total_seconds())
            t1=t2
            Hz = 1/(sum(per)/len(per))
            elapsed = (t1-t0).total_seconds()

            #Queueing
            Q_depth=''
            for q in queue_list:
                Q_depth += '%s,' % (q.qsize())
            Q_depth = Q_depth[:-1] #trim a comma

            #Variable to accumulate logs across processes
            latency = 'Queue_depths: %s__Camera_in: %s__' % (Q_depth ,t2,)

            #Annotate the frame/gather the dubugging data
            annot_str = ''
            if self.timestamp:  annot_str += 't: %.3fs, ' % elapsed
            if self.reportHz:   annot_str += 'FR: %.3f, ' % Hz
            if self.monitor_qs: annot_str += Q_depth   
            if self.timestamp or self.reportHz or self.monitor_qs:
                camera.annotate_text = annot_str
                camera.annotate_background = picamera.Color('black')
         
            #Check if we're displaying video
            if self.display & (self.display_proc == 'camera_reader'):
                cv2.imshow('frame', frame)
                key = cv2.waitKey(1) & 0xFF
                latency += 'CameraReader_display: %s__' % dt.datetime.now()

            #Break if time runs out
            if elapsed > self.rec_length :
                latency += 'Camera_out: %s__' % dt.datetime.now()
                queue.put((True, frame, latency))
                
                c_logger.info('Average Framerate: %.3f Hz' % (counter/elapsed,))
                if abs(counter/elapsed/self.framerate-1) >0.05: c_logger.warning('Camera ONLY averaged %.3f Hz' % (counter/elapsed,))
                break

            else:
                #write the frame to the queue
                latency += 'Camera_out: %s__' % dt.datetime.now()
                queue.put((False, frame, latency))
                        

    #Write the buffer to file
    def file_writer(self, queue, cb_queue, vid_path):

        #Setup logging
        fw_logger = logging.getLogger('file_writer_logger')
        fw_logger.setLevel('DEBUG')
        fw_logger.addHandler(logging.FileHandler(self.log_file, 'w')) #needs to ouput to here       

        #define our tiff writer
        with iio.get_writer(vid_path, bigtiff=True, software='ProcessedPiRecorder') as tif:
                
            #intialize our frame buffer if '2Proc'
            if self.cb_type == '2Proc': buffer = collections.deque(maxlen=self.buffer_length)

            #infinite loop
            while True:
                #Grab the next entry in the queue
                if not queue.empty():
                    end, frame, latency = queue.get()
                    latency += 'FileWriter_in: %s__' % dt.datetime.now()
                    
                    #Write the frame to the buffer if using a 2Proc callback
                    if self.cb_type == '2Proc': buffer.append(frame)
                    
                    #Catch the break condition
                    if end is True:
                        break
                    
                    #write to file
                    else:                        
                        #check if we're running the two task callback
                        if self.cb_type == '2Proc': frame = self.callback(buffer, cb_queue)

                        #Check if we're displaying video
                        if self.display & (self.display_proc == 'file_writer'):
                            cv2.imshow('frame', frame)
                            key = cv2.waitKey(1) & 0xFF
                            latency += 'FileWriter_display: %s__' % dt.datetime.now()
                        
                        #save to tif
                        if self.write_vid:
                            tif.append_data(frame)
                            latency += 'FileWriter_save: %s__' % dt.datetime.now()

                        #Write the log
                        if self.log_file != None: fw_logger.debug(latency)
    
    
    def proc_callback(self, queue1, queue2, cb_queue):
        #Set up logging
        pcb_logger = logging.getLogger('proccb_logger')


        #init the buffer
        buffer = collections.deque(maxlen=self.buffer_length)

        #infinite loop
        while True:
            #Grab the next entry in the queue
            if not queue1.empty():
                #get frame
                end, frame, latency = queue1.get()
                latency += 'ProcCB_in: %s__' % dt.datetime.now()
                buffer.append(frame)
                
                #execute callback
                frame = self.callback(buffer, cb_queue)
                latency += 'ProcCB_out: %s__' % dt.datetime.now()
                
                #Catch the break condition and pass the frame
                if end is True:
                    queue2.put((True, frame, latency))
                    break
                else:
                    queue2.put((False, frame, latency))
                
    #Starts the recorder            
    def recordVid(self):
        #Handle the callback options to setup the queues and args
        #mandatory queue
        queue1        = mp.Queue()
        self.cb_queue = mp.Queue()
        
        if self.cb_type == '3Proc':
            #queues
            queue2 = mp.Queue()
            
            #args
            args1 = (queue1, [queue1, queue2, self.cb_queue],)
            args2 = (queue2, self.cb_queue, self.video_path,)
            args3 = (queue1, queue2, self.cb_queue,)

        else:
            #args
            args1 = (queue1, [queue1, self.cb_queue],)
            args2 = (queue1, self.cb_queue, self.video_path,)

        #Run it
        try:
            p1 = mp.Process(target=self.camera_reader, args=args1)
            p2 = mp.Process(target=self.file_writer,   args=args2)
            if self.cb_type == '3Proc':
                p3 = mp.Process(target=self.proc_callback, args=args3)
            p1.start()
            p2.start()
            if self.cb_type == '3Proc':
                p3.start()
            if self.blocking:
                p1.join()
                p2.join()
                if self.cb_type == '3Proc':
                    p3.join()
            
        except Exception as e:
            logging.exception(e)
