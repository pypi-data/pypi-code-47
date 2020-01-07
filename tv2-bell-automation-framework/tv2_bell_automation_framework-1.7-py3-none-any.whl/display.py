'''
This module contains the Display class used for most devices
under test with HDMI output.
'''

from future.utils import native, raise_, string_types, text_to_native_str

from collections import deque, namedtuple
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import time
import threading
import weakref
import uuid

import cv2
import gi

from datetime import datetime
from tv2test.gst_utils import array_from_sample, gst_sample_make_writable
from tv2test.imgutils import Frame
from tv2test.timeutil import date_diff_in_seconds

gi.require_version('Gst', '1.0')
from gi.repository import GLib, GObject, Gst

Gst.init(None)

class GObjectTimeout:
    '''
    Responsible for setting a timeout in the GTK main loop
    '''
    def __init__(self, timeout_secs, handler, *args):
        self.timeout_secs = timeout_secs
        self.handler = handler
        self.args = args
        self.timeout_id = None

    def start(self):
        self.timeout_id = GObject.timeout_add(
            self.timeout_secs * 1000, self.handler, *self.args
        )

    def cancel(self):
        if self.timeout_id:
            GObject.source_remove(self.timeout_id)
        self.timeout_id = None

# Define source and sink GStreamer pipelines
appsink = (
    'appsink name=appsink max-buffers=1 drop=false sync=true '
    'emit-signals=true '
    'caps=video/x-raw,format=BGR'
)

source_pipeline_description = " ! ".join([
    #'videotestsrc',
    #'videoconvert',

    'v4l2src name=v4l2src',
    #'jpegdec',
    'video/x-raw',
    'videoconvert',
    'queue',
    appsink
])


@contextmanager
def _mainloop():
    '''
    GLib/GTK+ main loop

    This main loop is required to attach message handlers to the GStreamer bus. Without this
    loop, no message notifications will be received. 
    '''

    mainloop = GLib.MainLoop.new(context=None, is_running=False)

    thread = threading.Thread(target=mainloop.run)
    thread.daemon = True
    thread.start()

    try:
        yield
    finally:
        mainloop.quit()
        thread.join(10)
        print("teardown: Exiting (GLib mainloop %s)" % (
              "is still alive!" if thread.isAlive() else "ok"))

class SinkPipeline(object):
    def __init__(self, user_sink_pipeline, raise_in_user_thread, save_video=""):
        import time as _time

        self.annotations_lock = threading.Lock()
        self.text_annotations = []
        self.region_annotations = []
        self._raise_in_user_thread = raise_in_user_thread
        self.received_eos = threading.Event()
        self._frames = deque(maxlen=35)
        self._time = _time
        self._sample_count = 0
        self._start_time = None
        self.is_recording = False

        # The test script can draw on the video, but this happens in a different
        # thread.  We don't know when they're finished drawing so we just give
        # them 0.5s instead.
        self._sink_latency_secs = 0.5

        sink_pipeline_description = (
            "appsrc name=appsrc format=time is-live=true "
            "caps=video/x-raw,format=(string)BGR ")

        if save_video and user_sink_pipeline:
            sink_pipeline_description += "! tee name=t "
            src = "t. ! queue leaky=downstream"
        else:
            src = "appsrc."

        if save_video:
            if not save_video.endswith(".mp4"):
                save_video += ".mp4"
            print("Saving video to '%s'" % save_video)
            sink_pipeline_description += (
                "{src} ! videoconvert ! queue !"
                "x264enc ! queue ! mp4mux ! filesink location={save_video} ").format(
                src=src, save_video=save_video)

        if user_sink_pipeline:
            sink_pipeline_description += (
                "{src} ! videoconvert ! {user_sink_pipeline}").format(
                src=src, user_sink_pipeline=user_sink_pipeline)

        print(sink_pipeline_description)

        self.sink_pipeline = Gst.parse_launch(sink_pipeline_description)
        sink_bus = self.sink_pipeline.get_bus()
        sink_bus.connect("message::error", self._on_error)
        sink_bus.connect("message::warning", self._on_warning)
        sink_bus.connect("message::eos", self._on_eos_from_sink_pipeline)
        sink_bus.connect("message", self._on_message)
        sink_bus.add_signal_watch()
        self.appsrc = self.sink_pipeline.get_by_name("appsrc")

    def _on_eos_from_sink_pipeline(self, _bus, _message):
        print("Got EOS from sink pipeline")
        self.received_eos.set()

    def _on_message(self, _bus, message):
        print('Sink pipeline message: ' + str(message.type))

    def _on_warning(self, _bus, message):
        assert message.type == Gst.MessageType.WARNING
        Gst.debug_bin_to_dot_file_with_ts(
            self.sink_pipeline, Gst.DebugGraphDetails.ALL, "WARNING")
        err, dbg = message.parse_warning()
        print("%s: %s\n%s\n" % (err, err.message, dbg))

    def _on_error(self, _bus, message):
        assert message.type == Gst.MessageType.ERROR
        if self.sink_pipeline is not None:
            Gst.debug_bin_to_dot_file_with_ts(
                self.sink_pipeline, Gst.DebugGraphDetails.ALL, "ERROR")
        err, dbg = message.parse_error()
        self._raise_in_user_thread(
            RuntimeError("%s: %s\n%s\n" % (err, err.message, dbg)))

    def __enter__(self):
        print('Sink pipeline started')
        self.received_eos.clear()
        #self.sink_pipeline.set_state(Gst.State.PLAYING)

    def start_recording(self):
        self.is_recording = True
        self.sink_pipeline.set_state(Gst.State.PLAYING)
    
    def exit_prep(self):
        # It goes sink.exit_prep, src.__exit__, sink.__exit__, so we can do
        # teardown things here that require the src to still be running.

        # Dropping the sink latency to 0 will cause all the frames in
        # self._frames to be pushed next time on_sample is called.  We can't
        # flush here because on_sample is called from the thread that is running
        # `Display`.
        self._sink_latency_secs = 0

        # Wait for up to 1s for the sink pipeline to get into the RUNNING state.
        # This is to avoid teardown races in the sink pipeline caused by buggy
        # GStreamer elements
        self.sink_pipeline.get_state(1 * Gst.SECOND)

    def __exit__(self, _1, _2, _3):
        print('SinkPipeline.__exit__')
        # Drain the frame queue
        while self._frames:
            self._push_sample(self._frames.pop())

        if self._sample_count > 0:
            state = self.sink_pipeline.get_state(0)
            print('Sink pipeline state = ' + str(state))
            if (state[0] != Gst.StateChangeReturn.SUCCESS or
                    state[1] != Gst.State.PLAYING):
                print("teardown: Sink pipeline not in state PLAYING: %r"
                      % (state,))
            print("teardown: Sending eos on sink pipeline")
            if self.appsrc.emit("end-of-stream") == Gst.FlowReturn.OK:
                print("  Sent end-of-stream")
                print("Waiting for EOS....")
                #self.sink_pipeline.send_event(Gst.Event.new_eos())
                #time.sleep(2.0)
                if not self.received_eos.wait(120):
                    print("Timeout waiting for sink EOS")
            else:
                print("Sending EOS to sink pipeline failed")
        else:
            print("SinkPipeline teardown: Not sending EOS, no samples sent")

        self.sink_pipeline.set_state(Gst.State.NULL)

        # Don't want to cause the Display object to hang around on our account,
        # we won't be raising any errors from now on anyway:
        self._raise_in_user_thread = None

    def on_sample(self, sample):
        """
        Called from `Display` for each frame.
        """
        if self.is_recording:
            now = sample.time
            self._frames.appendleft(sample)

            while self._frames:
                oldest = self._frames.pop()
                if oldest.time > now - self._sink_latency_secs:
                    self._frames.append(oldest)
                    break
                self._push_sample(oldest)

    def _push_sample(self, sample):
        # Calculate whether we need to draw any annotations on the output video.
        #print('  sample {0:d} pushed'.format(self._sample_count))
        now = sample.time
        #print("now = %s" % (datetime.utcfromtimestamp(now)))
        if self._sample_count == 0:
            self._start_time = datetime.utcfromtimestamp(now)
            print('start time = ' + str(self._start_time))

        with self.annotations_lock:
            # Remove expired text annotations

            self.text_annotations = [x for x in self.text_annotations
                                     if now < x.end_time]
            # Because the sink pipeline has a 0.5 sec delay, text annotations should
            # not be displayed until the timestamp of the frame at which they were created                     
            current_text_annotations = [x for x in self.text_annotations if x.time <= now]

            self.region_annotations = [x for x in self.region_annotations
                                     if now < x.end_time]
            current_region_annotations = [x for x in self.region_annotations if x.time <= now]

        sample = gst_sample_make_writable(sample)
        img = array_from_sample(sample, readwrite=True)

        # Timestamp
        timestamp_width = self._draw_timestamp(img, date_diff_in_seconds(datetime.utcfromtimestamp(now), self._start_time))

        # Draw text annotations
        for i, x in enumerate(current_text_annotations):
            overlay = img.copy()
            opacity =  1.0 - (now - x.time) / (x.end_time - x.time)

            x_top_left_cord = timestamp_width if x.top_left_cord_pos[0] is None else x.top_left_cord_pos[0]
            y_top_left_cord = 1020 if x.top_left_cord_pos[1] is None else x.top_left_cord_pos[1]
            if y_top_left_cord == 1020 :
                i = 0

            text_origin = (x_top_left_cord + 10, (y_top_left_cord + 40) - i * 62)

            text_size = cv2.getTextSize(x.text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
            text_width = text_size[0] + 20
            background_p1 = (x_top_left_cord, y_top_left_cord - i * 62)
            background_p2 = (x_top_left_cord + text_width, (y_top_left_cord + 60) - i * 62)
            cv2.rectangle(overlay, background_p1, background_p2, x.background_color, -1)
            cv2.putText(overlay, x.text, text_origin, cv2.FONT_HERSHEY_SIMPLEX, 1, x.text_color, 2, cv2.LINE_AA)
            cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0, img)

        # Draw region annotations
        for i, x in enumerate(reversed(current_region_annotations)):
            self._draw_region_annotation(img, x)

        # for annotation in annotations:
        #     annotation.draw(img)

        #fname = './imgs/frame%d.jpg' % (self._sample_count)
        #cv2.imwrite(fname, img)

        self.appsrc.props.caps = sample.get_caps()
        self.appsrc.emit("push-buffer", sample.get_buffer())
        self._sample_count += 1

    def _draw_timestamp(self, frame, seconds_since_first_frame):
        time_str = '{:.2f}'.format(seconds_since_first_frame)
        time_str_size = cv2.getTextSize(time_str, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        cv2.rectangle(frame, (0, 1020), (time_str_size[0] + 20, 1080), (255, 0, 0), -1)
        cv2.putText(frame, time_str, (10,1060), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        return(time_str_size[0] + 20)

    def _draw_region_annotation(self, frame, annotation):
        pt1 = (annotation.region.x, annotation.region.y)
        pt2 = (annotation.region.x+annotation.region.width, annotation.region.y+annotation.region.height)
        cv2.rectangle(frame, pt1, pt2, annotation.color, 2)
        if annotation.text:
            text_origin = (pt1[0] + 5, pt1[1] + 20)
            cv2.putText(frame, annotation.text, text_origin, cv2.FONT_HERSHEY_SIMPLEX, 0.75, annotation.text_color, 1, cv2.LINE_AA)
        elif annotation.image is not None:
            height, width, _ = annotation.image.shape
            pt1 = (annotation.region.x, annotation.region.y)
            frame[pt1[1]:pt1[1]+height, pt1[0]:pt1[0]+width] = annotation.image
    # def draw(self, obj, duration_secs=None, label=""):
    #     with self.annotations_lock:
    #         if isinstance(obj, string_types):
    #             start_time = self._time.time()
    #             text = (
    #                 to_unicode(
    #                     datetime.datetime.fromtimestamp(start_time).strftime(
    #                         "%H:%M:%S.%f")[:-4]) +
    #                 ' ' +
    #                 to_unicode(obj))
    #             self.text_annotations.append(
    #                 _TextAnnotation(start_time, text, duration_secs))
    #         elif hasattr(obj, "region") and hasattr(obj, "time"):
    #             annotation = _Annotation.from_result(obj, label=label)
    #             if annotation.time:
    #                 self.annotations.append(annotation)
    #         else:
    #             raise TypeError(
    #                 "Can't draw object of type '%s'" % type(obj).__name__)


class Display():
    last_frame = None
    start_time = datetime.now()
    cap_thread = None
    max_duration = 5.0
    run = True
    msg_start = None
    msg = None
    msg2_start = None
    msg2 = None
    running = False
    search_boxes = {}
    first_frame_read = False

    def __init__(self, mainloop, recording_filename, is_video_recording=True):
        self.is_video_recording = is_video_recording
        self.mainloop = mainloop()
        self.recording_filename = recording_filename
        #self.received_eos = threading.Event()

        self._condition = threading.Condition()
        self.frame_num = 0
        self.tearing_down = False

        Gst.debug_set_active(True)
        Gst.debug_set_default_threshold(Gst.DebugLevel.WARNING)
        Gst.debug_add_log_function(self.on_debug, None)
        self.source_pipeline = Gst.parse_launch(source_pipeline_description)

        # Connect message handlers
        source_bus = self.source_pipeline.get_bus()
        source_bus.connect("message::error", self.on_error)
        source_bus.connect("message::warning", self.on_warning)
        source_bus.connect("message::eos", self.on_eos_from_source_pipeline)
        #source_bus.connect("message", self.on_bus_message_cb)
        source_bus.add_signal_watch()
        appsink = self.source_pipeline.get_by_name('appsink')
        appsink.connect('new-sample', self.on_new_sample)
        appsink.connect('eos', self.on_eos_from_appsink)

        # A realtime clock gives timestamps compatible with time.time()
        self.source_pipeline.use_clock(
            Gst.SystemClock(clock_type=Gst.ClockType.REALTIME)
        )
        
        if self.is_video_recording:
            self._sink_pipeline = SinkPipeline(None, False, save_video=self.recording_filename)

        self.source_pipeline.set_state(Gst.State.PLAYING)

    def __enter__(self):
        self.mainloop.__enter__()
        if self.is_video_recording:
            self._sink_pipeline.__enter__()
            self.start_recording()

    def start_recording(self):
        self._sink_pipeline.start_recording()

    def __exit__(self, exc_type, exc_value, tb):
        print('Display.__exit__')
        self.tearing_down = True
        self.source_pipeline.set_state(Gst.State.NULL)
        #self.source_pipeline.send_event(Gst.Event.new_eos())

        if self.is_video_recording:
            self._sink_pipeline.exit_prep()
            self._sink_pipeline.__exit__(exc_type, exc_value, tb)
            self._sink_pipeline = None

        #self.source_pipeline.set_state(Gst.State.PAUSED)
        #self.source_pipeline.set_state(Gst.State.READY)
        self.source_pipeline.get_by_name("appsink").get_static_pad("sink").send_event(Gst.Event.new_eos())

        #if not self.received_eos.wait(10):
            #print("Timeout waiting for sink EOS")

        self.mainloop.__exit__(exc_type, exc_value, tb)
        self.source_pipeline.get_bus().remove_signal_watch()
        self.source_pipeline = None
        del self.source_pipeline

    def on_new_sample(self, appsink):
        # Stop sending samples once teardown has started
        if self.tearing_down:
            return
        #print('on_new_sample ' + str(self.frame_num))
        
        sample = appsink.emit('pull-sample')

        # Add time attribute to the sample
        running_time = sample.get_segment().to_running_time(
            Gst.Format.TIME, sample.get_buffer().pts)
        sample.time = float(appsink.base_time + running_time) / 1e9

        frame = array_from_sample(sample)

        #fname = 'imgs/frame%d.jpg' % (self.frame_num)
        #cv2.imwrite(fname, frame)

        self.tell_user_thread(frame)
        if self.is_video_recording:
            self._sink_pipeline.on_sample(sample)
        self.frame_num += 1
        return Gst.FlowReturn.OK

    def on_error(self, _bus, message):
        #assert message.type == Gst.MessageType.ERROR
        #pipeline = self.source_pipeline
        #if pipeline is not None:
        #    Gst.debug_bin_to_dot_file_with_ts(
        #        pipeline, Gst.DebugGraphDetails.ALL, "ERROR")
        print(message)
        err, dbg = message.parse_error()
        self.tell_user_thread(
           RuntimeError("%s: %s\n%s\n" % (err, err.message, dbg)))

    def on_warning(self, _bus, message):
        #assert message.type == Gst.MessageType.WARNING
        #Gst.debug_bin_to_dot_file_with_ts(
        #    self.source_pipeline, Gst.DebugGraphDetails.ALL, "WARNING")
        err, dbg = message.parse_warning()
        print("%s: %s\n%s\n" % (err, err.message, dbg))

    def on_eos_from_source_pipeline(self, _bus, _message):
        print('eos')

    def on_eos_from_appsink(self, sink):
        print("EOS FROM APPSINK")
        #self.received_eos.set()

    #def on_bus_message_cb(self, bus, message):
        #print('Status: ', message.type)
        #print('Object: ', message.src)
        #print('Parsed Message: ', message.parse_state_changed())

        #if self.tearing_down:
            #if message.type == Gst.MessageType.STATE_CHANGED and isinstance(message.src, Gst.Pipeline):
                #old_state, new_state, pending_state = message.parse_state_changed()
                #if new_state == Gst.State.READY:
                    #print("IN THE CONDITION....")
                    #self.source_pipeline.set_state(Gst.State.NULL)
                    #self.source_pipeline.get_by_name("appsink").emit("eos")
                    #self.source_pipeline.get_by_name("v4l2src").send_event(Gst.Event.new_eos())
                    #self.source_pipeline.set_state(Gst.State.NULL)
                    #self.source_pipeline.send_event(Gst.Event.new_eos())

    def on_debug(self, category, level, dfile, dfctn, dline, source, message, user_data):
        if source:
            print('Debug {} {}: {}'.format(
                Gst.DebugLevel.get_name(level), source.name, message.get()))
        else:
            print('Debug {}: {}'.format(
                Gst.DebugLevel.get_name(level), message.get()))

    def is_running(self):
        return self.run

    def tell_user_thread(self, frame_or_exception):
        # `self.last_frame` is how we communicate from this thread (the GLib
        # main loop) to the main application thread running the user's script.
        # Note that only this thread writes to self.last_frame.

        if isinstance(frame_or_exception, Exception):
            print("glib thread: reporting exception to user thread: %s" %
                   frame_or_exception)
        # else:
        #     print("glib thread: new sample (time=%s)." %
        #            frame_or_exception.time)

        with self._condition:
            self.last_frame = frame_or_exception
            self._condition.notify_all()

    def get_frame(self, timeout_secs=10, since=None):
        t = time.time()
        end_time = t + timeout_secs
        if since is None:
            # If you want to wait 10s for a frame you're probably not interested
            # in a frame from 10s ago.
            since = t - timeout_secs

        with self._condition:
            while True:
                if (isinstance(self.last_frame, Frame) and
                        self.last_frame.time > since):
                    self.last_used_frame = self.last_frame
                    return self.last_frame
                elif isinstance(self.last_frame, Exception):
                    raise RuntimeError(str(self.last_frame))
                t = time.time()
                if t > end_time:
                    break
                self._condition.wait(end_time - t)

        pipeline = self.source_pipeline
        if pipeline:
            Gst.debug_bin_to_dot_file_with_ts(
                pipeline, Gst.DebugGraphDetails.ALL, "NoVideo")
        raise NoVideo("No video")

    def add_text_annotation(self, text, text_color=(255, 255, 255), background_color=(0, 200, 0), annotation_id=None, duration=1.0, top_left_cord_pos=(None, None)):
        '''
        Add a message to the video recording.
        '''
        last_frame = self.get_frame()
        text_annotation = TextAnnotation(last_frame.time,str(text), text_color=text_color, background_color=background_color, annotation_id=annotation_id, duration=duration, top_left_cord_pos=top_left_cord_pos)
        # If there is already a text annotation with the same id value, update the annotation
        # Otherwise, add a new annotation
        if self.is_video_recording:
            existing_annotations = [x for x in self._sink_pipeline.text_annotations if annotation_id == x.annotation_id]
            if len(existing_annotations) > 0:
                print('Updating existing annotation')
                existing_annotations[0].text = text_annotation.text
                existing_annotations[0].text_color = text_annotation.text_color
                existing_annotations[0].background_color = text_annotation.background_color
                existing_annotations[0].end_time = text_annotation.end_time
            else:
                self._sink_pipeline.text_annotations.append(text_annotation)
        #print('Adding text annotation', repr(text_annotation))
        return text_annotation

    def remove_text_annotation(self, annotation_id):
        self._sink_pipeline.text_annotations = [x for x in self._sink_pipeline.text_annotations if annotation_id != x.annotation_id]

    def add_region_annotation(self, region, text=None, image=None, color=(0, 0, 255), annotation_id=None, duration=1.0):
        '''
        Add a region annotation to the video recording
        '''
        last_frame = self.get_frame()
        region_annotation = RegionAnnotation(last_frame.time, 
                            #Region(x=pt1[0], y=pt1[1], width=pt2[0]-pt1[0], height=pt2[1]-pt1[1]),
                            region,
                            text=text,
                            image=image,
                            color=color,
                            annotation_id=annotation_id,
                            duration=duration)
        if self.is_video_recording:
            self._sink_pipeline.region_annotations.append(region_annotation)
        #print('Adding region annotation', repr(region_annotation))
        return(region_annotation)

    def remove_region_annotation(self, annotation_id):
        self._sink_pipeline.region_annotations = [x for x in self._sink_pipeline.region_annotations if annotation_id != x.annotation_id]


class NoVideo(Exception):
    """No video available from the source pipeline."""
    pass

class Region(namedtuple('Region', 'x y width height')):
    def __new__(cls, x, y, width, height):
        return super(Region, cls).__new__(cls, x, y, width, height)

class RegionAnnotation():
    def __init__(self, current_frame_time, region, text=None, image=None, color=(0, 0, 255), text_color=(255, 255, 255), annotation_id=None, duration=1.0):
        self.region = region
        self.color = color
        self.text_color = text_color
        self.text = text
        if image is not None:
            scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            height, width, _ = scaled_image.shape
            overlay = scaled_image.copy()
            cv2.rectangle(overlay, (0, 0), (width, height), color, -1)
            alpha = 0.5
            cv2.addWeighted(overlay, alpha, scaled_image, 1-alpha, 0, scaled_image)
            self.image = scaled_image
        self.annotation_id = annotation_id if annotation_id is not None else uuid.uuid4()
        self.duration = duration
        self.time = current_frame_time
        end_time_local = (datetime.utcfromtimestamp(current_frame_time) + timedelta(seconds=duration))
        self.end_time = end_time_local.replace(tzinfo=timezone.utc).timestamp()

class TextAnnotation():
    def __init__(self, current_frame_time, text, text_color=(255, 255, 255), background_color=(0, 0, 0), annotation_id=None, duration=1.0, top_left_cord_pos=(None, None)):
        self.top_left_cord_pos = top_left_cord_pos
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.annotation_id = annotation_id if annotation_id is not None else uuid.uuid4()
        self.duration = duration
        self.time = current_frame_time
        end_time_local = (datetime.utcfromtimestamp(current_frame_time) + timedelta(seconds=duration))
        self.end_time = end_time_local.replace(tzinfo=timezone.utc).timestamp()

    def __repr__(self):
        return (
           "TextAnnotation(id=%s, text=%s, time=%s, end_time=%s" % (self.annotation_id, self.text, datetime.utcfromtimestamp(self.time), datetime.utcfromtimestamp(self.end_time))) 
