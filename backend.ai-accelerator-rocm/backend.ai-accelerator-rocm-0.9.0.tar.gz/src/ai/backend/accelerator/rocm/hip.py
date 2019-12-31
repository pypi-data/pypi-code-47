from abc import ABCMeta, abstractmethod
import ctypes
from typing import Any, MutableMapping
import platform

from .exception import LibraryError


class hipDeviceArch_t(ctypes.Structure):
    _fields_ = [
        ('hasGlobalInt32Atomics', ctypes.c_uint, 1),
        ('hasGlobalFloatAtomicExch', ctypes.c_uint, 1),
        ('hasSharedInt32Atomics', ctypes.c_uint, 1),
        ('hasSharedFloatAtomicExch', ctypes.c_uint, 1),
        ('hasFloatAtomicAdd', ctypes.c_uint, 1),
        ('hasGlobalInt64Atomics', ctypes.c_uint, 1),
        ('hasSharedInt64Atomics', ctypes.c_uint, 1),
        ('hasDoubles', ctypes.c_uint, 1),
        ('hasWarpVote', ctypes.c_uint, 1),
        ('hasWarpBallot', ctypes.c_uint, 1),
        ('hasWarpShuffle', ctypes.c_uint, 1),
        ('hasFunnelShift', ctypes.c_uint, 1),
        ('hasThreadFenceSystem', ctypes.c_uint, 1),
        ('hasSyncThreadsExt', ctypes.c_uint, 1),
        ('hasSurfaceFuncs', ctypes.c_uint, 1),
        ('has3dGrid', ctypes.c_uint, 1),
        ('hasDynamicParallelism', ctypes.c_uint, 1),
    ]


class hipDeviceProp(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char * 256),
        ('totalGlobalMem', ctypes.c_size_t),
        ('sharedMemPerBlock', ctypes.c_size_t),
        ('regsPerBlock', ctypes.c_int),
        ('warpSize', ctypes.c_int),
        ('maxThreadsPerBlock', ctypes.c_int),
        ('maxThreadsDim', ctypes.c_int * 3),
        ('maxGridSize', ctypes.c_int * 3),
        ('clockRate', ctypes.c_int),
        ('memoryClockRate', ctypes.c_int),
        ('memoryBusWidth', ctypes.c_int),
        ('totalConstMem', ctypes.c_size_t),
        ('major', ctypes.c_int),
        ('minor', ctypes.c_int),
        ('multiProcessorCount', ctypes.c_int),
        ('l2CacheSize', ctypes.c_int),
        ('maxThreadsPerMultiProcessor', ctypes.c_int),
        ('computeMode', ctypes.c_int),
        ('clockInstructionRate', ctypes.c_int),
        ('arch', hipDeviceArch_t),
        ('concurrentKernels', ctypes.c_int),
        ('pciDomainID', ctypes.c_int),
        ('pciBusID', ctypes.c_int),
        ('pciDeviceID', ctypes.c_int),
        ('maxSharedMemoryPerMultiProcessor', ctypes.c_size_t),
        ('isMultiGpuBoard', ctypes.c_int),
        ('canMapHostMemory', ctypes.c_int),
        ('gcnArch', ctypes.c_int),
        ('integrated', ctypes.c_int),
        ('cooperativeLaunch', ctypes.c_int),
        ('cooperativeMultiDeviceLaunch', ctypes.c_int),
        ('maxTexture1D', ctypes.c_int),
        ('maxTexture2D', ctypes.c_int * 2),
        ('maxTexture3D', ctypes.c_int * 3),
        ('hdpMemFlushCntl', ctypes.POINTER(ctypes.c_uint)),
        ('hdpRegFlushCntl', ctypes.POINTER(ctypes.c_uint)),
        ('memPitch', ctypes.c_size_t),
        ('textureAlignment', ctypes.c_size_t),
        ('kernelExecTimeoutEnabled', ctypes.c_int),
        ('ECCEnabled', ctypes.c_int),
        ('tccDriver', ctypes.c_int),
    ]


def _load_library(name):
    try:
        if platform.system() == 'Windows':
            return ctypes.windll.LoadLibrary(name)
        else:
            return ctypes.cdll.LoadLibrary(name)
    except OSError:
        pass
    return None


class LibraryBase(metaclass=ABCMeta):

    name = 'LIBRARY'

    _lib = None

    @classmethod
    @abstractmethod
    def load_library(cls) -> ctypes.CDLL:
        pass

    @classmethod
    def _ensure_lib(cls):
        if cls._lib is None:
            cls._lib = cls.load_library()
        if cls._lib is None:
            raise ImportError(f'Could not load the {cls.name} library!')

    @classmethod
    def invoke(cls, func_name, *args, check_rc=True):
        try:
            cls._ensure_lib()
        except ImportError:
            raise
        func = getattr(cls._lib, func_name)
        rc = func(*args)
        if check_rc and rc != 0:
            raise LibraryError(cls.name, func_name, rc)
        return rc


class libhip(LibraryBase):

    name = 'HIP'

    _version = (0, 0)

    @classmethod
    def load_library(cls):
        system_type = platform.system()
        if system_type == 'Linux':
            return _load_library('libhip_hcc.so')
        else:
            raise NotImplementedError()

    @classmethod
    def get_device_count(cls) -> int:
        count = ctypes.c_int()
        cls.invoke('hipGetDeviceCount', ctypes.byref(count))
        return count.value

    @classmethod
    def get_device_props(cls, device_idx: int):
        props_struct = hipDeviceProp()
        cls.invoke('hipGetDeviceProperties', ctypes.byref(props_struct), device_idx)
        props: MutableMapping[str, Any] = {
            k: getattr(props_struct, k) for k, _ in hipDeviceProp._fields_
        }
        pci_bus_id = b' ' * 16
        cls.invoke('hipDeviceGetPCIBusId',
                   ctypes.c_char_p(pci_bus_id), 16, device_idx)
        props['name'] = props['name'].decode()
        props['pciBusID_str'] = pci_bus_id.split(b'\x00')[0].decode()
        return props
