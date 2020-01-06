import sys
import numpy as np
import ctypes as ct
# Stub code for OpenCL setup.

import pyopencl as cl
import numpy as np
import sys

if cl.version.VERSION < (2015,2):
    raise Exception('Futhark requires at least PyOpenCL version 2015.2.  Installed version is %s.' %
                    cl.version.VERSION_TEXT)

def parse_preferred_device(s):
    pref_num = 0
    if len(s) > 1 and s[0] == '#':
        i = 1
        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                pref_num = pref_num * 10 + int(s[i])
            i += 1
        while i < len(s) and s[i].isspace():
            i += 1
        return (s[i:], pref_num)
    else:
        return (s, 0)

def get_prefered_context(interactive=False, platform_pref=None, device_pref=None):
    if device_pref != None:
        (device_pref, device_num) = parse_preferred_device(device_pref)
    else:
        device_num = 0

    if interactive:
        return cl.create_some_context(interactive=True)

    def blacklisted(p, d):
        return platform_pref == None and device_pref == None and \
            p.name == "Apple" and d.name.find("Intel(R) Core(TM)") >= 0
    def platform_ok(p):
        return not platform_pref or p.name.find(platform_pref) >= 0
    def device_ok(d):
        return not device_pref or d.name.find(device_pref) >= 0

    device_matches = 0

    for p in cl.get_platforms():
        if not platform_ok(p):
            continue
        for d in p.get_devices():
            if blacklisted(p,d) or not device_ok(d):
                continue
            if device_matches == device_num:
                return cl.Context(devices=[d])
            else:
                device_matches += 1
    raise Exception('No OpenCL platform and device matching constraints found.')

def size_assignment(s):
    name, value = s.split('=')
    return (name, int(value))

def check_types(self, required_types):
    if 'f64' in required_types:
        if self.device.get_info(cl.device_info.PREFERRED_VECTOR_WIDTH_DOUBLE) == 0:
            raise Exception('Program uses double-precision floats, but this is not supported on chosen device: %s' % self.device.name)

def apply_size_heuristics(self, size_heuristics, sizes):
    for (platform_name, device_type, size, value) in size_heuristics:
        if sizes[size] == None \
           and self.platform.name.find(platform_name) >= 0 \
           and self.device.type == device_type:
               if type(value) == str:
                   sizes[size] = self.device.get_info(getattr(cl.device_info,value))
               else:
                   sizes[size] = value
    return sizes

def initialise_opencl_object(self,
                             program_src='',
                             command_queue=None,
                             interactive=False,
                             platform_pref=None,
                             device_pref=None,
                             default_group_size=None,
                             default_num_groups=None,
                             default_tile_size=None,
                             default_threshold=None,
                             size_heuristics=[],
                             required_types=[],
                             all_sizes={},
                             user_sizes={}):
    if command_queue is None:
        self.ctx = get_prefered_context(interactive, platform_pref, device_pref)
        self.queue = cl.CommandQueue(self.ctx)
    else:
        self.ctx = command_queue.context
        self.queue = command_queue
    self.device = self.queue.device
    self.platform = self.device.platform
    self.pool = cl.tools.MemoryPool(cl.tools.ImmediateAllocator(self.queue))
    device_type = self.device.type

    check_types(self, required_types)

    max_group_size = int(self.device.max_work_group_size)
    max_tile_size = int(np.sqrt(self.device.max_work_group_size))

    self.max_group_size = max_group_size
    self.max_tile_size = max_tile_size
    self.max_threshold = 0
    self.max_num_groups = 0
    self.max_local_memory = int(self.device.local_mem_size)
    self.free_list = {}

    if 'default_group_size' in sizes:
        default_group_size = sizes['default_group_size']
        del sizes['default_group_size']

    if 'default_num_groups' in sizes:
        default_num_groups = sizes['default_num_groups']
        del sizes['default_num_groups']

    if 'default_tile_size' in sizes:
        default_tile_size = sizes['default_tile_size']
        del sizes['default_tile_size']

    if 'default_threshold' in sizes:
        default_threshold = sizes['default_threshold']
        del sizes['default_threshold']

    default_group_size_set = default_group_size != None
    default_tile_size_set = default_tile_size != None
    default_sizes = apply_size_heuristics(self, size_heuristics,
                                          {'group_size': default_group_size,
                                           'tile_size': default_tile_size,
                                           'num_groups': default_num_groups,
                                           'lockstep_width': None,
                                           'threshold': default_threshold})
    default_group_size = default_sizes['group_size']
    default_num_groups = default_sizes['num_groups']
    default_threshold = default_sizes['threshold']
    default_tile_size = default_sizes['tile_size']
    lockstep_width = default_sizes['lockstep_width']

    if default_group_size > max_group_size:
        if default_group_size_set:
            sys.stderr.write('Note: Device limits group size to {} (down from {})\n'.
                             format(max_tile_size, default_group_size))
        default_group_size = max_group_size

    if default_tile_size > max_tile_size:
        if default_tile_size_set:
            sys.stderr.write('Note: Device limits tile size to {} (down from {})\n'.
                             format(max_tile_size, default_tile_size))
        default_tile_size = max_tile_size

    for (k,v) in user_sizes.items():
        if k in all_sizes:
            all_sizes[k]['value'] = v
        else:
            raise Exception('Unknown size: {}\nKnown sizes: {}'.format(k, ' '.join(all_sizes.keys())))

    self.sizes = {}
    for (k,v) in all_sizes.items():
        if v['class'] == 'group_size':
            max_value = max_group_size
            default_value = default_group_size
        elif v['class'] == 'num_groups':
            max_value = max_group_size # Intentional!
            default_value = default_num_groups
        elif v['class'] == 'tile_size':
            max_value = max_tile_size
            default_value = default_tile_size
        elif v['class'].startswith('threshold'):
            max_value = None
            default_value = default_threshold
        else:
            # Bespoke sizes have no limit or default.
            max_value = None
        if v['value'] == None:
            self.sizes[k] = default_value
        elif max_value != None and v['value'] > max_value:
            sys.stderr.write('Note: Device limits {} to {} (down from {}\n'.
                             format(k, max_value, v['value']))
            self.sizes[k] = max_value
        else:
            self.sizes[k] = v['value']

    # XXX: we perform only a subset of z-encoding here.  Really, the
    # compiler should provide us with the variables to which
    # parameters are mapped.
    if (len(program_src) >= 0):
        return cl.Program(self.ctx, program_src).build(
            ["-DLOCKSTEP_WIDTH={}".format(lockstep_width)]
            + ["-D{}={}".format(s.replace('z', 'zz').replace('.', 'zi'),v) for (s,v) in self.sizes.items()])

def opencl_alloc(self, min_size, tag):
    min_size = 1 if min_size == 0 else min_size
    assert min_size > 0
    return self.pool.allocate(min_size)

def opencl_free_all(self):
    self.pool.free_held()
import pyopencl.array
import time
import argparse
sizes = {}
synchronous = False
preferred_platform = None
preferred_device = None
default_threshold = None
default_group_size = None
default_num_groups = None
default_tile_size = None
fut_opencl_src = """#ifdef cl_clang_storage_class_specifiers
#pragma OPENCL EXTENSION cl_clang_storage_class_specifiers : enable
#endif
#pragma OPENCL EXTENSION cl_khr_byte_addressable_store : enable
#pragma OPENCL EXTENSION cl_khr_fp64 : enable
__kernel void dummy_kernel(__global unsigned char *dummy, int n)
{
    const int thread_gid = get_global_id(0);
    
    if (thread_gid >= n)
        return;
}
typedef char int8_t;
typedef short int16_t;
typedef int int32_t;
typedef long int64_t;
typedef uchar uint8_t;
typedef ushort uint16_t;
typedef uint uint32_t;
typedef ulong uint64_t;
#ifdef cl_nv_pragma_unroll
static inline void mem_fence_global()
{
    asm("membar.gl;");
}
#else
static inline void mem_fence_global()
{
    mem_fence(CLK_LOCAL_MEM_FENCE | CLK_GLOBAL_MEM_FENCE);
}
#endif
static inline void mem_fence_local()
{
    mem_fence(CLK_LOCAL_MEM_FENCE);
}
static inline int8_t add8(int8_t x, int8_t y)
{
    return x + y;
}
static inline int16_t add16(int16_t x, int16_t y)
{
    return x + y;
}
static inline int32_t add32(int32_t x, int32_t y)
{
    return x + y;
}
static inline int64_t add64(int64_t x, int64_t y)
{
    return x + y;
}
static inline int8_t sub8(int8_t x, int8_t y)
{
    return x - y;
}
static inline int16_t sub16(int16_t x, int16_t y)
{
    return x - y;
}
static inline int32_t sub32(int32_t x, int32_t y)
{
    return x - y;
}
static inline int64_t sub64(int64_t x, int64_t y)
{
    return x - y;
}
static inline int8_t mul8(int8_t x, int8_t y)
{
    return x * y;
}
static inline int16_t mul16(int16_t x, int16_t y)
{
    return x * y;
}
static inline int32_t mul32(int32_t x, int32_t y)
{
    return x * y;
}
static inline int64_t mul64(int64_t x, int64_t y)
{
    return x * y;
}
static inline uint8_t udiv8(uint8_t x, uint8_t y)
{
    return x / y;
}
static inline uint16_t udiv16(uint16_t x, uint16_t y)
{
    return x / y;
}
static inline uint32_t udiv32(uint32_t x, uint32_t y)
{
    return x / y;
}
static inline uint64_t udiv64(uint64_t x, uint64_t y)
{
    return x / y;
}
static inline uint8_t umod8(uint8_t x, uint8_t y)
{
    return x % y;
}
static inline uint16_t umod16(uint16_t x, uint16_t y)
{
    return x % y;
}
static inline uint32_t umod32(uint32_t x, uint32_t y)
{
    return x % y;
}
static inline uint64_t umod64(uint64_t x, uint64_t y)
{
    return x % y;
}
static inline int8_t sdiv8(int8_t x, int8_t y)
{
    int8_t q = x / y;
    int8_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int16_t sdiv16(int16_t x, int16_t y)
{
    int16_t q = x / y;
    int16_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int32_t sdiv32(int32_t x, int32_t y)
{
    int32_t q = x / y;
    int32_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int64_t sdiv64(int64_t x, int64_t y)
{
    int64_t q = x / y;
    int64_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int8_t smod8(int8_t x, int8_t y)
{
    int8_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int16_t smod16(int16_t x, int16_t y)
{
    int16_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int32_t smod32(int32_t x, int32_t y)
{
    int32_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int64_t smod64(int64_t x, int64_t y)
{
    int64_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int8_t squot8(int8_t x, int8_t y)
{
    return x / y;
}
static inline int16_t squot16(int16_t x, int16_t y)
{
    return x / y;
}
static inline int32_t squot32(int32_t x, int32_t y)
{
    return x / y;
}
static inline int64_t squot64(int64_t x, int64_t y)
{
    return x / y;
}
static inline int8_t srem8(int8_t x, int8_t y)
{
    return x % y;
}
static inline int16_t srem16(int16_t x, int16_t y)
{
    return x % y;
}
static inline int32_t srem32(int32_t x, int32_t y)
{
    return x % y;
}
static inline int64_t srem64(int64_t x, int64_t y)
{
    return x % y;
}
static inline int8_t smin8(int8_t x, int8_t y)
{
    return x < y ? x : y;
}
static inline int16_t smin16(int16_t x, int16_t y)
{
    return x < y ? x : y;
}
static inline int32_t smin32(int32_t x, int32_t y)
{
    return x < y ? x : y;
}
static inline int64_t smin64(int64_t x, int64_t y)
{
    return x < y ? x : y;
}
static inline uint8_t umin8(uint8_t x, uint8_t y)
{
    return x < y ? x : y;
}
static inline uint16_t umin16(uint16_t x, uint16_t y)
{
    return x < y ? x : y;
}
static inline uint32_t umin32(uint32_t x, uint32_t y)
{
    return x < y ? x : y;
}
static inline uint64_t umin64(uint64_t x, uint64_t y)
{
    return x < y ? x : y;
}
static inline int8_t smax8(int8_t x, int8_t y)
{
    return x < y ? y : x;
}
static inline int16_t smax16(int16_t x, int16_t y)
{
    return x < y ? y : x;
}
static inline int32_t smax32(int32_t x, int32_t y)
{
    return x < y ? y : x;
}
static inline int64_t smax64(int64_t x, int64_t y)
{
    return x < y ? y : x;
}
static inline uint8_t umax8(uint8_t x, uint8_t y)
{
    return x < y ? y : x;
}
static inline uint16_t umax16(uint16_t x, uint16_t y)
{
    return x < y ? y : x;
}
static inline uint32_t umax32(uint32_t x, uint32_t y)
{
    return x < y ? y : x;
}
static inline uint64_t umax64(uint64_t x, uint64_t y)
{
    return x < y ? y : x;
}
static inline uint8_t shl8(uint8_t x, uint8_t y)
{
    return x << y;
}
static inline uint16_t shl16(uint16_t x, uint16_t y)
{
    return x << y;
}
static inline uint32_t shl32(uint32_t x, uint32_t y)
{
    return x << y;
}
static inline uint64_t shl64(uint64_t x, uint64_t y)
{
    return x << y;
}
static inline uint8_t lshr8(uint8_t x, uint8_t y)
{
    return x >> y;
}
static inline uint16_t lshr16(uint16_t x, uint16_t y)
{
    return x >> y;
}
static inline uint32_t lshr32(uint32_t x, uint32_t y)
{
    return x >> y;
}
static inline uint64_t lshr64(uint64_t x, uint64_t y)
{
    return x >> y;
}
static inline int8_t ashr8(int8_t x, int8_t y)
{
    return x >> y;
}
static inline int16_t ashr16(int16_t x, int16_t y)
{
    return x >> y;
}
static inline int32_t ashr32(int32_t x, int32_t y)
{
    return x >> y;
}
static inline int64_t ashr64(int64_t x, int64_t y)
{
    return x >> y;
}
static inline uint8_t and8(uint8_t x, uint8_t y)
{
    return x & y;
}
static inline uint16_t and16(uint16_t x, uint16_t y)
{
    return x & y;
}
static inline uint32_t and32(uint32_t x, uint32_t y)
{
    return x & y;
}
static inline uint64_t and64(uint64_t x, uint64_t y)
{
    return x & y;
}
static inline uint8_t or8(uint8_t x, uint8_t y)
{
    return x | y;
}
static inline uint16_t or16(uint16_t x, uint16_t y)
{
    return x | y;
}
static inline uint32_t or32(uint32_t x, uint32_t y)
{
    return x | y;
}
static inline uint64_t or64(uint64_t x, uint64_t y)
{
    return x | y;
}
static inline uint8_t xor8(uint8_t x, uint8_t y)
{
    return x ^ y;
}
static inline uint16_t xor16(uint16_t x, uint16_t y)
{
    return x ^ y;
}
static inline uint32_t xor32(uint32_t x, uint32_t y)
{
    return x ^ y;
}
static inline uint64_t xor64(uint64_t x, uint64_t y)
{
    return x ^ y;
}
static inline char ult8(uint8_t x, uint8_t y)
{
    return x < y;
}
static inline char ult16(uint16_t x, uint16_t y)
{
    return x < y;
}
static inline char ult32(uint32_t x, uint32_t y)
{
    return x < y;
}
static inline char ult64(uint64_t x, uint64_t y)
{
    return x < y;
}
static inline char ule8(uint8_t x, uint8_t y)
{
    return x <= y;
}
static inline char ule16(uint16_t x, uint16_t y)
{
    return x <= y;
}
static inline char ule32(uint32_t x, uint32_t y)
{
    return x <= y;
}
static inline char ule64(uint64_t x, uint64_t y)
{
    return x <= y;
}
static inline char slt8(int8_t x, int8_t y)
{
    return x < y;
}
static inline char slt16(int16_t x, int16_t y)
{
    return x < y;
}
static inline char slt32(int32_t x, int32_t y)
{
    return x < y;
}
static inline char slt64(int64_t x, int64_t y)
{
    return x < y;
}
static inline char sle8(int8_t x, int8_t y)
{
    return x <= y;
}
static inline char sle16(int16_t x, int16_t y)
{
    return x <= y;
}
static inline char sle32(int32_t x, int32_t y)
{
    return x <= y;
}
static inline char sle64(int64_t x, int64_t y)
{
    return x <= y;
}
static inline int8_t pow8(int8_t x, int8_t y)
{
    int8_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline int16_t pow16(int16_t x, int16_t y)
{
    int16_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline int32_t pow32(int32_t x, int32_t y)
{
    int32_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline int64_t pow64(int64_t x, int64_t y)
{
    int64_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline bool itob_i8_bool(int8_t x)
{
    return x;
}
static inline bool itob_i16_bool(int16_t x)
{
    return x;
}
static inline bool itob_i32_bool(int32_t x)
{
    return x;
}
static inline bool itob_i64_bool(int64_t x)
{
    return x;
}
static inline int8_t btoi_bool_i8(bool x)
{
    return x;
}
static inline int16_t btoi_bool_i16(bool x)
{
    return x;
}
static inline int32_t btoi_bool_i32(bool x)
{
    return x;
}
static inline int64_t btoi_bool_i64(bool x)
{
    return x;
}
#define sext_i8_i8(x) ((int8_t) (int8_t) x)
#define sext_i8_i16(x) ((int16_t) (int8_t) x)
#define sext_i8_i32(x) ((int32_t) (int8_t) x)
#define sext_i8_i64(x) ((int64_t) (int8_t) x)
#define sext_i16_i8(x) ((int8_t) (int16_t) x)
#define sext_i16_i16(x) ((int16_t) (int16_t) x)
#define sext_i16_i32(x) ((int32_t) (int16_t) x)
#define sext_i16_i64(x) ((int64_t) (int16_t) x)
#define sext_i32_i8(x) ((int8_t) (int32_t) x)
#define sext_i32_i16(x) ((int16_t) (int32_t) x)
#define sext_i32_i32(x) ((int32_t) (int32_t) x)
#define sext_i32_i64(x) ((int64_t) (int32_t) x)
#define sext_i64_i8(x) ((int8_t) (int64_t) x)
#define sext_i64_i16(x) ((int16_t) (int64_t) x)
#define sext_i64_i32(x) ((int32_t) (int64_t) x)
#define sext_i64_i64(x) ((int64_t) (int64_t) x)
#define zext_i8_i8(x) ((uint8_t) (uint8_t) x)
#define zext_i8_i16(x) ((uint16_t) (uint8_t) x)
#define zext_i8_i32(x) ((uint32_t) (uint8_t) x)
#define zext_i8_i64(x) ((uint64_t) (uint8_t) x)
#define zext_i16_i8(x) ((uint8_t) (uint16_t) x)
#define zext_i16_i16(x) ((uint16_t) (uint16_t) x)
#define zext_i16_i32(x) ((uint32_t) (uint16_t) x)
#define zext_i16_i64(x) ((uint64_t) (uint16_t) x)
#define zext_i32_i8(x) ((uint8_t) (uint32_t) x)
#define zext_i32_i16(x) ((uint16_t) (uint32_t) x)
#define zext_i32_i32(x) ((uint32_t) (uint32_t) x)
#define zext_i32_i64(x) ((uint64_t) (uint32_t) x)
#define zext_i64_i8(x) ((uint8_t) (uint64_t) x)
#define zext_i64_i16(x) ((uint16_t) (uint64_t) x)
#define zext_i64_i32(x) ((uint32_t) (uint64_t) x)
#define zext_i64_i64(x) ((uint64_t) (uint64_t) x)
#ifdef __OPENCL_VERSION__
int32_t futrts_popc8(int8_t x)
{
    return popcount(x);
}
int32_t futrts_popc16(int16_t x)
{
    return popcount(x);
}
int32_t futrts_popc32(int32_t x)
{
    return popcount(x);
}
int32_t futrts_popc64(int64_t x)
{
    return popcount(x);
}
#elif __CUDA_ARCH__
int32_t futrts_popc8(int8_t x)
{
    return __popc(zext_i8_i32(x));
}
int32_t futrts_popc16(int16_t x)
{
    return __popc(zext_i16_i32(x));
}
int32_t futrts_popc32(int32_t x)
{
    return __popc(x);
}
int32_t futrts_popc64(int64_t x)
{
    return __popcll(x);
}
#else
int32_t futrts_popc8(int8_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
int32_t futrts_popc16(int16_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
int32_t futrts_popc32(int32_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
int32_t futrts_popc64(int64_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
#endif
#ifdef __OPENCL_VERSION__
int32_t futrts_clzz8(int8_t x)
{
    return clz(x);
}
int32_t futrts_clzz16(int16_t x)
{
    return clz(x);
}
int32_t futrts_clzz32(int32_t x)
{
    return clz(x);
}
int32_t futrts_clzz64(int64_t x)
{
    return clz(x);
}
#elif __CUDA_ARCH__
int32_t futrts_clzz8(int8_t x)
{
    return __clz(zext_i8_i32(x)) - 24;
}
int32_t futrts_clzz16(int16_t x)
{
    return __clz(zext_i16_i32(x)) - 16;
}
int32_t futrts_clzz32(int32_t x)
{
    return __clz(x);
}
int32_t futrts_clzz64(int64_t x)
{
    return __clzll(x);
}
#else
int32_t futrts_clzz8(int8_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
int32_t futrts_clzz16(int16_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
int32_t futrts_clzz32(int32_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
int32_t futrts_clzz64(int64_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
#endif
static inline float fdiv32(float x, float y)
{
    return x / y;
}
static inline float fadd32(float x, float y)
{
    return x + y;
}
static inline float fsub32(float x, float y)
{
    return x - y;
}
static inline float fmul32(float x, float y)
{
    return x * y;
}
static inline float fmin32(float x, float y)
{
    return fmin(x, y);
}
static inline float fmax32(float x, float y)
{
    return fmax(x, y);
}
static inline float fpow32(float x, float y)
{
    return pow(x, y);
}
static inline char cmplt32(float x, float y)
{
    return x < y;
}
static inline char cmple32(float x, float y)
{
    return x <= y;
}
static inline float sitofp_i8_f32(int8_t x)
{
    return x;
}
static inline float sitofp_i16_f32(int16_t x)
{
    return x;
}
static inline float sitofp_i32_f32(int32_t x)
{
    return x;
}
static inline float sitofp_i64_f32(int64_t x)
{
    return x;
}
static inline float uitofp_i8_f32(uint8_t x)
{
    return x;
}
static inline float uitofp_i16_f32(uint16_t x)
{
    return x;
}
static inline float uitofp_i32_f32(uint32_t x)
{
    return x;
}
static inline float uitofp_i64_f32(uint64_t x)
{
    return x;
}
static inline int8_t fptosi_f32_i8(float x)
{
    return x;
}
static inline int16_t fptosi_f32_i16(float x)
{
    return x;
}
static inline int32_t fptosi_f32_i32(float x)
{
    return x;
}
static inline int64_t fptosi_f32_i64(float x)
{
    return x;
}
static inline uint8_t fptoui_f32_i8(float x)
{
    return x;
}
static inline uint16_t fptoui_f32_i16(float x)
{
    return x;
}
static inline uint32_t fptoui_f32_i32(float x)
{
    return x;
}
static inline uint64_t fptoui_f32_i64(float x)
{
    return x;
}
static inline float futrts_log32(float x)
{
    return log(x);
}
static inline float futrts_log2_32(float x)
{
    return log2(x);
}
static inline float futrts_log10_32(float x)
{
    return log10(x);
}
static inline float futrts_sqrt32(float x)
{
    return sqrt(x);
}
static inline float futrts_exp32(float x)
{
    return exp(x);
}
static inline float futrts_cos32(float x)
{
    return cos(x);
}
static inline float futrts_sin32(float x)
{
    return sin(x);
}
static inline float futrts_tan32(float x)
{
    return tan(x);
}
static inline float futrts_acos32(float x)
{
    return acos(x);
}
static inline float futrts_asin32(float x)
{
    return asin(x);
}
static inline float futrts_atan32(float x)
{
    return atan(x);
}
static inline float futrts_atan2_32(float x, float y)
{
    return atan2(x, y);
}
static inline float futrts_gamma32(float x)
{
    return tgamma(x);
}
static inline float futrts_lgamma32(float x)
{
    return lgamma(x);
}
static inline char futrts_isnan32(float x)
{
    return isnan(x);
}
static inline char futrts_isinf32(float x)
{
    return isinf(x);
}
static inline int32_t futrts_to_bits32(float x)
{
    union {
        float f;
        int32_t t;
    } p;
    
    p.f = x;
    return p.t;
}
static inline float futrts_from_bits32(int32_t x)
{
    union {
        int32_t f;
        float t;
    } p;
    
    p.f = x;
    return p.t;
}
#ifdef __OPENCL_VERSION__
static inline float fmod32(float x, float y)
{
    return fmod(x, y);
}
static inline float futrts_round32(float x)
{
    return rint(x);
}
static inline float futrts_floor32(float x)
{
    return floor(x);
}
static inline float futrts_ceil32(float x)
{
    return ceil(x);
}
static inline float futrts_lerp32(float v0, float v1, float t)
{
    return mix(v0, v1, t);
}
#else
static inline float fmod32(float x, float y)
{
    return fmodf(x, y);
}
static inline float futrts_round32(float x)
{
    return rintf(x);
}
static inline float futrts_floor32(float x)
{
    return floorf(x);
}
static inline float futrts_ceil32(float x)
{
    return ceilf(x);
}
static inline float futrts_lerp32(float v0, float v1, float t)
{
    return v0 + (v1 - v0) * t;
}
#endif
static inline double fdiv64(double x, double y)
{
    return x / y;
}
static inline double fadd64(double x, double y)
{
    return x + y;
}
static inline double fsub64(double x, double y)
{
    return x - y;
}
static inline double fmul64(double x, double y)
{
    return x * y;
}
static inline double fmin64(double x, double y)
{
    return fmin(x, y);
}
static inline double fmax64(double x, double y)
{
    return fmax(x, y);
}
static inline double fpow64(double x, double y)
{
    return pow(x, y);
}
static inline char cmplt64(double x, double y)
{
    return x < y;
}
static inline char cmple64(double x, double y)
{
    return x <= y;
}
static inline double sitofp_i8_f64(int8_t x)
{
    return x;
}
static inline double sitofp_i16_f64(int16_t x)
{
    return x;
}
static inline double sitofp_i32_f64(int32_t x)
{
    return x;
}
static inline double sitofp_i64_f64(int64_t x)
{
    return x;
}
static inline double uitofp_i8_f64(uint8_t x)
{
    return x;
}
static inline double uitofp_i16_f64(uint16_t x)
{
    return x;
}
static inline double uitofp_i32_f64(uint32_t x)
{
    return x;
}
static inline double uitofp_i64_f64(uint64_t x)
{
    return x;
}
static inline int8_t fptosi_f64_i8(double x)
{
    return x;
}
static inline int16_t fptosi_f64_i16(double x)
{
    return x;
}
static inline int32_t fptosi_f64_i32(double x)
{
    return x;
}
static inline int64_t fptosi_f64_i64(double x)
{
    return x;
}
static inline uint8_t fptoui_f64_i8(double x)
{
    return x;
}
static inline uint16_t fptoui_f64_i16(double x)
{
    return x;
}
static inline uint32_t fptoui_f64_i32(double x)
{
    return x;
}
static inline uint64_t fptoui_f64_i64(double x)
{
    return x;
}
static inline double futrts_log64(double x)
{
    return log(x);
}
static inline double futrts_log2_64(double x)
{
    return log2(x);
}
static inline double futrts_log10_64(double x)
{
    return log10(x);
}
static inline double futrts_sqrt64(double x)
{
    return sqrt(x);
}
static inline double futrts_exp64(double x)
{
    return exp(x);
}
static inline double futrts_cos64(double x)
{
    return cos(x);
}
static inline double futrts_sin64(double x)
{
    return sin(x);
}
static inline double futrts_tan64(double x)
{
    return tan(x);
}
static inline double futrts_acos64(double x)
{
    return acos(x);
}
static inline double futrts_asin64(double x)
{
    return asin(x);
}
static inline double futrts_atan64(double x)
{
    return atan(x);
}
static inline double futrts_atan2_64(double x, double y)
{
    return atan2(x, y);
}
static inline double futrts_gamma64(double x)
{
    return tgamma(x);
}
static inline double futrts_lgamma64(double x)
{
    return lgamma(x);
}
static inline double futrts_round64(double x)
{
    return rint(x);
}
static inline double futrts_ceil64(double x)
{
    return ceil(x);
}
static inline double futrts_floor64(double x)
{
    return floor(x);
}
static inline char futrts_isnan64(double x)
{
    return isnan(x);
}
static inline char futrts_isinf64(double x)
{
    return isinf(x);
}
static inline int64_t futrts_to_bits64(double x)
{
    union {
        double f;
        int64_t t;
    } p;
    
    p.f = x;
    return p.t;
}
static inline double futrts_from_bits64(int64_t x)
{
    union {
        int64_t f;
        double t;
    } p;
    
    p.f = x;
    return p.t;
}
static inline float fmod64(float x, float y)
{
    return fmod(x, y);
}
#ifdef __OPENCL_VERSION__
static inline double futrts_lerp64(double v0, double v1, double t)
{
    return mix(v0, v1, t);
}
#else
static inline double futrts_lerp64(double v0, double v1, double t)
{
    return v0 + (v1 - v0) * t;
}
#endif
static inline float fpconv_f32_f32(float x)
{
    return x;
}
static inline double fpconv_f32_f64(float x)
{
    return x;
}
static inline float fpconv_f64_f32(double x)
{
    return x;
}
static inline double fpconv_f64_f64(double x)
{
    return x;
}
__kernel void segred_nonseg_7309(__local volatile
                                 int64_t *sync_arr_mem_7510_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7512_backing_aligned_1,
                                 int32_t sizze_7143, int32_t num_groups_7304,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7460, __global
                                 unsigned char *counter_mem_7500, __global
                                 unsigned char *group_res_arr_mem_7502,
                                 int32_t num_threads_7504)
{
    const int32_t segred_group_sizze_7302 =
                  entropy_f64zisegred_group_sizze_7301;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7510_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7510_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7512_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7512_backing_aligned_1;
    int32_t global_tid_7505;
    int32_t local_tid_7506;
    int32_t group_sizze_7509;
    int32_t wave_sizze_7508;
    int32_t group_tid_7507;
    
    global_tid_7505 = get_global_id(0);
    local_tid_7506 = get_local_id(0);
    group_sizze_7509 = get_local_size(0);
    wave_sizze_7508 = LOCKSTEP_WIDTH;
    group_tid_7507 = get_group_id(0);
    
    int32_t phys_tid_7309 = global_tid_7505;
    __local char *sync_arr_mem_7510;
    
    sync_arr_mem_7510 = (__local char *) sync_arr_mem_7510_backing_0;
    
    __local char *red_arr_mem_7512;
    
    red_arr_mem_7512 = (__local char *) red_arr_mem_7512_backing_1;
    
    int32_t dummy_7307 = 0;
    int32_t gtid_7308;
    
    gtid_7308 = 0;
    
    double x_acc_7514;
    int32_t chunk_sizze_7515 = smin32(squot32(sizze_7143 +
                                              segred_group_sizze_7302 *
                                              num_groups_7304 - 1,
                                              segred_group_sizze_7302 *
                                              num_groups_7304),
                                      squot32(sizze_7143 - phys_tid_7309 +
                                              num_threads_7504 - 1,
                                              num_threads_7504));
    double x_7146;
    double x_7147;
    
    // neutral-initialise the accumulators
    {
        x_acc_7514 = 0.0;
    }
    for (int32_t i_7519 = 0; i_7519 < chunk_sizze_7515; i_7519++) {
        gtid_7308 = phys_tid_7309 + num_threads_7504 * i_7519;
        // apply map function
        {
            double x_7149 = ((__global double *) x_mem_7456)[gtid_7308];
            double res_7150;
            
            res_7150 = futrts_log64(x_7149);
            
            double res_7151 = x_7149 * res_7150;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7146 = x_acc_7514;
            }
            // load new values
            {
                x_7147 = res_7151;
            }
            // apply reduction operator
            {
                double res_7148 = x_7146 + x_7147;
                
                // store in accumulator
                {
                    x_acc_7514 = res_7148;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7146 = x_acc_7514;
        ((__local double *) red_arr_mem_7512)[local_tid_7506] = x_7146;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7520;
    int32_t skip_waves_7521;
    double x_7516;
    double x_7517;
    
    offset_7520 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7506, segred_group_sizze_7302)) {
            x_7516 = ((__local double *) red_arr_mem_7512)[local_tid_7506 +
                                                           offset_7520];
        }
    }
    offset_7520 = 1;
    while (slt32(offset_7520, wave_sizze_7508)) {
        if (slt32(local_tid_7506 + offset_7520, segred_group_sizze_7302) &&
            ((local_tid_7506 - squot32(local_tid_7506, wave_sizze_7508) *
              wave_sizze_7508) & (2 * offset_7520 - 1)) == 0) {
            // read array element
            {
                x_7517 = ((volatile __local
                           double *) red_arr_mem_7512)[local_tid_7506 +
                                                       offset_7520];
            }
            // apply reduction operation
            {
                double res_7518 = x_7516 + x_7517;
                
                x_7516 = res_7518;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_7512)[local_tid_7506] =
                    x_7516;
            }
        }
        offset_7520 *= 2;
    }
    skip_waves_7521 = 1;
    while (slt32(skip_waves_7521, squot32(segred_group_sizze_7302 +
                                          wave_sizze_7508 - 1,
                                          wave_sizze_7508))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7520 = skip_waves_7521 * wave_sizze_7508;
        if (slt32(local_tid_7506 + offset_7520, segred_group_sizze_7302) &&
            ((local_tid_7506 - squot32(local_tid_7506, wave_sizze_7508) *
              wave_sizze_7508) == 0 && (squot32(local_tid_7506,
                                                wave_sizze_7508) & (2 *
                                                                    skip_waves_7521 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7517 = ((__local double *) red_arr_mem_7512)[local_tid_7506 +
                                                               offset_7520];
            }
            // apply reduction operation
            {
                double res_7518 = x_7516 + x_7517;
                
                x_7516 = res_7518;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_7512)[local_tid_7506] = x_7516;
            }
        }
        skip_waves_7521 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7506 == 0) {
            x_acc_7514 = x_7516;
        }
    }
    
    int32_t old_counter_7522;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7506 == 0) {
            ((__global double *) group_res_arr_mem_7502)[group_tid_7507 *
                                                         segred_group_sizze_7302] =
                x_acc_7514;
            mem_fence_global();
            old_counter_7522 = atomic_add(&((volatile __global
                                             int *) counter_mem_7500)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7510)[0] = old_counter_7522 ==
                num_groups_7304 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7523 = ((__local bool *) sync_arr_mem_7510)[0];
    
    if (is_last_group_7523) {
        if (local_tid_7506 == 0) {
            old_counter_7522 = atomic_add(&((volatile __global
                                             int *) counter_mem_7500)[0],
                                          (int) (0 - num_groups_7304));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7506, num_groups_7304)) {
                x_7146 = ((__global
                           double *) group_res_arr_mem_7502)[local_tid_7506 *
                                                             segred_group_sizze_7302];
            } else {
                x_7146 = 0.0;
            }
            ((__local double *) red_arr_mem_7512)[local_tid_7506] = x_7146;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7524;
            int32_t skip_waves_7525;
            double x_7516;
            double x_7517;
            
            offset_7524 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7506, segred_group_sizze_7302)) {
                    x_7516 = ((__local
                               double *) red_arr_mem_7512)[local_tid_7506 +
                                                           offset_7524];
                }
            }
            offset_7524 = 1;
            while (slt32(offset_7524, wave_sizze_7508)) {
                if (slt32(local_tid_7506 + offset_7524,
                          segred_group_sizze_7302) && ((local_tid_7506 -
                                                        squot32(local_tid_7506,
                                                                wave_sizze_7508) *
                                                        wave_sizze_7508) & (2 *
                                                                            offset_7524 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7517 = ((volatile __local
                                   double *) red_arr_mem_7512)[local_tid_7506 +
                                                               offset_7524];
                    }
                    // apply reduction operation
                    {
                        double res_7518 = x_7516 + x_7517;
                        
                        x_7516 = res_7518;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_7512)[local_tid_7506] = x_7516;
                    }
                }
                offset_7524 *= 2;
            }
            skip_waves_7525 = 1;
            while (slt32(skip_waves_7525, squot32(segred_group_sizze_7302 +
                                                  wave_sizze_7508 - 1,
                                                  wave_sizze_7508))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7524 = skip_waves_7525 * wave_sizze_7508;
                if (slt32(local_tid_7506 + offset_7524,
                          segred_group_sizze_7302) && ((local_tid_7506 -
                                                        squot32(local_tid_7506,
                                                                wave_sizze_7508) *
                                                        wave_sizze_7508) == 0 &&
                                                       (squot32(local_tid_7506,
                                                                wave_sizze_7508) &
                                                        (2 * skip_waves_7525 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7517 = ((__local
                                   double *) red_arr_mem_7512)[local_tid_7506 +
                                                               offset_7524];
                    }
                    // apply reduction operation
                    {
                        double res_7518 = x_7516 + x_7517;
                        
                        x_7516 = res_7518;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_7512)[local_tid_7506] =
                            x_7516;
                    }
                }
                skip_waves_7525 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7506 == 0) {
                    ((__global double *) mem_7460)[0] = x_7516;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7320(__local volatile
                                 int64_t *sync_arr_mem_7538_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7540_backing_aligned_1,
                                 int32_t sizze_7153, int32_t num_groups_7315,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7460, __global
                                 unsigned char *counter_mem_7528, __global
                                 unsigned char *group_res_arr_mem_7530,
                                 int32_t num_threads_7532)
{
    const int32_t segred_group_sizze_7313 =
                  entropy_f32zisegred_group_sizze_7312;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7538_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7538_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7540_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7540_backing_aligned_1;
    int32_t global_tid_7533;
    int32_t local_tid_7534;
    int32_t group_sizze_7537;
    int32_t wave_sizze_7536;
    int32_t group_tid_7535;
    
    global_tid_7533 = get_global_id(0);
    local_tid_7534 = get_local_id(0);
    group_sizze_7537 = get_local_size(0);
    wave_sizze_7536 = LOCKSTEP_WIDTH;
    group_tid_7535 = get_group_id(0);
    
    int32_t phys_tid_7320 = global_tid_7533;
    __local char *sync_arr_mem_7538;
    
    sync_arr_mem_7538 = (__local char *) sync_arr_mem_7538_backing_0;
    
    __local char *red_arr_mem_7540;
    
    red_arr_mem_7540 = (__local char *) red_arr_mem_7540_backing_1;
    
    int32_t dummy_7318 = 0;
    int32_t gtid_7319;
    
    gtid_7319 = 0;
    
    float x_acc_7542;
    int32_t chunk_sizze_7543 = smin32(squot32(sizze_7153 +
                                              segred_group_sizze_7313 *
                                              num_groups_7315 - 1,
                                              segred_group_sizze_7313 *
                                              num_groups_7315),
                                      squot32(sizze_7153 - phys_tid_7320 +
                                              num_threads_7532 - 1,
                                              num_threads_7532));
    float x_7156;
    float x_7157;
    
    // neutral-initialise the accumulators
    {
        x_acc_7542 = 0.0F;
    }
    for (int32_t i_7547 = 0; i_7547 < chunk_sizze_7543; i_7547++) {
        gtid_7319 = phys_tid_7320 + num_threads_7532 * i_7547;
        // apply map function
        {
            float x_7159 = ((__global float *) x_mem_7456)[gtid_7319];
            float res_7160;
            
            res_7160 = futrts_log32(x_7159);
            
            float res_7161 = x_7159 * res_7160;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7156 = x_acc_7542;
            }
            // load new values
            {
                x_7157 = res_7161;
            }
            // apply reduction operator
            {
                float res_7158 = x_7156 + x_7157;
                
                // store in accumulator
                {
                    x_acc_7542 = res_7158;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7156 = x_acc_7542;
        ((__local float *) red_arr_mem_7540)[local_tid_7534] = x_7156;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7548;
    int32_t skip_waves_7549;
    float x_7544;
    float x_7545;
    
    offset_7548 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7534, segred_group_sizze_7313)) {
            x_7544 = ((__local float *) red_arr_mem_7540)[local_tid_7534 +
                                                          offset_7548];
        }
    }
    offset_7548 = 1;
    while (slt32(offset_7548, wave_sizze_7536)) {
        if (slt32(local_tid_7534 + offset_7548, segred_group_sizze_7313) &&
            ((local_tid_7534 - squot32(local_tid_7534, wave_sizze_7536) *
              wave_sizze_7536) & (2 * offset_7548 - 1)) == 0) {
            // read array element
            {
                x_7545 = ((volatile __local
                           float *) red_arr_mem_7540)[local_tid_7534 +
                                                      offset_7548];
            }
            // apply reduction operation
            {
                float res_7546 = x_7544 + x_7545;
                
                x_7544 = res_7546;
            }
            // write result of operation
            {
                ((volatile __local float *) red_arr_mem_7540)[local_tid_7534] =
                    x_7544;
            }
        }
        offset_7548 *= 2;
    }
    skip_waves_7549 = 1;
    while (slt32(skip_waves_7549, squot32(segred_group_sizze_7313 +
                                          wave_sizze_7536 - 1,
                                          wave_sizze_7536))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7548 = skip_waves_7549 * wave_sizze_7536;
        if (slt32(local_tid_7534 + offset_7548, segred_group_sizze_7313) &&
            ((local_tid_7534 - squot32(local_tid_7534, wave_sizze_7536) *
              wave_sizze_7536) == 0 && (squot32(local_tid_7534,
                                                wave_sizze_7536) & (2 *
                                                                    skip_waves_7549 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7545 = ((__local float *) red_arr_mem_7540)[local_tid_7534 +
                                                              offset_7548];
            }
            // apply reduction operation
            {
                float res_7546 = x_7544 + x_7545;
                
                x_7544 = res_7546;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_7540)[local_tid_7534] = x_7544;
            }
        }
        skip_waves_7549 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7534 == 0) {
            x_acc_7542 = x_7544;
        }
    }
    
    int32_t old_counter_7550;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7534 == 0) {
            ((__global float *) group_res_arr_mem_7530)[group_tid_7535 *
                                                        segred_group_sizze_7313] =
                x_acc_7542;
            mem_fence_global();
            old_counter_7550 = atomic_add(&((volatile __global
                                             int *) counter_mem_7528)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7538)[0] = old_counter_7550 ==
                num_groups_7315 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7551 = ((__local bool *) sync_arr_mem_7538)[0];
    
    if (is_last_group_7551) {
        if (local_tid_7534 == 0) {
            old_counter_7550 = atomic_add(&((volatile __global
                                             int *) counter_mem_7528)[0],
                                          (int) (0 - num_groups_7315));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7534, num_groups_7315)) {
                x_7156 = ((__global
                           float *) group_res_arr_mem_7530)[local_tid_7534 *
                                                            segred_group_sizze_7313];
            } else {
                x_7156 = 0.0F;
            }
            ((__local float *) red_arr_mem_7540)[local_tid_7534] = x_7156;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7552;
            int32_t skip_waves_7553;
            float x_7544;
            float x_7545;
            
            offset_7552 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7534, segred_group_sizze_7313)) {
                    x_7544 = ((__local
                               float *) red_arr_mem_7540)[local_tid_7534 +
                                                          offset_7552];
                }
            }
            offset_7552 = 1;
            while (slt32(offset_7552, wave_sizze_7536)) {
                if (slt32(local_tid_7534 + offset_7552,
                          segred_group_sizze_7313) && ((local_tid_7534 -
                                                        squot32(local_tid_7534,
                                                                wave_sizze_7536) *
                                                        wave_sizze_7536) & (2 *
                                                                            offset_7552 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7545 = ((volatile __local
                                   float *) red_arr_mem_7540)[local_tid_7534 +
                                                              offset_7552];
                    }
                    // apply reduction operation
                    {
                        float res_7546 = x_7544 + x_7545;
                        
                        x_7544 = res_7546;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_7540)[local_tid_7534] = x_7544;
                    }
                }
                offset_7552 *= 2;
            }
            skip_waves_7553 = 1;
            while (slt32(skip_waves_7553, squot32(segred_group_sizze_7313 +
                                                  wave_sizze_7536 - 1,
                                                  wave_sizze_7536))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7552 = skip_waves_7553 * wave_sizze_7536;
                if (slt32(local_tid_7534 + offset_7552,
                          segred_group_sizze_7313) && ((local_tid_7534 -
                                                        squot32(local_tid_7534,
                                                                wave_sizze_7536) *
                                                        wave_sizze_7536) == 0 &&
                                                       (squot32(local_tid_7534,
                                                                wave_sizze_7536) &
                                                        (2 * skip_waves_7553 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7545 = ((__local
                                   float *) red_arr_mem_7540)[local_tid_7534 +
                                                              offset_7552];
                    }
                    // apply reduction operation
                    {
                        float res_7546 = x_7544 + x_7545;
                        
                        x_7544 = res_7546;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_7540)[local_tid_7534] =
                            x_7544;
                    }
                }
                skip_waves_7553 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7534 == 0) {
                    ((__global float *) mem_7460)[0] = x_7544;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7331(__local volatile
                                 int64_t *sync_arr_mem_7566_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7568_backing_aligned_1,
                                 int32_t sizze_7163, int32_t num_groups_7326,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7460, __global
                                 unsigned char *counter_mem_7556, __global
                                 unsigned char *group_res_arr_mem_7558,
                                 int32_t num_threads_7560)
{
    const int32_t segred_group_sizze_7324 =
                  entropy_scaled_f64zisegred_group_sizze_7323;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7566_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7566_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7568_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7568_backing_aligned_1;
    int32_t global_tid_7561;
    int32_t local_tid_7562;
    int32_t group_sizze_7565;
    int32_t wave_sizze_7564;
    int32_t group_tid_7563;
    
    global_tid_7561 = get_global_id(0);
    local_tid_7562 = get_local_id(0);
    group_sizze_7565 = get_local_size(0);
    wave_sizze_7564 = LOCKSTEP_WIDTH;
    group_tid_7563 = get_group_id(0);
    
    int32_t phys_tid_7331 = global_tid_7561;
    __local char *sync_arr_mem_7566;
    
    sync_arr_mem_7566 = (__local char *) sync_arr_mem_7566_backing_0;
    
    __local char *red_arr_mem_7568;
    
    red_arr_mem_7568 = (__local char *) red_arr_mem_7568_backing_1;
    
    int32_t dummy_7329 = 0;
    int32_t gtid_7330;
    
    gtid_7330 = 0;
    
    double x_acc_7570;
    int32_t chunk_sizze_7571 = smin32(squot32(sizze_7163 +
                                              segred_group_sizze_7324 *
                                              num_groups_7326 - 1,
                                              segred_group_sizze_7324 *
                                              num_groups_7326),
                                      squot32(sizze_7163 - phys_tid_7331 +
                                              num_threads_7560 - 1,
                                              num_threads_7560));
    double x_7166;
    double x_7167;
    
    // neutral-initialise the accumulators
    {
        x_acc_7570 = 0.0;
    }
    for (int32_t i_7575 = 0; i_7575 < chunk_sizze_7571; i_7575++) {
        gtid_7330 = phys_tid_7331 + num_threads_7560 * i_7575;
        // apply map function
        {
            double x_7169 = ((__global double *) x_mem_7456)[gtid_7330];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7166 = x_acc_7570;
            }
            // load new values
            {
                x_7167 = x_7169;
            }
            // apply reduction operator
            {
                double res_7168 = x_7166 + x_7167;
                
                // store in accumulator
                {
                    x_acc_7570 = res_7168;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7166 = x_acc_7570;
        ((__local double *) red_arr_mem_7568)[local_tid_7562] = x_7166;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7576;
    int32_t skip_waves_7577;
    double x_7572;
    double x_7573;
    
    offset_7576 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7562, segred_group_sizze_7324)) {
            x_7572 = ((__local double *) red_arr_mem_7568)[local_tid_7562 +
                                                           offset_7576];
        }
    }
    offset_7576 = 1;
    while (slt32(offset_7576, wave_sizze_7564)) {
        if (slt32(local_tid_7562 + offset_7576, segred_group_sizze_7324) &&
            ((local_tid_7562 - squot32(local_tid_7562, wave_sizze_7564) *
              wave_sizze_7564) & (2 * offset_7576 - 1)) == 0) {
            // read array element
            {
                x_7573 = ((volatile __local
                           double *) red_arr_mem_7568)[local_tid_7562 +
                                                       offset_7576];
            }
            // apply reduction operation
            {
                double res_7574 = x_7572 + x_7573;
                
                x_7572 = res_7574;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_7568)[local_tid_7562] =
                    x_7572;
            }
        }
        offset_7576 *= 2;
    }
    skip_waves_7577 = 1;
    while (slt32(skip_waves_7577, squot32(segred_group_sizze_7324 +
                                          wave_sizze_7564 - 1,
                                          wave_sizze_7564))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7576 = skip_waves_7577 * wave_sizze_7564;
        if (slt32(local_tid_7562 + offset_7576, segred_group_sizze_7324) &&
            ((local_tid_7562 - squot32(local_tid_7562, wave_sizze_7564) *
              wave_sizze_7564) == 0 && (squot32(local_tid_7562,
                                                wave_sizze_7564) & (2 *
                                                                    skip_waves_7577 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7573 = ((__local double *) red_arr_mem_7568)[local_tid_7562 +
                                                               offset_7576];
            }
            // apply reduction operation
            {
                double res_7574 = x_7572 + x_7573;
                
                x_7572 = res_7574;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_7568)[local_tid_7562] = x_7572;
            }
        }
        skip_waves_7577 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7562 == 0) {
            x_acc_7570 = x_7572;
        }
    }
    
    int32_t old_counter_7578;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7562 == 0) {
            ((__global double *) group_res_arr_mem_7558)[group_tid_7563 *
                                                         segred_group_sizze_7324] =
                x_acc_7570;
            mem_fence_global();
            old_counter_7578 = atomic_add(&((volatile __global
                                             int *) counter_mem_7556)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7566)[0] = old_counter_7578 ==
                num_groups_7326 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7579 = ((__local bool *) sync_arr_mem_7566)[0];
    
    if (is_last_group_7579) {
        if (local_tid_7562 == 0) {
            old_counter_7578 = atomic_add(&((volatile __global
                                             int *) counter_mem_7556)[0],
                                          (int) (0 - num_groups_7326));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7562, num_groups_7326)) {
                x_7166 = ((__global
                           double *) group_res_arr_mem_7558)[local_tid_7562 *
                                                             segred_group_sizze_7324];
            } else {
                x_7166 = 0.0;
            }
            ((__local double *) red_arr_mem_7568)[local_tid_7562] = x_7166;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7580;
            int32_t skip_waves_7581;
            double x_7572;
            double x_7573;
            
            offset_7580 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7562, segred_group_sizze_7324)) {
                    x_7572 = ((__local
                               double *) red_arr_mem_7568)[local_tid_7562 +
                                                           offset_7580];
                }
            }
            offset_7580 = 1;
            while (slt32(offset_7580, wave_sizze_7564)) {
                if (slt32(local_tid_7562 + offset_7580,
                          segred_group_sizze_7324) && ((local_tid_7562 -
                                                        squot32(local_tid_7562,
                                                                wave_sizze_7564) *
                                                        wave_sizze_7564) & (2 *
                                                                            offset_7580 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7573 = ((volatile __local
                                   double *) red_arr_mem_7568)[local_tid_7562 +
                                                               offset_7580];
                    }
                    // apply reduction operation
                    {
                        double res_7574 = x_7572 + x_7573;
                        
                        x_7572 = res_7574;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_7568)[local_tid_7562] = x_7572;
                    }
                }
                offset_7580 *= 2;
            }
            skip_waves_7581 = 1;
            while (slt32(skip_waves_7581, squot32(segred_group_sizze_7324 +
                                                  wave_sizze_7564 - 1,
                                                  wave_sizze_7564))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7580 = skip_waves_7581 * wave_sizze_7564;
                if (slt32(local_tid_7562 + offset_7580,
                          segred_group_sizze_7324) && ((local_tid_7562 -
                                                        squot32(local_tid_7562,
                                                                wave_sizze_7564) *
                                                        wave_sizze_7564) == 0 &&
                                                       (squot32(local_tid_7562,
                                                                wave_sizze_7564) &
                                                        (2 * skip_waves_7581 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7573 = ((__local
                                   double *) red_arr_mem_7568)[local_tid_7562 +
                                                               offset_7580];
                    }
                    // apply reduction operation
                    {
                        double res_7574 = x_7572 + x_7573;
                        
                        x_7572 = res_7574;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_7568)[local_tid_7562] =
                            x_7572;
                    }
                }
                skip_waves_7581 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7562 == 0) {
                    ((__global double *) mem_7460)[0] = x_7572;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7342(__local volatile
                                 int64_t *sync_arr_mem_7593_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7595_backing_aligned_1,
                                 int32_t sizze_7163, double res_7165,
                                 int32_t num_groups_7337, __global
                                 unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7464, __global
                                 unsigned char *counter_mem_7583, __global
                                 unsigned char *group_res_arr_mem_7585,
                                 int32_t num_threads_7587)
{
    const int32_t segred_group_sizze_7335 =
                  entropy_scaled_f64zisegred_group_sizze_7334;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7593_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7593_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7595_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7595_backing_aligned_1;
    int32_t global_tid_7588;
    int32_t local_tid_7589;
    int32_t group_sizze_7592;
    int32_t wave_sizze_7591;
    int32_t group_tid_7590;
    
    global_tid_7588 = get_global_id(0);
    local_tid_7589 = get_local_id(0);
    group_sizze_7592 = get_local_size(0);
    wave_sizze_7591 = LOCKSTEP_WIDTH;
    group_tid_7590 = get_group_id(0);
    
    int32_t phys_tid_7342 = global_tid_7588;
    __local char *sync_arr_mem_7593;
    
    sync_arr_mem_7593 = (__local char *) sync_arr_mem_7593_backing_0;
    
    __local char *red_arr_mem_7595;
    
    red_arr_mem_7595 = (__local char *) red_arr_mem_7595_backing_1;
    
    int32_t dummy_7340 = 0;
    int32_t gtid_7341;
    
    gtid_7341 = 0;
    
    double x_acc_7597;
    int32_t chunk_sizze_7598 = smin32(squot32(sizze_7163 +
                                              segred_group_sizze_7335 *
                                              num_groups_7337 - 1,
                                              segred_group_sizze_7335 *
                                              num_groups_7337),
                                      squot32(sizze_7163 - phys_tid_7342 +
                                              num_threads_7587 - 1,
                                              num_threads_7587));
    double x_7171;
    double x_7172;
    
    // neutral-initialise the accumulators
    {
        x_acc_7597 = 0.0;
    }
    for (int32_t i_7602 = 0; i_7602 < chunk_sizze_7598; i_7602++) {
        gtid_7341 = phys_tid_7342 + num_threads_7587 * i_7602;
        // apply map function
        {
            double x_7174 = ((__global double *) x_mem_7456)[gtid_7341];
            double res_7175 = x_7174 / res_7165;
            double res_7176;
            
            res_7176 = futrts_log64(res_7175);
            
            double res_7177 = res_7175 * res_7176;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7171 = x_acc_7597;
            }
            // load new values
            {
                x_7172 = res_7177;
            }
            // apply reduction operator
            {
                double res_7173 = x_7171 + x_7172;
                
                // store in accumulator
                {
                    x_acc_7597 = res_7173;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7171 = x_acc_7597;
        ((__local double *) red_arr_mem_7595)[local_tid_7589] = x_7171;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7603;
    int32_t skip_waves_7604;
    double x_7599;
    double x_7600;
    
    offset_7603 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7589, segred_group_sizze_7335)) {
            x_7599 = ((__local double *) red_arr_mem_7595)[local_tid_7589 +
                                                           offset_7603];
        }
    }
    offset_7603 = 1;
    while (slt32(offset_7603, wave_sizze_7591)) {
        if (slt32(local_tid_7589 + offset_7603, segred_group_sizze_7335) &&
            ((local_tid_7589 - squot32(local_tid_7589, wave_sizze_7591) *
              wave_sizze_7591) & (2 * offset_7603 - 1)) == 0) {
            // read array element
            {
                x_7600 = ((volatile __local
                           double *) red_arr_mem_7595)[local_tid_7589 +
                                                       offset_7603];
            }
            // apply reduction operation
            {
                double res_7601 = x_7599 + x_7600;
                
                x_7599 = res_7601;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_7595)[local_tid_7589] =
                    x_7599;
            }
        }
        offset_7603 *= 2;
    }
    skip_waves_7604 = 1;
    while (slt32(skip_waves_7604, squot32(segred_group_sizze_7335 +
                                          wave_sizze_7591 - 1,
                                          wave_sizze_7591))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7603 = skip_waves_7604 * wave_sizze_7591;
        if (slt32(local_tid_7589 + offset_7603, segred_group_sizze_7335) &&
            ((local_tid_7589 - squot32(local_tid_7589, wave_sizze_7591) *
              wave_sizze_7591) == 0 && (squot32(local_tid_7589,
                                                wave_sizze_7591) & (2 *
                                                                    skip_waves_7604 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7600 = ((__local double *) red_arr_mem_7595)[local_tid_7589 +
                                                               offset_7603];
            }
            // apply reduction operation
            {
                double res_7601 = x_7599 + x_7600;
                
                x_7599 = res_7601;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_7595)[local_tid_7589] = x_7599;
            }
        }
        skip_waves_7604 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7589 == 0) {
            x_acc_7597 = x_7599;
        }
    }
    
    int32_t old_counter_7605;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7589 == 0) {
            ((__global double *) group_res_arr_mem_7585)[group_tid_7590 *
                                                         segred_group_sizze_7335] =
                x_acc_7597;
            mem_fence_global();
            old_counter_7605 = atomic_add(&((volatile __global
                                             int *) counter_mem_7583)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7593)[0] = old_counter_7605 ==
                num_groups_7337 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7606 = ((__local bool *) sync_arr_mem_7593)[0];
    
    if (is_last_group_7606) {
        if (local_tid_7589 == 0) {
            old_counter_7605 = atomic_add(&((volatile __global
                                             int *) counter_mem_7583)[0],
                                          (int) (0 - num_groups_7337));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7589, num_groups_7337)) {
                x_7171 = ((__global
                           double *) group_res_arr_mem_7585)[local_tid_7589 *
                                                             segred_group_sizze_7335];
            } else {
                x_7171 = 0.0;
            }
            ((__local double *) red_arr_mem_7595)[local_tid_7589] = x_7171;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7607;
            int32_t skip_waves_7608;
            double x_7599;
            double x_7600;
            
            offset_7607 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7589, segred_group_sizze_7335)) {
                    x_7599 = ((__local
                               double *) red_arr_mem_7595)[local_tid_7589 +
                                                           offset_7607];
                }
            }
            offset_7607 = 1;
            while (slt32(offset_7607, wave_sizze_7591)) {
                if (slt32(local_tid_7589 + offset_7607,
                          segred_group_sizze_7335) && ((local_tid_7589 -
                                                        squot32(local_tid_7589,
                                                                wave_sizze_7591) *
                                                        wave_sizze_7591) & (2 *
                                                                            offset_7607 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7600 = ((volatile __local
                                   double *) red_arr_mem_7595)[local_tid_7589 +
                                                               offset_7607];
                    }
                    // apply reduction operation
                    {
                        double res_7601 = x_7599 + x_7600;
                        
                        x_7599 = res_7601;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_7595)[local_tid_7589] = x_7599;
                    }
                }
                offset_7607 *= 2;
            }
            skip_waves_7608 = 1;
            while (slt32(skip_waves_7608, squot32(segred_group_sizze_7335 +
                                                  wave_sizze_7591 - 1,
                                                  wave_sizze_7591))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7607 = skip_waves_7608 * wave_sizze_7591;
                if (slt32(local_tid_7589 + offset_7607,
                          segred_group_sizze_7335) && ((local_tid_7589 -
                                                        squot32(local_tid_7589,
                                                                wave_sizze_7591) *
                                                        wave_sizze_7591) == 0 &&
                                                       (squot32(local_tid_7589,
                                                                wave_sizze_7591) &
                                                        (2 * skip_waves_7608 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7600 = ((__local
                                   double *) red_arr_mem_7595)[local_tid_7589 +
                                                               offset_7607];
                    }
                    // apply reduction operation
                    {
                        double res_7601 = x_7599 + x_7600;
                        
                        x_7599 = res_7601;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_7595)[local_tid_7589] =
                            x_7599;
                    }
                }
                skip_waves_7608 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7589 == 0) {
                    ((__global double *) mem_7464)[0] = x_7599;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7353(__local volatile
                                 int64_t *sync_arr_mem_7621_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7623_backing_aligned_1,
                                 int32_t sizze_7179, int32_t num_groups_7348,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7460, __global
                                 unsigned char *counter_mem_7611, __global
                                 unsigned char *group_res_arr_mem_7613,
                                 int32_t num_threads_7615)
{
    const int32_t segred_group_sizze_7346 =
                  entropy_scaled_f32zisegred_group_sizze_7345;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7621_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7621_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7623_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7623_backing_aligned_1;
    int32_t global_tid_7616;
    int32_t local_tid_7617;
    int32_t group_sizze_7620;
    int32_t wave_sizze_7619;
    int32_t group_tid_7618;
    
    global_tid_7616 = get_global_id(0);
    local_tid_7617 = get_local_id(0);
    group_sizze_7620 = get_local_size(0);
    wave_sizze_7619 = LOCKSTEP_WIDTH;
    group_tid_7618 = get_group_id(0);
    
    int32_t phys_tid_7353 = global_tid_7616;
    __local char *sync_arr_mem_7621;
    
    sync_arr_mem_7621 = (__local char *) sync_arr_mem_7621_backing_0;
    
    __local char *red_arr_mem_7623;
    
    red_arr_mem_7623 = (__local char *) red_arr_mem_7623_backing_1;
    
    int32_t dummy_7351 = 0;
    int32_t gtid_7352;
    
    gtid_7352 = 0;
    
    float x_acc_7625;
    int32_t chunk_sizze_7626 = smin32(squot32(sizze_7179 +
                                              segred_group_sizze_7346 *
                                              num_groups_7348 - 1,
                                              segred_group_sizze_7346 *
                                              num_groups_7348),
                                      squot32(sizze_7179 - phys_tid_7353 +
                                              num_threads_7615 - 1,
                                              num_threads_7615));
    float x_7182;
    float x_7183;
    
    // neutral-initialise the accumulators
    {
        x_acc_7625 = 0.0F;
    }
    for (int32_t i_7630 = 0; i_7630 < chunk_sizze_7626; i_7630++) {
        gtid_7352 = phys_tid_7353 + num_threads_7615 * i_7630;
        // apply map function
        {
            float x_7185 = ((__global float *) x_mem_7456)[gtid_7352];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7182 = x_acc_7625;
            }
            // load new values
            {
                x_7183 = x_7185;
            }
            // apply reduction operator
            {
                float res_7184 = x_7182 + x_7183;
                
                // store in accumulator
                {
                    x_acc_7625 = res_7184;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7182 = x_acc_7625;
        ((__local float *) red_arr_mem_7623)[local_tid_7617] = x_7182;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7631;
    int32_t skip_waves_7632;
    float x_7627;
    float x_7628;
    
    offset_7631 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7617, segred_group_sizze_7346)) {
            x_7627 = ((__local float *) red_arr_mem_7623)[local_tid_7617 +
                                                          offset_7631];
        }
    }
    offset_7631 = 1;
    while (slt32(offset_7631, wave_sizze_7619)) {
        if (slt32(local_tid_7617 + offset_7631, segred_group_sizze_7346) &&
            ((local_tid_7617 - squot32(local_tid_7617, wave_sizze_7619) *
              wave_sizze_7619) & (2 * offset_7631 - 1)) == 0) {
            // read array element
            {
                x_7628 = ((volatile __local
                           float *) red_arr_mem_7623)[local_tid_7617 +
                                                      offset_7631];
            }
            // apply reduction operation
            {
                float res_7629 = x_7627 + x_7628;
                
                x_7627 = res_7629;
            }
            // write result of operation
            {
                ((volatile __local float *) red_arr_mem_7623)[local_tid_7617] =
                    x_7627;
            }
        }
        offset_7631 *= 2;
    }
    skip_waves_7632 = 1;
    while (slt32(skip_waves_7632, squot32(segred_group_sizze_7346 +
                                          wave_sizze_7619 - 1,
                                          wave_sizze_7619))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7631 = skip_waves_7632 * wave_sizze_7619;
        if (slt32(local_tid_7617 + offset_7631, segred_group_sizze_7346) &&
            ((local_tid_7617 - squot32(local_tid_7617, wave_sizze_7619) *
              wave_sizze_7619) == 0 && (squot32(local_tid_7617,
                                                wave_sizze_7619) & (2 *
                                                                    skip_waves_7632 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7628 = ((__local float *) red_arr_mem_7623)[local_tid_7617 +
                                                              offset_7631];
            }
            // apply reduction operation
            {
                float res_7629 = x_7627 + x_7628;
                
                x_7627 = res_7629;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_7623)[local_tid_7617] = x_7627;
            }
        }
        skip_waves_7632 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7617 == 0) {
            x_acc_7625 = x_7627;
        }
    }
    
    int32_t old_counter_7633;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7617 == 0) {
            ((__global float *) group_res_arr_mem_7613)[group_tid_7618 *
                                                        segred_group_sizze_7346] =
                x_acc_7625;
            mem_fence_global();
            old_counter_7633 = atomic_add(&((volatile __global
                                             int *) counter_mem_7611)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7621)[0] = old_counter_7633 ==
                num_groups_7348 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7634 = ((__local bool *) sync_arr_mem_7621)[0];
    
    if (is_last_group_7634) {
        if (local_tid_7617 == 0) {
            old_counter_7633 = atomic_add(&((volatile __global
                                             int *) counter_mem_7611)[0],
                                          (int) (0 - num_groups_7348));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7617, num_groups_7348)) {
                x_7182 = ((__global
                           float *) group_res_arr_mem_7613)[local_tid_7617 *
                                                            segred_group_sizze_7346];
            } else {
                x_7182 = 0.0F;
            }
            ((__local float *) red_arr_mem_7623)[local_tid_7617] = x_7182;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7635;
            int32_t skip_waves_7636;
            float x_7627;
            float x_7628;
            
            offset_7635 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7617, segred_group_sizze_7346)) {
                    x_7627 = ((__local
                               float *) red_arr_mem_7623)[local_tid_7617 +
                                                          offset_7635];
                }
            }
            offset_7635 = 1;
            while (slt32(offset_7635, wave_sizze_7619)) {
                if (slt32(local_tid_7617 + offset_7635,
                          segred_group_sizze_7346) && ((local_tid_7617 -
                                                        squot32(local_tid_7617,
                                                                wave_sizze_7619) *
                                                        wave_sizze_7619) & (2 *
                                                                            offset_7635 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7628 = ((volatile __local
                                   float *) red_arr_mem_7623)[local_tid_7617 +
                                                              offset_7635];
                    }
                    // apply reduction operation
                    {
                        float res_7629 = x_7627 + x_7628;
                        
                        x_7627 = res_7629;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_7623)[local_tid_7617] = x_7627;
                    }
                }
                offset_7635 *= 2;
            }
            skip_waves_7636 = 1;
            while (slt32(skip_waves_7636, squot32(segred_group_sizze_7346 +
                                                  wave_sizze_7619 - 1,
                                                  wave_sizze_7619))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7635 = skip_waves_7636 * wave_sizze_7619;
                if (slt32(local_tid_7617 + offset_7635,
                          segred_group_sizze_7346) && ((local_tid_7617 -
                                                        squot32(local_tid_7617,
                                                                wave_sizze_7619) *
                                                        wave_sizze_7619) == 0 &&
                                                       (squot32(local_tid_7617,
                                                                wave_sizze_7619) &
                                                        (2 * skip_waves_7636 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7628 = ((__local
                                   float *) red_arr_mem_7623)[local_tid_7617 +
                                                              offset_7635];
                    }
                    // apply reduction operation
                    {
                        float res_7629 = x_7627 + x_7628;
                        
                        x_7627 = res_7629;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_7623)[local_tid_7617] =
                            x_7627;
                    }
                }
                skip_waves_7636 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7617 == 0) {
                    ((__global float *) mem_7460)[0] = x_7627;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7364(__local volatile
                                 int64_t *sync_arr_mem_7648_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7650_backing_aligned_1,
                                 int32_t sizze_7179, float res_7181,
                                 int32_t num_groups_7359, __global
                                 unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7464, __global
                                 unsigned char *counter_mem_7638, __global
                                 unsigned char *group_res_arr_mem_7640,
                                 int32_t num_threads_7642)
{
    const int32_t segred_group_sizze_7357 =
                  entropy_scaled_f32zisegred_group_sizze_7356;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7648_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7648_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7650_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7650_backing_aligned_1;
    int32_t global_tid_7643;
    int32_t local_tid_7644;
    int32_t group_sizze_7647;
    int32_t wave_sizze_7646;
    int32_t group_tid_7645;
    
    global_tid_7643 = get_global_id(0);
    local_tid_7644 = get_local_id(0);
    group_sizze_7647 = get_local_size(0);
    wave_sizze_7646 = LOCKSTEP_WIDTH;
    group_tid_7645 = get_group_id(0);
    
    int32_t phys_tid_7364 = global_tid_7643;
    __local char *sync_arr_mem_7648;
    
    sync_arr_mem_7648 = (__local char *) sync_arr_mem_7648_backing_0;
    
    __local char *red_arr_mem_7650;
    
    red_arr_mem_7650 = (__local char *) red_arr_mem_7650_backing_1;
    
    int32_t dummy_7362 = 0;
    int32_t gtid_7363;
    
    gtid_7363 = 0;
    
    float x_acc_7652;
    int32_t chunk_sizze_7653 = smin32(squot32(sizze_7179 +
                                              segred_group_sizze_7357 *
                                              num_groups_7359 - 1,
                                              segred_group_sizze_7357 *
                                              num_groups_7359),
                                      squot32(sizze_7179 - phys_tid_7364 +
                                              num_threads_7642 - 1,
                                              num_threads_7642));
    float x_7187;
    float x_7188;
    
    // neutral-initialise the accumulators
    {
        x_acc_7652 = 0.0F;
    }
    for (int32_t i_7657 = 0; i_7657 < chunk_sizze_7653; i_7657++) {
        gtid_7363 = phys_tid_7364 + num_threads_7642 * i_7657;
        // apply map function
        {
            float x_7190 = ((__global float *) x_mem_7456)[gtid_7363];
            float res_7191 = x_7190 / res_7181;
            float res_7192;
            
            res_7192 = futrts_log32(res_7191);
            
            float res_7193 = res_7191 * res_7192;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7187 = x_acc_7652;
            }
            // load new values
            {
                x_7188 = res_7193;
            }
            // apply reduction operator
            {
                float res_7189 = x_7187 + x_7188;
                
                // store in accumulator
                {
                    x_acc_7652 = res_7189;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7187 = x_acc_7652;
        ((__local float *) red_arr_mem_7650)[local_tid_7644] = x_7187;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7658;
    int32_t skip_waves_7659;
    float x_7654;
    float x_7655;
    
    offset_7658 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7644, segred_group_sizze_7357)) {
            x_7654 = ((__local float *) red_arr_mem_7650)[local_tid_7644 +
                                                          offset_7658];
        }
    }
    offset_7658 = 1;
    while (slt32(offset_7658, wave_sizze_7646)) {
        if (slt32(local_tid_7644 + offset_7658, segred_group_sizze_7357) &&
            ((local_tid_7644 - squot32(local_tid_7644, wave_sizze_7646) *
              wave_sizze_7646) & (2 * offset_7658 - 1)) == 0) {
            // read array element
            {
                x_7655 = ((volatile __local
                           float *) red_arr_mem_7650)[local_tid_7644 +
                                                      offset_7658];
            }
            // apply reduction operation
            {
                float res_7656 = x_7654 + x_7655;
                
                x_7654 = res_7656;
            }
            // write result of operation
            {
                ((volatile __local float *) red_arr_mem_7650)[local_tid_7644] =
                    x_7654;
            }
        }
        offset_7658 *= 2;
    }
    skip_waves_7659 = 1;
    while (slt32(skip_waves_7659, squot32(segred_group_sizze_7357 +
                                          wave_sizze_7646 - 1,
                                          wave_sizze_7646))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7658 = skip_waves_7659 * wave_sizze_7646;
        if (slt32(local_tid_7644 + offset_7658, segred_group_sizze_7357) &&
            ((local_tid_7644 - squot32(local_tid_7644, wave_sizze_7646) *
              wave_sizze_7646) == 0 && (squot32(local_tid_7644,
                                                wave_sizze_7646) & (2 *
                                                                    skip_waves_7659 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7655 = ((__local float *) red_arr_mem_7650)[local_tid_7644 +
                                                              offset_7658];
            }
            // apply reduction operation
            {
                float res_7656 = x_7654 + x_7655;
                
                x_7654 = res_7656;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_7650)[local_tid_7644] = x_7654;
            }
        }
        skip_waves_7659 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7644 == 0) {
            x_acc_7652 = x_7654;
        }
    }
    
    int32_t old_counter_7660;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7644 == 0) {
            ((__global float *) group_res_arr_mem_7640)[group_tid_7645 *
                                                        segred_group_sizze_7357] =
                x_acc_7652;
            mem_fence_global();
            old_counter_7660 = atomic_add(&((volatile __global
                                             int *) counter_mem_7638)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7648)[0] = old_counter_7660 ==
                num_groups_7359 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7661 = ((__local bool *) sync_arr_mem_7648)[0];
    
    if (is_last_group_7661) {
        if (local_tid_7644 == 0) {
            old_counter_7660 = atomic_add(&((volatile __global
                                             int *) counter_mem_7638)[0],
                                          (int) (0 - num_groups_7359));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7644, num_groups_7359)) {
                x_7187 = ((__global
                           float *) group_res_arr_mem_7640)[local_tid_7644 *
                                                            segred_group_sizze_7357];
            } else {
                x_7187 = 0.0F;
            }
            ((__local float *) red_arr_mem_7650)[local_tid_7644] = x_7187;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7662;
            int32_t skip_waves_7663;
            float x_7654;
            float x_7655;
            
            offset_7662 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7644, segred_group_sizze_7357)) {
                    x_7654 = ((__local
                               float *) red_arr_mem_7650)[local_tid_7644 +
                                                          offset_7662];
                }
            }
            offset_7662 = 1;
            while (slt32(offset_7662, wave_sizze_7646)) {
                if (slt32(local_tid_7644 + offset_7662,
                          segred_group_sizze_7357) && ((local_tid_7644 -
                                                        squot32(local_tid_7644,
                                                                wave_sizze_7646) *
                                                        wave_sizze_7646) & (2 *
                                                                            offset_7662 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7655 = ((volatile __local
                                   float *) red_arr_mem_7650)[local_tid_7644 +
                                                              offset_7662];
                    }
                    // apply reduction operation
                    {
                        float res_7656 = x_7654 + x_7655;
                        
                        x_7654 = res_7656;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_7650)[local_tid_7644] = x_7654;
                    }
                }
                offset_7662 *= 2;
            }
            skip_waves_7663 = 1;
            while (slt32(skip_waves_7663, squot32(segred_group_sizze_7357 +
                                                  wave_sizze_7646 - 1,
                                                  wave_sizze_7646))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7662 = skip_waves_7663 * wave_sizze_7646;
                if (slt32(local_tid_7644 + offset_7662,
                          segred_group_sizze_7357) && ((local_tid_7644 -
                                                        squot32(local_tid_7644,
                                                                wave_sizze_7646) *
                                                        wave_sizze_7646) == 0 &&
                                                       (squot32(local_tid_7644,
                                                                wave_sizze_7646) &
                                                        (2 * skip_waves_7663 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7655 = ((__local
                                   float *) red_arr_mem_7650)[local_tid_7644 +
                                                              offset_7662];
                    }
                    // apply reduction operation
                    {
                        float res_7656 = x_7654 + x_7655;
                        
                        x_7654 = res_7656;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_7650)[local_tid_7644] =
                            x_7654;
                    }
                }
                skip_waves_7663 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7644 == 0) {
                    ((__global float *) mem_7464)[0] = x_7654;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7375(__local volatile
                                 int64_t *sync_arr_mem_7676_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7678_backing_aligned_1,
                                 int32_t sizze_7195, int32_t num_groups_7370,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *x_mem_7457, __global
                                 unsigned char *mem_7461, __global
                                 unsigned char *counter_mem_7666, __global
                                 unsigned char *group_res_arr_mem_7668,
                                 int32_t num_threads_7670)
{
    const int32_t segred_group_sizze_7368 =
                  kullback_liebler_f64zisegred_group_sizze_7367;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7676_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7676_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7678_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7678_backing_aligned_1;
    int32_t global_tid_7671;
    int32_t local_tid_7672;
    int32_t group_sizze_7675;
    int32_t wave_sizze_7674;
    int32_t group_tid_7673;
    
    global_tid_7671 = get_global_id(0);
    local_tid_7672 = get_local_id(0);
    group_sizze_7675 = get_local_size(0);
    wave_sizze_7674 = LOCKSTEP_WIDTH;
    group_tid_7673 = get_group_id(0);
    
    int32_t phys_tid_7375 = global_tid_7671;
    __local char *sync_arr_mem_7676;
    
    sync_arr_mem_7676 = (__local char *) sync_arr_mem_7676_backing_0;
    
    __local char *red_arr_mem_7678;
    
    red_arr_mem_7678 = (__local char *) red_arr_mem_7678_backing_1;
    
    int32_t dummy_7373 = 0;
    int32_t gtid_7374;
    
    gtid_7374 = 0;
    
    double x_acc_7680;
    int32_t chunk_sizze_7681 = smin32(squot32(sizze_7195 +
                                              segred_group_sizze_7368 *
                                              num_groups_7370 - 1,
                                              segred_group_sizze_7368 *
                                              num_groups_7370),
                                      squot32(sizze_7195 - phys_tid_7375 +
                                              num_threads_7670 - 1,
                                              num_threads_7670));
    double x_7207;
    double x_7208;
    
    // neutral-initialise the accumulators
    {
        x_acc_7680 = 0.0;
    }
    for (int32_t i_7685 = 0; i_7685 < chunk_sizze_7681; i_7685++) {
        gtid_7374 = phys_tid_7375 + num_threads_7670 * i_7685;
        // apply map function
        {
            double x_7210 = ((__global double *) x_mem_7456)[gtid_7374];
            double x_7211 = ((__global double *) x_mem_7457)[gtid_7374];
            double res_7212 = x_7210 / x_7211;
            double res_7213;
            
            res_7213 = futrts_log64(res_7212);
            
            double res_7214 = x_7210 * res_7213;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7207 = x_acc_7680;
            }
            // load new values
            {
                x_7208 = res_7214;
            }
            // apply reduction operator
            {
                double res_7209 = x_7207 + x_7208;
                
                // store in accumulator
                {
                    x_acc_7680 = res_7209;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7207 = x_acc_7680;
        ((__local double *) red_arr_mem_7678)[local_tid_7672] = x_7207;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7686;
    int32_t skip_waves_7687;
    double x_7682;
    double x_7683;
    
    offset_7686 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7672, segred_group_sizze_7368)) {
            x_7682 = ((__local double *) red_arr_mem_7678)[local_tid_7672 +
                                                           offset_7686];
        }
    }
    offset_7686 = 1;
    while (slt32(offset_7686, wave_sizze_7674)) {
        if (slt32(local_tid_7672 + offset_7686, segred_group_sizze_7368) &&
            ((local_tid_7672 - squot32(local_tid_7672, wave_sizze_7674) *
              wave_sizze_7674) & (2 * offset_7686 - 1)) == 0) {
            // read array element
            {
                x_7683 = ((volatile __local
                           double *) red_arr_mem_7678)[local_tid_7672 +
                                                       offset_7686];
            }
            // apply reduction operation
            {
                double res_7684 = x_7682 + x_7683;
                
                x_7682 = res_7684;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_7678)[local_tid_7672] =
                    x_7682;
            }
        }
        offset_7686 *= 2;
    }
    skip_waves_7687 = 1;
    while (slt32(skip_waves_7687, squot32(segred_group_sizze_7368 +
                                          wave_sizze_7674 - 1,
                                          wave_sizze_7674))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7686 = skip_waves_7687 * wave_sizze_7674;
        if (slt32(local_tid_7672 + offset_7686, segred_group_sizze_7368) &&
            ((local_tid_7672 - squot32(local_tid_7672, wave_sizze_7674) *
              wave_sizze_7674) == 0 && (squot32(local_tid_7672,
                                                wave_sizze_7674) & (2 *
                                                                    skip_waves_7687 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7683 = ((__local double *) red_arr_mem_7678)[local_tid_7672 +
                                                               offset_7686];
            }
            // apply reduction operation
            {
                double res_7684 = x_7682 + x_7683;
                
                x_7682 = res_7684;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_7678)[local_tid_7672] = x_7682;
            }
        }
        skip_waves_7687 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7672 == 0) {
            x_acc_7680 = x_7682;
        }
    }
    
    int32_t old_counter_7688;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7672 == 0) {
            ((__global double *) group_res_arr_mem_7668)[group_tid_7673 *
                                                         segred_group_sizze_7368] =
                x_acc_7680;
            mem_fence_global();
            old_counter_7688 = atomic_add(&((volatile __global
                                             int *) counter_mem_7666)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7676)[0] = old_counter_7688 ==
                num_groups_7370 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7689 = ((__local bool *) sync_arr_mem_7676)[0];
    
    if (is_last_group_7689) {
        if (local_tid_7672 == 0) {
            old_counter_7688 = atomic_add(&((volatile __global
                                             int *) counter_mem_7666)[0],
                                          (int) (0 - num_groups_7370));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7672, num_groups_7370)) {
                x_7207 = ((__global
                           double *) group_res_arr_mem_7668)[local_tid_7672 *
                                                             segred_group_sizze_7368];
            } else {
                x_7207 = 0.0;
            }
            ((__local double *) red_arr_mem_7678)[local_tid_7672] = x_7207;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7690;
            int32_t skip_waves_7691;
            double x_7682;
            double x_7683;
            
            offset_7690 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7672, segred_group_sizze_7368)) {
                    x_7682 = ((__local
                               double *) red_arr_mem_7678)[local_tid_7672 +
                                                           offset_7690];
                }
            }
            offset_7690 = 1;
            while (slt32(offset_7690, wave_sizze_7674)) {
                if (slt32(local_tid_7672 + offset_7690,
                          segred_group_sizze_7368) && ((local_tid_7672 -
                                                        squot32(local_tid_7672,
                                                                wave_sizze_7674) *
                                                        wave_sizze_7674) & (2 *
                                                                            offset_7690 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7683 = ((volatile __local
                                   double *) red_arr_mem_7678)[local_tid_7672 +
                                                               offset_7690];
                    }
                    // apply reduction operation
                    {
                        double res_7684 = x_7682 + x_7683;
                        
                        x_7682 = res_7684;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_7678)[local_tid_7672] = x_7682;
                    }
                }
                offset_7690 *= 2;
            }
            skip_waves_7691 = 1;
            while (slt32(skip_waves_7691, squot32(segred_group_sizze_7368 +
                                                  wave_sizze_7674 - 1,
                                                  wave_sizze_7674))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7690 = skip_waves_7691 * wave_sizze_7674;
                if (slt32(local_tid_7672 + offset_7690,
                          segred_group_sizze_7368) && ((local_tid_7672 -
                                                        squot32(local_tid_7672,
                                                                wave_sizze_7674) *
                                                        wave_sizze_7674) == 0 &&
                                                       (squot32(local_tid_7672,
                                                                wave_sizze_7674) &
                                                        (2 * skip_waves_7691 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7683 = ((__local
                                   double *) red_arr_mem_7678)[local_tid_7672 +
                                                               offset_7690];
                    }
                    // apply reduction operation
                    {
                        double res_7684 = x_7682 + x_7683;
                        
                        x_7682 = res_7684;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_7678)[local_tid_7672] =
                            x_7682;
                    }
                }
                skip_waves_7691 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7672 == 0) {
                    ((__global double *) mem_7461)[0] = x_7682;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7386(__local volatile
                                 int64_t *sync_arr_mem_7704_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7706_backing_aligned_1,
                                 int32_t sizze_7215, int32_t num_groups_7381,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7461, __global
                                 unsigned char *counter_mem_7694, __global
                                 unsigned char *group_res_arr_mem_7696,
                                 int32_t num_threads_7698)
{
    const int32_t segred_group_sizze_7379 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_7378;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7704_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7704_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7706_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7706_backing_aligned_1;
    int32_t global_tid_7699;
    int32_t local_tid_7700;
    int32_t group_sizze_7703;
    int32_t wave_sizze_7702;
    int32_t group_tid_7701;
    
    global_tid_7699 = get_global_id(0);
    local_tid_7700 = get_local_id(0);
    group_sizze_7703 = get_local_size(0);
    wave_sizze_7702 = LOCKSTEP_WIDTH;
    group_tid_7701 = get_group_id(0);
    
    int32_t phys_tid_7386 = global_tid_7699;
    __local char *sync_arr_mem_7704;
    
    sync_arr_mem_7704 = (__local char *) sync_arr_mem_7704_backing_0;
    
    __local char *red_arr_mem_7706;
    
    red_arr_mem_7706 = (__local char *) red_arr_mem_7706_backing_1;
    
    int32_t dummy_7384 = 0;
    int32_t gtid_7385;
    
    gtid_7385 = 0;
    
    double x_acc_7708;
    int32_t chunk_sizze_7709 = smin32(squot32(sizze_7215 +
                                              segred_group_sizze_7379 *
                                              num_groups_7381 - 1,
                                              segred_group_sizze_7379 *
                                              num_groups_7381),
                                      squot32(sizze_7215 - phys_tid_7386 +
                                              num_threads_7698 - 1,
                                              num_threads_7698));
    double x_7220;
    double x_7221;
    
    // neutral-initialise the accumulators
    {
        x_acc_7708 = 0.0;
    }
    for (int32_t i_7713 = 0; i_7713 < chunk_sizze_7709; i_7713++) {
        gtid_7385 = phys_tid_7386 + num_threads_7698 * i_7713;
        // apply map function
        {
            double x_7223 = ((__global double *) x_mem_7456)[gtid_7385];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7220 = x_acc_7708;
            }
            // load new values
            {
                x_7221 = x_7223;
            }
            // apply reduction operator
            {
                double res_7222 = x_7220 + x_7221;
                
                // store in accumulator
                {
                    x_acc_7708 = res_7222;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7220 = x_acc_7708;
        ((__local double *) red_arr_mem_7706)[local_tid_7700] = x_7220;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7714;
    int32_t skip_waves_7715;
    double x_7710;
    double x_7711;
    
    offset_7714 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7700, segred_group_sizze_7379)) {
            x_7710 = ((__local double *) red_arr_mem_7706)[local_tid_7700 +
                                                           offset_7714];
        }
    }
    offset_7714 = 1;
    while (slt32(offset_7714, wave_sizze_7702)) {
        if (slt32(local_tid_7700 + offset_7714, segred_group_sizze_7379) &&
            ((local_tid_7700 - squot32(local_tid_7700, wave_sizze_7702) *
              wave_sizze_7702) & (2 * offset_7714 - 1)) == 0) {
            // read array element
            {
                x_7711 = ((volatile __local
                           double *) red_arr_mem_7706)[local_tid_7700 +
                                                       offset_7714];
            }
            // apply reduction operation
            {
                double res_7712 = x_7710 + x_7711;
                
                x_7710 = res_7712;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_7706)[local_tid_7700] =
                    x_7710;
            }
        }
        offset_7714 *= 2;
    }
    skip_waves_7715 = 1;
    while (slt32(skip_waves_7715, squot32(segred_group_sizze_7379 +
                                          wave_sizze_7702 - 1,
                                          wave_sizze_7702))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7714 = skip_waves_7715 * wave_sizze_7702;
        if (slt32(local_tid_7700 + offset_7714, segred_group_sizze_7379) &&
            ((local_tid_7700 - squot32(local_tid_7700, wave_sizze_7702) *
              wave_sizze_7702) == 0 && (squot32(local_tid_7700,
                                                wave_sizze_7702) & (2 *
                                                                    skip_waves_7715 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7711 = ((__local double *) red_arr_mem_7706)[local_tid_7700 +
                                                               offset_7714];
            }
            // apply reduction operation
            {
                double res_7712 = x_7710 + x_7711;
                
                x_7710 = res_7712;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_7706)[local_tid_7700] = x_7710;
            }
        }
        skip_waves_7715 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7700 == 0) {
            x_acc_7708 = x_7710;
        }
    }
    
    int32_t old_counter_7716;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7700 == 0) {
            ((__global double *) group_res_arr_mem_7696)[group_tid_7701 *
                                                         segred_group_sizze_7379] =
                x_acc_7708;
            mem_fence_global();
            old_counter_7716 = atomic_add(&((volatile __global
                                             int *) counter_mem_7694)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7704)[0] = old_counter_7716 ==
                num_groups_7381 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7717 = ((__local bool *) sync_arr_mem_7704)[0];
    
    if (is_last_group_7717) {
        if (local_tid_7700 == 0) {
            old_counter_7716 = atomic_add(&((volatile __global
                                             int *) counter_mem_7694)[0],
                                          (int) (0 - num_groups_7381));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7700, num_groups_7381)) {
                x_7220 = ((__global
                           double *) group_res_arr_mem_7696)[local_tid_7700 *
                                                             segred_group_sizze_7379];
            } else {
                x_7220 = 0.0;
            }
            ((__local double *) red_arr_mem_7706)[local_tid_7700] = x_7220;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7718;
            int32_t skip_waves_7719;
            double x_7710;
            double x_7711;
            
            offset_7718 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7700, segred_group_sizze_7379)) {
                    x_7710 = ((__local
                               double *) red_arr_mem_7706)[local_tid_7700 +
                                                           offset_7718];
                }
            }
            offset_7718 = 1;
            while (slt32(offset_7718, wave_sizze_7702)) {
                if (slt32(local_tid_7700 + offset_7718,
                          segred_group_sizze_7379) && ((local_tid_7700 -
                                                        squot32(local_tid_7700,
                                                                wave_sizze_7702) *
                                                        wave_sizze_7702) & (2 *
                                                                            offset_7718 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7711 = ((volatile __local
                                   double *) red_arr_mem_7706)[local_tid_7700 +
                                                               offset_7718];
                    }
                    // apply reduction operation
                    {
                        double res_7712 = x_7710 + x_7711;
                        
                        x_7710 = res_7712;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_7706)[local_tid_7700] = x_7710;
                    }
                }
                offset_7718 *= 2;
            }
            skip_waves_7719 = 1;
            while (slt32(skip_waves_7719, squot32(segred_group_sizze_7379 +
                                                  wave_sizze_7702 - 1,
                                                  wave_sizze_7702))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7718 = skip_waves_7719 * wave_sizze_7702;
                if (slt32(local_tid_7700 + offset_7718,
                          segred_group_sizze_7379) && ((local_tid_7700 -
                                                        squot32(local_tid_7700,
                                                                wave_sizze_7702) *
                                                        wave_sizze_7702) == 0 &&
                                                       (squot32(local_tid_7700,
                                                                wave_sizze_7702) &
                                                        (2 * skip_waves_7719 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7711 = ((__local
                                   double *) red_arr_mem_7706)[local_tid_7700 +
                                                               offset_7718];
                    }
                    // apply reduction operation
                    {
                        double res_7712 = x_7710 + x_7711;
                        
                        x_7710 = res_7712;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_7706)[local_tid_7700] =
                            x_7710;
                    }
                }
                skip_waves_7719 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7700 == 0) {
                    ((__global double *) mem_7461)[0] = x_7710;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7397(__local volatile
                                 int64_t *sync_arr_mem_7731_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7733_backing_aligned_1,
                                 int32_t sizze_7216, int32_t num_groups_7392,
                                 __global unsigned char *y_mem_7457, __global
                                 unsigned char *mem_7465, __global
                                 unsigned char *counter_mem_7721, __global
                                 unsigned char *group_res_arr_mem_7723,
                                 int32_t num_threads_7725)
{
    const int32_t segred_group_sizze_7390 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_7389;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7731_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7731_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7733_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7733_backing_aligned_1;
    int32_t global_tid_7726;
    int32_t local_tid_7727;
    int32_t group_sizze_7730;
    int32_t wave_sizze_7729;
    int32_t group_tid_7728;
    
    global_tid_7726 = get_global_id(0);
    local_tid_7727 = get_local_id(0);
    group_sizze_7730 = get_local_size(0);
    wave_sizze_7729 = LOCKSTEP_WIDTH;
    group_tid_7728 = get_group_id(0);
    
    int32_t phys_tid_7397 = global_tid_7726;
    __local char *sync_arr_mem_7731;
    
    sync_arr_mem_7731 = (__local char *) sync_arr_mem_7731_backing_0;
    
    __local char *red_arr_mem_7733;
    
    red_arr_mem_7733 = (__local char *) red_arr_mem_7733_backing_1;
    
    int32_t dummy_7395 = 0;
    int32_t gtid_7396;
    
    gtid_7396 = 0;
    
    double x_acc_7735;
    int32_t chunk_sizze_7736 = smin32(squot32(sizze_7216 +
                                              segred_group_sizze_7390 *
                                              num_groups_7392 - 1,
                                              segred_group_sizze_7390 *
                                              num_groups_7392),
                                      squot32(sizze_7216 - phys_tid_7397 +
                                              num_threads_7725 - 1,
                                              num_threads_7725));
    double x_7226;
    double x_7227;
    
    // neutral-initialise the accumulators
    {
        x_acc_7735 = 0.0;
    }
    for (int32_t i_7740 = 0; i_7740 < chunk_sizze_7736; i_7740++) {
        gtid_7396 = phys_tid_7397 + num_threads_7725 * i_7740;
        // apply map function
        {
            double x_7229 = ((__global double *) y_mem_7457)[gtid_7396];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7226 = x_acc_7735;
            }
            // load new values
            {
                x_7227 = x_7229;
            }
            // apply reduction operator
            {
                double res_7228 = x_7226 + x_7227;
                
                // store in accumulator
                {
                    x_acc_7735 = res_7228;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7226 = x_acc_7735;
        ((__local double *) red_arr_mem_7733)[local_tid_7727] = x_7226;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7741;
    int32_t skip_waves_7742;
    double x_7737;
    double x_7738;
    
    offset_7741 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7727, segred_group_sizze_7390)) {
            x_7737 = ((__local double *) red_arr_mem_7733)[local_tid_7727 +
                                                           offset_7741];
        }
    }
    offset_7741 = 1;
    while (slt32(offset_7741, wave_sizze_7729)) {
        if (slt32(local_tid_7727 + offset_7741, segred_group_sizze_7390) &&
            ((local_tid_7727 - squot32(local_tid_7727, wave_sizze_7729) *
              wave_sizze_7729) & (2 * offset_7741 - 1)) == 0) {
            // read array element
            {
                x_7738 = ((volatile __local
                           double *) red_arr_mem_7733)[local_tid_7727 +
                                                       offset_7741];
            }
            // apply reduction operation
            {
                double res_7739 = x_7737 + x_7738;
                
                x_7737 = res_7739;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_7733)[local_tid_7727] =
                    x_7737;
            }
        }
        offset_7741 *= 2;
    }
    skip_waves_7742 = 1;
    while (slt32(skip_waves_7742, squot32(segred_group_sizze_7390 +
                                          wave_sizze_7729 - 1,
                                          wave_sizze_7729))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7741 = skip_waves_7742 * wave_sizze_7729;
        if (slt32(local_tid_7727 + offset_7741, segred_group_sizze_7390) &&
            ((local_tid_7727 - squot32(local_tid_7727, wave_sizze_7729) *
              wave_sizze_7729) == 0 && (squot32(local_tid_7727,
                                                wave_sizze_7729) & (2 *
                                                                    skip_waves_7742 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7738 = ((__local double *) red_arr_mem_7733)[local_tid_7727 +
                                                               offset_7741];
            }
            // apply reduction operation
            {
                double res_7739 = x_7737 + x_7738;
                
                x_7737 = res_7739;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_7733)[local_tid_7727] = x_7737;
            }
        }
        skip_waves_7742 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7727 == 0) {
            x_acc_7735 = x_7737;
        }
    }
    
    int32_t old_counter_7743;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7727 == 0) {
            ((__global double *) group_res_arr_mem_7723)[group_tid_7728 *
                                                         segred_group_sizze_7390] =
                x_acc_7735;
            mem_fence_global();
            old_counter_7743 = atomic_add(&((volatile __global
                                             int *) counter_mem_7721)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7731)[0] = old_counter_7743 ==
                num_groups_7392 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7744 = ((__local bool *) sync_arr_mem_7731)[0];
    
    if (is_last_group_7744) {
        if (local_tid_7727 == 0) {
            old_counter_7743 = atomic_add(&((volatile __global
                                             int *) counter_mem_7721)[0],
                                          (int) (0 - num_groups_7392));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7727, num_groups_7392)) {
                x_7226 = ((__global
                           double *) group_res_arr_mem_7723)[local_tid_7727 *
                                                             segred_group_sizze_7390];
            } else {
                x_7226 = 0.0;
            }
            ((__local double *) red_arr_mem_7733)[local_tid_7727] = x_7226;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7745;
            int32_t skip_waves_7746;
            double x_7737;
            double x_7738;
            
            offset_7745 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7727, segred_group_sizze_7390)) {
                    x_7737 = ((__local
                               double *) red_arr_mem_7733)[local_tid_7727 +
                                                           offset_7745];
                }
            }
            offset_7745 = 1;
            while (slt32(offset_7745, wave_sizze_7729)) {
                if (slt32(local_tid_7727 + offset_7745,
                          segred_group_sizze_7390) && ((local_tid_7727 -
                                                        squot32(local_tid_7727,
                                                                wave_sizze_7729) *
                                                        wave_sizze_7729) & (2 *
                                                                            offset_7745 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7738 = ((volatile __local
                                   double *) red_arr_mem_7733)[local_tid_7727 +
                                                               offset_7745];
                    }
                    // apply reduction operation
                    {
                        double res_7739 = x_7737 + x_7738;
                        
                        x_7737 = res_7739;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_7733)[local_tid_7727] = x_7737;
                    }
                }
                offset_7745 *= 2;
            }
            skip_waves_7746 = 1;
            while (slt32(skip_waves_7746, squot32(segred_group_sizze_7390 +
                                                  wave_sizze_7729 - 1,
                                                  wave_sizze_7729))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7745 = skip_waves_7746 * wave_sizze_7729;
                if (slt32(local_tid_7727 + offset_7745,
                          segred_group_sizze_7390) && ((local_tid_7727 -
                                                        squot32(local_tid_7727,
                                                                wave_sizze_7729) *
                                                        wave_sizze_7729) == 0 &&
                                                       (squot32(local_tid_7727,
                                                                wave_sizze_7729) &
                                                        (2 * skip_waves_7746 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7738 = ((__local
                                   double *) red_arr_mem_7733)[local_tid_7727 +
                                                               offset_7745];
                    }
                    // apply reduction operation
                    {
                        double res_7739 = x_7737 + x_7738;
                        
                        x_7737 = res_7739;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_7733)[local_tid_7727] =
                            x_7737;
                    }
                }
                skip_waves_7746 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7727 == 0) {
                    ((__global double *) mem_7465)[0] = x_7737;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7408(__local volatile
                                 int64_t *sync_arr_mem_7758_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7760_backing_aligned_1,
                                 int32_t sizze_7215, double res_7219,
                                 double res_7225, int32_t num_groups_7403,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *y_mem_7457, __global
                                 unsigned char *mem_7469, __global
                                 unsigned char *counter_mem_7748, __global
                                 unsigned char *group_res_arr_mem_7750,
                                 int32_t num_threads_7752)
{
    const int32_t segred_group_sizze_7401 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_7400;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7758_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7758_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7760_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7760_backing_aligned_1;
    int32_t global_tid_7753;
    int32_t local_tid_7754;
    int32_t group_sizze_7757;
    int32_t wave_sizze_7756;
    int32_t group_tid_7755;
    
    global_tid_7753 = get_global_id(0);
    local_tid_7754 = get_local_id(0);
    group_sizze_7757 = get_local_size(0);
    wave_sizze_7756 = LOCKSTEP_WIDTH;
    group_tid_7755 = get_group_id(0);
    
    int32_t phys_tid_7408 = global_tid_7753;
    __local char *sync_arr_mem_7758;
    
    sync_arr_mem_7758 = (__local char *) sync_arr_mem_7758_backing_0;
    
    __local char *red_arr_mem_7760;
    
    red_arr_mem_7760 = (__local char *) red_arr_mem_7760_backing_1;
    
    int32_t dummy_7406 = 0;
    int32_t gtid_7407;
    
    gtid_7407 = 0;
    
    double x_acc_7762;
    int32_t chunk_sizze_7763 = smin32(squot32(sizze_7215 +
                                              segred_group_sizze_7401 *
                                              num_groups_7403 - 1,
                                              segred_group_sizze_7401 *
                                              num_groups_7403),
                                      squot32(sizze_7215 - phys_tid_7408 +
                                              num_threads_7752 - 1,
                                              num_threads_7752));
    double x_7237;
    double x_7238;
    
    // neutral-initialise the accumulators
    {
        x_acc_7762 = 0.0;
    }
    for (int32_t i_7767 = 0; i_7767 < chunk_sizze_7763; i_7767++) {
        gtid_7407 = phys_tid_7408 + num_threads_7752 * i_7767;
        // apply map function
        {
            double x_7240 = ((__global double *) x_mem_7456)[gtid_7407];
            double x_7241 = ((__global double *) y_mem_7457)[gtid_7407];
            double res_7242 = x_7240 / res_7219;
            double res_7243 = x_7241 / res_7225;
            double res_7244 = res_7242 / res_7243;
            double res_7245;
            
            res_7245 = futrts_log64(res_7244);
            
            double res_7246 = res_7242 * res_7245;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7237 = x_acc_7762;
            }
            // load new values
            {
                x_7238 = res_7246;
            }
            // apply reduction operator
            {
                double res_7239 = x_7237 + x_7238;
                
                // store in accumulator
                {
                    x_acc_7762 = res_7239;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7237 = x_acc_7762;
        ((__local double *) red_arr_mem_7760)[local_tid_7754] = x_7237;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7768;
    int32_t skip_waves_7769;
    double x_7764;
    double x_7765;
    
    offset_7768 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7754, segred_group_sizze_7401)) {
            x_7764 = ((__local double *) red_arr_mem_7760)[local_tid_7754 +
                                                           offset_7768];
        }
    }
    offset_7768 = 1;
    while (slt32(offset_7768, wave_sizze_7756)) {
        if (slt32(local_tid_7754 + offset_7768, segred_group_sizze_7401) &&
            ((local_tid_7754 - squot32(local_tid_7754, wave_sizze_7756) *
              wave_sizze_7756) & (2 * offset_7768 - 1)) == 0) {
            // read array element
            {
                x_7765 = ((volatile __local
                           double *) red_arr_mem_7760)[local_tid_7754 +
                                                       offset_7768];
            }
            // apply reduction operation
            {
                double res_7766 = x_7764 + x_7765;
                
                x_7764 = res_7766;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_7760)[local_tid_7754] =
                    x_7764;
            }
        }
        offset_7768 *= 2;
    }
    skip_waves_7769 = 1;
    while (slt32(skip_waves_7769, squot32(segred_group_sizze_7401 +
                                          wave_sizze_7756 - 1,
                                          wave_sizze_7756))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7768 = skip_waves_7769 * wave_sizze_7756;
        if (slt32(local_tid_7754 + offset_7768, segred_group_sizze_7401) &&
            ((local_tid_7754 - squot32(local_tid_7754, wave_sizze_7756) *
              wave_sizze_7756) == 0 && (squot32(local_tid_7754,
                                                wave_sizze_7756) & (2 *
                                                                    skip_waves_7769 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7765 = ((__local double *) red_arr_mem_7760)[local_tid_7754 +
                                                               offset_7768];
            }
            // apply reduction operation
            {
                double res_7766 = x_7764 + x_7765;
                
                x_7764 = res_7766;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_7760)[local_tid_7754] = x_7764;
            }
        }
        skip_waves_7769 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7754 == 0) {
            x_acc_7762 = x_7764;
        }
    }
    
    int32_t old_counter_7770;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7754 == 0) {
            ((__global double *) group_res_arr_mem_7750)[group_tid_7755 *
                                                         segred_group_sizze_7401] =
                x_acc_7762;
            mem_fence_global();
            old_counter_7770 = atomic_add(&((volatile __global
                                             int *) counter_mem_7748)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7758)[0] = old_counter_7770 ==
                num_groups_7403 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7771 = ((__local bool *) sync_arr_mem_7758)[0];
    
    if (is_last_group_7771) {
        if (local_tid_7754 == 0) {
            old_counter_7770 = atomic_add(&((volatile __global
                                             int *) counter_mem_7748)[0],
                                          (int) (0 - num_groups_7403));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7754, num_groups_7403)) {
                x_7237 = ((__global
                           double *) group_res_arr_mem_7750)[local_tid_7754 *
                                                             segred_group_sizze_7401];
            } else {
                x_7237 = 0.0;
            }
            ((__local double *) red_arr_mem_7760)[local_tid_7754] = x_7237;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7772;
            int32_t skip_waves_7773;
            double x_7764;
            double x_7765;
            
            offset_7772 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7754, segred_group_sizze_7401)) {
                    x_7764 = ((__local
                               double *) red_arr_mem_7760)[local_tid_7754 +
                                                           offset_7772];
                }
            }
            offset_7772 = 1;
            while (slt32(offset_7772, wave_sizze_7756)) {
                if (slt32(local_tid_7754 + offset_7772,
                          segred_group_sizze_7401) && ((local_tid_7754 -
                                                        squot32(local_tid_7754,
                                                                wave_sizze_7756) *
                                                        wave_sizze_7756) & (2 *
                                                                            offset_7772 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7765 = ((volatile __local
                                   double *) red_arr_mem_7760)[local_tid_7754 +
                                                               offset_7772];
                    }
                    // apply reduction operation
                    {
                        double res_7766 = x_7764 + x_7765;
                        
                        x_7764 = res_7766;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_7760)[local_tid_7754] = x_7764;
                    }
                }
                offset_7772 *= 2;
            }
            skip_waves_7773 = 1;
            while (slt32(skip_waves_7773, squot32(segred_group_sizze_7401 +
                                                  wave_sizze_7756 - 1,
                                                  wave_sizze_7756))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7772 = skip_waves_7773 * wave_sizze_7756;
                if (slt32(local_tid_7754 + offset_7772,
                          segred_group_sizze_7401) && ((local_tid_7754 -
                                                        squot32(local_tid_7754,
                                                                wave_sizze_7756) *
                                                        wave_sizze_7756) == 0 &&
                                                       (squot32(local_tid_7754,
                                                                wave_sizze_7756) &
                                                        (2 * skip_waves_7773 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7765 = ((__local
                                   double *) red_arr_mem_7760)[local_tid_7754 +
                                                               offset_7772];
                    }
                    // apply reduction operation
                    {
                        double res_7766 = x_7764 + x_7765;
                        
                        x_7764 = res_7766;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_7760)[local_tid_7754] =
                            x_7764;
                    }
                }
                skip_waves_7773 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7754 == 0) {
                    ((__global double *) mem_7469)[0] = x_7764;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7419(__local volatile
                                 int64_t *sync_arr_mem_7786_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7788_backing_aligned_1,
                                 int32_t sizze_7247, int32_t num_groups_7414,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *x_mem_7457, __global
                                 unsigned char *mem_7461, __global
                                 unsigned char *counter_mem_7776, __global
                                 unsigned char *group_res_arr_mem_7778,
                                 int32_t num_threads_7780)
{
    const int32_t segred_group_sizze_7412 =
                  kullback_liebler_f32zisegred_group_sizze_7411;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7786_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7786_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7788_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7788_backing_aligned_1;
    int32_t global_tid_7781;
    int32_t local_tid_7782;
    int32_t group_sizze_7785;
    int32_t wave_sizze_7784;
    int32_t group_tid_7783;
    
    global_tid_7781 = get_global_id(0);
    local_tid_7782 = get_local_id(0);
    group_sizze_7785 = get_local_size(0);
    wave_sizze_7784 = LOCKSTEP_WIDTH;
    group_tid_7783 = get_group_id(0);
    
    int32_t phys_tid_7419 = global_tid_7781;
    __local char *sync_arr_mem_7786;
    
    sync_arr_mem_7786 = (__local char *) sync_arr_mem_7786_backing_0;
    
    __local char *red_arr_mem_7788;
    
    red_arr_mem_7788 = (__local char *) red_arr_mem_7788_backing_1;
    
    int32_t dummy_7417 = 0;
    int32_t gtid_7418;
    
    gtid_7418 = 0;
    
    float x_acc_7790;
    int32_t chunk_sizze_7791 = smin32(squot32(sizze_7247 +
                                              segred_group_sizze_7412 *
                                              num_groups_7414 - 1,
                                              segred_group_sizze_7412 *
                                              num_groups_7414),
                                      squot32(sizze_7247 - phys_tid_7419 +
                                              num_threads_7780 - 1,
                                              num_threads_7780));
    float x_7259;
    float x_7260;
    
    // neutral-initialise the accumulators
    {
        x_acc_7790 = 0.0F;
    }
    for (int32_t i_7795 = 0; i_7795 < chunk_sizze_7791; i_7795++) {
        gtid_7418 = phys_tid_7419 + num_threads_7780 * i_7795;
        // apply map function
        {
            float x_7262 = ((__global float *) x_mem_7456)[gtid_7418];
            float x_7263 = ((__global float *) x_mem_7457)[gtid_7418];
            float res_7264 = x_7262 / x_7263;
            float res_7265;
            
            res_7265 = futrts_log32(res_7264);
            
            float res_7266 = x_7262 * res_7265;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7259 = x_acc_7790;
            }
            // load new values
            {
                x_7260 = res_7266;
            }
            // apply reduction operator
            {
                float res_7261 = x_7259 + x_7260;
                
                // store in accumulator
                {
                    x_acc_7790 = res_7261;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7259 = x_acc_7790;
        ((__local float *) red_arr_mem_7788)[local_tid_7782] = x_7259;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7796;
    int32_t skip_waves_7797;
    float x_7792;
    float x_7793;
    
    offset_7796 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7782, segred_group_sizze_7412)) {
            x_7792 = ((__local float *) red_arr_mem_7788)[local_tid_7782 +
                                                          offset_7796];
        }
    }
    offset_7796 = 1;
    while (slt32(offset_7796, wave_sizze_7784)) {
        if (slt32(local_tid_7782 + offset_7796, segred_group_sizze_7412) &&
            ((local_tid_7782 - squot32(local_tid_7782, wave_sizze_7784) *
              wave_sizze_7784) & (2 * offset_7796 - 1)) == 0) {
            // read array element
            {
                x_7793 = ((volatile __local
                           float *) red_arr_mem_7788)[local_tid_7782 +
                                                      offset_7796];
            }
            // apply reduction operation
            {
                float res_7794 = x_7792 + x_7793;
                
                x_7792 = res_7794;
            }
            // write result of operation
            {
                ((volatile __local float *) red_arr_mem_7788)[local_tid_7782] =
                    x_7792;
            }
        }
        offset_7796 *= 2;
    }
    skip_waves_7797 = 1;
    while (slt32(skip_waves_7797, squot32(segred_group_sizze_7412 +
                                          wave_sizze_7784 - 1,
                                          wave_sizze_7784))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7796 = skip_waves_7797 * wave_sizze_7784;
        if (slt32(local_tid_7782 + offset_7796, segred_group_sizze_7412) &&
            ((local_tid_7782 - squot32(local_tid_7782, wave_sizze_7784) *
              wave_sizze_7784) == 0 && (squot32(local_tid_7782,
                                                wave_sizze_7784) & (2 *
                                                                    skip_waves_7797 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7793 = ((__local float *) red_arr_mem_7788)[local_tid_7782 +
                                                              offset_7796];
            }
            // apply reduction operation
            {
                float res_7794 = x_7792 + x_7793;
                
                x_7792 = res_7794;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_7788)[local_tid_7782] = x_7792;
            }
        }
        skip_waves_7797 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7782 == 0) {
            x_acc_7790 = x_7792;
        }
    }
    
    int32_t old_counter_7798;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7782 == 0) {
            ((__global float *) group_res_arr_mem_7778)[group_tid_7783 *
                                                        segred_group_sizze_7412] =
                x_acc_7790;
            mem_fence_global();
            old_counter_7798 = atomic_add(&((volatile __global
                                             int *) counter_mem_7776)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7786)[0] = old_counter_7798 ==
                num_groups_7414 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7799 = ((__local bool *) sync_arr_mem_7786)[0];
    
    if (is_last_group_7799) {
        if (local_tid_7782 == 0) {
            old_counter_7798 = atomic_add(&((volatile __global
                                             int *) counter_mem_7776)[0],
                                          (int) (0 - num_groups_7414));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7782, num_groups_7414)) {
                x_7259 = ((__global
                           float *) group_res_arr_mem_7778)[local_tid_7782 *
                                                            segred_group_sizze_7412];
            } else {
                x_7259 = 0.0F;
            }
            ((__local float *) red_arr_mem_7788)[local_tid_7782] = x_7259;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7800;
            int32_t skip_waves_7801;
            float x_7792;
            float x_7793;
            
            offset_7800 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7782, segred_group_sizze_7412)) {
                    x_7792 = ((__local
                               float *) red_arr_mem_7788)[local_tid_7782 +
                                                          offset_7800];
                }
            }
            offset_7800 = 1;
            while (slt32(offset_7800, wave_sizze_7784)) {
                if (slt32(local_tid_7782 + offset_7800,
                          segred_group_sizze_7412) && ((local_tid_7782 -
                                                        squot32(local_tid_7782,
                                                                wave_sizze_7784) *
                                                        wave_sizze_7784) & (2 *
                                                                            offset_7800 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7793 = ((volatile __local
                                   float *) red_arr_mem_7788)[local_tid_7782 +
                                                              offset_7800];
                    }
                    // apply reduction operation
                    {
                        float res_7794 = x_7792 + x_7793;
                        
                        x_7792 = res_7794;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_7788)[local_tid_7782] = x_7792;
                    }
                }
                offset_7800 *= 2;
            }
            skip_waves_7801 = 1;
            while (slt32(skip_waves_7801, squot32(segred_group_sizze_7412 +
                                                  wave_sizze_7784 - 1,
                                                  wave_sizze_7784))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7800 = skip_waves_7801 * wave_sizze_7784;
                if (slt32(local_tid_7782 + offset_7800,
                          segred_group_sizze_7412) && ((local_tid_7782 -
                                                        squot32(local_tid_7782,
                                                                wave_sizze_7784) *
                                                        wave_sizze_7784) == 0 &&
                                                       (squot32(local_tid_7782,
                                                                wave_sizze_7784) &
                                                        (2 * skip_waves_7801 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7793 = ((__local
                                   float *) red_arr_mem_7788)[local_tid_7782 +
                                                              offset_7800];
                    }
                    // apply reduction operation
                    {
                        float res_7794 = x_7792 + x_7793;
                        
                        x_7792 = res_7794;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_7788)[local_tid_7782] =
                            x_7792;
                    }
                }
                skip_waves_7801 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7782 == 0) {
                    ((__global float *) mem_7461)[0] = x_7792;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7430(__local volatile
                                 int64_t *sync_arr_mem_7814_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7816_backing_aligned_1,
                                 int32_t sizze_7267, int32_t num_groups_7425,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *mem_7461, __global
                                 unsigned char *counter_mem_7804, __global
                                 unsigned char *group_res_arr_mem_7806,
                                 int32_t num_threads_7808)
{
    const int32_t segred_group_sizze_7423 =
                  kullback_liebler_scaled_f32zisegred_group_sizze_7422;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7814_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7814_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7816_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7816_backing_aligned_1;
    int32_t global_tid_7809;
    int32_t local_tid_7810;
    int32_t group_sizze_7813;
    int32_t wave_sizze_7812;
    int32_t group_tid_7811;
    
    global_tid_7809 = get_global_id(0);
    local_tid_7810 = get_local_id(0);
    group_sizze_7813 = get_local_size(0);
    wave_sizze_7812 = LOCKSTEP_WIDTH;
    group_tid_7811 = get_group_id(0);
    
    int32_t phys_tid_7430 = global_tid_7809;
    __local char *sync_arr_mem_7814;
    
    sync_arr_mem_7814 = (__local char *) sync_arr_mem_7814_backing_0;
    
    __local char *red_arr_mem_7816;
    
    red_arr_mem_7816 = (__local char *) red_arr_mem_7816_backing_1;
    
    int32_t dummy_7428 = 0;
    int32_t gtid_7429;
    
    gtid_7429 = 0;
    
    float x_acc_7818;
    int32_t chunk_sizze_7819 = smin32(squot32(sizze_7267 +
                                              segred_group_sizze_7423 *
                                              num_groups_7425 - 1,
                                              segred_group_sizze_7423 *
                                              num_groups_7425),
                                      squot32(sizze_7267 - phys_tid_7430 +
                                              num_threads_7808 - 1,
                                              num_threads_7808));
    float x_7272;
    float x_7273;
    
    // neutral-initialise the accumulators
    {
        x_acc_7818 = 0.0F;
    }
    for (int32_t i_7823 = 0; i_7823 < chunk_sizze_7819; i_7823++) {
        gtid_7429 = phys_tid_7430 + num_threads_7808 * i_7823;
        // apply map function
        {
            float x_7275 = ((__global float *) x_mem_7456)[gtid_7429];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7272 = x_acc_7818;
            }
            // load new values
            {
                x_7273 = x_7275;
            }
            // apply reduction operator
            {
                float res_7274 = x_7272 + x_7273;
                
                // store in accumulator
                {
                    x_acc_7818 = res_7274;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7272 = x_acc_7818;
        ((__local float *) red_arr_mem_7816)[local_tid_7810] = x_7272;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7824;
    int32_t skip_waves_7825;
    float x_7820;
    float x_7821;
    
    offset_7824 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7810, segred_group_sizze_7423)) {
            x_7820 = ((__local float *) red_arr_mem_7816)[local_tid_7810 +
                                                          offset_7824];
        }
    }
    offset_7824 = 1;
    while (slt32(offset_7824, wave_sizze_7812)) {
        if (slt32(local_tid_7810 + offset_7824, segred_group_sizze_7423) &&
            ((local_tid_7810 - squot32(local_tid_7810, wave_sizze_7812) *
              wave_sizze_7812) & (2 * offset_7824 - 1)) == 0) {
            // read array element
            {
                x_7821 = ((volatile __local
                           float *) red_arr_mem_7816)[local_tid_7810 +
                                                      offset_7824];
            }
            // apply reduction operation
            {
                float res_7822 = x_7820 + x_7821;
                
                x_7820 = res_7822;
            }
            // write result of operation
            {
                ((volatile __local float *) red_arr_mem_7816)[local_tid_7810] =
                    x_7820;
            }
        }
        offset_7824 *= 2;
    }
    skip_waves_7825 = 1;
    while (slt32(skip_waves_7825, squot32(segred_group_sizze_7423 +
                                          wave_sizze_7812 - 1,
                                          wave_sizze_7812))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7824 = skip_waves_7825 * wave_sizze_7812;
        if (slt32(local_tid_7810 + offset_7824, segred_group_sizze_7423) &&
            ((local_tid_7810 - squot32(local_tid_7810, wave_sizze_7812) *
              wave_sizze_7812) == 0 && (squot32(local_tid_7810,
                                                wave_sizze_7812) & (2 *
                                                                    skip_waves_7825 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7821 = ((__local float *) red_arr_mem_7816)[local_tid_7810 +
                                                              offset_7824];
            }
            // apply reduction operation
            {
                float res_7822 = x_7820 + x_7821;
                
                x_7820 = res_7822;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_7816)[local_tid_7810] = x_7820;
            }
        }
        skip_waves_7825 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7810 == 0) {
            x_acc_7818 = x_7820;
        }
    }
    
    int32_t old_counter_7826;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7810 == 0) {
            ((__global float *) group_res_arr_mem_7806)[group_tid_7811 *
                                                        segred_group_sizze_7423] =
                x_acc_7818;
            mem_fence_global();
            old_counter_7826 = atomic_add(&((volatile __global
                                             int *) counter_mem_7804)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7814)[0] = old_counter_7826 ==
                num_groups_7425 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7827 = ((__local bool *) sync_arr_mem_7814)[0];
    
    if (is_last_group_7827) {
        if (local_tid_7810 == 0) {
            old_counter_7826 = atomic_add(&((volatile __global
                                             int *) counter_mem_7804)[0],
                                          (int) (0 - num_groups_7425));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7810, num_groups_7425)) {
                x_7272 = ((__global
                           float *) group_res_arr_mem_7806)[local_tid_7810 *
                                                            segred_group_sizze_7423];
            } else {
                x_7272 = 0.0F;
            }
            ((__local float *) red_arr_mem_7816)[local_tid_7810] = x_7272;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7828;
            int32_t skip_waves_7829;
            float x_7820;
            float x_7821;
            
            offset_7828 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7810, segred_group_sizze_7423)) {
                    x_7820 = ((__local
                               float *) red_arr_mem_7816)[local_tid_7810 +
                                                          offset_7828];
                }
            }
            offset_7828 = 1;
            while (slt32(offset_7828, wave_sizze_7812)) {
                if (slt32(local_tid_7810 + offset_7828,
                          segred_group_sizze_7423) && ((local_tid_7810 -
                                                        squot32(local_tid_7810,
                                                                wave_sizze_7812) *
                                                        wave_sizze_7812) & (2 *
                                                                            offset_7828 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7821 = ((volatile __local
                                   float *) red_arr_mem_7816)[local_tid_7810 +
                                                              offset_7828];
                    }
                    // apply reduction operation
                    {
                        float res_7822 = x_7820 + x_7821;
                        
                        x_7820 = res_7822;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_7816)[local_tid_7810] = x_7820;
                    }
                }
                offset_7828 *= 2;
            }
            skip_waves_7829 = 1;
            while (slt32(skip_waves_7829, squot32(segred_group_sizze_7423 +
                                                  wave_sizze_7812 - 1,
                                                  wave_sizze_7812))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7828 = skip_waves_7829 * wave_sizze_7812;
                if (slt32(local_tid_7810 + offset_7828,
                          segred_group_sizze_7423) && ((local_tid_7810 -
                                                        squot32(local_tid_7810,
                                                                wave_sizze_7812) *
                                                        wave_sizze_7812) == 0 &&
                                                       (squot32(local_tid_7810,
                                                                wave_sizze_7812) &
                                                        (2 * skip_waves_7829 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7821 = ((__local
                                   float *) red_arr_mem_7816)[local_tid_7810 +
                                                              offset_7828];
                    }
                    // apply reduction operation
                    {
                        float res_7822 = x_7820 + x_7821;
                        
                        x_7820 = res_7822;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_7816)[local_tid_7810] =
                            x_7820;
                    }
                }
                skip_waves_7829 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7810 == 0) {
                    ((__global float *) mem_7461)[0] = x_7820;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7441(__local volatile
                                 int64_t *sync_arr_mem_7841_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7843_backing_aligned_1,
                                 int32_t sizze_7268, int32_t num_groups_7436,
                                 __global unsigned char *y_mem_7457, __global
                                 unsigned char *mem_7465, __global
                                 unsigned char *counter_mem_7831, __global
                                 unsigned char *group_res_arr_mem_7833,
                                 int32_t num_threads_7835)
{
    const int32_t segred_group_sizze_7434 =
                  kullback_liebler_scaled_f32zisegred_group_sizze_7433;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7841_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7841_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7843_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7843_backing_aligned_1;
    int32_t global_tid_7836;
    int32_t local_tid_7837;
    int32_t group_sizze_7840;
    int32_t wave_sizze_7839;
    int32_t group_tid_7838;
    
    global_tid_7836 = get_global_id(0);
    local_tid_7837 = get_local_id(0);
    group_sizze_7840 = get_local_size(0);
    wave_sizze_7839 = LOCKSTEP_WIDTH;
    group_tid_7838 = get_group_id(0);
    
    int32_t phys_tid_7441 = global_tid_7836;
    __local char *sync_arr_mem_7841;
    
    sync_arr_mem_7841 = (__local char *) sync_arr_mem_7841_backing_0;
    
    __local char *red_arr_mem_7843;
    
    red_arr_mem_7843 = (__local char *) red_arr_mem_7843_backing_1;
    
    int32_t dummy_7439 = 0;
    int32_t gtid_7440;
    
    gtid_7440 = 0;
    
    float x_acc_7845;
    int32_t chunk_sizze_7846 = smin32(squot32(sizze_7268 +
                                              segred_group_sizze_7434 *
                                              num_groups_7436 - 1,
                                              segred_group_sizze_7434 *
                                              num_groups_7436),
                                      squot32(sizze_7268 - phys_tid_7441 +
                                              num_threads_7835 - 1,
                                              num_threads_7835));
    float x_7278;
    float x_7279;
    
    // neutral-initialise the accumulators
    {
        x_acc_7845 = 0.0F;
    }
    for (int32_t i_7850 = 0; i_7850 < chunk_sizze_7846; i_7850++) {
        gtid_7440 = phys_tid_7441 + num_threads_7835 * i_7850;
        // apply map function
        {
            float x_7281 = ((__global float *) y_mem_7457)[gtid_7440];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7278 = x_acc_7845;
            }
            // load new values
            {
                x_7279 = x_7281;
            }
            // apply reduction operator
            {
                float res_7280 = x_7278 + x_7279;
                
                // store in accumulator
                {
                    x_acc_7845 = res_7280;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7278 = x_acc_7845;
        ((__local float *) red_arr_mem_7843)[local_tid_7837] = x_7278;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7851;
    int32_t skip_waves_7852;
    float x_7847;
    float x_7848;
    
    offset_7851 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7837, segred_group_sizze_7434)) {
            x_7847 = ((__local float *) red_arr_mem_7843)[local_tid_7837 +
                                                          offset_7851];
        }
    }
    offset_7851 = 1;
    while (slt32(offset_7851, wave_sizze_7839)) {
        if (slt32(local_tid_7837 + offset_7851, segred_group_sizze_7434) &&
            ((local_tid_7837 - squot32(local_tid_7837, wave_sizze_7839) *
              wave_sizze_7839) & (2 * offset_7851 - 1)) == 0) {
            // read array element
            {
                x_7848 = ((volatile __local
                           float *) red_arr_mem_7843)[local_tid_7837 +
                                                      offset_7851];
            }
            // apply reduction operation
            {
                float res_7849 = x_7847 + x_7848;
                
                x_7847 = res_7849;
            }
            // write result of operation
            {
                ((volatile __local float *) red_arr_mem_7843)[local_tid_7837] =
                    x_7847;
            }
        }
        offset_7851 *= 2;
    }
    skip_waves_7852 = 1;
    while (slt32(skip_waves_7852, squot32(segred_group_sizze_7434 +
                                          wave_sizze_7839 - 1,
                                          wave_sizze_7839))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7851 = skip_waves_7852 * wave_sizze_7839;
        if (slt32(local_tid_7837 + offset_7851, segred_group_sizze_7434) &&
            ((local_tid_7837 - squot32(local_tid_7837, wave_sizze_7839) *
              wave_sizze_7839) == 0 && (squot32(local_tid_7837,
                                                wave_sizze_7839) & (2 *
                                                                    skip_waves_7852 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7848 = ((__local float *) red_arr_mem_7843)[local_tid_7837 +
                                                              offset_7851];
            }
            // apply reduction operation
            {
                float res_7849 = x_7847 + x_7848;
                
                x_7847 = res_7849;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_7843)[local_tid_7837] = x_7847;
            }
        }
        skip_waves_7852 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7837 == 0) {
            x_acc_7845 = x_7847;
        }
    }
    
    int32_t old_counter_7853;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7837 == 0) {
            ((__global float *) group_res_arr_mem_7833)[group_tid_7838 *
                                                        segred_group_sizze_7434] =
                x_acc_7845;
            mem_fence_global();
            old_counter_7853 = atomic_add(&((volatile __global
                                             int *) counter_mem_7831)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7841)[0] = old_counter_7853 ==
                num_groups_7436 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7854 = ((__local bool *) sync_arr_mem_7841)[0];
    
    if (is_last_group_7854) {
        if (local_tid_7837 == 0) {
            old_counter_7853 = atomic_add(&((volatile __global
                                             int *) counter_mem_7831)[0],
                                          (int) (0 - num_groups_7436));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7837, num_groups_7436)) {
                x_7278 = ((__global
                           float *) group_res_arr_mem_7833)[local_tid_7837 *
                                                            segred_group_sizze_7434];
            } else {
                x_7278 = 0.0F;
            }
            ((__local float *) red_arr_mem_7843)[local_tid_7837] = x_7278;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7855;
            int32_t skip_waves_7856;
            float x_7847;
            float x_7848;
            
            offset_7855 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7837, segred_group_sizze_7434)) {
                    x_7847 = ((__local
                               float *) red_arr_mem_7843)[local_tid_7837 +
                                                          offset_7855];
                }
            }
            offset_7855 = 1;
            while (slt32(offset_7855, wave_sizze_7839)) {
                if (slt32(local_tid_7837 + offset_7855,
                          segred_group_sizze_7434) && ((local_tid_7837 -
                                                        squot32(local_tid_7837,
                                                                wave_sizze_7839) *
                                                        wave_sizze_7839) & (2 *
                                                                            offset_7855 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7848 = ((volatile __local
                                   float *) red_arr_mem_7843)[local_tid_7837 +
                                                              offset_7855];
                    }
                    // apply reduction operation
                    {
                        float res_7849 = x_7847 + x_7848;
                        
                        x_7847 = res_7849;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_7843)[local_tid_7837] = x_7847;
                    }
                }
                offset_7855 *= 2;
            }
            skip_waves_7856 = 1;
            while (slt32(skip_waves_7856, squot32(segred_group_sizze_7434 +
                                                  wave_sizze_7839 - 1,
                                                  wave_sizze_7839))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7855 = skip_waves_7856 * wave_sizze_7839;
                if (slt32(local_tid_7837 + offset_7855,
                          segred_group_sizze_7434) && ((local_tid_7837 -
                                                        squot32(local_tid_7837,
                                                                wave_sizze_7839) *
                                                        wave_sizze_7839) == 0 &&
                                                       (squot32(local_tid_7837,
                                                                wave_sizze_7839) &
                                                        (2 * skip_waves_7856 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7848 = ((__local
                                   float *) red_arr_mem_7843)[local_tid_7837 +
                                                              offset_7855];
                    }
                    // apply reduction operation
                    {
                        float res_7849 = x_7847 + x_7848;
                        
                        x_7847 = res_7849;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_7843)[local_tid_7837] =
                            x_7847;
                    }
                }
                skip_waves_7856 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7837 == 0) {
                    ((__global float *) mem_7465)[0] = x_7847;
                }
            }
        }
    }
}
__kernel void segred_nonseg_7452(__local volatile
                                 int64_t *sync_arr_mem_7868_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_7870_backing_aligned_1,
                                 int32_t sizze_7267, float res_7271,
                                 float res_7277, int32_t num_groups_7447,
                                 __global unsigned char *x_mem_7456, __global
                                 unsigned char *y_mem_7457, __global
                                 unsigned char *mem_7469, __global
                                 unsigned char *counter_mem_7858, __global
                                 unsigned char *group_res_arr_mem_7860,
                                 int32_t num_threads_7862)
{
    const int32_t segred_group_sizze_7445 =
                  kullback_liebler_scaled_f32zisegred_group_sizze_7444;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_7868_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_7868_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_7870_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_7870_backing_aligned_1;
    int32_t global_tid_7863;
    int32_t local_tid_7864;
    int32_t group_sizze_7867;
    int32_t wave_sizze_7866;
    int32_t group_tid_7865;
    
    global_tid_7863 = get_global_id(0);
    local_tid_7864 = get_local_id(0);
    group_sizze_7867 = get_local_size(0);
    wave_sizze_7866 = LOCKSTEP_WIDTH;
    group_tid_7865 = get_group_id(0);
    
    int32_t phys_tid_7452 = global_tid_7863;
    __local char *sync_arr_mem_7868;
    
    sync_arr_mem_7868 = (__local char *) sync_arr_mem_7868_backing_0;
    
    __local char *red_arr_mem_7870;
    
    red_arr_mem_7870 = (__local char *) red_arr_mem_7870_backing_1;
    
    int32_t dummy_7450 = 0;
    int32_t gtid_7451;
    
    gtid_7451 = 0;
    
    float x_acc_7872;
    int32_t chunk_sizze_7873 = smin32(squot32(sizze_7267 +
                                              segred_group_sizze_7445 *
                                              num_groups_7447 - 1,
                                              segred_group_sizze_7445 *
                                              num_groups_7447),
                                      squot32(sizze_7267 - phys_tid_7452 +
                                              num_threads_7862 - 1,
                                              num_threads_7862));
    float x_7289;
    float x_7290;
    
    // neutral-initialise the accumulators
    {
        x_acc_7872 = 0.0F;
    }
    for (int32_t i_7877 = 0; i_7877 < chunk_sizze_7873; i_7877++) {
        gtid_7451 = phys_tid_7452 + num_threads_7862 * i_7877;
        // apply map function
        {
            float x_7292 = ((__global float *) x_mem_7456)[gtid_7451];
            float x_7293 = ((__global float *) y_mem_7457)[gtid_7451];
            float res_7294 = x_7292 / res_7271;
            float res_7295 = x_7293 / res_7277;
            float res_7296 = res_7294 / res_7295;
            float res_7297;
            
            res_7297 = futrts_log32(res_7296);
            
            float res_7298 = res_7294 * res_7297;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_7289 = x_acc_7872;
            }
            // load new values
            {
                x_7290 = res_7298;
            }
            // apply reduction operator
            {
                float res_7291 = x_7289 + x_7290;
                
                // store in accumulator
                {
                    x_acc_7872 = res_7291;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_7289 = x_acc_7872;
        ((__local float *) red_arr_mem_7870)[local_tid_7864] = x_7289;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_7878;
    int32_t skip_waves_7879;
    float x_7874;
    float x_7875;
    
    offset_7878 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_7864, segred_group_sizze_7445)) {
            x_7874 = ((__local float *) red_arr_mem_7870)[local_tid_7864 +
                                                          offset_7878];
        }
    }
    offset_7878 = 1;
    while (slt32(offset_7878, wave_sizze_7866)) {
        if (slt32(local_tid_7864 + offset_7878, segred_group_sizze_7445) &&
            ((local_tid_7864 - squot32(local_tid_7864, wave_sizze_7866) *
              wave_sizze_7866) & (2 * offset_7878 - 1)) == 0) {
            // read array element
            {
                x_7875 = ((volatile __local
                           float *) red_arr_mem_7870)[local_tid_7864 +
                                                      offset_7878];
            }
            // apply reduction operation
            {
                float res_7876 = x_7874 + x_7875;
                
                x_7874 = res_7876;
            }
            // write result of operation
            {
                ((volatile __local float *) red_arr_mem_7870)[local_tid_7864] =
                    x_7874;
            }
        }
        offset_7878 *= 2;
    }
    skip_waves_7879 = 1;
    while (slt32(skip_waves_7879, squot32(segred_group_sizze_7445 +
                                          wave_sizze_7866 - 1,
                                          wave_sizze_7866))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_7878 = skip_waves_7879 * wave_sizze_7866;
        if (slt32(local_tid_7864 + offset_7878, segred_group_sizze_7445) &&
            ((local_tid_7864 - squot32(local_tid_7864, wave_sizze_7866) *
              wave_sizze_7866) == 0 && (squot32(local_tid_7864,
                                                wave_sizze_7866) & (2 *
                                                                    skip_waves_7879 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_7875 = ((__local float *) red_arr_mem_7870)[local_tid_7864 +
                                                              offset_7878];
            }
            // apply reduction operation
            {
                float res_7876 = x_7874 + x_7875;
                
                x_7874 = res_7876;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_7870)[local_tid_7864] = x_7874;
            }
        }
        skip_waves_7879 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_7864 == 0) {
            x_acc_7872 = x_7874;
        }
    }
    
    int32_t old_counter_7880;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_7864 == 0) {
            ((__global float *) group_res_arr_mem_7860)[group_tid_7865 *
                                                        segred_group_sizze_7445] =
                x_acc_7872;
            mem_fence_global();
            old_counter_7880 = atomic_add(&((volatile __global
                                             int *) counter_mem_7858)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_7868)[0] = old_counter_7880 ==
                num_groups_7447 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_7881 = ((__local bool *) sync_arr_mem_7868)[0];
    
    if (is_last_group_7881) {
        if (local_tid_7864 == 0) {
            old_counter_7880 = atomic_add(&((volatile __global
                                             int *) counter_mem_7858)[0],
                                          (int) (0 - num_groups_7447));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_7864, num_groups_7447)) {
                x_7289 = ((__global
                           float *) group_res_arr_mem_7860)[local_tid_7864 *
                                                            segred_group_sizze_7445];
            } else {
                x_7289 = 0.0F;
            }
            ((__local float *) red_arr_mem_7870)[local_tid_7864] = x_7289;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_7882;
            int32_t skip_waves_7883;
            float x_7874;
            float x_7875;
            
            offset_7882 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_7864, segred_group_sizze_7445)) {
                    x_7874 = ((__local
                               float *) red_arr_mem_7870)[local_tid_7864 +
                                                          offset_7882];
                }
            }
            offset_7882 = 1;
            while (slt32(offset_7882, wave_sizze_7866)) {
                if (slt32(local_tid_7864 + offset_7882,
                          segred_group_sizze_7445) && ((local_tid_7864 -
                                                        squot32(local_tid_7864,
                                                                wave_sizze_7866) *
                                                        wave_sizze_7866) & (2 *
                                                                            offset_7882 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_7875 = ((volatile __local
                                   float *) red_arr_mem_7870)[local_tid_7864 +
                                                              offset_7882];
                    }
                    // apply reduction operation
                    {
                        float res_7876 = x_7874 + x_7875;
                        
                        x_7874 = res_7876;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_7870)[local_tid_7864] = x_7874;
                    }
                }
                offset_7882 *= 2;
            }
            skip_waves_7883 = 1;
            while (slt32(skip_waves_7883, squot32(segred_group_sizze_7445 +
                                                  wave_sizze_7866 - 1,
                                                  wave_sizze_7866))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_7882 = skip_waves_7883 * wave_sizze_7866;
                if (slt32(local_tid_7864 + offset_7882,
                          segred_group_sizze_7445) && ((local_tid_7864 -
                                                        squot32(local_tid_7864,
                                                                wave_sizze_7866) *
                                                        wave_sizze_7866) == 0 &&
                                                       (squot32(local_tid_7864,
                                                                wave_sizze_7866) &
                                                        (2 * skip_waves_7883 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_7875 = ((__local
                                   float *) red_arr_mem_7870)[local_tid_7864 +
                                                              offset_7882];
                    }
                    // apply reduction operation
                    {
                        float res_7876 = x_7874 + x_7875;
                        
                        x_7874 = res_7876;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_7870)[local_tid_7864] =
                            x_7874;
                    }
                }
                skip_waves_7883 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_7864 == 0) {
                    ((__global float *) mem_7469)[0] = x_7874;
                }
            }
        }
    }
}
"""
# Start of values.py.

# Hacky parser/reader/writer for values written in Futhark syntax.
# Used for reading stdin when compiling standalone programs with the
# Python code generator.

import numpy as np
import string
import struct
import sys

class ReaderInput:
    def __init__(self, f):
        self.f = f
        self.lookahead_buffer = []

    def get_char(self):
        if len(self.lookahead_buffer) == 0:
            return self.f.read(1)
        else:
            c = self.lookahead_buffer[0]
            self.lookahead_buffer = self.lookahead_buffer[1:]
            return c

    def unget_char(self, c):
        self.lookahead_buffer = [c] + self.lookahead_buffer

    def get_chars(self, n):
        n1 = min(n, len(self.lookahead_buffer))
        s = b''.join(self.lookahead_buffer[:n1])
        self.lookahead_buffer = self.lookahead_buffer[n1:]
        n2 = n - n1
        if n2 > 0:
            s += self.f.read(n2)
        return s

    def peek_char(self):
        c = self.get_char()
        if c:
            self.unget_char(c)
        return c

def skip_spaces(f):
    c = f.get_char()
    while c != None:
        if c.isspace():
            c = f.get_char()
        elif c == b'-':
          # May be line comment.
          if f.peek_char() == b'-':
            # Yes, line comment. Skip to end of line.
            while (c != b'\n' and c != None):
              c = f.get_char()
          else:
            break
        else:
          break
    if c:
        f.unget_char(c)

def parse_specific_char(f, expected):
    got = f.get_char()
    if got != expected:
        f.unget_char(got)
        raise ValueError
    return True

def parse_specific_string(f, s):
    # This funky mess is intended, and is caused by the fact that if `type(b) ==
    # bytes` then `type(b[0]) == int`, but we need to match each element with a
    # `bytes`, so therefore we make each character an array element
    b = s.encode('utf8')
    bs = [b[i:i+1] for i in range(len(b))]
    read = []
    try:
        for c in bs:
            parse_specific_char(f, c)
            read.append(c)
        return True
    except ValueError:
        for c in read[::-1]:
            f.unget_char(c)
        raise

def optional(p, *args):
    try:
        return p(*args)
    except ValueError:
        return None

def optional_specific_string(f, s):
    c = f.peek_char()
    # This funky mess is intended, and is caused by the fact that if `type(b) ==
    # bytes` then `type(b[0]) == int`, but we need to match each element with a
    # `bytes`, so therefore we make each character an array element
    b = s.encode('utf8')
    bs = [b[i:i+1] for i in range(len(b))]
    if c == bs[0]:
        return parse_specific_string(f, s)
    else:
        return False

def sepBy(p, sep, *args):
    elems = []
    x = optional(p, *args)
    if x != None:
        elems += [x]
        while optional(sep, *args) != None:
            x = p(*args)
            elems += [x]
    return elems

# Assumes '0x' has already been read
def parse_hex_int(f):
    s = b''
    c = f.get_char()
    while c != None:
        if c in b'01234556789ABCDEFabcdef':
            s += c
            c = f.get_char()
        elif c == b'_':
            c = f.get_char() # skip _
        else:
            f.unget_char(c)
            break
    return str(int(s, 16)).encode('utf8') # ugh

def parse_int(f):
    s = b''
    c = f.get_char()
    if c == b'0' and f.peek_char() in b'xX':
        c = f.get_char() # skip X
        return parse_hex_int(f)
    else:
        while c != None:
            if c.isdigit():
                s += c
                c = f.get_char()
            elif c == b'_':
                c = f.get_char() # skip _
            else:
                f.unget_char(c)
                break
        if len(s) == 0:
            raise ValueError
        return s

def parse_int_signed(f):
    s = b''
    c = f.get_char()

    if c == b'-' and f.peek_char().isdigit():
      return c + parse_int(f)
    else:
      if c != b'+':
          f.unget_char(c)
      return parse_int(f)

def read_str_comma(f):
    skip_spaces(f)
    parse_specific_char(f, b',')
    return b','

def read_str_int(f, s):
    skip_spaces(f)
    x = int(parse_int_signed(f))
    optional_specific_string(f, s)
    return x

def read_str_uint(f, s):
    skip_spaces(f)
    x = int(parse_int(f))
    optional_specific_string(f, s)
    return x

def read_str_i8(f):
    return np.int8(read_str_int(f, 'i8'))
def read_str_i16(f):
    return np.int16(read_str_int(f, 'i16'))
def read_str_i32(f):
    return np.int32(read_str_int(f, 'i32'))
def read_str_i64(f):
    return np.int64(read_str_int(f, 'i64'))

def read_str_u8(f):
    return np.uint8(read_str_int(f, 'u8'))
def read_str_u16(f):
    return np.uint16(read_str_int(f, 'u16'))
def read_str_u32(f):
    return np.uint32(read_str_int(f, 'u32'))
def read_str_u64(f):
    return np.uint64(read_str_int(f, 'u64'))

def read_char(f):
    skip_spaces(f)
    parse_specific_char(f, b'\'')
    c = f.get_char()
    parse_specific_char(f, b'\'')
    return c

def read_str_hex_float(f, sign):
    int_part = parse_hex_int(f)
    parse_specific_char(f, b'.')
    frac_part = parse_hex_int(f)
    parse_specific_char(f, b'p')
    exponent = parse_int(f)

    int_val = int(int_part, 16)
    frac_val = float(int(frac_part, 16)) / (16 ** len(frac_part))
    exp_val = int(exponent)

    total_val = (int_val + frac_val) * (2.0 ** exp_val)
    if sign == b'-':
        total_val = -1 * total_val

    return float(total_val)


def read_str_decimal(f):
    skip_spaces(f)
    c = f.get_char()
    if (c == b'-'):
      sign = b'-'
    else:
      f.unget_char(c)
      sign = b''

    # Check for hexadecimal float
    c = f.get_char()
    if (c == '0' and (f.peek_char() in ['x', 'X'])):
        f.get_char()
        return read_str_hex_float(f, sign)
    else:
        f.unget_char(c)

    bef = optional(parse_int, f)
    if bef == None:
        bef = b'0'
        parse_specific_char(f, b'.')
        aft = parse_int(f)
    elif optional(parse_specific_char, f, b'.'):
        aft = parse_int(f)
    else:
        aft = b'0'
    if (optional(parse_specific_char, f, b'E') or
        optional(parse_specific_char, f, b'e')):
        expt = parse_int_signed(f)
    else:
        expt = b'0'
    return float(sign + bef + b'.' + aft + b'E' + expt)

def read_str_f32(f):
    skip_spaces(f)
    try:
        parse_specific_string(f, 'f32.nan')
        return np.float32(np.nan)
    except ValueError:
        try:
            parse_specific_string(f, 'f32.inf')
            return np.float32(np.inf)
        except ValueError:
            try:
               parse_specific_string(f, '-f32.inf')
               return np.float32(-np.inf)
            except ValueError:
               x = read_str_decimal(f)
               optional_specific_string(f, 'f32')
               return x

def read_str_f64(f):
    skip_spaces(f)
    try:
        parse_specific_string(f, 'f64.nan')
        return np.float64(np.nan)
    except ValueError:
        try:
            parse_specific_string(f, 'f64.inf')
            return np.float64(np.inf)
        except ValueError:
            try:
               parse_specific_string(f, '-f64.inf')
               return np.float64(-np.inf)
            except ValueError:
               x = read_str_decimal(f)
               optional_specific_string(f, 'f64')
               return x

def read_str_bool(f):
    skip_spaces(f)
    if f.peek_char() == b't':
        parse_specific_string(f, 'true')
        return True
    elif f.peek_char() == b'f':
        parse_specific_string(f, 'false')
        return False
    else:
        raise ValueError

def read_str_empty_array(f, type_name, rank):
    parse_specific_string(f, 'empty')
    parse_specific_char(f, b'(')
    smallest = 1
    for i in range(rank):
        parse_specific_string(f, '[')
        smallest = min(smallest, int(parse_int(f)))
        parse_specific_string(f, ']')
    if smallest != 0:
        raise ValueError
    parse_specific_string(f, type_name)
    parse_specific_char(f, b')')

    return None

def read_str_array_elems(f, elem_reader, type_name, rank):
    skip_spaces(f)
    try:
        parse_specific_char(f, b'[')
    except ValueError:
        return read_str_empty_array(f, type_name, rank)
    else:
        xs = sepBy(elem_reader, read_str_comma, f)
        skip_spaces(f)
        parse_specific_char(f, b']')
        return xs

def read_str_array_helper(f, elem_reader, type_name, rank):
    def nested_row_reader(_):
        return read_str_array_helper(f, elem_reader, type_name, rank-1)
    if rank == 1:
        row_reader = elem_reader
    else:
        row_reader = nested_row_reader
    return read_str_array_elems(f, row_reader, type_name, rank)

def expected_array_dims(l, rank):
  if rank > 1:
      n = len(l)
      if n == 0:
          elem = []
      else:
          elem = l[0]
      return [n] + expected_array_dims(elem, rank-1)
  else:
      return [len(l)]

def verify_array_dims(l, dims):
    if dims[0] != len(l):
        raise ValueError
    if len(dims) > 1:
        for x in l:
            verify_array_dims(x, dims[1:])

def read_str_array(f, elem_reader, type_name, rank, bt):
    elems = read_str_array_helper(f, elem_reader, type_name, rank)
    if elems == None:
        # Empty array
        return np.empty([0]*rank, dtype=bt)
    else:
        dims = expected_array_dims(elems, rank)
        verify_array_dims(elems, dims)
        return np.array(elems, dtype=bt)

################################################################################

READ_BINARY_VERSION = 2

# struct format specified at
# https://docs.python.org/2/library/struct.html#format-characters

def mk_bin_scalar_reader(t):
    def bin_reader(f):
        fmt = FUTHARK_PRIMTYPES[t]['bin_format']
        size = FUTHARK_PRIMTYPES[t]['size']
        return struct.unpack('<' + fmt, f.get_chars(size))[0]
    return bin_reader

read_bin_i8 = mk_bin_scalar_reader('i8')
read_bin_i16 = mk_bin_scalar_reader('i16')
read_bin_i32 = mk_bin_scalar_reader('i32')
read_bin_i64 = mk_bin_scalar_reader('i64')

read_bin_u8 = mk_bin_scalar_reader('u8')
read_bin_u16 = mk_bin_scalar_reader('u16')
read_bin_u32 = mk_bin_scalar_reader('u32')
read_bin_u64 = mk_bin_scalar_reader('u64')

read_bin_f32 = mk_bin_scalar_reader('f32')
read_bin_f64 = mk_bin_scalar_reader('f64')

read_bin_bool = mk_bin_scalar_reader('bool')

def read_is_binary(f):
    skip_spaces(f)
    c = f.get_char()
    if c == b'b':
        bin_version = read_bin_u8(f)
        if bin_version != READ_BINARY_VERSION:
            panic(1, "binary-input: File uses version %i, but I only understand version %i.\n",
                  bin_version, READ_BINARY_VERSION)
        return True
    else:
        f.unget_char(c)
        return False

FUTHARK_PRIMTYPES = {
    'i8':  {'binname' : b"  i8",
            'size' : 1,
            'bin_reader': read_bin_i8,
            'str_reader': read_str_i8,
            'bin_format': 'b',
            'numpy_type': np.int8 },

    'i16': {'binname' : b" i16",
            'size' : 2,
            'bin_reader': read_bin_i16,
            'str_reader': read_str_i16,
            'bin_format': 'h',
            'numpy_type': np.int16 },

    'i32': {'binname' : b" i32",
            'size' : 4,
            'bin_reader': read_bin_i32,
            'str_reader': read_str_i32,
            'bin_format': 'i',
            'numpy_type': np.int32 },

    'i64': {'binname' : b" i64",
            'size' : 8,
            'bin_reader': read_bin_i64,
            'str_reader': read_str_i64,
            'bin_format': 'q',
            'numpy_type': np.int64},

    'u8':  {'binname' : b"  u8",
            'size' : 1,
            'bin_reader': read_bin_u8,
            'str_reader': read_str_u8,
            'bin_format': 'B',
            'numpy_type': np.uint8 },

    'u16': {'binname' : b" u16",
            'size' : 2,
            'bin_reader': read_bin_u16,
            'str_reader': read_str_u16,
            'bin_format': 'H',
            'numpy_type': np.uint16 },

    'u32': {'binname' : b" u32",
            'size' : 4,
            'bin_reader': read_bin_u32,
            'str_reader': read_str_u32,
            'bin_format': 'I',
            'numpy_type': np.uint32 },

    'u64': {'binname' : b" u64",
            'size' : 8,
            'bin_reader': read_bin_u64,
            'str_reader': read_str_u64,
            'bin_format': 'Q',
            'numpy_type': np.uint64 },

    'f32': {'binname' : b" f32",
            'size' : 4,
            'bin_reader': read_bin_f32,
            'str_reader': read_str_f32,
            'bin_format': 'f',
            'numpy_type': np.float32 },

    'f64': {'binname' : b" f64",
            'size' : 8,
            'bin_reader': read_bin_f64,
            'str_reader': read_str_f64,
            'bin_format': 'd',
            'numpy_type': np.float64 },

    'bool': {'binname' : b"bool",
             'size' : 1,
             'bin_reader': read_bin_bool,
             'str_reader': read_str_bool,
             'bin_format': 'b',
             'numpy_type': np.bool }
}

def read_bin_read_type(f):
    read_binname = f.get_chars(4)

    for (k,v) in FUTHARK_PRIMTYPES.items():
        if v['binname'] == read_binname:
            return k
    panic(1, "binary-input: Did not recognize the type '%s'.\n", read_binname)

def numpy_type_to_type_name(t):
    for (k,v) in FUTHARK_PRIMTYPES.items():
        if v['numpy_type'] == t:
            return k
    raise Exception('Unknown Numpy type: {}'.format(t))

def read_bin_ensure_scalar(f, expected_type):
  dims = read_bin_i8(f)

  if dims != 0:
      panic(1, "binary-input: Expected scalar (0 dimensions), but got array with %i dimensions.\n", dims)

  bin_type = read_bin_read_type(f)
  if bin_type != expected_type:
      panic(1, "binary-input: Expected scalar of type %s but got scalar of type %s.\n",
            expected_type, bin_type)

# ------------------------------------------------------------------------------
# General interface for reading Primitive Futhark Values
# ------------------------------------------------------------------------------

def read_scalar(f, ty):
    if read_is_binary(f):
        read_bin_ensure_scalar(f, ty)
        return FUTHARK_PRIMTYPES[ty]['bin_reader'](f)
    return FUTHARK_PRIMTYPES[ty]['str_reader'](f)

def read_array(f, expected_type, rank):
    if not read_is_binary(f):
        str_reader = FUTHARK_PRIMTYPES[expected_type]['str_reader']
        return read_str_array(f, str_reader, expected_type, rank,
                              FUTHARK_PRIMTYPES[expected_type]['numpy_type'])

    bin_rank = read_bin_u8(f)

    if bin_rank != rank:
        panic(1, "binary-input: Expected %i dimensions, but got array with %i dimensions.\n",
              rank, bin_rank)

    bin_type_enum = read_bin_read_type(f)
    if expected_type != bin_type_enum:
        panic(1, "binary-input: Expected %iD-array with element type '%s' but got %iD-array with element type '%s'.\n",
              rank, expected_type, bin_rank, bin_type_enum)

    shape = []
    elem_count = 1
    for i in range(rank):
        bin_size = read_bin_u64(f)
        elem_count *= bin_size
        shape.append(bin_size)

    bin_fmt = FUTHARK_PRIMTYPES[bin_type_enum]['bin_format']

    # We first read the expected number of types into a bytestring,
    # then use np.fromstring.  This is because np.fromfile does not
    # work on things that are insufficiently file-like, like a network
    # stream.
    bytes = f.get_chars(elem_count * FUTHARK_PRIMTYPES[expected_type]['size'])
    arr = np.fromstring(bytes, dtype=FUTHARK_PRIMTYPES[bin_type_enum]['numpy_type'])
    arr.shape = shape

    return arr

if sys.version_info >= (3,0):
    input_reader = ReaderInput(sys.stdin.buffer)
else:
    input_reader = ReaderInput(sys.stdin)

import re

def read_value(type_desc, reader=input_reader):
    """Read a value of the given type.  The type is a string
representation of the Futhark type."""
    m = re.match(r'((?:\[\])*)([a-z0-9]+)$', type_desc)
    if m:
        dims = int(len(m.group(1))/2)
        basetype = m.group(2)
        assert basetype in FUTHARK_PRIMTYPES, "Unknown type: {}".format(type_desc)
        if dims > 0:
            return read_array(reader, basetype, dims)
        else:
            return read_scalar(reader, basetype)
        return (dims, basetype)

def write_value_text(v, out=sys.stdout):
    if type(v) == np.uint8:
        out.write("%uu8" % v)
    elif type(v) == np.uint16:
        out.write("%uu16" % v)
    elif type(v) == np.uint32:
        out.write("%uu32" % v)
    elif type(v) == np.uint64:
        out.write("%uu64" % v)
    elif type(v) == np.int8:
        out.write("%di8" % v)
    elif type(v) == np.int16:
        out.write("%di16" % v)
    elif type(v) == np.int32:
        out.write("%di32" % v)
    elif type(v) == np.int64:
        out.write("%di64" % v)
    elif type(v) in [np.bool, np.bool_]:
        if v:
            out.write("true")
        else:
            out.write("false")
    elif type(v) == np.float32:
        if np.isnan(v):
            out.write('f32.nan')
        elif np.isinf(v):
            if v >= 0:
                out.write('f32.inf')
            else:
                out.write('-f32.inf')
        else:
            out.write("%.6ff32" % v)
    elif type(v) == np.float64:
        if np.isnan(v):
            out.write('f64.nan')
        elif np.isinf(v):
            if v >= 0:
                out.write('f64.inf')
            else:
                out.write('-f64.inf')
        else:
            out.write("%.6ff64" % v)
    elif type(v) == np.ndarray:
        if np.product(v.shape) == 0:
            tname = numpy_type_to_type_name(v.dtype)
            out.write('empty({}{})'.format(''.join(['[{}]'.format(d)
                                                    for d in v.shape]), tname))
        else:
            first = True
            out.write('[')
            for x in v:
                if not first: out.write(', ')
                first = False
                write_value(x, out=out)
            out.write(']')
    else:
        raise Exception("Cannot print value of type {}: {}".format(type(v), v))

type_strs = { np.dtype('int8'): b'  i8',
              np.dtype('int16'): b' i16',
              np.dtype('int32'): b' i32',
              np.dtype('int64'): b' i64',
              np.dtype('uint8'): b'  u8',
              np.dtype('uint16'): b' u16',
              np.dtype('uint32'): b' u32',
              np.dtype('uint64'): b' u64',
              np.dtype('float32'): b' f32',
              np.dtype('float64'): b' f64',
              np.dtype('bool'): b'bool'}

def construct_binary_value(v):
    t = v.dtype
    shape = v.shape

    elems = 1
    for d in shape:
        elems *= d

    num_bytes = 1 + 1 + 1 + 4 + len(shape) * 8 + elems * t.itemsize
    bytes = bytearray(num_bytes)
    bytes[0] = np.int8(ord('b'))
    bytes[1] = 2
    bytes[2] = np.int8(len(shape))
    bytes[3:7] = type_strs[t]

    for i in range(len(shape)):
        bytes[7+i*8:7+(i+1)*8] = np.int64(shape[i]).tostring()

    bytes[7+len(shape)*8:] = np.ascontiguousarray(v).tostring()

    return bytes

def write_value_binary(v, out=sys.stdout):
    if sys.version_info >= (3,0):
        out = out.buffer
    out.write(construct_binary_value(v))

def write_value(v, out=sys.stdout, binary=False):
    if binary:
        return write_value_binary(v, out=out)
    else:
        return write_value_text(v, out=out)

# End of values.py.
# Start of memory.py.

import ctypes as ct

def addressOffset(x, offset, bt):
  return ct.cast(ct.addressof(x.contents)+int(offset), ct.POINTER(bt))

def allocateMem(size):
  return ct.cast((ct.c_byte * max(0,size))(), ct.POINTER(ct.c_byte))

# Copy an array if its is not-None.  This is important for treating
# Numpy arrays as flat memory, but has some overhead.
def normaliseArray(x):
  if (x.base is x) or (x.base is None):
    return x
  else:
    return x.copy()

def unwrapArray(x):
  return normaliseArray(x).ctypes.data_as(ct.POINTER(ct.c_byte))

def createArray(x, shape):
  # HACK: np.ctypeslib.as_array may fail if the shape contains zeroes,
  # for some reason.
  if any(map(lambda x: x == 0, shape)):
      return np.ndarray(shape, dtype=x._type_)
  else:
      return np.ctypeslib.as_array(x, shape=shape)

def indexArray(x, offset, bt, nptype):
  return nptype(addressOffset(x, offset*ct.sizeof(bt), bt)[0])

def writeScalarArray(x, offset, v):
  ct.memmove(ct.addressof(x.contents)+int(offset)*ct.sizeof(v), ct.addressof(v), ct.sizeof(v))

# An opaque Futhark value.
class opaque(object):
  def __init__(self, desc, *payload):
    self.data = payload
    self.desc = desc

  def __repr__(self):
    return "<opaque Futhark value of type {}>".format(self.desc)

# End of memory.py.
# Start of panic.py.

def panic(exitcode, fmt, *args):
    sys.stderr.write('%s: ' % sys.argv[0])
    sys.stderr.write(fmt % args)
    sys.exit(exitcode)

# End of panic.py.
# Start of tuning.py

def read_tuning_file(kvs, f):
    for line in f.read().splitlines():
        size, value = line.split('=')
        kvs[size] = int(value)
    return kvs

# End of tuning.py.
# Start of scalar.py.

import numpy as np
import math
import struct

def signed(x):
  if type(x) == np.uint8:
    return np.int8(x)
  elif type(x) == np.uint16:
    return np.int16(x)
  elif type(x) == np.uint32:
    return np.int32(x)
  else:
    return np.int64(x)

def unsigned(x):
  if type(x) == np.int8:
    return np.uint8(x)
  elif type(x) == np.int16:
    return np.uint16(x)
  elif type(x) == np.int32:
    return np.uint32(x)
  else:
    return np.uint64(x)

def shlN(x,y):
  return x << y

def ashrN(x,y):
  return x >> y

def sdivN(x,y):
  return x // y

def smodN(x,y):
  return x % y

def udivN(x,y):
  return signed(unsigned(x) // unsigned(y))

def umodN(x,y):
  return signed(unsigned(x) % unsigned(y))

def squotN(x,y):
  return np.floor_divide(np.abs(x), np.abs(y)) * np.sign(x) * np.sign(y)

def sremN(x,y):
  return np.remainder(np.abs(x), np.abs(y)) * np.sign(x)

def sminN(x,y):
  return min(x,y)

def smaxN(x,y):
  return max(x,y)

def uminN(x,y):
  return signed(min(unsigned(x),unsigned(y)))

def umaxN(x,y):
  return signed(max(unsigned(x),unsigned(y)))

def fminN(x,y):
  return min(x,y)

def fmaxN(x,y):
  return max(x,y)

def powN(x,y):
  return x ** y

def fpowN(x,y):
  return x ** y

def sleN(x,y):
  return x <= y

def sltN(x,y):
  return x < y

def uleN(x,y):
  return unsigned(x) <= unsigned(y)

def ultN(x,y):
  return unsigned(x) < unsigned(y)

def lshr8(x,y):
  return np.int8(np.uint8(x) >> np.uint8(y))

def lshr16(x,y):
  return np.int16(np.uint16(x) >> np.uint16(y))

def lshr32(x,y):
  return np.int32(np.uint32(x) >> np.uint32(y))

def lshr64(x,y):
  return np.int64(np.uint64(x) >> np.uint64(y))

def sext_T_i8(x):
  return np.int8(x)

def sext_T_i16(x):
  return np.int16(x)

def sext_T_i32(x):
  return np.int32(x)

def sext_T_i64(x):
  return np.int64(x)

def itob_T_bool(x):
  return np.bool(x)

def btoi_bool_i8(x):
  return np.int8(x)

def btoi_bool_i16(x):
  return np.int8(x)

def btoi_bool_i32(x):
  return np.int8(x)

def btoi_bool_i64(x):
  return np.int8(x)

def zext_i8_i8(x):
  return np.int8(np.uint8(x))

def zext_i8_i16(x):
  return np.int16(np.uint8(x))

def zext_i8_i32(x):
  return np.int32(np.uint8(x))

def zext_i8_i64(x):
  return np.int64(np.uint8(x))

def zext_i16_i8(x):
  return np.int8(np.uint16(x))

def zext_i16_i16(x):
  return np.int16(np.uint16(x))

def zext_i16_i32(x):
  return np.int32(np.uint16(x))

def zext_i16_i64(x):
  return np.int64(np.uint16(x))

def zext_i32_i8(x):
  return np.int8(np.uint32(x))

def zext_i32_i16(x):
  return np.int16(np.uint32(x))

def zext_i32_i32(x):
  return np.int32(np.uint32(x))

def zext_i32_i64(x):
  return np.int64(np.uint32(x))

def zext_i64_i8(x):
  return np.int8(np.uint64(x))

def zext_i64_i16(x):
  return np.int16(np.uint64(x))

def zext_i64_i32(x):
  return np.int32(np.uint64(x))

def zext_i64_i64(x):
  return np.int64(np.uint64(x))

shl8 = shl16 = shl32 = shl64 = shlN
ashr8 = ashr16 = ashr32 = ashr64 = ashrN
sdiv8 = sdiv16 = sdiv32 = sdiv64 = sdivN
smod8 = smod16 = smod32 = smod64 = smodN
udiv8 = udiv16 = udiv32 = udiv64 = udivN
umod8 = umod16 = umod32 = umod64 = umodN
squot8 = squot16 = squot32 = squot64 = squotN
srem8 = srem16 = srem32 = srem64 = sremN
smax8 = smax16 = smax32 = smax64 = smaxN
smin8 = smin16 = smin32 = smin64 = sminN
umax8 = umax16 = umax32 = umax64 = umaxN
umin8 = umin16 = umin32 = umin64 = uminN
pow8 = pow16 = pow32 = pow64 = powN
fpow32 = fpow64 = fpowN
fmax32 = fmax64 = fmaxN
fmin32 = fmin64 = fminN
sle8 = sle16 = sle32 = sle64 = sleN
slt8 = slt16 = slt32 = slt64 = sltN
ule8 = ule16 = ule32 = ule64 = uleN
ult8 = ult16 = ult32 = ult64 = ultN
sext_i8_i8 = sext_i16_i8 = sext_i32_i8 = sext_i64_i8 = sext_T_i8
sext_i8_i16 = sext_i16_i16 = sext_i32_i16 = sext_i64_i16 = sext_T_i16
sext_i8_i32 = sext_i16_i32 = sext_i32_i32 = sext_i64_i32 = sext_T_i32
sext_i8_i64 = sext_i16_i64 = sext_i32_i64 = sext_i64_i64 = sext_T_i64
itob_i8_bool = itob_i16_bool = itob_i32_bool = itob_i64_bool = itob_T_bool

def clz_T(x):
  n = np.int32(0)
  bits = x.itemsize * 8
  for i in range(bits):
    if x < 0:
      break
    n += 1
    x <<= np.int8(1)
  return n

def popc_T(x):
  c = np.int32(0)
  while x != 0:
    x &= x - np.int8(1)
    c += np.int8(1)
  return c

futhark_popc8 = futhark_popc16 = futhark_popc32 = futhark_popc64 = popc_T
futhark_clzz8 = futhark_clzz16 = futhark_clzz32 = futhark_clzz64 = clz_T

def ssignum(x):
  return np.sign(x)

def usignum(x):
  if x < 0:
    return ssignum(-x)
  else:
    return ssignum(x)

def sitofp_T_f32(x):
  return np.float32(x)
sitofp_i8_f32 = sitofp_i16_f32 = sitofp_i32_f32 = sitofp_i64_f32 = sitofp_T_f32

def sitofp_T_f64(x):
  return np.float64(x)
sitofp_i8_f64 = sitofp_i16_f64 = sitofp_i32_f64 = sitofp_i64_f64 = sitofp_T_f64

def uitofp_T_f32(x):
  return np.float32(unsigned(x))
uitofp_i8_f32 = uitofp_i16_f32 = uitofp_i32_f32 = uitofp_i64_f32 = uitofp_T_f32

def uitofp_T_f64(x):
  return np.float64(unsigned(x))
uitofp_i8_f64 = uitofp_i16_f64 = uitofp_i32_f64 = uitofp_i64_f64 = uitofp_T_f64

def fptosi_T_i8(x):
  return np.int8(np.trunc(x))
fptosi_f32_i8 = fptosi_f64_i8 = fptosi_T_i8

def fptosi_T_i16(x):
  return np.int16(np.trunc(x))
fptosi_f32_i16 = fptosi_f64_i16 = fptosi_T_i16

def fptosi_T_i32(x):
  return np.int32(np.trunc(x))
fptosi_f32_i32 = fptosi_f64_i32 = fptosi_T_i32

def fptosi_T_i64(x):
  return np.int64(np.trunc(x))
fptosi_f32_i64 = fptosi_f64_i64 = fptosi_T_i64

def fptoui_T_i8(x):
  return np.uint8(np.trunc(x))
fptoui_f32_i8 = fptoui_f64_i8 = fptoui_T_i8

def fptoui_T_i16(x):
  return np.uint16(np.trunc(x))
fptoui_f32_i16 = fptoui_f64_i16 = fptoui_T_i16

def fptoui_T_i32(x):
  return np.uint32(np.trunc(x))
fptoui_f32_i32 = fptoui_f64_i32 = fptoui_T_i32

def fptoui_T_i64(x):
  return np.uint64(np.trunc(x))
fptoui_f32_i64 = fptoui_f64_i64 = fptoui_T_i64

def fpconv_f32_f64(x):
  return np.float64(x)

def fpconv_f64_f32(x):
  return np.float32(x)

def futhark_log64(x):
  return np.float64(np.log(x))

def futhark_log2_64(x):
  return np.float64(np.log2(x))

def futhark_log10_64(x):
  return np.float64(np.log10(x))

def futhark_sqrt64(x):
  return np.sqrt(x)

def futhark_exp64(x):
  return np.exp(x)

def futhark_cos64(x):
  return np.cos(x)

def futhark_sin64(x):
  return np.sin(x)

def futhark_tan64(x):
  return np.tan(x)

def futhark_acos64(x):
  return np.arccos(x)

def futhark_asin64(x):
  return np.arcsin(x)

def futhark_atan64(x):
  return np.arctan(x)

def futhark_atan2_64(x, y):
  return np.arctan2(x, y)

def futhark_gamma64(x):
  return np.float64(math.gamma(x))

def futhark_lgamma64(x):
  return np.float64(math.lgamma(x))

def futhark_round64(x):
  return np.round(x)

def futhark_ceil64(x):
  return np.ceil(x)

def futhark_floor64(x):
  return np.floor(x)

def futhark_isnan64(x):
  return np.isnan(x)

def futhark_isinf64(x):
  return np.isinf(x)

def futhark_to_bits64(x):
  s = struct.pack('>d', x)
  return np.int64(struct.unpack('>q', s)[0])

def futhark_from_bits64(x):
  s = struct.pack('>q', x)
  return np.float64(struct.unpack('>d', s)[0])

def futhark_log32(x):
  return np.float32(np.log(x))

def futhark_log2_32(x):
  return np.float32(np.log2(x))

def futhark_log10_32(x):
  return np.float32(np.log10(x))

def futhark_sqrt32(x):
  return np.float32(np.sqrt(x))

def futhark_exp32(x):
  return np.exp(x)

def futhark_cos32(x):
  return np.cos(x)

def futhark_sin32(x):
  return np.sin(x)

def futhark_tan32(x):
  return np.tan(x)

def futhark_acos32(x):
  return np.arccos(x)

def futhark_asin32(x):
  return np.arcsin(x)

def futhark_atan32(x):
  return np.arctan(x)

def futhark_atan2_32(x, y):
  return np.arctan2(x, y)

def futhark_gamma32(x):
  return np.float32(math.gamma(x))

def futhark_lgamma32(x):
  return np.float32(math.lgamma(x))

def futhark_round32(x):
  return np.round(x)

def futhark_ceil32(x):
  return np.ceil(x)

def futhark_floor32(x):
  return np.floor(x)

def futhark_isnan32(x):
  return np.isnan(x)

def futhark_isinf32(x):
  return np.isinf(x)

def futhark_to_bits32(x):
  s = struct.pack('>f', x)
  return np.int32(struct.unpack('>l', s)[0])

def futhark_from_bits32(x):
  s = struct.pack('>l', x)
  return np.float32(struct.unpack('>f', s)[0])

def futhark_lerp32(v0, v1, t):
  return v0 + (v1-v0)*t

def futhark_lerp64(v0, v1, t):
  return v0 + (v1-v0)*t

# End of scalar.py.
class information:
  entry_points = {"kullback_liebler_scaled_f32": (["[]f32", "[]f32"], ["f32"]),
                  "kullback_liebler_f32": (["[]f32", "[]f32"], ["f32"]),
                  "kullback_liebler_scaled_f64": (["[]f64", "[]f64"], ["f64"]),
                  "kullback_liebler_f64": (["[]f64", "[]f64"], ["f64"]),
                  "entropy_scaled_f32": (["[]f32"], ["f32"]),
                  "entropy_scaled_f64": (["[]f64"], ["f64"]),
                  "entropy_f32": (["[]f32"], ["f32"]),
                  "entropy_f64": (["[]f64"], ["f64"])}
  def __init__(self, command_queue=None, interactive=False,
               platform_pref=preferred_platform, device_pref=preferred_device,
               default_group_size=default_group_size,
               default_num_groups=default_num_groups,
               default_tile_size=default_tile_size,
               default_threshold=default_threshold, sizes=sizes):
    size_heuristics=[("NVIDIA CUDA", cl.device_type.GPU, "lockstep_width", 32),
     ("AMD Accelerated Parallel Processing", cl.device_type.GPU, "lockstep_width",
      32), ("", cl.device_type.GPU, "lockstep_width", 1), ("", cl.device_type.GPU,
                                                           "num_groups", 256), ("",
                                                                                cl.device_type.GPU,
                                                                                "group_size",
                                                                                256),
     ("", cl.device_type.GPU, "tile_size", 32), ("", cl.device_type.GPU,
                                                 "threshold", 32768), ("",
                                                                       cl.device_type.CPU,
                                                                       "lockstep_width",
                                                                       1), ("",
                                                                            cl.device_type.CPU,
                                                                            "num_groups",
                                                                            "MAX_COMPUTE_UNITS"),
     ("", cl.device_type.CPU, "group_size", 32), ("", cl.device_type.CPU,
                                                  "tile_size", 4), ("",
                                                                    cl.device_type.CPU,
                                                                    "threshold",
                                                                    "MAX_COMPUTE_UNITS")]
    program = initialise_opencl_object(self,
                                       program_src=fut_opencl_src,
                                       command_queue=command_queue,
                                       interactive=interactive,
                                       platform_pref=platform_pref,
                                       device_pref=device_pref,
                                       default_group_size=default_group_size,
                                       default_num_groups=default_num_groups,
                                       default_tile_size=default_tile_size,
                                       default_threshold=default_threshold,
                                       size_heuristics=size_heuristics,
                                       required_types=["i32", "f32", "f64", "bool"],
                                       user_sizes=sizes,
                                       all_sizes={"entropy_f32.segred_group_size_7312": {"class": "group_size", "value": None},
                                        "entropy_f32.segred_num_groups_7314": {"class": "num_groups", "value": None},
                                        "entropy_f64.segred_group_size_7301": {"class": "group_size", "value": None},
                                        "entropy_f64.segred_num_groups_7303": {"class": "num_groups", "value": None},
                                        "entropy_scaled_f32.segred_group_size_7345": {"class": "group_size",
                                                                                      "value": None},
                                        "entropy_scaled_f32.segred_group_size_7356": {"class": "group_size",
                                                                                      "value": None},
                                        "entropy_scaled_f32.segred_num_groups_7347": {"class": "num_groups",
                                                                                      "value": None},
                                        "entropy_scaled_f32.segred_num_groups_7358": {"class": "num_groups",
                                                                                      "value": None},
                                        "entropy_scaled_f64.segred_group_size_7323": {"class": "group_size",
                                                                                      "value": None},
                                        "entropy_scaled_f64.segred_group_size_7334": {"class": "group_size",
                                                                                      "value": None},
                                        "entropy_scaled_f64.segred_num_groups_7325": {"class": "num_groups",
                                                                                      "value": None},
                                        "entropy_scaled_f64.segred_num_groups_7336": {"class": "num_groups",
                                                                                      "value": None},
                                        "kullback_liebler_f32.segred_group_size_7411": {"class": "group_size",
                                                                                        "value": None},
                                        "kullback_liebler_f32.segred_num_groups_7413": {"class": "num_groups",
                                                                                        "value": None},
                                        "kullback_liebler_f64.segred_group_size_7367": {"class": "group_size",
                                                                                        "value": None},
                                        "kullback_liebler_f64.segred_num_groups_7369": {"class": "num_groups",
                                                                                        "value": None},
                                        "kullback_liebler_scaled_f32.segred_group_size_7422": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f32.segred_group_size_7433": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f32.segred_group_size_7444": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f32.segred_num_groups_7424": {"class": "num_groups",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f32.segred_num_groups_7435": {"class": "num_groups",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f32.segred_num_groups_7446": {"class": "num_groups",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_7378": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_7389": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_7400": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_7380": {"class": "num_groups",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_7391": {"class": "num_groups",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_7402": {"class": "num_groups",
                                                                                               "value": None}})
    self.segred_nonseg_7309_var = program.segred_nonseg_7309
    self.segred_nonseg_7320_var = program.segred_nonseg_7320
    self.segred_nonseg_7331_var = program.segred_nonseg_7331
    self.segred_nonseg_7342_var = program.segred_nonseg_7342
    self.segred_nonseg_7353_var = program.segred_nonseg_7353
    self.segred_nonseg_7364_var = program.segred_nonseg_7364
    self.segred_nonseg_7375_var = program.segred_nonseg_7375
    self.segred_nonseg_7386_var = program.segred_nonseg_7386
    self.segred_nonseg_7397_var = program.segred_nonseg_7397
    self.segred_nonseg_7408_var = program.segred_nonseg_7408
    self.segred_nonseg_7419_var = program.segred_nonseg_7419
    self.segred_nonseg_7430_var = program.segred_nonseg_7430
    self.segred_nonseg_7441_var = program.segred_nonseg_7441
    self.segred_nonseg_7452_var = program.segred_nonseg_7452
    counter_mem_7804 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7884 = opencl_alloc(self, 40, "static_mem_7884")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7884,
                      normaliseArray(counter_mem_7804), is_blocking=synchronous)
    self.counter_mem_7804 = static_mem_7884
    counter_mem_7831 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7886 = opencl_alloc(self, 40, "static_mem_7886")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7886,
                      normaliseArray(counter_mem_7831), is_blocking=synchronous)
    self.counter_mem_7831 = static_mem_7886
    counter_mem_7858 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7888 = opencl_alloc(self, 40, "static_mem_7888")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7888,
                      normaliseArray(counter_mem_7858), is_blocking=synchronous)
    self.counter_mem_7858 = static_mem_7888
    counter_mem_7776 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7890 = opencl_alloc(self, 40, "static_mem_7890")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7890,
                      normaliseArray(counter_mem_7776), is_blocking=synchronous)
    self.counter_mem_7776 = static_mem_7890
    counter_mem_7694 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7892 = opencl_alloc(self, 40, "static_mem_7892")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7892,
                      normaliseArray(counter_mem_7694), is_blocking=synchronous)
    self.counter_mem_7694 = static_mem_7892
    counter_mem_7721 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7894 = opencl_alloc(self, 40, "static_mem_7894")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7894,
                      normaliseArray(counter_mem_7721), is_blocking=synchronous)
    self.counter_mem_7721 = static_mem_7894
    counter_mem_7748 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7896 = opencl_alloc(self, 40, "static_mem_7896")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7896,
                      normaliseArray(counter_mem_7748), is_blocking=synchronous)
    self.counter_mem_7748 = static_mem_7896
    counter_mem_7666 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7898 = opencl_alloc(self, 40, "static_mem_7898")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7898,
                      normaliseArray(counter_mem_7666), is_blocking=synchronous)
    self.counter_mem_7666 = static_mem_7898
    counter_mem_7611 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7900 = opencl_alloc(self, 40, "static_mem_7900")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7900,
                      normaliseArray(counter_mem_7611), is_blocking=synchronous)
    self.counter_mem_7611 = static_mem_7900
    counter_mem_7638 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7902 = opencl_alloc(self, 40, "static_mem_7902")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7902,
                      normaliseArray(counter_mem_7638), is_blocking=synchronous)
    self.counter_mem_7638 = static_mem_7902
    counter_mem_7556 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7904 = opencl_alloc(self, 40, "static_mem_7904")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7904,
                      normaliseArray(counter_mem_7556), is_blocking=synchronous)
    self.counter_mem_7556 = static_mem_7904
    counter_mem_7583 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7906 = opencl_alloc(self, 40, "static_mem_7906")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7906,
                      normaliseArray(counter_mem_7583), is_blocking=synchronous)
    self.counter_mem_7583 = static_mem_7906
    counter_mem_7528 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7908 = opencl_alloc(self, 40, "static_mem_7908")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7908,
                      normaliseArray(counter_mem_7528), is_blocking=synchronous)
    self.counter_mem_7528 = static_mem_7908
    counter_mem_7500 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_7910 = opencl_alloc(self, 40, "static_mem_7910")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_7910,
                      normaliseArray(counter_mem_7500), is_blocking=synchronous)
    self.counter_mem_7500 = static_mem_7910
  def futhark_kullback_liebler_scaled_f32(self, x_mem_7456, y_mem_7457,
                                          sizze_7267, sizze_7268):
    sizze_7420 = sext_i32_i64(sizze_7267)
    segred_group_sizze_7423 = self.sizes["kullback_liebler_scaled_f32.segred_group_size_7422"]
    max_num_groups_7803 = self.sizes["kullback_liebler_scaled_f32.segred_num_groups_7424"]
    num_groups_7425 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7420 + sext_i32_i64(segred_group_sizze_7423)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7423)),
                                                 sext_i32_i64(max_num_groups_7803))))
    mem_7461 = opencl_alloc(self, np.int64(4), "mem_7461")
    counter_mem_7804 = self.counter_mem_7804
    group_res_arr_mem_7806 = opencl_alloc(self,
                                          (np.int32(4) * (segred_group_sizze_7423 * num_groups_7425)),
                                          "group_res_arr_mem_7806")
    num_threads_7808 = (num_groups_7425 * segred_group_sizze_7423)
    if ((1 * (np.long(num_groups_7425) * np.long(segred_group_sizze_7423))) != 0):
      self.segred_nonseg_7430_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_7423))),
                                           np.int32(sizze_7267),
                                           np.int32(num_groups_7425),
                                           x_mem_7456, mem_7461,
                                           counter_mem_7804,
                                           group_res_arr_mem_7806,
                                           np.int32(num_threads_7808))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7430_var,
                                 ((np.long(num_groups_7425) * np.long(segred_group_sizze_7423)),),
                                 (np.long(segred_group_sizze_7423),))
      if synchronous:
        self.queue.finish()
    read_res_7885 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_7885, mem_7461,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_7271 = read_res_7885[0]
    mem_7461 = None
    dim_zzero_7276 = (np.int32(0) == sizze_7267)
    sizze_7431 = sext_i32_i64(sizze_7268)
    segred_group_sizze_7434 = self.sizes["kullback_liebler_scaled_f32.segred_group_size_7433"]
    max_num_groups_7830 = self.sizes["kullback_liebler_scaled_f32.segred_num_groups_7435"]
    num_groups_7436 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7431 + sext_i32_i64(segred_group_sizze_7434)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7434)),
                                                 sext_i32_i64(max_num_groups_7830))))
    mem_7465 = opencl_alloc(self, np.int64(4), "mem_7465")
    counter_mem_7831 = self.counter_mem_7831
    group_res_arr_mem_7833 = opencl_alloc(self,
                                          (np.int32(4) * (segred_group_sizze_7434 * num_groups_7436)),
                                          "group_res_arr_mem_7833")
    num_threads_7835 = (num_groups_7436 * segred_group_sizze_7434)
    if ((1 * (np.long(num_groups_7436) * np.long(segred_group_sizze_7434))) != 0):
      self.segred_nonseg_7441_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_7434))),
                                           np.int32(sizze_7268),
                                           np.int32(num_groups_7436),
                                           y_mem_7457, mem_7465,
                                           counter_mem_7831,
                                           group_res_arr_mem_7833,
                                           np.int32(num_threads_7835))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7441_var,
                                 ((np.long(num_groups_7436) * np.long(segred_group_sizze_7434)),),
                                 (np.long(segred_group_sizze_7434),))
      if synchronous:
        self.queue.finish()
    read_res_7887 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_7887, mem_7465,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_7277 = read_res_7887[0]
    mem_7465 = None
    dim_zzero_7282 = (np.int32(0) == sizze_7268)
    both_empty_7283 = (dim_zzero_7276 and dim_zzero_7282)
    dim_match_7284 = (sizze_7267 == sizze_7268)
    empty_or_match_7285 = (both_empty_7283 or dim_match_7284)
    empty_or_match_cert_7286 = True
    assert empty_or_match_7285, ("Error at\n |-> information.fut:43:1-44:86\n `-> information.fut:44:3-86\n\n: %s" % ("function arguments of wrong shape",))
    segred_group_sizze_7445 = self.sizes["kullback_liebler_scaled_f32.segred_group_size_7444"]
    max_num_groups_7857 = self.sizes["kullback_liebler_scaled_f32.segred_num_groups_7446"]
    num_groups_7447 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7420 + sext_i32_i64(segred_group_sizze_7445)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7445)),
                                                 sext_i32_i64(max_num_groups_7857))))
    mem_7469 = opencl_alloc(self, np.int64(4), "mem_7469")
    counter_mem_7858 = self.counter_mem_7858
    group_res_arr_mem_7860 = opencl_alloc(self,
                                          (np.int32(4) * (segred_group_sizze_7445 * num_groups_7447)),
                                          "group_res_arr_mem_7860")
    num_threads_7862 = (num_groups_7447 * segred_group_sizze_7445)
    if ((1 * (np.long(num_groups_7447) * np.long(segred_group_sizze_7445))) != 0):
      self.segred_nonseg_7452_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_7445))),
                                           np.int32(sizze_7267),
                                           np.float32(res_7271),
                                           np.float32(res_7277),
                                           np.int32(num_groups_7447),
                                           x_mem_7456, y_mem_7457, mem_7469,
                                           counter_mem_7858,
                                           group_res_arr_mem_7860,
                                           np.int32(num_threads_7862))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7452_var,
                                 ((np.long(num_groups_7447) * np.long(segred_group_sizze_7445)),),
                                 (np.long(segred_group_sizze_7445),))
      if synchronous:
        self.queue.finish()
    read_res_7889 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_7889, mem_7469,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_7288 = read_res_7889[0]
    mem_7469 = None
    scalar_out_7802 = res_7288
    return scalar_out_7802
  def futhark_kullback_liebler_f32(self, x_mem_7456, x_mem_7457, sizze_7247,
                                   sizze_7248):
    dim_zzero_7251 = (np.int32(0) == sizze_7248)
    dim_zzero_7252 = (np.int32(0) == sizze_7247)
    both_empty_7253 = (dim_zzero_7251 and dim_zzero_7252)
    dim_match_7254 = (sizze_7247 == sizze_7248)
    empty_or_match_7255 = (both_empty_7253 or dim_match_7254)
    empty_or_match_cert_7256 = True
    assert empty_or_match_7255, ("Error at\n |-> information.fut:40:1-41:34\n `-> unknown location\n\n: %s" % ("function arguments of wrong shape",))
    sizze_7409 = sext_i32_i64(sizze_7247)
    segred_group_sizze_7412 = self.sizes["kullback_liebler_f32.segred_group_size_7411"]
    max_num_groups_7775 = self.sizes["kullback_liebler_f32.segred_num_groups_7413"]
    num_groups_7414 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7409 + sext_i32_i64(segred_group_sizze_7412)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7412)),
                                                 sext_i32_i64(max_num_groups_7775))))
    mem_7461 = opencl_alloc(self, np.int64(4), "mem_7461")
    counter_mem_7776 = self.counter_mem_7776
    group_res_arr_mem_7778 = opencl_alloc(self,
                                          (np.int32(4) * (segred_group_sizze_7412 * num_groups_7414)),
                                          "group_res_arr_mem_7778")
    num_threads_7780 = (num_groups_7414 * segred_group_sizze_7412)
    if ((1 * (np.long(num_groups_7414) * np.long(segred_group_sizze_7412))) != 0):
      self.segred_nonseg_7419_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_7412))),
                                           np.int32(sizze_7247),
                                           np.int32(num_groups_7414),
                                           x_mem_7456, x_mem_7457, mem_7461,
                                           counter_mem_7776,
                                           group_res_arr_mem_7778,
                                           np.int32(num_threads_7780))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7419_var,
                                 ((np.long(num_groups_7414) * np.long(segred_group_sizze_7412)),),
                                 (np.long(segred_group_sizze_7412),))
      if synchronous:
        self.queue.finish()
    read_res_7891 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_7891, mem_7461,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_7258 = read_res_7891[0]
    mem_7461 = None
    scalar_out_7774 = res_7258
    return scalar_out_7774
  def futhark_kullback_liebler_scaled_f64(self, x_mem_7456, y_mem_7457,
                                          sizze_7215, sizze_7216):
    sizze_7376 = sext_i32_i64(sizze_7215)
    segred_group_sizze_7379 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_7378"]
    max_num_groups_7693 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_7380"]
    num_groups_7381 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7376 + sext_i32_i64(segred_group_sizze_7379)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7379)),
                                                 sext_i32_i64(max_num_groups_7693))))
    mem_7461 = opencl_alloc(self, np.int64(8), "mem_7461")
    counter_mem_7694 = self.counter_mem_7694
    group_res_arr_mem_7696 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_7379 * num_groups_7381)),
                                          "group_res_arr_mem_7696")
    num_threads_7698 = (num_groups_7381 * segred_group_sizze_7379)
    if ((1 * (np.long(num_groups_7381) * np.long(segred_group_sizze_7379))) != 0):
      self.segred_nonseg_7386_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_7379))),
                                           np.int32(sizze_7215),
                                           np.int32(num_groups_7381),
                                           x_mem_7456, mem_7461,
                                           counter_mem_7694,
                                           group_res_arr_mem_7696,
                                           np.int32(num_threads_7698))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7386_var,
                                 ((np.long(num_groups_7381) * np.long(segred_group_sizze_7379)),),
                                 (np.long(segred_group_sizze_7379),))
      if synchronous:
        self.queue.finish()
    read_res_7893 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_7893, mem_7461,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_7219 = read_res_7893[0]
    mem_7461 = None
    dim_zzero_7224 = (np.int32(0) == sizze_7215)
    sizze_7387 = sext_i32_i64(sizze_7216)
    segred_group_sizze_7390 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_7389"]
    max_num_groups_7720 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_7391"]
    num_groups_7392 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7387 + sext_i32_i64(segred_group_sizze_7390)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7390)),
                                                 sext_i32_i64(max_num_groups_7720))))
    mem_7465 = opencl_alloc(self, np.int64(8), "mem_7465")
    counter_mem_7721 = self.counter_mem_7721
    group_res_arr_mem_7723 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_7390 * num_groups_7392)),
                                          "group_res_arr_mem_7723")
    num_threads_7725 = (num_groups_7392 * segred_group_sizze_7390)
    if ((1 * (np.long(num_groups_7392) * np.long(segred_group_sizze_7390))) != 0):
      self.segred_nonseg_7397_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_7390))),
                                           np.int32(sizze_7216),
                                           np.int32(num_groups_7392),
                                           y_mem_7457, mem_7465,
                                           counter_mem_7721,
                                           group_res_arr_mem_7723,
                                           np.int32(num_threads_7725))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7397_var,
                                 ((np.long(num_groups_7392) * np.long(segred_group_sizze_7390)),),
                                 (np.long(segred_group_sizze_7390),))
      if synchronous:
        self.queue.finish()
    read_res_7895 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_7895, mem_7465,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_7225 = read_res_7895[0]
    mem_7465 = None
    dim_zzero_7230 = (np.int32(0) == sizze_7216)
    both_empty_7231 = (dim_zzero_7224 and dim_zzero_7230)
    dim_match_7232 = (sizze_7215 == sizze_7216)
    empty_or_match_7233 = (both_empty_7231 or dim_match_7232)
    empty_or_match_cert_7234 = True
    assert empty_or_match_7233, ("Error at\n |-> information.fut:31:1-32:86\n `-> information.fut:32:3-86\n\n: %s" % ("function arguments of wrong shape",))
    segred_group_sizze_7401 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_7400"]
    max_num_groups_7747 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_7402"]
    num_groups_7403 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7376 + sext_i32_i64(segred_group_sizze_7401)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7401)),
                                                 sext_i32_i64(max_num_groups_7747))))
    mem_7469 = opencl_alloc(self, np.int64(8), "mem_7469")
    counter_mem_7748 = self.counter_mem_7748
    group_res_arr_mem_7750 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_7401 * num_groups_7403)),
                                          "group_res_arr_mem_7750")
    num_threads_7752 = (num_groups_7403 * segred_group_sizze_7401)
    if ((1 * (np.long(num_groups_7403) * np.long(segred_group_sizze_7401))) != 0):
      self.segred_nonseg_7408_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_7401))),
                                           np.int32(sizze_7215),
                                           np.float64(res_7219),
                                           np.float64(res_7225),
                                           np.int32(num_groups_7403),
                                           x_mem_7456, y_mem_7457, mem_7469,
                                           counter_mem_7748,
                                           group_res_arr_mem_7750,
                                           np.int32(num_threads_7752))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7408_var,
                                 ((np.long(num_groups_7403) * np.long(segred_group_sizze_7401)),),
                                 (np.long(segred_group_sizze_7401),))
      if synchronous:
        self.queue.finish()
    read_res_7897 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_7897, mem_7469,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_7236 = read_res_7897[0]
    mem_7469 = None
    scalar_out_7692 = res_7236
    return scalar_out_7692
  def futhark_kullback_liebler_f64(self, x_mem_7456, x_mem_7457, sizze_7195,
                                   sizze_7196):
    dim_zzero_7199 = (np.int32(0) == sizze_7196)
    dim_zzero_7200 = (np.int32(0) == sizze_7195)
    both_empty_7201 = (dim_zzero_7199 and dim_zzero_7200)
    dim_match_7202 = (sizze_7195 == sizze_7196)
    empty_or_match_7203 = (both_empty_7201 or dim_match_7202)
    empty_or_match_cert_7204 = True
    assert empty_or_match_7203, ("Error at\n |-> information.fut:28:1-29:34\n `-> unknown location\n\n: %s" % ("function arguments of wrong shape",))
    sizze_7365 = sext_i32_i64(sizze_7195)
    segred_group_sizze_7368 = self.sizes["kullback_liebler_f64.segred_group_size_7367"]
    max_num_groups_7665 = self.sizes["kullback_liebler_f64.segred_num_groups_7369"]
    num_groups_7370 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7365 + sext_i32_i64(segred_group_sizze_7368)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7368)),
                                                 sext_i32_i64(max_num_groups_7665))))
    mem_7461 = opencl_alloc(self, np.int64(8), "mem_7461")
    counter_mem_7666 = self.counter_mem_7666
    group_res_arr_mem_7668 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_7368 * num_groups_7370)),
                                          "group_res_arr_mem_7668")
    num_threads_7670 = (num_groups_7370 * segred_group_sizze_7368)
    if ((1 * (np.long(num_groups_7370) * np.long(segred_group_sizze_7368))) != 0):
      self.segred_nonseg_7375_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_7368))),
                                           np.int32(sizze_7195),
                                           np.int32(num_groups_7370),
                                           x_mem_7456, x_mem_7457, mem_7461,
                                           counter_mem_7666,
                                           group_res_arr_mem_7668,
                                           np.int32(num_threads_7670))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7375_var,
                                 ((np.long(num_groups_7370) * np.long(segred_group_sizze_7368)),),
                                 (np.long(segred_group_sizze_7368),))
      if synchronous:
        self.queue.finish()
    read_res_7899 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_7899, mem_7461,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_7206 = read_res_7899[0]
    mem_7461 = None
    scalar_out_7664 = res_7206
    return scalar_out_7664
  def futhark_entropy_scaled_f32(self, x_mem_7456, sizze_7179):
    sizze_7343 = sext_i32_i64(sizze_7179)
    segred_group_sizze_7346 = self.sizes["entropy_scaled_f32.segred_group_size_7345"]
    max_num_groups_7610 = self.sizes["entropy_scaled_f32.segred_num_groups_7347"]
    num_groups_7348 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7343 + sext_i32_i64(segred_group_sizze_7346)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7346)),
                                                 sext_i32_i64(max_num_groups_7610))))
    mem_7460 = opencl_alloc(self, np.int64(4), "mem_7460")
    counter_mem_7611 = self.counter_mem_7611
    group_res_arr_mem_7613 = opencl_alloc(self,
                                          (np.int32(4) * (segred_group_sizze_7346 * num_groups_7348)),
                                          "group_res_arr_mem_7613")
    num_threads_7615 = (num_groups_7348 * segred_group_sizze_7346)
    if ((1 * (np.long(num_groups_7348) * np.long(segred_group_sizze_7346))) != 0):
      self.segred_nonseg_7353_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_7346))),
                                           np.int32(sizze_7179),
                                           np.int32(num_groups_7348),
                                           x_mem_7456, mem_7460,
                                           counter_mem_7611,
                                           group_res_arr_mem_7613,
                                           np.int32(num_threads_7615))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7353_var,
                                 ((np.long(num_groups_7348) * np.long(segred_group_sizze_7346)),),
                                 (np.long(segred_group_sizze_7346),))
      if synchronous:
        self.queue.finish()
    read_res_7901 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_7901, mem_7460,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_7181 = read_res_7901[0]
    mem_7460 = None
    segred_group_sizze_7357 = self.sizes["entropy_scaled_f32.segred_group_size_7356"]
    max_num_groups_7637 = self.sizes["entropy_scaled_f32.segred_num_groups_7358"]
    num_groups_7359 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7343 + sext_i32_i64(segred_group_sizze_7357)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7357)),
                                                 sext_i32_i64(max_num_groups_7637))))
    mem_7464 = opencl_alloc(self, np.int64(4), "mem_7464")
    counter_mem_7638 = self.counter_mem_7638
    group_res_arr_mem_7640 = opencl_alloc(self,
                                          (np.int32(4) * (segred_group_sizze_7357 * num_groups_7359)),
                                          "group_res_arr_mem_7640")
    num_threads_7642 = (num_groups_7359 * segred_group_sizze_7357)
    if ((1 * (np.long(num_groups_7359) * np.long(segred_group_sizze_7357))) != 0):
      self.segred_nonseg_7364_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_7357))),
                                           np.int32(sizze_7179),
                                           np.float32(res_7181),
                                           np.int32(num_groups_7359),
                                           x_mem_7456, mem_7464,
                                           counter_mem_7638,
                                           group_res_arr_mem_7640,
                                           np.int32(num_threads_7642))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7364_var,
                                 ((np.long(num_groups_7359) * np.long(segred_group_sizze_7357)),),
                                 (np.long(segred_group_sizze_7357),))
      if synchronous:
        self.queue.finish()
    read_res_7903 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_7903, mem_7464,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_7186 = read_res_7903[0]
    mem_7464 = None
    res_7194 = (np.float32(0.0) - res_7186)
    scalar_out_7609 = res_7194
    return scalar_out_7609
  def futhark_entropy_scaled_f64(self, x_mem_7456, sizze_7163):
    sizze_7321 = sext_i32_i64(sizze_7163)
    segred_group_sizze_7324 = self.sizes["entropy_scaled_f64.segred_group_size_7323"]
    max_num_groups_7555 = self.sizes["entropy_scaled_f64.segred_num_groups_7325"]
    num_groups_7326 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7321 + sext_i32_i64(segred_group_sizze_7324)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7324)),
                                                 sext_i32_i64(max_num_groups_7555))))
    mem_7460 = opencl_alloc(self, np.int64(8), "mem_7460")
    counter_mem_7556 = self.counter_mem_7556
    group_res_arr_mem_7558 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_7324 * num_groups_7326)),
                                          "group_res_arr_mem_7558")
    num_threads_7560 = (num_groups_7326 * segred_group_sizze_7324)
    if ((1 * (np.long(num_groups_7326) * np.long(segred_group_sizze_7324))) != 0):
      self.segred_nonseg_7331_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_7324))),
                                           np.int32(sizze_7163),
                                           np.int32(num_groups_7326),
                                           x_mem_7456, mem_7460,
                                           counter_mem_7556,
                                           group_res_arr_mem_7558,
                                           np.int32(num_threads_7560))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7331_var,
                                 ((np.long(num_groups_7326) * np.long(segred_group_sizze_7324)),),
                                 (np.long(segred_group_sizze_7324),))
      if synchronous:
        self.queue.finish()
    read_res_7905 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_7905, mem_7460,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_7165 = read_res_7905[0]
    mem_7460 = None
    segred_group_sizze_7335 = self.sizes["entropy_scaled_f64.segred_group_size_7334"]
    max_num_groups_7582 = self.sizes["entropy_scaled_f64.segred_num_groups_7336"]
    num_groups_7337 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7321 + sext_i32_i64(segred_group_sizze_7335)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7335)),
                                                 sext_i32_i64(max_num_groups_7582))))
    mem_7464 = opencl_alloc(self, np.int64(8), "mem_7464")
    counter_mem_7583 = self.counter_mem_7583
    group_res_arr_mem_7585 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_7335 * num_groups_7337)),
                                          "group_res_arr_mem_7585")
    num_threads_7587 = (num_groups_7337 * segred_group_sizze_7335)
    if ((1 * (np.long(num_groups_7337) * np.long(segred_group_sizze_7335))) != 0):
      self.segred_nonseg_7342_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_7335))),
                                           np.int32(sizze_7163),
                                           np.float64(res_7165),
                                           np.int32(num_groups_7337),
                                           x_mem_7456, mem_7464,
                                           counter_mem_7583,
                                           group_res_arr_mem_7585,
                                           np.int32(num_threads_7587))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7342_var,
                                 ((np.long(num_groups_7337) * np.long(segred_group_sizze_7335)),),
                                 (np.long(segred_group_sizze_7335),))
      if synchronous:
        self.queue.finish()
    read_res_7907 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_7907, mem_7464,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_7170 = read_res_7907[0]
    mem_7464 = None
    res_7178 = (np.float64(0.0) - res_7170)
    scalar_out_7554 = res_7178
    return scalar_out_7554
  def futhark_entropy_f32(self, x_mem_7456, sizze_7153):
    sizze_7310 = sext_i32_i64(sizze_7153)
    segred_group_sizze_7313 = self.sizes["entropy_f32.segred_group_size_7312"]
    max_num_groups_7527 = self.sizes["entropy_f32.segred_num_groups_7314"]
    num_groups_7315 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7310 + sext_i32_i64(segred_group_sizze_7313)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7313)),
                                                 sext_i32_i64(max_num_groups_7527))))
    mem_7460 = opencl_alloc(self, np.int64(4), "mem_7460")
    counter_mem_7528 = self.counter_mem_7528
    group_res_arr_mem_7530 = opencl_alloc(self,
                                          (np.int32(4) * (segred_group_sizze_7313 * num_groups_7315)),
                                          "group_res_arr_mem_7530")
    num_threads_7532 = (num_groups_7315 * segred_group_sizze_7313)
    if ((1 * (np.long(num_groups_7315) * np.long(segred_group_sizze_7313))) != 0):
      self.segred_nonseg_7320_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_7313))),
                                           np.int32(sizze_7153),
                                           np.int32(num_groups_7315),
                                           x_mem_7456, mem_7460,
                                           counter_mem_7528,
                                           group_res_arr_mem_7530,
                                           np.int32(num_threads_7532))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7320_var,
                                 ((np.long(num_groups_7315) * np.long(segred_group_sizze_7313)),),
                                 (np.long(segred_group_sizze_7313),))
      if synchronous:
        self.queue.finish()
    read_res_7909 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_7909, mem_7460,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_7155 = read_res_7909[0]
    mem_7460 = None
    res_7162 = (np.float32(0.0) - res_7155)
    scalar_out_7526 = res_7162
    return scalar_out_7526
  def futhark_entropy_f64(self, x_mem_7456, sizze_7143):
    sizze_7299 = sext_i32_i64(sizze_7143)
    segred_group_sizze_7302 = self.sizes["entropy_f64.segred_group_size_7301"]
    max_num_groups_7499 = self.sizes["entropy_f64.segred_num_groups_7303"]
    num_groups_7304 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_7299 + sext_i32_i64(segred_group_sizze_7302)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_7302)),
                                                 sext_i32_i64(max_num_groups_7499))))
    mem_7460 = opencl_alloc(self, np.int64(8), "mem_7460")
    counter_mem_7500 = self.counter_mem_7500
    group_res_arr_mem_7502 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_7302 * num_groups_7304)),
                                          "group_res_arr_mem_7502")
    num_threads_7504 = (num_groups_7304 * segred_group_sizze_7302)
    if ((1 * (np.long(num_groups_7304) * np.long(segred_group_sizze_7302))) != 0):
      self.segred_nonseg_7309_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_7302))),
                                           np.int32(sizze_7143),
                                           np.int32(num_groups_7304),
                                           x_mem_7456, mem_7460,
                                           counter_mem_7500,
                                           group_res_arr_mem_7502,
                                           np.int32(num_threads_7504))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_7309_var,
                                 ((np.long(num_groups_7304) * np.long(segred_group_sizze_7302)),),
                                 (np.long(segred_group_sizze_7302),))
      if synchronous:
        self.queue.finish()
    read_res_7911 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_7911, mem_7460,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_7145 = read_res_7911[0]
    mem_7460 = None
    res_7152 = (np.float64(0.0) - res_7145)
    scalar_out_7498 = res_7152
    return scalar_out_7498
  def kullback_liebler_scaled_f32(self, x_mem_7456_ext, y_mem_7457_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_7267 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    try:
      assert ((type(y_mem_7457_ext) in [np.ndarray,
                                        cl.array.Array]) and (y_mem_7457_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_7268 = np.int32(y_mem_7457_ext.shape[0])
      if (type(y_mem_7457_ext) == cl.array.Array):
        y_mem_7457 = y_mem_7457_ext.data
      else:
        y_mem_7457 = opencl_alloc(self, np.int64(y_mem_7457_ext.nbytes),
                                  "y_mem_7457")
        if (np.int64(y_mem_7457_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, y_mem_7457,
                          normaliseArray(y_mem_7457_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(y_mem_7457_ext),
                                                                                                                            y_mem_7457_ext))
    scalar_out_7802 = self.futhark_kullback_liebler_scaled_f32(x_mem_7456,
                                                               y_mem_7457,
                                                               sizze_7267,
                                                               sizze_7268)
    return np.float32(scalar_out_7802)
  def kullback_liebler_f32(self, x_mem_7456_ext, x_mem_7457_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_7247 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    try:
      assert ((type(x_mem_7457_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7457_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_7248 = np.int32(x_mem_7457_ext.shape[0])
      if (type(x_mem_7457_ext) == cl.array.Array):
        x_mem_7457 = x_mem_7457_ext.data
      else:
        x_mem_7457 = opencl_alloc(self, np.int64(x_mem_7457_ext.nbytes),
                                  "x_mem_7457")
        if (np.int64(x_mem_7457_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7457,
                          normaliseArray(x_mem_7457_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_7457_ext),
                                                                                                                            x_mem_7457_ext))
    scalar_out_7774 = self.futhark_kullback_liebler_f32(x_mem_7456, x_mem_7457,
                                                        sizze_7247, sizze_7248)
    return np.float32(scalar_out_7774)
  def kullback_liebler_scaled_f64(self, x_mem_7456_ext, y_mem_7457_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_7215 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    try:
      assert ((type(y_mem_7457_ext) in [np.ndarray,
                                        cl.array.Array]) and (y_mem_7457_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_7216 = np.int32(y_mem_7457_ext.shape[0])
      if (type(y_mem_7457_ext) == cl.array.Array):
        y_mem_7457 = y_mem_7457_ext.data
      else:
        y_mem_7457 = opencl_alloc(self, np.int64(y_mem_7457_ext.nbytes),
                                  "y_mem_7457")
        if (np.int64(y_mem_7457_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, y_mem_7457,
                          normaliseArray(y_mem_7457_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(y_mem_7457_ext),
                                                                                                                            y_mem_7457_ext))
    scalar_out_7692 = self.futhark_kullback_liebler_scaled_f64(x_mem_7456,
                                                               y_mem_7457,
                                                               sizze_7215,
                                                               sizze_7216)
    return np.float64(scalar_out_7692)
  def kullback_liebler_f64(self, x_mem_7456_ext, x_mem_7457_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_7195 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    try:
      assert ((type(x_mem_7457_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7457_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_7196 = np.int32(x_mem_7457_ext.shape[0])
      if (type(x_mem_7457_ext) == cl.array.Array):
        x_mem_7457 = x_mem_7457_ext.data
      else:
        x_mem_7457 = opencl_alloc(self, np.int64(x_mem_7457_ext.nbytes),
                                  "x_mem_7457")
        if (np.int64(x_mem_7457_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7457,
                          normaliseArray(x_mem_7457_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_7457_ext),
                                                                                                                            x_mem_7457_ext))
    scalar_out_7664 = self.futhark_kullback_liebler_f64(x_mem_7456, x_mem_7457,
                                                        sizze_7195, sizze_7196)
    return np.float64(scalar_out_7664)
  def entropy_scaled_f32(self, x_mem_7456_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_7179 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    scalar_out_7609 = self.futhark_entropy_scaled_f32(x_mem_7456, sizze_7179)
    return np.float32(scalar_out_7609)
  def entropy_scaled_f64(self, x_mem_7456_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_7163 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    scalar_out_7554 = self.futhark_entropy_scaled_f64(x_mem_7456, sizze_7163)
    return np.float64(scalar_out_7554)
  def entropy_f32(self, x_mem_7456_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_7153 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    scalar_out_7526 = self.futhark_entropy_f32(x_mem_7456, sizze_7153)
    return np.float32(scalar_out_7526)
  def entropy_f64(self, x_mem_7456_ext):
    try:
      assert ((type(x_mem_7456_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_7456_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_7143 = np.int32(x_mem_7456_ext.shape[0])
      if (type(x_mem_7456_ext) == cl.array.Array):
        x_mem_7456 = x_mem_7456_ext.data
      else:
        x_mem_7456 = opencl_alloc(self, np.int64(x_mem_7456_ext.nbytes),
                                  "x_mem_7456")
        if (np.int64(x_mem_7456_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_7456,
                          normaliseArray(x_mem_7456_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_7456_ext),
                                                                                                                            x_mem_7456_ext))
    scalar_out_7498 = self.futhark_entropy_f64(x_mem_7456, sizze_7143)
    return np.float64(scalar_out_7498)