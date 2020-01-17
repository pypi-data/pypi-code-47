import numpy as np
import sqlite3
import os, sys
from ctypes import *
from collections import defaultdict

if sys.platform[:5] == "win32":
    libname = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'brukerlib', "timsdata.dll")
elif sys.platform[:5] == "linux":
    libname = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'brukerlib', "libtimsdata.so")
else:
    raise Exception("Unsupported platform.")
assert os.path.exists(libname), libname    
    
dll = cdll.LoadLibrary(libname)
dll.tims_open.argtypes = [ c_char_p, c_uint32 ]
dll.tims_open.restype = c_uint64
dll.tims_close.argtypes = [ c_uint64 ]
dll.tims_close.restype = None
dll.tims_get_last_error_string.argtypes = [ c_char_p, c_uint32 ]
dll.tims_get_last_error_string.restype = c_uint32
dll.tims_has_recalibrated_state.argtypes = [ c_uint64 ]
dll.tims_has_recalibrated_state.restype = c_uint32
dll.tims_read_scans_v2.argtypes = [ c_uint64, c_int64, c_uint32, c_uint32, c_void_p, c_uint32 ]
dll.tims_read_scans_v2.restype = c_uint32

convfunc_argtypes = [ c_uint64, c_int64, POINTER(c_double), POINTER(c_double), c_uint32 ]

dll.tims_index_to_mz.argtypes = convfunc_argtypes
dll.tims_index_to_mz.restype = c_uint32
dll.tims_mz_to_index.argtypes = convfunc_argtypes
dll.tims_mz_to_index.restype = c_uint32

dll.tims_scannum_to_oneoverk0.argtypes = convfunc_argtypes
dll.tims_scannum_to_oneoverk0.restype = c_uint32
dll.tims_oneoverk0_to_scannum.argtypes = convfunc_argtypes
dll.tims_oneoverk0_to_scannum.restype = c_uint32

dll.tims_scannum_to_voltage.argtypes = convfunc_argtypes
dll.tims_scannum_to_voltage.restype = c_uint32
dll.tims_voltage_to_scannum.argtypes = convfunc_argtypes
dll.tims_voltage_to_scannum.restype = c_uint32







# This is from the example file Bruker provided; will probably want to
# rewrite/replace it if this is going to be released with multiplierz.
def decodeArrayOfStrings (blob):
    if blob is None:
        return None # property not set

    if len(blob) == 0:
        return [] # empty list

    blob = bytearray(blob)
    if blob[-1] != 0:
        raise ValueError("Illegal BLOB contents.") # trailing nonsense

    if sys.version_info.major == 2:
        return str(str(blob), 'utf-8').split('\0')[:-1]
    if sys.version_info.major == 3:
        return str(blob, 'utf-8').split('\0')[:-1]
class TimsData:

    def __init__ (self, analysis_directory, use_recalibrated_state=False):

        if sys.version_info.major == 2:
            if not isinstance(analysis_directory, str):
                raise ValueError("analysis_directory must be a Unicode string.")
        if sys.version_info.major == 3:
            if not isinstance(analysis_directory, str):
                raise ValueError("analysis_directory must be a string.")

        self.dll = dll

        self.handle = self.dll.tims_open(
            analysis_directory.encode('utf-8'),
            1 if use_recalibrated_state else 0 )
        if self.handle == 0:
            throwLastTimsDataError(self.dll)

        self.conn = sqlite3.connect(os.path.join(analysis_directory, "analysis.tdf"))

        self.initial_frame_buffer_size = 128 # may grow in readScans()

    def __del__ (self):
        if hasattr(self, 'handle'):
            self.dll.tims_close(self.handle)         
            
    def __callConversionFunc (self, frame_id, input_data, func):

        if type(input_data) is np.ndarray and input_data.dtype == np.float64:
            # already "native" format understood by DLL -> avoid extra copy
            in_array = input_data
        else:
            # convert data to format understood by DLL:
            in_array = np.array(input_data, dtype=np.float64)

        cnt = len(in_array)
        out = np.empty(shape=cnt, dtype=np.float64)
        success = func(self.handle, frame_id,
                       in_array.ctypes.data_as(POINTER(c_double)),
                       out.ctypes.data_as(POINTER(c_double)),
                       cnt)

        if success == 0:
            throwLastTimsDataError(self.dll)

        return out

    def indexToMz (self, frame_id, mzs):
        return self.__callConversionFunc(frame_id, mzs, self.dll.tims_index_to_mz)
        
    def mzToIndex (self, frame_id, mzs):
        return self.__callConversionFunc(frame_id, mzs, self.dll.tims_mz_to_index)
        
    def scanNumToOneOverK0 (self, frame_id, mzs):
        return self.__callConversionFunc(frame_id, mzs, self.dll.tims_scannum_to_oneoverk0)

    def oneOverK0ToScanNum (self, frame_id, mzs):
        return self.__callConversionFunc(frame_id, mzs, self.dll.tims_oneoverk0_to_scannum)

    def scanNumToVoltage (self, frame_id, mzs):
        return self.__callConversionFunc(frame_id, mzs, self.dll.tims_scannum_to_voltage)

    def voltageToScanNum (self, frame_id, mzs):
        return self.__callConversionFunc(frame_id, mzs, self.dll.tims_voltage_to_scannum)

        
    # Output: list of tuples (indices, intensities)
    def readScans (self, frame_id, scan_begin, scan_end):

        # buffer-growing loop
        while True:
            cnt = int(self.initial_frame_buffer_size) # necessary cast to run with python 3.5
            buf = np.empty(shape=cnt, dtype=np.uint32)
            len = 4 * cnt

            required_len = self.dll.tims_read_scans_v2(self.handle, frame_id, scan_begin, scan_end,
                                                    buf.ctypes.data_as(POINTER(c_uint32)),
                                                    len)
            if required_len == 0:
                throwLastTimsDataError(self.dll)

            if required_len > len:
                if required_len > 16777216:
                    # arbitrary limit for now...
                    raise RuntimeError("Maximum expected frame size exceeded.")
                self.initial_frame_buffer_size = required_len / 4 + 1 # grow buffer
            else:
                break

        result = []
        d = scan_end - scan_begin
        for i in range(scan_begin, scan_end):
            npeaks = buf[i-scan_begin]
            indices     = buf[d : d+npeaks]
            d += npeaks
            intensities = buf[d : d+npeaks]
            d += npeaks
            result.append((indices,intensities))

        return result


class mzBruker(object): # Re-add mzFile inheritance (for some reason.)
    def __init__(self, d_directory):
        tdf = os.path.join(d_directory, 'analysis.tdf')
        tdf_bin = os.path.join(d_directory, 'analysis.tdf_bin')
        if not os.path.exists(tdf):
            raise IOError("%s not found." % tdf)
        if not os.path.exists(tdf_bin):
            raise IOError('%s not found.' % tdf_bin)
        
        self.db_conn = sqlite3.connect(tdf)
        self.cur = self.db_conn.cursor()
        self.source = TimsData(str(d_directory, 'utf-8'), 
                               use_recalibrated_state=False) # True?

        #self.pasef_frames = set(self.dbquery('SELECT Frame FROM PasefFrameMSMSInfo'))
        frame_types = self.dbquery("SELECT Id, MsMsType, Time FROM Frames")
        self.pasef_frames = []
        self.ms1_frames = []
        for f_id, typenum, rt in frame_types:
            if typenum == 8:
                self.pasef_frames.append((f_id, rt))
            elif typenum == 0:
                self.ms1_frames.append((f_id, rt))
            else:
                raise IOError("Unknown frame type: %s" % typenum)
        
    def dbquery(self, command):
        results = self.cur.execute(command).fetchall()
        if all([len(x) == 1 for x in results]):
            return [x[0] for x in results]
        else:
            return results
        
    def frame(self, framenum, start_scan = None, stop_scan = None):
        """
        Returns all points from the specified frame; each point is a 3D
        coordinate (mz, k0, intensity).
        """
        scan_count = self.dbquery("SELECT NumScans FROM Frames WHERE Id=%d" % framenum)[0]
        if start_scan == None and stop_scan == None:        
            scans = self.source.readScans(framenum, 0, scan_count)
            k0s = self.source.scanNumToOneOverK0(framenum, list(range(scan_count)))
        else:
            scans = self.source.readScans(framenum, start_scan, stop_scan)
            k0s = self.source.scanNumToOneOverK0(framenum, list(range(scan_count)))[start_scan:stop_scan]
            
        pts = []
        assert len(k0s) == len(scans), (len(k0s), len(scans))
        for scannum, (k0, (indexes, ints)) in enumerate(zip(list(k0s), scans)):
            if len(indexes) > 0:
                mzs = self.source.indexToMz(framenum, indexes)
                assert len(mzs) == len(ints), list(map(len, [mzs, k0s, ints]))
                pts += [(mz, k0, intensity) for mz, intensity in zip(mzs, ints)]
        return pts        
    
    def pasef_scans(self, framenum, include_k0 = False):
        """
        Returns scans for distinct precursors from a PASEF frame.
        """
        
        subscans = self.dbquery(("SELECT ScanNumBegin, ScanNumEnd, Precursor "
                                 "FROM PasefFrameMsMsInfo WHERE Frame = %d")
                                % framenum)
        scans = []
        for start, stop, prec in subscans:
            partial_frame = self.frame(framenum, start, stop)
            if include_k0:
                scans.append(partial_frame)
            else:
                scans.append([(x[0], x[2]) for x in partial_frame])
        
        return scans
    
    #def scan()
    
    def xic_batch(self, windows, dimensions = ['rt', 'k0', 'int']):
        """
        The Bruker API has no concept of XICs as far as I've been able to
        determine; thus, they have to be constructed directly from MS1s. MS1
        frames, also, seem to be only requestable all-or-nothing; at best,
        they can be limited in the k0 dimension by limiting the scan numbers 
        requested, but this is probably of limited use (since precursors tend
        to be targetted by MZ/RT, at least for now.)
        
        Thus, provide an arbitrary number of XIC requests simultaneously, and
        they'll all be built up in a single run through the required frames.
        
        Each window should be a tuple: (start_rt, stop_rt, start_mz, 
                                        stop_mz, start_k0, stop_k0)
                                        
        Axes of the output can be controlled by the "dimensions" argument,
        which supports the keys 'rt', 'mz', 'k0', and 'int'.
        """
        
        if not windows:
            return []
        
        pep_windows.sort(key = lambda x: x[1][0])
        
        elements = list(zip(*windows))
        for i in range(len(windows)):
            assert len(windows[i]) == 6, "Window %d: Too few elements." % i
            assert elements[0][i] <= elements[1][i], "Window %d: Start RT later than stop RT" % i
            assert elements[2][i] <= elements[3][i], "Window %d: Start MZ greater than stop MZ" % i
            assert elements[4][i] <= elements[5][i], "Window %d: Start k0 later than stop k0" % i
        
        window_starts = elements[0] # Sorted (from above)
        window_stops = elements[1] # Not necessarily sorted!
        
        earliest, latest = min(elements[0]), max(elements[1])
        ms1frames = [x for x in self.ms1_frames if earliest <= x[1] <= latest]
        
        print(("0/%d" % len(ms1frames)))
        c = 0
        
        xics = dict([(w, []) for w in windows])
        for fnum, rt in ms1frames:
            frame = self.frame(fnum)
            for window in list(xics.keys()):
                mzl, mzh, k0l, k0h = window[2:]
                subframe = [(rt, mz, k0, i) for mz, k0, i in frame if
                            (mzl <= mz <= mzh and k0l <= k0 <= k0h)]
                xics[window] += subframe
        
            c += 1
            if c % 10 == 0:
                print(("\r%d/%d" % (c, len(ms1frames))))
                
        axis_indexes = {'rt':0, 'mz':1, 'k0':2, 'int':3, 'intensity':3}        
        output = []
        for window, pts in list(xics.items()):        
            if not pts:
                output.append((window, []))
            else:
                elements = []
                for dim in dimensions:
                    el = list(zip(*pts))[axis_indexes[dim]]
                    elements.append(el)
                output.append((window, list(zip(*elements))))
        
        
        return output
    
    def mobiligram(self, rt_start, rt_stop, mz_start, mz_stop, k0_start, k0_stop):
        framenums = [fnum for fnum, rt in self.ms1_frames if rt_start <= rt <= rt_stop]
        frames = list(map(self.frame, framenums))
        pts = defaultdict(float)
        for frame in frames:
            for mz, k0, i in frame:
                if mz_start <= mz <= mz_stop and k0_start <= k0 <= k0_stop:
                    pts[k0] += i
        
        return sorted(pts.items())
        
        
        
        
    

if __name__ == '__main__':
    foo = mzBruker(r'\\rc-data1\blaise\ms_data_share\Max\BrukerAPI\example_data\C0004.3_Slot1-01_01_2454.d')
    bar = foo.xic_batch(None)