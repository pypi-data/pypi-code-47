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
__kernel void segred_nonseg_5569(__local volatile
                                 int64_t *sync_arr_mem_5679_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_5681_backing_aligned_1,
                                 int32_t sizze_5481, int32_t num_groups_5564,
                                 __global unsigned char *x_mem_5639, __global
                                 unsigned char *mem_5643, __global
                                 unsigned char *counter_mem_5669, __global
                                 unsigned char *group_res_arr_mem_5671,
                                 int32_t num_threads_5673)
{
    const int32_t segred_group_sizze_5562 =
                  entropy_f64zisegred_group_sizze_5561;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_5679_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_5679_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_5681_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_5681_backing_aligned_1;
    int32_t global_tid_5674;
    int32_t local_tid_5675;
    int32_t group_sizze_5678;
    int32_t wave_sizze_5677;
    int32_t group_tid_5676;
    
    global_tid_5674 = get_global_id(0);
    local_tid_5675 = get_local_id(0);
    group_sizze_5678 = get_local_size(0);
    wave_sizze_5677 = LOCKSTEP_WIDTH;
    group_tid_5676 = get_group_id(0);
    
    int32_t phys_tid_5569 = global_tid_5674;
    __local char *sync_arr_mem_5679;
    
    sync_arr_mem_5679 = (__local char *) sync_arr_mem_5679_backing_0;
    
    __local char *red_arr_mem_5681;
    
    red_arr_mem_5681 = (__local char *) red_arr_mem_5681_backing_1;
    
    int32_t dummy_5567 = 0;
    int32_t gtid_5568;
    
    gtid_5568 = 0;
    
    double x_acc_5683;
    int32_t chunk_sizze_5684 = smin32(squot32(sizze_5481 +
                                              segred_group_sizze_5562 *
                                              num_groups_5564 - 1,
                                              segred_group_sizze_5562 *
                                              num_groups_5564),
                                      squot32(sizze_5481 - phys_tid_5569 +
                                              num_threads_5673 - 1,
                                              num_threads_5673));
    double x_5484;
    double x_5485;
    
    // neutral-initialise the accumulators
    {
        x_acc_5683 = 0.0;
    }
    for (int32_t i_5688 = 0; i_5688 < chunk_sizze_5684; i_5688++) {
        gtid_5568 = phys_tid_5569 + num_threads_5673 * i_5688;
        // apply map function
        {
            double x_5487 = ((__global double *) x_mem_5639)[gtid_5568];
            double res_5488;
            
            res_5488 = futrts_log64(x_5487);
            
            double res_5489 = x_5487 * res_5488;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_5484 = x_acc_5683;
            }
            // load new values
            {
                x_5485 = res_5489;
            }
            // apply reduction operator
            {
                double res_5486 = x_5484 + x_5485;
                
                // store in accumulator
                {
                    x_acc_5683 = res_5486;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_5484 = x_acc_5683;
        ((__local double *) red_arr_mem_5681)[local_tid_5675] = x_5484;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_5689;
    int32_t skip_waves_5690;
    double x_5685;
    double x_5686;
    
    offset_5689 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_5675, segred_group_sizze_5562)) {
            x_5685 = ((__local double *) red_arr_mem_5681)[local_tid_5675 +
                                                           offset_5689];
        }
    }
    offset_5689 = 1;
    while (slt32(offset_5689, wave_sizze_5677)) {
        if (slt32(local_tid_5675 + offset_5689, segred_group_sizze_5562) &&
            ((local_tid_5675 - squot32(local_tid_5675, wave_sizze_5677) *
              wave_sizze_5677) & (2 * offset_5689 - 1)) == 0) {
            // read array element
            {
                x_5686 = ((volatile __local
                           double *) red_arr_mem_5681)[local_tid_5675 +
                                                       offset_5689];
            }
            // apply reduction operation
            {
                double res_5687 = x_5685 + x_5686;
                
                x_5685 = res_5687;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_5681)[local_tid_5675] =
                    x_5685;
            }
        }
        offset_5689 *= 2;
    }
    skip_waves_5690 = 1;
    while (slt32(skip_waves_5690, squot32(segred_group_sizze_5562 +
                                          wave_sizze_5677 - 1,
                                          wave_sizze_5677))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_5689 = skip_waves_5690 * wave_sizze_5677;
        if (slt32(local_tid_5675 + offset_5689, segred_group_sizze_5562) &&
            ((local_tid_5675 - squot32(local_tid_5675, wave_sizze_5677) *
              wave_sizze_5677) == 0 && (squot32(local_tid_5675,
                                                wave_sizze_5677) & (2 *
                                                                    skip_waves_5690 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_5686 = ((__local double *) red_arr_mem_5681)[local_tid_5675 +
                                                               offset_5689];
            }
            // apply reduction operation
            {
                double res_5687 = x_5685 + x_5686;
                
                x_5685 = res_5687;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_5681)[local_tid_5675] = x_5685;
            }
        }
        skip_waves_5690 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_5675 == 0) {
            x_acc_5683 = x_5685;
        }
    }
    
    int32_t old_counter_5691;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_5675 == 0) {
            ((__global double *) group_res_arr_mem_5671)[group_tid_5676 *
                                                         segred_group_sizze_5562] =
                x_acc_5683;
            mem_fence_global();
            old_counter_5691 = atomic_add(&((volatile __global
                                             int *) counter_mem_5669)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_5679)[0] = old_counter_5691 ==
                num_groups_5564 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_5692 = ((__local bool *) sync_arr_mem_5679)[0];
    
    if (is_last_group_5692) {
        if (local_tid_5675 == 0) {
            old_counter_5691 = atomic_add(&((volatile __global
                                             int *) counter_mem_5669)[0],
                                          (int) (0 - num_groups_5564));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_5675, num_groups_5564)) {
                x_5484 = ((__global
                           double *) group_res_arr_mem_5671)[local_tid_5675 *
                                                             segred_group_sizze_5562];
            } else {
                x_5484 = 0.0;
            }
            ((__local double *) red_arr_mem_5681)[local_tid_5675] = x_5484;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_5693;
            int32_t skip_waves_5694;
            double x_5685;
            double x_5686;
            
            offset_5693 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_5675, segred_group_sizze_5562)) {
                    x_5685 = ((__local
                               double *) red_arr_mem_5681)[local_tid_5675 +
                                                           offset_5693];
                }
            }
            offset_5693 = 1;
            while (slt32(offset_5693, wave_sizze_5677)) {
                if (slt32(local_tid_5675 + offset_5693,
                          segred_group_sizze_5562) && ((local_tid_5675 -
                                                        squot32(local_tid_5675,
                                                                wave_sizze_5677) *
                                                        wave_sizze_5677) & (2 *
                                                                            offset_5693 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_5686 = ((volatile __local
                                   double *) red_arr_mem_5681)[local_tid_5675 +
                                                               offset_5693];
                    }
                    // apply reduction operation
                    {
                        double res_5687 = x_5685 + x_5686;
                        
                        x_5685 = res_5687;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_5681)[local_tid_5675] = x_5685;
                    }
                }
                offset_5693 *= 2;
            }
            skip_waves_5694 = 1;
            while (slt32(skip_waves_5694, squot32(segred_group_sizze_5562 +
                                                  wave_sizze_5677 - 1,
                                                  wave_sizze_5677))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_5693 = skip_waves_5694 * wave_sizze_5677;
                if (slt32(local_tid_5675 + offset_5693,
                          segred_group_sizze_5562) && ((local_tid_5675 -
                                                        squot32(local_tid_5675,
                                                                wave_sizze_5677) *
                                                        wave_sizze_5677) == 0 &&
                                                       (squot32(local_tid_5675,
                                                                wave_sizze_5677) &
                                                        (2 * skip_waves_5694 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_5686 = ((__local
                                   double *) red_arr_mem_5681)[local_tid_5675 +
                                                               offset_5693];
                    }
                    // apply reduction operation
                    {
                        double res_5687 = x_5685 + x_5686;
                        
                        x_5685 = res_5687;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_5681)[local_tid_5675] =
                            x_5685;
                    }
                }
                skip_waves_5694 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_5675 == 0) {
                    ((__global double *) mem_5643)[0] = x_5685;
                }
            }
        }
    }
}
__kernel void segred_nonseg_5580(__local volatile
                                 int64_t *sync_arr_mem_5707_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_5709_backing_aligned_1,
                                 int32_t sizze_5491, int32_t num_groups_5575,
                                 __global unsigned char *x_mem_5639, __global
                                 unsigned char *mem_5643, __global
                                 unsigned char *counter_mem_5697, __global
                                 unsigned char *group_res_arr_mem_5699,
                                 int32_t num_threads_5701)
{
    const int32_t segred_group_sizze_5573 =
                  entropy_scaled_f64zisegred_group_sizze_5572;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_5707_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_5707_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_5709_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_5709_backing_aligned_1;
    int32_t global_tid_5702;
    int32_t local_tid_5703;
    int32_t group_sizze_5706;
    int32_t wave_sizze_5705;
    int32_t group_tid_5704;
    
    global_tid_5702 = get_global_id(0);
    local_tid_5703 = get_local_id(0);
    group_sizze_5706 = get_local_size(0);
    wave_sizze_5705 = LOCKSTEP_WIDTH;
    group_tid_5704 = get_group_id(0);
    
    int32_t phys_tid_5580 = global_tid_5702;
    __local char *sync_arr_mem_5707;
    
    sync_arr_mem_5707 = (__local char *) sync_arr_mem_5707_backing_0;
    
    __local char *red_arr_mem_5709;
    
    red_arr_mem_5709 = (__local char *) red_arr_mem_5709_backing_1;
    
    int32_t dummy_5578 = 0;
    int32_t gtid_5579;
    
    gtid_5579 = 0;
    
    double x_acc_5711;
    int32_t chunk_sizze_5712 = smin32(squot32(sizze_5491 +
                                              segred_group_sizze_5573 *
                                              num_groups_5575 - 1,
                                              segred_group_sizze_5573 *
                                              num_groups_5575),
                                      squot32(sizze_5491 - phys_tid_5580 +
                                              num_threads_5701 - 1,
                                              num_threads_5701));
    double x_5494;
    double x_5495;
    
    // neutral-initialise the accumulators
    {
        x_acc_5711 = 0.0;
    }
    for (int32_t i_5716 = 0; i_5716 < chunk_sizze_5712; i_5716++) {
        gtid_5579 = phys_tid_5580 + num_threads_5701 * i_5716;
        // apply map function
        {
            double x_5497 = ((__global double *) x_mem_5639)[gtid_5579];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_5494 = x_acc_5711;
            }
            // load new values
            {
                x_5495 = x_5497;
            }
            // apply reduction operator
            {
                double res_5496 = x_5494 + x_5495;
                
                // store in accumulator
                {
                    x_acc_5711 = res_5496;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_5494 = x_acc_5711;
        ((__local double *) red_arr_mem_5709)[local_tid_5703] = x_5494;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_5717;
    int32_t skip_waves_5718;
    double x_5713;
    double x_5714;
    
    offset_5717 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_5703, segred_group_sizze_5573)) {
            x_5713 = ((__local double *) red_arr_mem_5709)[local_tid_5703 +
                                                           offset_5717];
        }
    }
    offset_5717 = 1;
    while (slt32(offset_5717, wave_sizze_5705)) {
        if (slt32(local_tid_5703 + offset_5717, segred_group_sizze_5573) &&
            ((local_tid_5703 - squot32(local_tid_5703, wave_sizze_5705) *
              wave_sizze_5705) & (2 * offset_5717 - 1)) == 0) {
            // read array element
            {
                x_5714 = ((volatile __local
                           double *) red_arr_mem_5709)[local_tid_5703 +
                                                       offset_5717];
            }
            // apply reduction operation
            {
                double res_5715 = x_5713 + x_5714;
                
                x_5713 = res_5715;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_5709)[local_tid_5703] =
                    x_5713;
            }
        }
        offset_5717 *= 2;
    }
    skip_waves_5718 = 1;
    while (slt32(skip_waves_5718, squot32(segred_group_sizze_5573 +
                                          wave_sizze_5705 - 1,
                                          wave_sizze_5705))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_5717 = skip_waves_5718 * wave_sizze_5705;
        if (slt32(local_tid_5703 + offset_5717, segred_group_sizze_5573) &&
            ((local_tid_5703 - squot32(local_tid_5703, wave_sizze_5705) *
              wave_sizze_5705) == 0 && (squot32(local_tid_5703,
                                                wave_sizze_5705) & (2 *
                                                                    skip_waves_5718 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_5714 = ((__local double *) red_arr_mem_5709)[local_tid_5703 +
                                                               offset_5717];
            }
            // apply reduction operation
            {
                double res_5715 = x_5713 + x_5714;
                
                x_5713 = res_5715;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_5709)[local_tid_5703] = x_5713;
            }
        }
        skip_waves_5718 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_5703 == 0) {
            x_acc_5711 = x_5713;
        }
    }
    
    int32_t old_counter_5719;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_5703 == 0) {
            ((__global double *) group_res_arr_mem_5699)[group_tid_5704 *
                                                         segred_group_sizze_5573] =
                x_acc_5711;
            mem_fence_global();
            old_counter_5719 = atomic_add(&((volatile __global
                                             int *) counter_mem_5697)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_5707)[0] = old_counter_5719 ==
                num_groups_5575 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_5720 = ((__local bool *) sync_arr_mem_5707)[0];
    
    if (is_last_group_5720) {
        if (local_tid_5703 == 0) {
            old_counter_5719 = atomic_add(&((volatile __global
                                             int *) counter_mem_5697)[0],
                                          (int) (0 - num_groups_5575));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_5703, num_groups_5575)) {
                x_5494 = ((__global
                           double *) group_res_arr_mem_5699)[local_tid_5703 *
                                                             segred_group_sizze_5573];
            } else {
                x_5494 = 0.0;
            }
            ((__local double *) red_arr_mem_5709)[local_tid_5703] = x_5494;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_5721;
            int32_t skip_waves_5722;
            double x_5713;
            double x_5714;
            
            offset_5721 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_5703, segred_group_sizze_5573)) {
                    x_5713 = ((__local
                               double *) red_arr_mem_5709)[local_tid_5703 +
                                                           offset_5721];
                }
            }
            offset_5721 = 1;
            while (slt32(offset_5721, wave_sizze_5705)) {
                if (slt32(local_tid_5703 + offset_5721,
                          segred_group_sizze_5573) && ((local_tid_5703 -
                                                        squot32(local_tid_5703,
                                                                wave_sizze_5705) *
                                                        wave_sizze_5705) & (2 *
                                                                            offset_5721 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_5714 = ((volatile __local
                                   double *) red_arr_mem_5709)[local_tid_5703 +
                                                               offset_5721];
                    }
                    // apply reduction operation
                    {
                        double res_5715 = x_5713 + x_5714;
                        
                        x_5713 = res_5715;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_5709)[local_tid_5703] = x_5713;
                    }
                }
                offset_5721 *= 2;
            }
            skip_waves_5722 = 1;
            while (slt32(skip_waves_5722, squot32(segred_group_sizze_5573 +
                                                  wave_sizze_5705 - 1,
                                                  wave_sizze_5705))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_5721 = skip_waves_5722 * wave_sizze_5705;
                if (slt32(local_tid_5703 + offset_5721,
                          segred_group_sizze_5573) && ((local_tid_5703 -
                                                        squot32(local_tid_5703,
                                                                wave_sizze_5705) *
                                                        wave_sizze_5705) == 0 &&
                                                       (squot32(local_tid_5703,
                                                                wave_sizze_5705) &
                                                        (2 * skip_waves_5722 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_5714 = ((__local
                                   double *) red_arr_mem_5709)[local_tid_5703 +
                                                               offset_5721];
                    }
                    // apply reduction operation
                    {
                        double res_5715 = x_5713 + x_5714;
                        
                        x_5713 = res_5715;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_5709)[local_tid_5703] =
                            x_5713;
                    }
                }
                skip_waves_5722 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_5703 == 0) {
                    ((__global double *) mem_5643)[0] = x_5713;
                }
            }
        }
    }
}
__kernel void segred_nonseg_5591(__local volatile
                                 int64_t *sync_arr_mem_5734_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_5736_backing_aligned_1,
                                 int32_t sizze_5491, double res_5493,
                                 int32_t num_groups_5586, __global
                                 unsigned char *x_mem_5639, __global
                                 unsigned char *mem_5647, __global
                                 unsigned char *counter_mem_5724, __global
                                 unsigned char *group_res_arr_mem_5726,
                                 int32_t num_threads_5728)
{
    const int32_t segred_group_sizze_5584 =
                  entropy_scaled_f64zisegred_group_sizze_5583;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_5734_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_5734_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_5736_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_5736_backing_aligned_1;
    int32_t global_tid_5729;
    int32_t local_tid_5730;
    int32_t group_sizze_5733;
    int32_t wave_sizze_5732;
    int32_t group_tid_5731;
    
    global_tid_5729 = get_global_id(0);
    local_tid_5730 = get_local_id(0);
    group_sizze_5733 = get_local_size(0);
    wave_sizze_5732 = LOCKSTEP_WIDTH;
    group_tid_5731 = get_group_id(0);
    
    int32_t phys_tid_5591 = global_tid_5729;
    __local char *sync_arr_mem_5734;
    
    sync_arr_mem_5734 = (__local char *) sync_arr_mem_5734_backing_0;
    
    __local char *red_arr_mem_5736;
    
    red_arr_mem_5736 = (__local char *) red_arr_mem_5736_backing_1;
    
    int32_t dummy_5589 = 0;
    int32_t gtid_5590;
    
    gtid_5590 = 0;
    
    double x_acc_5738;
    int32_t chunk_sizze_5739 = smin32(squot32(sizze_5491 +
                                              segred_group_sizze_5584 *
                                              num_groups_5586 - 1,
                                              segred_group_sizze_5584 *
                                              num_groups_5586),
                                      squot32(sizze_5491 - phys_tid_5591 +
                                              num_threads_5728 - 1,
                                              num_threads_5728));
    double x_5499;
    double x_5500;
    
    // neutral-initialise the accumulators
    {
        x_acc_5738 = 0.0;
    }
    for (int32_t i_5743 = 0; i_5743 < chunk_sizze_5739; i_5743++) {
        gtid_5590 = phys_tid_5591 + num_threads_5728 * i_5743;
        // apply map function
        {
            double x_5502 = ((__global double *) x_mem_5639)[gtid_5590];
            double res_5503 = x_5502 / res_5493;
            double res_5504;
            
            res_5504 = futrts_log64(res_5503);
            
            double res_5505 = res_5503 * res_5504;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_5499 = x_acc_5738;
            }
            // load new values
            {
                x_5500 = res_5505;
            }
            // apply reduction operator
            {
                double res_5501 = x_5499 + x_5500;
                
                // store in accumulator
                {
                    x_acc_5738 = res_5501;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_5499 = x_acc_5738;
        ((__local double *) red_arr_mem_5736)[local_tid_5730] = x_5499;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_5744;
    int32_t skip_waves_5745;
    double x_5740;
    double x_5741;
    
    offset_5744 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_5730, segred_group_sizze_5584)) {
            x_5740 = ((__local double *) red_arr_mem_5736)[local_tid_5730 +
                                                           offset_5744];
        }
    }
    offset_5744 = 1;
    while (slt32(offset_5744, wave_sizze_5732)) {
        if (slt32(local_tid_5730 + offset_5744, segred_group_sizze_5584) &&
            ((local_tid_5730 - squot32(local_tid_5730, wave_sizze_5732) *
              wave_sizze_5732) & (2 * offset_5744 - 1)) == 0) {
            // read array element
            {
                x_5741 = ((volatile __local
                           double *) red_arr_mem_5736)[local_tid_5730 +
                                                       offset_5744];
            }
            // apply reduction operation
            {
                double res_5742 = x_5740 + x_5741;
                
                x_5740 = res_5742;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_5736)[local_tid_5730] =
                    x_5740;
            }
        }
        offset_5744 *= 2;
    }
    skip_waves_5745 = 1;
    while (slt32(skip_waves_5745, squot32(segred_group_sizze_5584 +
                                          wave_sizze_5732 - 1,
                                          wave_sizze_5732))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_5744 = skip_waves_5745 * wave_sizze_5732;
        if (slt32(local_tid_5730 + offset_5744, segred_group_sizze_5584) &&
            ((local_tid_5730 - squot32(local_tid_5730, wave_sizze_5732) *
              wave_sizze_5732) == 0 && (squot32(local_tid_5730,
                                                wave_sizze_5732) & (2 *
                                                                    skip_waves_5745 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_5741 = ((__local double *) red_arr_mem_5736)[local_tid_5730 +
                                                               offset_5744];
            }
            // apply reduction operation
            {
                double res_5742 = x_5740 + x_5741;
                
                x_5740 = res_5742;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_5736)[local_tid_5730] = x_5740;
            }
        }
        skip_waves_5745 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_5730 == 0) {
            x_acc_5738 = x_5740;
        }
    }
    
    int32_t old_counter_5746;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_5730 == 0) {
            ((__global double *) group_res_arr_mem_5726)[group_tid_5731 *
                                                         segred_group_sizze_5584] =
                x_acc_5738;
            mem_fence_global();
            old_counter_5746 = atomic_add(&((volatile __global
                                             int *) counter_mem_5724)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_5734)[0] = old_counter_5746 ==
                num_groups_5586 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_5747 = ((__local bool *) sync_arr_mem_5734)[0];
    
    if (is_last_group_5747) {
        if (local_tid_5730 == 0) {
            old_counter_5746 = atomic_add(&((volatile __global
                                             int *) counter_mem_5724)[0],
                                          (int) (0 - num_groups_5586));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_5730, num_groups_5586)) {
                x_5499 = ((__global
                           double *) group_res_arr_mem_5726)[local_tid_5730 *
                                                             segred_group_sizze_5584];
            } else {
                x_5499 = 0.0;
            }
            ((__local double *) red_arr_mem_5736)[local_tid_5730] = x_5499;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_5748;
            int32_t skip_waves_5749;
            double x_5740;
            double x_5741;
            
            offset_5748 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_5730, segred_group_sizze_5584)) {
                    x_5740 = ((__local
                               double *) red_arr_mem_5736)[local_tid_5730 +
                                                           offset_5748];
                }
            }
            offset_5748 = 1;
            while (slt32(offset_5748, wave_sizze_5732)) {
                if (slt32(local_tid_5730 + offset_5748,
                          segred_group_sizze_5584) && ((local_tid_5730 -
                                                        squot32(local_tid_5730,
                                                                wave_sizze_5732) *
                                                        wave_sizze_5732) & (2 *
                                                                            offset_5748 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_5741 = ((volatile __local
                                   double *) red_arr_mem_5736)[local_tid_5730 +
                                                               offset_5748];
                    }
                    // apply reduction operation
                    {
                        double res_5742 = x_5740 + x_5741;
                        
                        x_5740 = res_5742;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_5736)[local_tid_5730] = x_5740;
                    }
                }
                offset_5748 *= 2;
            }
            skip_waves_5749 = 1;
            while (slt32(skip_waves_5749, squot32(segred_group_sizze_5584 +
                                                  wave_sizze_5732 - 1,
                                                  wave_sizze_5732))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_5748 = skip_waves_5749 * wave_sizze_5732;
                if (slt32(local_tid_5730 + offset_5748,
                          segred_group_sizze_5584) && ((local_tid_5730 -
                                                        squot32(local_tid_5730,
                                                                wave_sizze_5732) *
                                                        wave_sizze_5732) == 0 &&
                                                       (squot32(local_tid_5730,
                                                                wave_sizze_5732) &
                                                        (2 * skip_waves_5749 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_5741 = ((__local
                                   double *) red_arr_mem_5736)[local_tid_5730 +
                                                               offset_5748];
                    }
                    // apply reduction operation
                    {
                        double res_5742 = x_5740 + x_5741;
                        
                        x_5740 = res_5742;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_5736)[local_tid_5730] =
                            x_5740;
                    }
                }
                skip_waves_5749 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_5730 == 0) {
                    ((__global double *) mem_5647)[0] = x_5740;
                }
            }
        }
    }
}
__kernel void segred_nonseg_5602(__local volatile
                                 int64_t *sync_arr_mem_5762_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_5764_backing_aligned_1,
                                 int32_t sizze_5507, int32_t num_groups_5597,
                                 __global unsigned char *x_mem_5639, __global
                                 unsigned char *x_mem_5640, __global
                                 unsigned char *mem_5644, __global
                                 unsigned char *counter_mem_5752, __global
                                 unsigned char *group_res_arr_mem_5754,
                                 int32_t num_threads_5756)
{
    const int32_t segred_group_sizze_5595 =
                  kullback_liebler_f64zisegred_group_sizze_5594;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_5762_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_5762_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_5764_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_5764_backing_aligned_1;
    int32_t global_tid_5757;
    int32_t local_tid_5758;
    int32_t group_sizze_5761;
    int32_t wave_sizze_5760;
    int32_t group_tid_5759;
    
    global_tid_5757 = get_global_id(0);
    local_tid_5758 = get_local_id(0);
    group_sizze_5761 = get_local_size(0);
    wave_sizze_5760 = LOCKSTEP_WIDTH;
    group_tid_5759 = get_group_id(0);
    
    int32_t phys_tid_5602 = global_tid_5757;
    __local char *sync_arr_mem_5762;
    
    sync_arr_mem_5762 = (__local char *) sync_arr_mem_5762_backing_0;
    
    __local char *red_arr_mem_5764;
    
    red_arr_mem_5764 = (__local char *) red_arr_mem_5764_backing_1;
    
    int32_t dummy_5600 = 0;
    int32_t gtid_5601;
    
    gtid_5601 = 0;
    
    double x_acc_5766;
    int32_t chunk_sizze_5767 = smin32(squot32(sizze_5507 +
                                              segred_group_sizze_5595 *
                                              num_groups_5597 - 1,
                                              segred_group_sizze_5595 *
                                              num_groups_5597),
                                      squot32(sizze_5507 - phys_tid_5602 +
                                              num_threads_5756 - 1,
                                              num_threads_5756));
    double x_5519;
    double x_5520;
    
    // neutral-initialise the accumulators
    {
        x_acc_5766 = 0.0;
    }
    for (int32_t i_5771 = 0; i_5771 < chunk_sizze_5767; i_5771++) {
        gtid_5601 = phys_tid_5602 + num_threads_5756 * i_5771;
        // apply map function
        {
            double x_5522 = ((__global double *) x_mem_5639)[gtid_5601];
            double x_5523 = ((__global double *) x_mem_5640)[gtid_5601];
            double res_5524 = x_5522 / x_5523;
            double res_5525;
            
            res_5525 = futrts_log64(res_5524);
            
            double res_5526 = x_5522 * res_5525;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_5519 = x_acc_5766;
            }
            // load new values
            {
                x_5520 = res_5526;
            }
            // apply reduction operator
            {
                double res_5521 = x_5519 + x_5520;
                
                // store in accumulator
                {
                    x_acc_5766 = res_5521;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_5519 = x_acc_5766;
        ((__local double *) red_arr_mem_5764)[local_tid_5758] = x_5519;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_5772;
    int32_t skip_waves_5773;
    double x_5768;
    double x_5769;
    
    offset_5772 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_5758, segred_group_sizze_5595)) {
            x_5768 = ((__local double *) red_arr_mem_5764)[local_tid_5758 +
                                                           offset_5772];
        }
    }
    offset_5772 = 1;
    while (slt32(offset_5772, wave_sizze_5760)) {
        if (slt32(local_tid_5758 + offset_5772, segred_group_sizze_5595) &&
            ((local_tid_5758 - squot32(local_tid_5758, wave_sizze_5760) *
              wave_sizze_5760) & (2 * offset_5772 - 1)) == 0) {
            // read array element
            {
                x_5769 = ((volatile __local
                           double *) red_arr_mem_5764)[local_tid_5758 +
                                                       offset_5772];
            }
            // apply reduction operation
            {
                double res_5770 = x_5768 + x_5769;
                
                x_5768 = res_5770;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_5764)[local_tid_5758] =
                    x_5768;
            }
        }
        offset_5772 *= 2;
    }
    skip_waves_5773 = 1;
    while (slt32(skip_waves_5773, squot32(segred_group_sizze_5595 +
                                          wave_sizze_5760 - 1,
                                          wave_sizze_5760))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_5772 = skip_waves_5773 * wave_sizze_5760;
        if (slt32(local_tid_5758 + offset_5772, segred_group_sizze_5595) &&
            ((local_tid_5758 - squot32(local_tid_5758, wave_sizze_5760) *
              wave_sizze_5760) == 0 && (squot32(local_tid_5758,
                                                wave_sizze_5760) & (2 *
                                                                    skip_waves_5773 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_5769 = ((__local double *) red_arr_mem_5764)[local_tid_5758 +
                                                               offset_5772];
            }
            // apply reduction operation
            {
                double res_5770 = x_5768 + x_5769;
                
                x_5768 = res_5770;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_5764)[local_tid_5758] = x_5768;
            }
        }
        skip_waves_5773 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_5758 == 0) {
            x_acc_5766 = x_5768;
        }
    }
    
    int32_t old_counter_5774;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_5758 == 0) {
            ((__global double *) group_res_arr_mem_5754)[group_tid_5759 *
                                                         segred_group_sizze_5595] =
                x_acc_5766;
            mem_fence_global();
            old_counter_5774 = atomic_add(&((volatile __global
                                             int *) counter_mem_5752)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_5762)[0] = old_counter_5774 ==
                num_groups_5597 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_5775 = ((__local bool *) sync_arr_mem_5762)[0];
    
    if (is_last_group_5775) {
        if (local_tid_5758 == 0) {
            old_counter_5774 = atomic_add(&((volatile __global
                                             int *) counter_mem_5752)[0],
                                          (int) (0 - num_groups_5597));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_5758, num_groups_5597)) {
                x_5519 = ((__global
                           double *) group_res_arr_mem_5754)[local_tid_5758 *
                                                             segred_group_sizze_5595];
            } else {
                x_5519 = 0.0;
            }
            ((__local double *) red_arr_mem_5764)[local_tid_5758] = x_5519;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_5776;
            int32_t skip_waves_5777;
            double x_5768;
            double x_5769;
            
            offset_5776 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_5758, segred_group_sizze_5595)) {
                    x_5768 = ((__local
                               double *) red_arr_mem_5764)[local_tid_5758 +
                                                           offset_5776];
                }
            }
            offset_5776 = 1;
            while (slt32(offset_5776, wave_sizze_5760)) {
                if (slt32(local_tid_5758 + offset_5776,
                          segred_group_sizze_5595) && ((local_tid_5758 -
                                                        squot32(local_tid_5758,
                                                                wave_sizze_5760) *
                                                        wave_sizze_5760) & (2 *
                                                                            offset_5776 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_5769 = ((volatile __local
                                   double *) red_arr_mem_5764)[local_tid_5758 +
                                                               offset_5776];
                    }
                    // apply reduction operation
                    {
                        double res_5770 = x_5768 + x_5769;
                        
                        x_5768 = res_5770;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_5764)[local_tid_5758] = x_5768;
                    }
                }
                offset_5776 *= 2;
            }
            skip_waves_5777 = 1;
            while (slt32(skip_waves_5777, squot32(segred_group_sizze_5595 +
                                                  wave_sizze_5760 - 1,
                                                  wave_sizze_5760))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_5776 = skip_waves_5777 * wave_sizze_5760;
                if (slt32(local_tid_5758 + offset_5776,
                          segred_group_sizze_5595) && ((local_tid_5758 -
                                                        squot32(local_tid_5758,
                                                                wave_sizze_5760) *
                                                        wave_sizze_5760) == 0 &&
                                                       (squot32(local_tid_5758,
                                                                wave_sizze_5760) &
                                                        (2 * skip_waves_5777 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_5769 = ((__local
                                   double *) red_arr_mem_5764)[local_tid_5758 +
                                                               offset_5776];
                    }
                    // apply reduction operation
                    {
                        double res_5770 = x_5768 + x_5769;
                        
                        x_5768 = res_5770;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_5764)[local_tid_5758] =
                            x_5768;
                    }
                }
                skip_waves_5777 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_5758 == 0) {
                    ((__global double *) mem_5644)[0] = x_5768;
                }
            }
        }
    }
}
__kernel void segred_nonseg_5613(__local volatile
                                 int64_t *sync_arr_mem_5790_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_5792_backing_aligned_1,
                                 int32_t sizze_5527, int32_t num_groups_5608,
                                 __global unsigned char *x_mem_5639, __global
                                 unsigned char *mem_5644, __global
                                 unsigned char *counter_mem_5780, __global
                                 unsigned char *group_res_arr_mem_5782,
                                 int32_t num_threads_5784)
{
    const int32_t segred_group_sizze_5606 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_5605;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_5790_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_5790_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_5792_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_5792_backing_aligned_1;
    int32_t global_tid_5785;
    int32_t local_tid_5786;
    int32_t group_sizze_5789;
    int32_t wave_sizze_5788;
    int32_t group_tid_5787;
    
    global_tid_5785 = get_global_id(0);
    local_tid_5786 = get_local_id(0);
    group_sizze_5789 = get_local_size(0);
    wave_sizze_5788 = LOCKSTEP_WIDTH;
    group_tid_5787 = get_group_id(0);
    
    int32_t phys_tid_5613 = global_tid_5785;
    __local char *sync_arr_mem_5790;
    
    sync_arr_mem_5790 = (__local char *) sync_arr_mem_5790_backing_0;
    
    __local char *red_arr_mem_5792;
    
    red_arr_mem_5792 = (__local char *) red_arr_mem_5792_backing_1;
    
    int32_t dummy_5611 = 0;
    int32_t gtid_5612;
    
    gtid_5612 = 0;
    
    double x_acc_5794;
    int32_t chunk_sizze_5795 = smin32(squot32(sizze_5527 +
                                              segred_group_sizze_5606 *
                                              num_groups_5608 - 1,
                                              segred_group_sizze_5606 *
                                              num_groups_5608),
                                      squot32(sizze_5527 - phys_tid_5613 +
                                              num_threads_5784 - 1,
                                              num_threads_5784));
    double x_5532;
    double x_5533;
    
    // neutral-initialise the accumulators
    {
        x_acc_5794 = 0.0;
    }
    for (int32_t i_5799 = 0; i_5799 < chunk_sizze_5795; i_5799++) {
        gtid_5612 = phys_tid_5613 + num_threads_5784 * i_5799;
        // apply map function
        {
            double x_5535 = ((__global double *) x_mem_5639)[gtid_5612];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_5532 = x_acc_5794;
            }
            // load new values
            {
                x_5533 = x_5535;
            }
            // apply reduction operator
            {
                double res_5534 = x_5532 + x_5533;
                
                // store in accumulator
                {
                    x_acc_5794 = res_5534;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_5532 = x_acc_5794;
        ((__local double *) red_arr_mem_5792)[local_tid_5786] = x_5532;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_5800;
    int32_t skip_waves_5801;
    double x_5796;
    double x_5797;
    
    offset_5800 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_5786, segred_group_sizze_5606)) {
            x_5796 = ((__local double *) red_arr_mem_5792)[local_tid_5786 +
                                                           offset_5800];
        }
    }
    offset_5800 = 1;
    while (slt32(offset_5800, wave_sizze_5788)) {
        if (slt32(local_tid_5786 + offset_5800, segred_group_sizze_5606) &&
            ((local_tid_5786 - squot32(local_tid_5786, wave_sizze_5788) *
              wave_sizze_5788) & (2 * offset_5800 - 1)) == 0) {
            // read array element
            {
                x_5797 = ((volatile __local
                           double *) red_arr_mem_5792)[local_tid_5786 +
                                                       offset_5800];
            }
            // apply reduction operation
            {
                double res_5798 = x_5796 + x_5797;
                
                x_5796 = res_5798;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_5792)[local_tid_5786] =
                    x_5796;
            }
        }
        offset_5800 *= 2;
    }
    skip_waves_5801 = 1;
    while (slt32(skip_waves_5801, squot32(segred_group_sizze_5606 +
                                          wave_sizze_5788 - 1,
                                          wave_sizze_5788))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_5800 = skip_waves_5801 * wave_sizze_5788;
        if (slt32(local_tid_5786 + offset_5800, segred_group_sizze_5606) &&
            ((local_tid_5786 - squot32(local_tid_5786, wave_sizze_5788) *
              wave_sizze_5788) == 0 && (squot32(local_tid_5786,
                                                wave_sizze_5788) & (2 *
                                                                    skip_waves_5801 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_5797 = ((__local double *) red_arr_mem_5792)[local_tid_5786 +
                                                               offset_5800];
            }
            // apply reduction operation
            {
                double res_5798 = x_5796 + x_5797;
                
                x_5796 = res_5798;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_5792)[local_tid_5786] = x_5796;
            }
        }
        skip_waves_5801 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_5786 == 0) {
            x_acc_5794 = x_5796;
        }
    }
    
    int32_t old_counter_5802;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_5786 == 0) {
            ((__global double *) group_res_arr_mem_5782)[group_tid_5787 *
                                                         segred_group_sizze_5606] =
                x_acc_5794;
            mem_fence_global();
            old_counter_5802 = atomic_add(&((volatile __global
                                             int *) counter_mem_5780)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_5790)[0] = old_counter_5802 ==
                num_groups_5608 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_5803 = ((__local bool *) sync_arr_mem_5790)[0];
    
    if (is_last_group_5803) {
        if (local_tid_5786 == 0) {
            old_counter_5802 = atomic_add(&((volatile __global
                                             int *) counter_mem_5780)[0],
                                          (int) (0 - num_groups_5608));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_5786, num_groups_5608)) {
                x_5532 = ((__global
                           double *) group_res_arr_mem_5782)[local_tid_5786 *
                                                             segred_group_sizze_5606];
            } else {
                x_5532 = 0.0;
            }
            ((__local double *) red_arr_mem_5792)[local_tid_5786] = x_5532;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_5804;
            int32_t skip_waves_5805;
            double x_5796;
            double x_5797;
            
            offset_5804 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_5786, segred_group_sizze_5606)) {
                    x_5796 = ((__local
                               double *) red_arr_mem_5792)[local_tid_5786 +
                                                           offset_5804];
                }
            }
            offset_5804 = 1;
            while (slt32(offset_5804, wave_sizze_5788)) {
                if (slt32(local_tid_5786 + offset_5804,
                          segred_group_sizze_5606) && ((local_tid_5786 -
                                                        squot32(local_tid_5786,
                                                                wave_sizze_5788) *
                                                        wave_sizze_5788) & (2 *
                                                                            offset_5804 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_5797 = ((volatile __local
                                   double *) red_arr_mem_5792)[local_tid_5786 +
                                                               offset_5804];
                    }
                    // apply reduction operation
                    {
                        double res_5798 = x_5796 + x_5797;
                        
                        x_5796 = res_5798;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_5792)[local_tid_5786] = x_5796;
                    }
                }
                offset_5804 *= 2;
            }
            skip_waves_5805 = 1;
            while (slt32(skip_waves_5805, squot32(segred_group_sizze_5606 +
                                                  wave_sizze_5788 - 1,
                                                  wave_sizze_5788))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_5804 = skip_waves_5805 * wave_sizze_5788;
                if (slt32(local_tid_5786 + offset_5804,
                          segred_group_sizze_5606) && ((local_tid_5786 -
                                                        squot32(local_tid_5786,
                                                                wave_sizze_5788) *
                                                        wave_sizze_5788) == 0 &&
                                                       (squot32(local_tid_5786,
                                                                wave_sizze_5788) &
                                                        (2 * skip_waves_5805 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_5797 = ((__local
                                   double *) red_arr_mem_5792)[local_tid_5786 +
                                                               offset_5804];
                    }
                    // apply reduction operation
                    {
                        double res_5798 = x_5796 + x_5797;
                        
                        x_5796 = res_5798;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_5792)[local_tid_5786] =
                            x_5796;
                    }
                }
                skip_waves_5805 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_5786 == 0) {
                    ((__global double *) mem_5644)[0] = x_5796;
                }
            }
        }
    }
}
__kernel void segred_nonseg_5624(__local volatile
                                 int64_t *sync_arr_mem_5817_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_5819_backing_aligned_1,
                                 int32_t sizze_5528, int32_t num_groups_5619,
                                 __global unsigned char *y_mem_5640, __global
                                 unsigned char *mem_5648, __global
                                 unsigned char *counter_mem_5807, __global
                                 unsigned char *group_res_arr_mem_5809,
                                 int32_t num_threads_5811)
{
    const int32_t segred_group_sizze_5617 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_5616;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_5817_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_5817_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_5819_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_5819_backing_aligned_1;
    int32_t global_tid_5812;
    int32_t local_tid_5813;
    int32_t group_sizze_5816;
    int32_t wave_sizze_5815;
    int32_t group_tid_5814;
    
    global_tid_5812 = get_global_id(0);
    local_tid_5813 = get_local_id(0);
    group_sizze_5816 = get_local_size(0);
    wave_sizze_5815 = LOCKSTEP_WIDTH;
    group_tid_5814 = get_group_id(0);
    
    int32_t phys_tid_5624 = global_tid_5812;
    __local char *sync_arr_mem_5817;
    
    sync_arr_mem_5817 = (__local char *) sync_arr_mem_5817_backing_0;
    
    __local char *red_arr_mem_5819;
    
    red_arr_mem_5819 = (__local char *) red_arr_mem_5819_backing_1;
    
    int32_t dummy_5622 = 0;
    int32_t gtid_5623;
    
    gtid_5623 = 0;
    
    double x_acc_5821;
    int32_t chunk_sizze_5822 = smin32(squot32(sizze_5528 +
                                              segred_group_sizze_5617 *
                                              num_groups_5619 - 1,
                                              segred_group_sizze_5617 *
                                              num_groups_5619),
                                      squot32(sizze_5528 - phys_tid_5624 +
                                              num_threads_5811 - 1,
                                              num_threads_5811));
    double x_5538;
    double x_5539;
    
    // neutral-initialise the accumulators
    {
        x_acc_5821 = 0.0;
    }
    for (int32_t i_5826 = 0; i_5826 < chunk_sizze_5822; i_5826++) {
        gtid_5623 = phys_tid_5624 + num_threads_5811 * i_5826;
        // apply map function
        {
            double x_5541 = ((__global double *) y_mem_5640)[gtid_5623];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_5538 = x_acc_5821;
            }
            // load new values
            {
                x_5539 = x_5541;
            }
            // apply reduction operator
            {
                double res_5540 = x_5538 + x_5539;
                
                // store in accumulator
                {
                    x_acc_5821 = res_5540;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_5538 = x_acc_5821;
        ((__local double *) red_arr_mem_5819)[local_tid_5813] = x_5538;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_5827;
    int32_t skip_waves_5828;
    double x_5823;
    double x_5824;
    
    offset_5827 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_5813, segred_group_sizze_5617)) {
            x_5823 = ((__local double *) red_arr_mem_5819)[local_tid_5813 +
                                                           offset_5827];
        }
    }
    offset_5827 = 1;
    while (slt32(offset_5827, wave_sizze_5815)) {
        if (slt32(local_tid_5813 + offset_5827, segred_group_sizze_5617) &&
            ((local_tid_5813 - squot32(local_tid_5813, wave_sizze_5815) *
              wave_sizze_5815) & (2 * offset_5827 - 1)) == 0) {
            // read array element
            {
                x_5824 = ((volatile __local
                           double *) red_arr_mem_5819)[local_tid_5813 +
                                                       offset_5827];
            }
            // apply reduction operation
            {
                double res_5825 = x_5823 + x_5824;
                
                x_5823 = res_5825;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_5819)[local_tid_5813] =
                    x_5823;
            }
        }
        offset_5827 *= 2;
    }
    skip_waves_5828 = 1;
    while (slt32(skip_waves_5828, squot32(segred_group_sizze_5617 +
                                          wave_sizze_5815 - 1,
                                          wave_sizze_5815))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_5827 = skip_waves_5828 * wave_sizze_5815;
        if (slt32(local_tid_5813 + offset_5827, segred_group_sizze_5617) &&
            ((local_tid_5813 - squot32(local_tid_5813, wave_sizze_5815) *
              wave_sizze_5815) == 0 && (squot32(local_tid_5813,
                                                wave_sizze_5815) & (2 *
                                                                    skip_waves_5828 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_5824 = ((__local double *) red_arr_mem_5819)[local_tid_5813 +
                                                               offset_5827];
            }
            // apply reduction operation
            {
                double res_5825 = x_5823 + x_5824;
                
                x_5823 = res_5825;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_5819)[local_tid_5813] = x_5823;
            }
        }
        skip_waves_5828 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_5813 == 0) {
            x_acc_5821 = x_5823;
        }
    }
    
    int32_t old_counter_5829;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_5813 == 0) {
            ((__global double *) group_res_arr_mem_5809)[group_tid_5814 *
                                                         segred_group_sizze_5617] =
                x_acc_5821;
            mem_fence_global();
            old_counter_5829 = atomic_add(&((volatile __global
                                             int *) counter_mem_5807)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_5817)[0] = old_counter_5829 ==
                num_groups_5619 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_5830 = ((__local bool *) sync_arr_mem_5817)[0];
    
    if (is_last_group_5830) {
        if (local_tid_5813 == 0) {
            old_counter_5829 = atomic_add(&((volatile __global
                                             int *) counter_mem_5807)[0],
                                          (int) (0 - num_groups_5619));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_5813, num_groups_5619)) {
                x_5538 = ((__global
                           double *) group_res_arr_mem_5809)[local_tid_5813 *
                                                             segred_group_sizze_5617];
            } else {
                x_5538 = 0.0;
            }
            ((__local double *) red_arr_mem_5819)[local_tid_5813] = x_5538;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_5831;
            int32_t skip_waves_5832;
            double x_5823;
            double x_5824;
            
            offset_5831 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_5813, segred_group_sizze_5617)) {
                    x_5823 = ((__local
                               double *) red_arr_mem_5819)[local_tid_5813 +
                                                           offset_5831];
                }
            }
            offset_5831 = 1;
            while (slt32(offset_5831, wave_sizze_5815)) {
                if (slt32(local_tid_5813 + offset_5831,
                          segred_group_sizze_5617) && ((local_tid_5813 -
                                                        squot32(local_tid_5813,
                                                                wave_sizze_5815) *
                                                        wave_sizze_5815) & (2 *
                                                                            offset_5831 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_5824 = ((volatile __local
                                   double *) red_arr_mem_5819)[local_tid_5813 +
                                                               offset_5831];
                    }
                    // apply reduction operation
                    {
                        double res_5825 = x_5823 + x_5824;
                        
                        x_5823 = res_5825;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_5819)[local_tid_5813] = x_5823;
                    }
                }
                offset_5831 *= 2;
            }
            skip_waves_5832 = 1;
            while (slt32(skip_waves_5832, squot32(segred_group_sizze_5617 +
                                                  wave_sizze_5815 - 1,
                                                  wave_sizze_5815))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_5831 = skip_waves_5832 * wave_sizze_5815;
                if (slt32(local_tid_5813 + offset_5831,
                          segred_group_sizze_5617) && ((local_tid_5813 -
                                                        squot32(local_tid_5813,
                                                                wave_sizze_5815) *
                                                        wave_sizze_5815) == 0 &&
                                                       (squot32(local_tid_5813,
                                                                wave_sizze_5815) &
                                                        (2 * skip_waves_5832 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_5824 = ((__local
                                   double *) red_arr_mem_5819)[local_tid_5813 +
                                                               offset_5831];
                    }
                    // apply reduction operation
                    {
                        double res_5825 = x_5823 + x_5824;
                        
                        x_5823 = res_5825;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_5819)[local_tid_5813] =
                            x_5823;
                    }
                }
                skip_waves_5832 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_5813 == 0) {
                    ((__global double *) mem_5648)[0] = x_5823;
                }
            }
        }
    }
}
__kernel void segred_nonseg_5635(__local volatile
                                 int64_t *sync_arr_mem_5844_backing_aligned_0,
                                 __local volatile
                                 int64_t *red_arr_mem_5846_backing_aligned_1,
                                 int32_t sizze_5527, double res_5531,
                                 double res_5537, int32_t num_groups_5630,
                                 __global unsigned char *x_mem_5639, __global
                                 unsigned char *y_mem_5640, __global
                                 unsigned char *mem_5652, __global
                                 unsigned char *counter_mem_5834, __global
                                 unsigned char *group_res_arr_mem_5836,
                                 int32_t num_threads_5838)
{
    const int32_t segred_group_sizze_5628 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_5627;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_5844_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_5844_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_5846_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_5846_backing_aligned_1;
    int32_t global_tid_5839;
    int32_t local_tid_5840;
    int32_t group_sizze_5843;
    int32_t wave_sizze_5842;
    int32_t group_tid_5841;
    
    global_tid_5839 = get_global_id(0);
    local_tid_5840 = get_local_id(0);
    group_sizze_5843 = get_local_size(0);
    wave_sizze_5842 = LOCKSTEP_WIDTH;
    group_tid_5841 = get_group_id(0);
    
    int32_t phys_tid_5635 = global_tid_5839;
    __local char *sync_arr_mem_5844;
    
    sync_arr_mem_5844 = (__local char *) sync_arr_mem_5844_backing_0;
    
    __local char *red_arr_mem_5846;
    
    red_arr_mem_5846 = (__local char *) red_arr_mem_5846_backing_1;
    
    int32_t dummy_5633 = 0;
    int32_t gtid_5634;
    
    gtid_5634 = 0;
    
    double x_acc_5848;
    int32_t chunk_sizze_5849 = smin32(squot32(sizze_5527 +
                                              segred_group_sizze_5628 *
                                              num_groups_5630 - 1,
                                              segred_group_sizze_5628 *
                                              num_groups_5630),
                                      squot32(sizze_5527 - phys_tid_5635 +
                                              num_threads_5838 - 1,
                                              num_threads_5838));
    double x_5549;
    double x_5550;
    
    // neutral-initialise the accumulators
    {
        x_acc_5848 = 0.0;
    }
    for (int32_t i_5853 = 0; i_5853 < chunk_sizze_5849; i_5853++) {
        gtid_5634 = phys_tid_5635 + num_threads_5838 * i_5853;
        // apply map function
        {
            double x_5552 = ((__global double *) x_mem_5639)[gtid_5634];
            double x_5553 = ((__global double *) y_mem_5640)[gtid_5634];
            double res_5554 = x_5552 / res_5531;
            double res_5555 = x_5553 / res_5537;
            double res_5556 = res_5554 / res_5555;
            double res_5557;
            
            res_5557 = futrts_log64(res_5556);
            
            double res_5558 = res_5554 * res_5557;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_5549 = x_acc_5848;
            }
            // load new values
            {
                x_5550 = res_5558;
            }
            // apply reduction operator
            {
                double res_5551 = x_5549 + x_5550;
                
                // store in accumulator
                {
                    x_acc_5848 = res_5551;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_5549 = x_acc_5848;
        ((__local double *) red_arr_mem_5846)[local_tid_5840] = x_5549;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_5854;
    int32_t skip_waves_5855;
    double x_5850;
    double x_5851;
    
    offset_5854 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_5840, segred_group_sizze_5628)) {
            x_5850 = ((__local double *) red_arr_mem_5846)[local_tid_5840 +
                                                           offset_5854];
        }
    }
    offset_5854 = 1;
    while (slt32(offset_5854, wave_sizze_5842)) {
        if (slt32(local_tid_5840 + offset_5854, segred_group_sizze_5628) &&
            ((local_tid_5840 - squot32(local_tid_5840, wave_sizze_5842) *
              wave_sizze_5842) & (2 * offset_5854 - 1)) == 0) {
            // read array element
            {
                x_5851 = ((volatile __local
                           double *) red_arr_mem_5846)[local_tid_5840 +
                                                       offset_5854];
            }
            // apply reduction operation
            {
                double res_5852 = x_5850 + x_5851;
                
                x_5850 = res_5852;
            }
            // write result of operation
            {
                ((volatile __local double *) red_arr_mem_5846)[local_tid_5840] =
                    x_5850;
            }
        }
        offset_5854 *= 2;
    }
    skip_waves_5855 = 1;
    while (slt32(skip_waves_5855, squot32(segred_group_sizze_5628 +
                                          wave_sizze_5842 - 1,
                                          wave_sizze_5842))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_5854 = skip_waves_5855 * wave_sizze_5842;
        if (slt32(local_tid_5840 + offset_5854, segred_group_sizze_5628) &&
            ((local_tid_5840 - squot32(local_tid_5840, wave_sizze_5842) *
              wave_sizze_5842) == 0 && (squot32(local_tid_5840,
                                                wave_sizze_5842) & (2 *
                                                                    skip_waves_5855 -
                                                                    1)) == 0)) {
            // read array element
            {
                x_5851 = ((__local double *) red_arr_mem_5846)[local_tid_5840 +
                                                               offset_5854];
            }
            // apply reduction operation
            {
                double res_5852 = x_5850 + x_5851;
                
                x_5850 = res_5852;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_5846)[local_tid_5840] = x_5850;
            }
        }
        skip_waves_5855 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_5840 == 0) {
            x_acc_5848 = x_5850;
        }
    }
    
    int32_t old_counter_5856;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_5840 == 0) {
            ((__global double *) group_res_arr_mem_5836)[group_tid_5841 *
                                                         segred_group_sizze_5628] =
                x_acc_5848;
            mem_fence_global();
            old_counter_5856 = atomic_add(&((volatile __global
                                             int *) counter_mem_5834)[0],
                                          (int) 1);
            ((__local bool *) sync_arr_mem_5844)[0] = old_counter_5856 ==
                num_groups_5630 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_5857 = ((__local bool *) sync_arr_mem_5844)[0];
    
    if (is_last_group_5857) {
        if (local_tid_5840 == 0) {
            old_counter_5856 = atomic_add(&((volatile __global
                                             int *) counter_mem_5834)[0],
                                          (int) (0 - num_groups_5630));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_5840, num_groups_5630)) {
                x_5549 = ((__global
                           double *) group_res_arr_mem_5836)[local_tid_5840 *
                                                             segred_group_sizze_5628];
            } else {
                x_5549 = 0.0;
            }
            ((__local double *) red_arr_mem_5846)[local_tid_5840] = x_5549;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_5858;
            int32_t skip_waves_5859;
            double x_5850;
            double x_5851;
            
            offset_5858 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_5840, segred_group_sizze_5628)) {
                    x_5850 = ((__local
                               double *) red_arr_mem_5846)[local_tid_5840 +
                                                           offset_5858];
                }
            }
            offset_5858 = 1;
            while (slt32(offset_5858, wave_sizze_5842)) {
                if (slt32(local_tid_5840 + offset_5858,
                          segred_group_sizze_5628) && ((local_tid_5840 -
                                                        squot32(local_tid_5840,
                                                                wave_sizze_5842) *
                                                        wave_sizze_5842) & (2 *
                                                                            offset_5858 -
                                                                            1)) ==
                    0) {
                    // read array element
                    {
                        x_5851 = ((volatile __local
                                   double *) red_arr_mem_5846)[local_tid_5840 +
                                                               offset_5858];
                    }
                    // apply reduction operation
                    {
                        double res_5852 = x_5850 + x_5851;
                        
                        x_5850 = res_5852;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_5846)[local_tid_5840] = x_5850;
                    }
                }
                offset_5858 *= 2;
            }
            skip_waves_5859 = 1;
            while (slt32(skip_waves_5859, squot32(segred_group_sizze_5628 +
                                                  wave_sizze_5842 - 1,
                                                  wave_sizze_5842))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_5858 = skip_waves_5859 * wave_sizze_5842;
                if (slt32(local_tid_5840 + offset_5858,
                          segred_group_sizze_5628) && ((local_tid_5840 -
                                                        squot32(local_tid_5840,
                                                                wave_sizze_5842) *
                                                        wave_sizze_5842) == 0 &&
                                                       (squot32(local_tid_5840,
                                                                wave_sizze_5842) &
                                                        (2 * skip_waves_5859 -
                                                         1)) == 0)) {
                    // read array element
                    {
                        x_5851 = ((__local
                                   double *) red_arr_mem_5846)[local_tid_5840 +
                                                               offset_5858];
                    }
                    // apply reduction operation
                    {
                        double res_5852 = x_5850 + x_5851;
                        
                        x_5850 = res_5852;
                    }
                    // write result of operation
                    {
                        ((__local double *) red_arr_mem_5846)[local_tid_5840] =
                            x_5850;
                    }
                }
                skip_waves_5859 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_5840 == 0) {
                    ((__global double *) mem_5652)[0] = x_5850;
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
  entry_points = {"kullback_liebler_scaled_f64": (["[]f64", "[]f64"], ["f64"]),
                  "kullback_liebler_f64": (["[]f64", "[]f64"], ["f64"]),
                  "entropy_scaled_f64": (["[]f64"], ["f64"]),
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
                                       required_types=["i32", "f64", "bool"],
                                       user_sizes=sizes,
                                       all_sizes={"entropy_f64.segred_group_size_5561": {"class": "group_size", "value": None},
                                        "entropy_f64.segred_num_groups_5563": {"class": "num_groups", "value": None},
                                        "entropy_scaled_f64.segred_group_size_5572": {"class": "group_size",
                                                                                      "value": None},
                                        "entropy_scaled_f64.segred_group_size_5583": {"class": "group_size",
                                                                                      "value": None},
                                        "entropy_scaled_f64.segred_num_groups_5574": {"class": "num_groups",
                                                                                      "value": None},
                                        "entropy_scaled_f64.segred_num_groups_5585": {"class": "num_groups",
                                                                                      "value": None},
                                        "kullback_liebler_f64.segred_group_size_5594": {"class": "group_size",
                                                                                        "value": None},
                                        "kullback_liebler_f64.segred_num_groups_5596": {"class": "num_groups",
                                                                                        "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_5605": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_5616": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_5627": {"class": "group_size",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_5607": {"class": "num_groups",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_5618": {"class": "num_groups",
                                                                                               "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_5629": {"class": "num_groups",
                                                                                               "value": None}})
    self.segred_nonseg_5569_var = program.segred_nonseg_5569
    self.segred_nonseg_5580_var = program.segred_nonseg_5580
    self.segred_nonseg_5591_var = program.segred_nonseg_5591
    self.segred_nonseg_5602_var = program.segred_nonseg_5602
    self.segred_nonseg_5613_var = program.segred_nonseg_5613
    self.segred_nonseg_5624_var = program.segred_nonseg_5624
    self.segred_nonseg_5635_var = program.segred_nonseg_5635
    counter_mem_5780 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_5860 = opencl_alloc(self, 40, "static_mem_5860")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_5860,
                      normaliseArray(counter_mem_5780), is_blocking=synchronous)
    self.counter_mem_5780 = static_mem_5860
    counter_mem_5807 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_5862 = opencl_alloc(self, 40, "static_mem_5862")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_5862,
                      normaliseArray(counter_mem_5807), is_blocking=synchronous)
    self.counter_mem_5807 = static_mem_5862
    counter_mem_5834 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_5864 = opencl_alloc(self, 40, "static_mem_5864")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_5864,
                      normaliseArray(counter_mem_5834), is_blocking=synchronous)
    self.counter_mem_5834 = static_mem_5864
    counter_mem_5752 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_5866 = opencl_alloc(self, 40, "static_mem_5866")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_5866,
                      normaliseArray(counter_mem_5752), is_blocking=synchronous)
    self.counter_mem_5752 = static_mem_5866
    counter_mem_5697 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_5868 = opencl_alloc(self, 40, "static_mem_5868")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_5868,
                      normaliseArray(counter_mem_5697), is_blocking=synchronous)
    self.counter_mem_5697 = static_mem_5868
    counter_mem_5724 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_5870 = opencl_alloc(self, 40, "static_mem_5870")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_5870,
                      normaliseArray(counter_mem_5724), is_blocking=synchronous)
    self.counter_mem_5724 = static_mem_5870
    counter_mem_5669 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0), np.int32(0), np.int32(0),
                                 np.int32(0)], dtype=np.int32)
    static_mem_5872 = opencl_alloc(self, 40, "static_mem_5872")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_5872,
                      normaliseArray(counter_mem_5669), is_blocking=synchronous)
    self.counter_mem_5669 = static_mem_5872
  def futhark_kullback_liebler_scaled_f64(self, x_mem_5639, y_mem_5640,
                                          sizze_5527, sizze_5528):
    sizze_5603 = sext_i32_i64(sizze_5527)
    segred_group_sizze_5606 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_5605"]
    max_num_groups_5779 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_5607"]
    num_groups_5608 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_5603 + sext_i32_i64(segred_group_sizze_5606)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_5606)),
                                                 sext_i32_i64(max_num_groups_5779))))
    mem_5644 = opencl_alloc(self, np.int64(8), "mem_5644")
    counter_mem_5780 = self.counter_mem_5780
    group_res_arr_mem_5782 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_5606 * num_groups_5608)),
                                          "group_res_arr_mem_5782")
    num_threads_5784 = (num_groups_5608 * segred_group_sizze_5606)
    if ((1 * (np.long(num_groups_5608) * np.long(segred_group_sizze_5606))) != 0):
      self.segred_nonseg_5613_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_5606))),
                                           np.int32(sizze_5527),
                                           np.int32(num_groups_5608),
                                           x_mem_5639, mem_5644,
                                           counter_mem_5780,
                                           group_res_arr_mem_5782,
                                           np.int32(num_threads_5784))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_5613_var,
                                 ((np.long(num_groups_5608) * np.long(segred_group_sizze_5606)),),
                                 (np.long(segred_group_sizze_5606),))
      if synchronous:
        self.queue.finish()
    read_res_5861 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_5861, mem_5644,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_5531 = read_res_5861[0]
    mem_5644 = None
    dim_zzero_5536 = (np.int32(0) == sizze_5527)
    sizze_5614 = sext_i32_i64(sizze_5528)
    segred_group_sizze_5617 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_5616"]
    max_num_groups_5806 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_5618"]
    num_groups_5619 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_5614 + sext_i32_i64(segred_group_sizze_5617)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_5617)),
                                                 sext_i32_i64(max_num_groups_5806))))
    mem_5648 = opencl_alloc(self, np.int64(8), "mem_5648")
    counter_mem_5807 = self.counter_mem_5807
    group_res_arr_mem_5809 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_5617 * num_groups_5619)),
                                          "group_res_arr_mem_5809")
    num_threads_5811 = (num_groups_5619 * segred_group_sizze_5617)
    if ((1 * (np.long(num_groups_5619) * np.long(segred_group_sizze_5617))) != 0):
      self.segred_nonseg_5624_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_5617))),
                                           np.int32(sizze_5528),
                                           np.int32(num_groups_5619),
                                           y_mem_5640, mem_5648,
                                           counter_mem_5807,
                                           group_res_arr_mem_5809,
                                           np.int32(num_threads_5811))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_5624_var,
                                 ((np.long(num_groups_5619) * np.long(segred_group_sizze_5617)),),
                                 (np.long(segred_group_sizze_5617),))
      if synchronous:
        self.queue.finish()
    read_res_5863 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_5863, mem_5648,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_5537 = read_res_5863[0]
    mem_5648 = None
    dim_zzero_5542 = (np.int32(0) == sizze_5528)
    both_empty_5543 = (dim_zzero_5536 and dim_zzero_5542)
    dim_match_5544 = (sizze_5527 == sizze_5528)
    empty_or_match_5545 = (both_empty_5543 or dim_match_5544)
    empty_or_match_cert_5546 = True
    assert empty_or_match_5545, ("Error at\n |-> information.fut:31:1-32:86\n `-> information.fut:32:3-86\n\n: %s" % ("function arguments of wrong shape",))
    segred_group_sizze_5628 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_5627"]
    max_num_groups_5833 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_5629"]
    num_groups_5630 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_5603 + sext_i32_i64(segred_group_sizze_5628)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_5628)),
                                                 sext_i32_i64(max_num_groups_5833))))
    mem_5652 = opencl_alloc(self, np.int64(8), "mem_5652")
    counter_mem_5834 = self.counter_mem_5834
    group_res_arr_mem_5836 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_5628 * num_groups_5630)),
                                          "group_res_arr_mem_5836")
    num_threads_5838 = (num_groups_5630 * segred_group_sizze_5628)
    if ((1 * (np.long(num_groups_5630) * np.long(segred_group_sizze_5628))) != 0):
      self.segred_nonseg_5635_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_5628))),
                                           np.int32(sizze_5527),
                                           np.float64(res_5531),
                                           np.float64(res_5537),
                                           np.int32(num_groups_5630),
                                           x_mem_5639, y_mem_5640, mem_5652,
                                           counter_mem_5834,
                                           group_res_arr_mem_5836,
                                           np.int32(num_threads_5838))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_5635_var,
                                 ((np.long(num_groups_5630) * np.long(segred_group_sizze_5628)),),
                                 (np.long(segred_group_sizze_5628),))
      if synchronous:
        self.queue.finish()
    read_res_5865 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_5865, mem_5652,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_5548 = read_res_5865[0]
    mem_5652 = None
    scalar_out_5778 = res_5548
    return scalar_out_5778
  def futhark_kullback_liebler_f64(self, x_mem_5639, x_mem_5640, sizze_5507,
                                   sizze_5508):
    dim_zzero_5511 = (np.int32(0) == sizze_5508)
    dim_zzero_5512 = (np.int32(0) == sizze_5507)
    both_empty_5513 = (dim_zzero_5511 and dim_zzero_5512)
    dim_match_5514 = (sizze_5507 == sizze_5508)
    empty_or_match_5515 = (both_empty_5513 or dim_match_5514)
    empty_or_match_cert_5516 = True
    assert empty_or_match_5515, ("Error at\n |-> information.fut:28:1-29:34\n `-> unknown location\n\n: %s" % ("function arguments of wrong shape",))
    sizze_5592 = sext_i32_i64(sizze_5507)
    segred_group_sizze_5595 = self.sizes["kullback_liebler_f64.segred_group_size_5594"]
    max_num_groups_5751 = self.sizes["kullback_liebler_f64.segred_num_groups_5596"]
    num_groups_5597 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_5592 + sext_i32_i64(segred_group_sizze_5595)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_5595)),
                                                 sext_i32_i64(max_num_groups_5751))))
    mem_5644 = opencl_alloc(self, np.int64(8), "mem_5644")
    counter_mem_5752 = self.counter_mem_5752
    group_res_arr_mem_5754 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_5595 * num_groups_5597)),
                                          "group_res_arr_mem_5754")
    num_threads_5756 = (num_groups_5597 * segred_group_sizze_5595)
    if ((1 * (np.long(num_groups_5597) * np.long(segred_group_sizze_5595))) != 0):
      self.segred_nonseg_5602_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_5595))),
                                           np.int32(sizze_5507),
                                           np.int32(num_groups_5597),
                                           x_mem_5639, x_mem_5640, mem_5644,
                                           counter_mem_5752,
                                           group_res_arr_mem_5754,
                                           np.int32(num_threads_5756))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_5602_var,
                                 ((np.long(num_groups_5597) * np.long(segred_group_sizze_5595)),),
                                 (np.long(segred_group_sizze_5595),))
      if synchronous:
        self.queue.finish()
    read_res_5867 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_5867, mem_5644,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_5518 = read_res_5867[0]
    mem_5644 = None
    scalar_out_5750 = res_5518
    return scalar_out_5750
  def futhark_entropy_scaled_f64(self, x_mem_5639, sizze_5491):
    sizze_5570 = sext_i32_i64(sizze_5491)
    segred_group_sizze_5573 = self.sizes["entropy_scaled_f64.segred_group_size_5572"]
    max_num_groups_5696 = self.sizes["entropy_scaled_f64.segred_num_groups_5574"]
    num_groups_5575 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_5570 + sext_i32_i64(segred_group_sizze_5573)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_5573)),
                                                 sext_i32_i64(max_num_groups_5696))))
    mem_5643 = opencl_alloc(self, np.int64(8), "mem_5643")
    counter_mem_5697 = self.counter_mem_5697
    group_res_arr_mem_5699 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_5573 * num_groups_5575)),
                                          "group_res_arr_mem_5699")
    num_threads_5701 = (num_groups_5575 * segred_group_sizze_5573)
    if ((1 * (np.long(num_groups_5575) * np.long(segred_group_sizze_5573))) != 0):
      self.segred_nonseg_5580_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_5573))),
                                           np.int32(sizze_5491),
                                           np.int32(num_groups_5575),
                                           x_mem_5639, mem_5643,
                                           counter_mem_5697,
                                           group_res_arr_mem_5699,
                                           np.int32(num_threads_5701))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_5580_var,
                                 ((np.long(num_groups_5575) * np.long(segred_group_sizze_5573)),),
                                 (np.long(segred_group_sizze_5573),))
      if synchronous:
        self.queue.finish()
    read_res_5869 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_5869, mem_5643,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_5493 = read_res_5869[0]
    mem_5643 = None
    segred_group_sizze_5584 = self.sizes["entropy_scaled_f64.segred_group_size_5583"]
    max_num_groups_5723 = self.sizes["entropy_scaled_f64.segred_num_groups_5585"]
    num_groups_5586 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_5570 + sext_i32_i64(segred_group_sizze_5584)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_5584)),
                                                 sext_i32_i64(max_num_groups_5723))))
    mem_5647 = opencl_alloc(self, np.int64(8), "mem_5647")
    counter_mem_5724 = self.counter_mem_5724
    group_res_arr_mem_5726 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_5584 * num_groups_5586)),
                                          "group_res_arr_mem_5726")
    num_threads_5728 = (num_groups_5586 * segred_group_sizze_5584)
    if ((1 * (np.long(num_groups_5586) * np.long(segred_group_sizze_5584))) != 0):
      self.segred_nonseg_5591_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_5584))),
                                           np.int32(sizze_5491),
                                           np.float64(res_5493),
                                           np.int32(num_groups_5586),
                                           x_mem_5639, mem_5647,
                                           counter_mem_5724,
                                           group_res_arr_mem_5726,
                                           np.int32(num_threads_5728))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_5591_var,
                                 ((np.long(num_groups_5586) * np.long(segred_group_sizze_5584)),),
                                 (np.long(segred_group_sizze_5584),))
      if synchronous:
        self.queue.finish()
    read_res_5871 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_5871, mem_5647,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_5498 = read_res_5871[0]
    mem_5647 = None
    res_5506 = (np.float64(0.0) - res_5498)
    scalar_out_5695 = res_5506
    return scalar_out_5695
  def futhark_entropy_f64(self, x_mem_5639, sizze_5481):
    sizze_5559 = sext_i32_i64(sizze_5481)
    segred_group_sizze_5562 = self.sizes["entropy_f64.segred_group_size_5561"]
    max_num_groups_5668 = self.sizes["entropy_f64.segred_num_groups_5563"]
    num_groups_5564 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((sizze_5559 + sext_i32_i64(segred_group_sizze_5562)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_5562)),
                                                 sext_i32_i64(max_num_groups_5668))))
    mem_5643 = opencl_alloc(self, np.int64(8), "mem_5643")
    counter_mem_5669 = self.counter_mem_5669
    group_res_arr_mem_5671 = opencl_alloc(self,
                                          (np.int32(8) * (segred_group_sizze_5562 * num_groups_5564)),
                                          "group_res_arr_mem_5671")
    num_threads_5673 = (num_groups_5564 * segred_group_sizze_5562)
    if ((1 * (np.long(num_groups_5564) * np.long(segred_group_sizze_5562))) != 0):
      self.segred_nonseg_5569_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                           cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_5562))),
                                           np.int32(sizze_5481),
                                           np.int32(num_groups_5564),
                                           x_mem_5639, mem_5643,
                                           counter_mem_5669,
                                           group_res_arr_mem_5671,
                                           np.int32(num_threads_5673))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_5569_var,
                                 ((np.long(num_groups_5564) * np.long(segred_group_sizze_5562)),),
                                 (np.long(segred_group_sizze_5562),))
      if synchronous:
        self.queue.finish()
    read_res_5873 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_5873, mem_5643,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_5483 = read_res_5873[0]
    mem_5643 = None
    res_5490 = (np.float64(0.0) - res_5483)
    scalar_out_5667 = res_5490
    return scalar_out_5667
  def kullback_liebler_scaled_f64(self, x_mem_5639_ext, y_mem_5640_ext):
    try:
      assert ((type(x_mem_5639_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_5639_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_5527 = np.int32(x_mem_5639_ext.shape[0])
      if (type(x_mem_5639_ext) == cl.array.Array):
        x_mem_5639 = x_mem_5639_ext.data
      else:
        x_mem_5639 = opencl_alloc(self, np.int64(x_mem_5639_ext.nbytes),
                                  "x_mem_5639")
        if (np.int64(x_mem_5639_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_5639,
                          normaliseArray(x_mem_5639_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_5639_ext),
                                                                                                                            x_mem_5639_ext))
    try:
      assert ((type(y_mem_5640_ext) in [np.ndarray,
                                        cl.array.Array]) and (y_mem_5640_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_5528 = np.int32(y_mem_5640_ext.shape[0])
      if (type(y_mem_5640_ext) == cl.array.Array):
        y_mem_5640 = y_mem_5640_ext.data
      else:
        y_mem_5640 = opencl_alloc(self, np.int64(y_mem_5640_ext.nbytes),
                                  "y_mem_5640")
        if (np.int64(y_mem_5640_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, y_mem_5640,
                          normaliseArray(y_mem_5640_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(y_mem_5640_ext),
                                                                                                                            y_mem_5640_ext))
    scalar_out_5778 = self.futhark_kullback_liebler_scaled_f64(x_mem_5639,
                                                               y_mem_5640,
                                                               sizze_5527,
                                                               sizze_5528)
    return np.float64(scalar_out_5778)
  def kullback_liebler_f64(self, x_mem_5639_ext, x_mem_5640_ext):
    try:
      assert ((type(x_mem_5639_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_5639_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_5507 = np.int32(x_mem_5639_ext.shape[0])
      if (type(x_mem_5639_ext) == cl.array.Array):
        x_mem_5639 = x_mem_5639_ext.data
      else:
        x_mem_5639 = opencl_alloc(self, np.int64(x_mem_5639_ext.nbytes),
                                  "x_mem_5639")
        if (np.int64(x_mem_5639_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_5639,
                          normaliseArray(x_mem_5639_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_5639_ext),
                                                                                                                            x_mem_5639_ext))
    try:
      assert ((type(x_mem_5640_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_5640_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_5508 = np.int32(x_mem_5640_ext.shape[0])
      if (type(x_mem_5640_ext) == cl.array.Array):
        x_mem_5640 = x_mem_5640_ext.data
      else:
        x_mem_5640 = opencl_alloc(self, np.int64(x_mem_5640_ext.nbytes),
                                  "x_mem_5640")
        if (np.int64(x_mem_5640_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_5640,
                          normaliseArray(x_mem_5640_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_5640_ext),
                                                                                                                            x_mem_5640_ext))
    scalar_out_5750 = self.futhark_kullback_liebler_f64(x_mem_5639, x_mem_5640,
                                                        sizze_5507, sizze_5508)
    return np.float64(scalar_out_5750)
  def entropy_scaled_f64(self, x_mem_5639_ext):
    try:
      assert ((type(x_mem_5639_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_5639_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_5491 = np.int32(x_mem_5639_ext.shape[0])
      if (type(x_mem_5639_ext) == cl.array.Array):
        x_mem_5639 = x_mem_5639_ext.data
      else:
        x_mem_5639 = opencl_alloc(self, np.int64(x_mem_5639_ext.nbytes),
                                  "x_mem_5639")
        if (np.int64(x_mem_5639_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_5639,
                          normaliseArray(x_mem_5639_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_5639_ext),
                                                                                                                            x_mem_5639_ext))
    scalar_out_5695 = self.futhark_entropy_scaled_f64(x_mem_5639, sizze_5491)
    return np.float64(scalar_out_5695)
  def entropy_f64(self, x_mem_5639_ext):
    try:
      assert ((type(x_mem_5639_ext) in [np.ndarray,
                                        cl.array.Array]) and (x_mem_5639_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_5481 = np.int32(x_mem_5639_ext.shape[0])
      if (type(x_mem_5639_ext) == cl.array.Array):
        x_mem_5639 = x_mem_5639_ext.data
      else:
        x_mem_5639 = opencl_alloc(self, np.int64(x_mem_5639_ext.nbytes),
                                  "x_mem_5639")
        if (np.int64(x_mem_5639_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_5639,
                          normaliseArray(x_mem_5639_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_5639_ext),
                                                                                                                            x_mem_5639_ext))
    scalar_out_5667 = self.futhark_entropy_f64(x_mem_5639, sizze_5481)
    return np.float64(scalar_out_5667)