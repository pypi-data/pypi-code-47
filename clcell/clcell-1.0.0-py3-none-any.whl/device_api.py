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
__kernel void segmap_9238(int32_t n_9047, int32_t m_9048, __global
                          unsigned char *ruleset_mem_9512, __global
                          unsigned char *mem_9526, __global
                          unsigned char *game_state_mem_9527, __global
                          unsigned char *mem_9532)
{
    const int32_t segmap_group_sizze_9244 = simulatezisegmap_group_sizze_9243;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    int32_t global_tid_9624;
    int32_t local_tid_9625;
    int32_t group_sizze_9628;
    int32_t wave_sizze_9627;
    int32_t group_tid_9626;
    
    global_tid_9624 = get_global_id(0);
    local_tid_9625 = get_local_id(0);
    group_sizze_9628 = get_local_size(0);
    wave_sizze_9627 = LOCKSTEP_WIDTH;
    group_tid_9626 = get_group_id(0);
    
    int32_t phys_tid_9238 = global_tid_9624;
    int32_t gtid_9236 = squot32(group_tid_9626 * segmap_group_sizze_9244 +
                                local_tid_9625, m_9048);
    int32_t gtid_9237;
    
    gtid_9237 = group_tid_9626 * segmap_group_sizze_9244 + local_tid_9625 -
        squot32(group_tid_9626 * segmap_group_sizze_9244 + local_tid_9625,
                m_9048) * m_9048;
    if (slt32(gtid_9236, n_9047) && slt32(gtid_9237, m_9048)) {
        bool res_9256 = ((__global bool *) mem_9526)[gtid_9236 * m_9048 +
                                                     gtid_9237];
        int32_t res_9257;
        
        if (res_9256) {
            int32_t game_state_elem_elem_9255 = ((__global
                                                  int32_t *) game_state_mem_9527)[gtid_9236 *
                                                                                  m_9048 +
                                                                                  gtid_9237];
            int32_t i_9258 = gtid_9236 - 1;
            int32_t i_9259 = gtid_9237 - 1;
            int32_t x_9260 = ((__global int32_t *) game_state_mem_9527)[i_9258 *
                                                                        m_9048 +
                                                                        i_9259];
            int32_t y_9261 = ((__global int32_t *) game_state_mem_9527)[i_9258 *
                                                                        m_9048 +
                                                                        gtid_9237];
            int32_t x_9262 = x_9260 + y_9261;
            int32_t i_9263 = 1 + gtid_9237;
            int32_t y_9264 = ((__global int32_t *) game_state_mem_9527)[i_9258 *
                                                                        m_9048 +
                                                                        i_9263];
            int32_t x_9265 = x_9262 + y_9264;
            int32_t y_9266 = ((__global
                               int32_t *) game_state_mem_9527)[gtid_9236 *
                                                               m_9048 + i_9259];
            int32_t x_9267 = x_9265 + y_9266;
            int32_t y_9268 = 9 * game_state_elem_elem_9255;
            int32_t x_9269 = x_9267 + y_9268;
            int32_t y_9270 = ((__global
                               int32_t *) game_state_mem_9527)[gtid_9236 *
                                                               m_9048 + i_9263];
            int32_t x_9271 = x_9269 + y_9270;
            int32_t i_9272 = 1 + gtid_9236;
            int32_t y_9273 = ((__global int32_t *) game_state_mem_9527)[i_9272 *
                                                                        m_9048 +
                                                                        i_9259];
            int32_t x_9274 = x_9271 + y_9273;
            int32_t y_9275 = ((__global int32_t *) game_state_mem_9527)[i_9272 *
                                                                        m_9048 +
                                                                        gtid_9237];
            int32_t x_9276 = x_9274 + y_9275;
            int32_t y_9277 = ((__global int32_t *) game_state_mem_9527)[i_9272 *
                                                                        m_9048 +
                                                                        i_9263];
            int32_t i_9278 = x_9276 + y_9277;
            int32_t res_9279 = ((__global int32_t *) ruleset_mem_9512)[i_9278];
            
            res_9257 = res_9279;
        } else {
            res_9257 = 0;
        }
        ((__global int32_t *) mem_9532)[gtid_9236 * m_9048 + gtid_9237] =
            res_9257;
    }
}
__kernel void segmap_9310(int32_t n_9047, int32_t m_9048, int32_t ni_9056,
                          int32_t mi_9057, int32_t num_groups_9318, __global
                          unsigned char *mem_9521)
{
    const int32_t segmap_group_sizze_9316 = simulatezisegmap_group_sizze_9315;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    int32_t global_tid_9564;
    int32_t local_tid_9565;
    int32_t group_sizze_9568;
    int32_t wave_sizze_9567;
    int32_t group_tid_9566;
    
    global_tid_9564 = get_global_id(0);
    local_tid_9565 = get_local_id(0);
    group_sizze_9568 = get_local_size(0);
    wave_sizze_9567 = LOCKSTEP_WIDTH;
    group_tid_9566 = get_group_id(0);
    
    int32_t phys_tid_9310 = global_tid_9564;
    int32_t phys_group_id_9569;
    
    phys_group_id_9569 = get_group_id(0);
    for (int32_t i_9570 = 0; i_9570 < squot32(squot32(n_9047 * m_9048 +
                                                      segmap_group_sizze_9316 -
                                                      1,
                                                      segmap_group_sizze_9316) -
                                              phys_group_id_9569 +
                                              num_groups_9318 - 1,
                                              num_groups_9318); i_9570++) {
        int32_t virt_group_id_9571 = phys_group_id_9569 + i_9570 *
                num_groups_9318;
        int32_t gtid_9308 = squot32(virt_group_id_9571 *
                                    segmap_group_sizze_9316 + local_tid_9565,
                                    m_9048);
        int32_t gtid_9309;
        
        gtid_9309 = virt_group_id_9571 * segmap_group_sizze_9316 +
            local_tid_9565 - squot32(virt_group_id_9571 *
                                     segmap_group_sizze_9316 + local_tid_9565,
                                     m_9048) * m_9048;
        if (slt32(gtid_9308, n_9047) && slt32(gtid_9309, m_9048)) {
            bool index_primexp_9484 = slt32(0, gtid_9308);
            bool index_primexp_9483 = slt32(gtid_9308, ni_9056);
            bool arr_elem_9323 = slt32(0, gtid_9309);
            bool arr_elem_9324 = slt32(gtid_9309, mi_9057);
            __private char *mem_9515;
            __private char mem_9515_backing_0[4];
            
            mem_9515 = mem_9515_backing_0;
            ((__private bool *) mem_9515)[0] = index_primexp_9484;
            ((__private bool *) mem_9515)[1] = index_primexp_9483;
            ((__private bool *) mem_9515)[2] = arr_elem_9323;
            ((__private bool *) mem_9515)[3] = arr_elem_9324;
            for (int32_t i_9572 = 0; i_9572 < 4; i_9572++) {
                ((__global bool *) mem_9521)[gtid_9308 * (4 * m_9048) +
                                             gtid_9309 * 4 + i_9572] =
                    ((__private bool *) mem_9515)[i_9572];
            }
        }
        barrier(CLK_GLOBAL_MEM_FENCE);
        barrier(CLK_LOCAL_MEM_FENCE);
    }
}
__kernel void segmap_9348(int32_t l_9129, int32_t n_9130, int32_t m_9131,
                          __global unsigned char *ruleset_mem_9512, __global
                          unsigned char *mem_9530, __global
                          unsigned char *game_state_expanded_mem_9531, __global
                          unsigned char *mem_9538)
{
    const int32_t segmap_group_sizze_9356 =
                  batch_simulatezisegmap_group_sizze_9355;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    int32_t global_tid_9694;
    int32_t local_tid_9695;
    int32_t group_sizze_9698;
    int32_t wave_sizze_9697;
    int32_t group_tid_9696;
    
    global_tid_9694 = get_global_id(0);
    local_tid_9695 = get_local_id(0);
    group_sizze_9698 = get_local_size(0);
    wave_sizze_9697 = LOCKSTEP_WIDTH;
    group_tid_9696 = get_group_id(0);
    
    int32_t phys_tid_9348 = global_tid_9694;
    int32_t gtid_9345 = squot32(group_tid_9696 * segmap_group_sizze_9356 +
                                local_tid_9695, n_9130 * m_9131);
    int32_t gtid_9346 = squot32(group_tid_9696 * segmap_group_sizze_9356 +
                                local_tid_9695 - squot32(group_tid_9696 *
                                                         segmap_group_sizze_9356 +
                                                         local_tid_9695,
                                                         n_9130 * m_9131) *
                                (n_9130 * m_9131), m_9131);
    int32_t gtid_9347;
    
    gtid_9347 = group_tid_9696 * segmap_group_sizze_9356 + local_tid_9695 -
        squot32(group_tid_9696 * segmap_group_sizze_9356 + local_tid_9695,
                n_9130 * m_9131) * (n_9130 * m_9131) - squot32(group_tid_9696 *
                                                               segmap_group_sizze_9356 +
                                                               local_tid_9695 -
                                                               squot32(group_tid_9696 *
                                                                       segmap_group_sizze_9356 +
                                                                       local_tid_9695,
                                                                       n_9130 *
                                                                       m_9131) *
                                                               (n_9130 *
                                                                m_9131),
                                                               m_9131) * m_9131;
    if ((slt32(gtid_9345, l_9129) && slt32(gtid_9346, n_9130)) &&
        slt32(gtid_9347, m_9131)) {
        bool res_9369 = ((__global bool *) mem_9530)[gtid_9345 * (m_9131 *
                                                                  n_9130) +
                                                     gtid_9346 * m_9131 +
                                                     gtid_9347];
        int32_t res_9370;
        
        if (res_9369) {
            int32_t game_state_elem_elem_9368 = ((__global
                                                  int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                                           (m_9131 *
                                                                                            n_9130) +
                                                                                           gtid_9346 *
                                                                                           m_9131 +
                                                                                           gtid_9347];
            int32_t i_9371 = gtid_9346 - 1;
            int32_t i_9372 = gtid_9347 - 1;
            int32_t x_9373 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        i_9371 *
                                                                        m_9131 +
                                                                        i_9372];
            int32_t y_9374 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        i_9371 *
                                                                        m_9131 +
                                                                        gtid_9347];
            int32_t x_9375 = x_9373 + y_9374;
            int32_t i_9376 = 1 + gtid_9347;
            int32_t y_9377 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        i_9371 *
                                                                        m_9131 +
                                                                        i_9376];
            int32_t x_9378 = x_9375 + y_9377;
            int32_t y_9379 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        gtid_9346 *
                                                                        m_9131 +
                                                                        i_9372];
            int32_t x_9380 = x_9378 + y_9379;
            int32_t y_9381 = 9 * game_state_elem_elem_9368;
            int32_t x_9382 = x_9380 + y_9381;
            int32_t y_9383 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        gtid_9346 *
                                                                        m_9131 +
                                                                        i_9376];
            int32_t x_9384 = x_9382 + y_9383;
            int32_t i_9385 = 1 + gtid_9346;
            int32_t y_9386 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        i_9385 *
                                                                        m_9131 +
                                                                        i_9372];
            int32_t x_9387 = x_9384 + y_9386;
            int32_t y_9388 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        i_9385 *
                                                                        m_9131 +
                                                                        gtid_9347];
            int32_t x_9389 = x_9387 + y_9388;
            int32_t y_9390 = ((__global
                               int32_t *) game_state_expanded_mem_9531)[gtid_9345 *
                                                                        (m_9131 *
                                                                         n_9130) +
                                                                        i_9385 *
                                                                        m_9131 +
                                                                        i_9376];
            int32_t i_9391 = x_9389 + y_9390;
            int32_t res_9392 = ((__global int32_t *) ruleset_mem_9512)[i_9391];
            
            res_9370 = res_9392;
        } else {
            res_9370 = 0;
        }
        ((__global int32_t *) mem_9538)[gtid_9345 * (m_9131 * n_9130) +
                                        gtid_9346 * m_9131 + gtid_9347] =
            res_9370;
    }
}
__kernel void segmap_9432(int32_t l_9129, int32_t n_9130, int32_t m_9131,
                          int32_t ni_9149, int32_t mi_9150,
                          int32_t num_groups_9442, __global
                          unsigned char *mem_9523)
{
    const int32_t segmap_group_sizze_9440 =
                  batch_simulatezisegmap_group_sizze_9439;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    int32_t global_tid_9634;
    int32_t local_tid_9635;
    int32_t group_sizze_9638;
    int32_t wave_sizze_9637;
    int32_t group_tid_9636;
    
    global_tid_9634 = get_global_id(0);
    local_tid_9635 = get_local_id(0);
    group_sizze_9638 = get_local_size(0);
    wave_sizze_9637 = LOCKSTEP_WIDTH;
    group_tid_9636 = get_group_id(0);
    
    int32_t phys_tid_9432 = global_tid_9634;
    int32_t phys_group_id_9639;
    
    phys_group_id_9639 = get_group_id(0);
    for (int32_t i_9640 = 0; i_9640 < squot32(squot32(l_9129 * n_9130 * m_9131 +
                                                      segmap_group_sizze_9440 -
                                                      1,
                                                      segmap_group_sizze_9440) -
                                              phys_group_id_9639 +
                                              num_groups_9442 - 1,
                                              num_groups_9442); i_9640++) {
        int32_t virt_group_id_9641 = phys_group_id_9639 + i_9640 *
                num_groups_9442;
        int32_t gtid_9429 = squot32(virt_group_id_9641 *
                                    segmap_group_sizze_9440 + local_tid_9635,
                                    n_9130 * m_9131);
        int32_t gtid_9430 = squot32(virt_group_id_9641 *
                                    segmap_group_sizze_9440 + local_tid_9635 -
                                    squot32(virt_group_id_9641 *
                                            segmap_group_sizze_9440 +
                                            local_tid_9635, n_9130 * m_9131) *
                                    (n_9130 * m_9131), m_9131);
        int32_t gtid_9431;
        
        gtid_9431 = virt_group_id_9641 * segmap_group_sizze_9440 +
            local_tid_9635 - squot32(virt_group_id_9641 *
                                     segmap_group_sizze_9440 + local_tid_9635,
                                     n_9130 * m_9131) * (n_9130 * m_9131) -
            squot32(virt_group_id_9641 * segmap_group_sizze_9440 +
                    local_tid_9635 - squot32(virt_group_id_9641 *
                                             segmap_group_sizze_9440 +
                                             local_tid_9635, n_9130 * m_9131) *
                    (n_9130 * m_9131), m_9131) * m_9131;
        if ((slt32(gtid_9429, l_9129) && slt32(gtid_9430, n_9130)) &&
            slt32(gtid_9431, m_9131)) {
            bool index_primexp_9508 = slt32(0, gtid_9430);
            bool index_primexp_9507 = slt32(gtid_9430, ni_9149);
            bool arr_elem_9447 = slt32(0, gtid_9431);
            bool arr_elem_9448 = slt32(gtid_9431, mi_9150);
            __private char *mem_9515;
            __private char mem_9515_backing_0[4];
            
            mem_9515 = mem_9515_backing_0;
            ((__private bool *) mem_9515)[0] = index_primexp_9508;
            ((__private bool *) mem_9515)[1] = index_primexp_9507;
            ((__private bool *) mem_9515)[2] = arr_elem_9447;
            ((__private bool *) mem_9515)[3] = arr_elem_9448;
            for (int32_t i_9642 = 0; i_9642 < 4; i_9642++) {
                ((__global bool *) mem_9523)[gtid_9429 * (4 * m_9131 * n_9130) +
                                             gtid_9430 * (4 * m_9131) +
                                             gtid_9431 * 4 + i_9642] =
                    ((__private bool *) mem_9515)[i_9642];
            }
        }
        barrier(CLK_GLOBAL_MEM_FENCE);
        barrier(CLK_LOCAL_MEM_FENCE);
    }
}
__kernel void segred_large_9299(__local volatile
                                int64_t *red_arr_mem_9603_backing_aligned_0,
                                __local volatile
                                int64_t *sync_arr_mem_9605_backing_aligned_1,
                                int32_t n_9047, int32_t m_9048,
                                int32_t num_groups_9296, __global
                                unsigned char *mem_9521, __global
                                unsigned char *mem_9526,
                                int32_t vit_num_groups_9591,
                                int32_t thread_per_segment_9593, __global
                                unsigned char *group_res_arr_mem_9594, __global
                                unsigned char *counter_mem_9596)
{
    const int32_t segred_group_sizze_9294 = simulatezisegred_group_sizze_9293;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict red_arr_mem_9603_backing_0 =
                          (__local volatile
                           char *) red_arr_mem_9603_backing_aligned_0;
    __local volatile char *restrict sync_arr_mem_9605_backing_1 =
                          (__local volatile
                           char *) sync_arr_mem_9605_backing_aligned_1;
    int32_t global_tid_9598;
    int32_t local_tid_9599;
    int32_t group_sizze_9602;
    int32_t wave_sizze_9601;
    int32_t group_tid_9600;
    
    global_tid_9598 = get_global_id(0);
    local_tid_9599 = get_local_id(0);
    group_sizze_9602 = get_local_size(0);
    wave_sizze_9601 = LOCKSTEP_WIDTH;
    group_tid_9600 = get_group_id(0);
    
    int32_t phys_tid_9299 = global_tid_9598;
    __local char *red_arr_mem_9603;
    
    red_arr_mem_9603 = (__local char *) red_arr_mem_9603_backing_0;
    
    __local char *sync_arr_mem_9605;
    
    sync_arr_mem_9605 = (__local char *) sync_arr_mem_9605_backing_1;
    
    int32_t phys_group_id_9607;
    
    phys_group_id_9607 = get_group_id(0);
    for (int32_t i_9608 = 0; i_9608 < squot32(vit_num_groups_9591 -
                                              phys_group_id_9607 +
                                              num_groups_9296 - 1,
                                              num_groups_9296); i_9608++) {
        int32_t virt_group_id_9609 = phys_group_id_9607 + i_9608 *
                num_groups_9296;
        int32_t gtid_9282 = squot32(squot32(virt_group_id_9609,
                                            squot32(num_groups_9296 + smax32(1,
                                                                             n_9047 *
                                                                             m_9048) -
                                                    1, smax32(1, n_9047 *
                                                              m_9048))),
                                    m_9048);
        int32_t gtid_9283;
        
        gtid_9283 = squot32(virt_group_id_9609, squot32(num_groups_9296 +
                                                        smax32(1, n_9047 *
                                                               m_9048) - 1,
                                                        smax32(1, n_9047 *
                                                               m_9048))) -
            squot32(squot32(virt_group_id_9609, squot32(num_groups_9296 +
                                                        smax32(1, n_9047 *
                                                               m_9048) - 1,
                                                        smax32(1, n_9047 *
                                                               m_9048))),
                    m_9048) * m_9048;
        
        int32_t gtid_9298;
        bool x_acc_9610;
        int32_t chunk_sizze_9611 = smin32(squot32(4 + segred_group_sizze_9294 *
                                                  squot32(num_groups_9296 +
                                                          smax32(1, n_9047 *
                                                                 m_9048) - 1,
                                                          smax32(1, n_9047 *
                                                                 m_9048)) - 1,
                                                  segred_group_sizze_9294 *
                                                  squot32(num_groups_9296 +
                                                          smax32(1, n_9047 *
                                                                 m_9048) - 1,
                                                          smax32(1, n_9047 *
                                                                 m_9048))),
                                          squot32(4 -
                                                  srem32(virt_group_id_9609 *
                                                         segred_group_sizze_9294 +
                                                         local_tid_9599,
                                                         segred_group_sizze_9294 *
                                                         squot32(num_groups_9296 +
                                                                 smax32(1,
                                                                        n_9047 *
                                                                        m_9048) -
                                                                 1, smax32(1,
                                                                           n_9047 *
                                                                           m_9048))) +
                                                  thread_per_segment_9593 - 1,
                                                  thread_per_segment_9593));
        bool x_9300;
        bool x_9301;
        
        // neutral-initialise the accumulators
        {
            x_acc_9610 = 1;
        }
        for (int32_t i_9615 = 0; i_9615 < chunk_sizze_9611; i_9615++) {
            gtid_9298 = srem32(virt_group_id_9609 * segred_group_sizze_9294 +
                               local_tid_9599, segred_group_sizze_9294 *
                               squot32(num_groups_9296 + smax32(1, n_9047 *
                                                                m_9048) - 1,
                                       smax32(1, n_9047 * m_9048))) +
                thread_per_segment_9593 * i_9615;
            // apply map function
            {
                bool x_9305 = ((__global bool *) mem_9521)[gtid_9282 * (4 *
                                                                        m_9048) +
                                                           gtid_9283 * 4 +
                                                           gtid_9298];
                
                // save map-out results
                { }
                // load accumulator
                {
                    x_9300 = x_acc_9610;
                }
                // load new values
                {
                    x_9301 = x_9305;
                }
                // apply reduction operator
                {
                    bool x_9302 = x_9300 && x_9301;
                    
                    // store in accumulator
                    {
                        x_acc_9610 = x_9302;
                    }
                }
            }
        }
        // to reduce current chunk, first store our result in memory
        {
            x_9300 = x_acc_9610;
            ((__local bool *) red_arr_mem_9603)[local_tid_9599] = x_9300;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        
        int32_t offset_9616;
        int32_t skip_waves_9617;
        bool x_9612;
        bool x_9613;
        
        offset_9616 = 0;
        // participating threads read initial accumulator
        {
            if (slt32(local_tid_9599, segred_group_sizze_9294)) {
                x_9612 = ((__local bool *) red_arr_mem_9603)[local_tid_9599 +
                                                             offset_9616];
            }
        }
        offset_9616 = 1;
        while (slt32(offset_9616, wave_sizze_9601)) {
            if (slt32(local_tid_9599 + offset_9616, segred_group_sizze_9294) &&
                ((local_tid_9599 - squot32(local_tid_9599, wave_sizze_9601) *
                  wave_sizze_9601) & (2 * offset_9616 - 1)) == 0) {
                // read array element
                {
                    x_9613 = ((volatile __local
                               bool *) red_arr_mem_9603)[local_tid_9599 +
                                                         offset_9616];
                }
                // apply reduction operation
                {
                    bool x_9614 = x_9612 && x_9613;
                    
                    x_9612 = x_9614;
                }
                // write result of operation
                {
                    ((volatile __local
                      bool *) red_arr_mem_9603)[local_tid_9599] = x_9612;
                }
            }
            offset_9616 *= 2;
        }
        skip_waves_9617 = 1;
        while (slt32(skip_waves_9617, squot32(segred_group_sizze_9294 +
                                              wave_sizze_9601 - 1,
                                              wave_sizze_9601))) {
            barrier(CLK_LOCAL_MEM_FENCE);
            offset_9616 = skip_waves_9617 * wave_sizze_9601;
            if (slt32(local_tid_9599 + offset_9616, segred_group_sizze_9294) &&
                ((local_tid_9599 - squot32(local_tid_9599, wave_sizze_9601) *
                  wave_sizze_9601) == 0 && (squot32(local_tid_9599,
                                                    wave_sizze_9601) & (2 *
                                                                        skip_waves_9617 -
                                                                        1)) ==
                 0)) {
                // read array element
                {
                    x_9613 = ((__local
                               bool *) red_arr_mem_9603)[local_tid_9599 +
                                                         offset_9616];
                }
                // apply reduction operation
                {
                    bool x_9614 = x_9612 && x_9613;
                    
                    x_9612 = x_9614;
                }
                // write result of operation
                {
                    ((__local bool *) red_arr_mem_9603)[local_tid_9599] =
                        x_9612;
                }
            }
            skip_waves_9617 *= 2;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // first thread saves the result in accumulator
        {
            if (local_tid_9599 == 0) {
                x_acc_9610 = x_9612;
            }
        }
        if (squot32(num_groups_9296 + smax32(1, n_9047 * m_9048) - 1, smax32(1,
                                                                             n_9047 *
                                                                             m_9048)) ==
            1) {
            // first thread in group saves final result to memory
            {
                if (local_tid_9599 == 0) {
                    ((__global bool *) mem_9526)[gtid_9282 * m_9048 +
                                                 gtid_9283] = x_acc_9610;
                }
            }
        } else {
            int32_t old_counter_9618;
            
            // first thread in group saves group result to global memory
            {
                if (local_tid_9599 == 0) {
                    ((__global
                      bool *) group_res_arr_mem_9594)[virt_group_id_9609 *
                                                      segred_group_sizze_9294] =
                        x_acc_9610;
                    mem_fence_global();
                    old_counter_9618 = atomic_add(&((volatile __global
                                                     int *) counter_mem_9596)[srem32(squot32(virt_group_id_9609,
                                                                                             squot32(num_groups_9296 +
                                                                                                     smax32(1,
                                                                                                            n_9047 *
                                                                                                            m_9048) -
                                                                                                     1,
                                                                                                     smax32(1,
                                                                                                            n_9047 *
                                                                                                            m_9048))),
                                                                                     10240)],
                                                  (int) 1);
                    ((__local bool *) sync_arr_mem_9605)[0] =
                        old_counter_9618 == squot32(num_groups_9296 + smax32(1,
                                                                             n_9047 *
                                                                             m_9048) -
                                                    1, smax32(1, n_9047 *
                                                              m_9048)) - 1;
                }
            }
            barrier(CLK_LOCAL_MEM_FENCE);
            barrier(CLK_GLOBAL_MEM_FENCE);
            
            bool is_last_group_9619 = ((__local bool *) sync_arr_mem_9605)[0];
            
            if (is_last_group_9619) {
                if (local_tid_9599 == 0) {
                    old_counter_9618 = atomic_add(&((volatile __global
                                                     int *) counter_mem_9596)[srem32(squot32(virt_group_id_9609,
                                                                                             squot32(num_groups_9296 +
                                                                                                     smax32(1,
                                                                                                            n_9047 *
                                                                                                            m_9048) -
                                                                                                     1,
                                                                                                     smax32(1,
                                                                                                            n_9047 *
                                                                                                            m_9048))),
                                                                                     10240)],
                                                  (int) (0 -
                                                         squot32(num_groups_9296 +
                                                                 smax32(1,
                                                                        n_9047 *
                                                                        m_9048) -
                                                                 1, smax32(1,
                                                                           n_9047 *
                                                                           m_9048))));
                }
                // read in the per-group-results
                {
                    if (slt32(local_tid_9599, squot32(num_groups_9296 +
                                                      smax32(1, n_9047 *
                                                             m_9048) - 1,
                                                      smax32(1, n_9047 *
                                                             m_9048)))) {
                        x_9300 = ((__global
                                   bool *) group_res_arr_mem_9594)[(squot32(virt_group_id_9609,
                                                                            squot32(num_groups_9296 +
                                                                                    smax32(1,
                                                                                           n_9047 *
                                                                                           m_9048) -
                                                                                    1,
                                                                                    smax32(1,
                                                                                           n_9047 *
                                                                                           m_9048))) *
                                                                    squot32(num_groups_9296 +
                                                                            smax32(1,
                                                                                   n_9047 *
                                                                                   m_9048) -
                                                                            1,
                                                                            smax32(1,
                                                                                   n_9047 *
                                                                                   m_9048)) +
                                                                    local_tid_9599) *
                                                                   segred_group_sizze_9294];
                    } else {
                        x_9300 = 1;
                    }
                    ((__local bool *) red_arr_mem_9603)[local_tid_9599] =
                        x_9300;
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // reduce the per-group results
                {
                    int32_t offset_9620;
                    int32_t skip_waves_9621;
                    bool x_9612;
                    bool x_9613;
                    
                    offset_9620 = 0;
                    // participating threads read initial accumulator
                    {
                        if (slt32(local_tid_9599, segred_group_sizze_9294)) {
                            x_9612 = ((__local
                                       bool *) red_arr_mem_9603)[local_tid_9599 +
                                                                 offset_9620];
                        }
                    }
                    offset_9620 = 1;
                    while (slt32(offset_9620, wave_sizze_9601)) {
                        if (slt32(local_tid_9599 + offset_9620,
                                  segred_group_sizze_9294) && ((local_tid_9599 -
                                                                squot32(local_tid_9599,
                                                                        wave_sizze_9601) *
                                                                wave_sizze_9601) &
                                                               (2 *
                                                                offset_9620 -
                                                                1)) == 0) {
                            // read array element
                            {
                                x_9613 = ((volatile __local
                                           bool *) red_arr_mem_9603)[local_tid_9599 +
                                                                     offset_9620];
                            }
                            // apply reduction operation
                            {
                                bool x_9614 = x_9612 && x_9613;
                                
                                x_9612 = x_9614;
                            }
                            // write result of operation
                            {
                                ((volatile __local
                                  bool *) red_arr_mem_9603)[local_tid_9599] =
                                    x_9612;
                            }
                        }
                        offset_9620 *= 2;
                    }
                    skip_waves_9621 = 1;
                    while (slt32(skip_waves_9621,
                                 squot32(segred_group_sizze_9294 +
                                         wave_sizze_9601 - 1,
                                         wave_sizze_9601))) {
                        barrier(CLK_LOCAL_MEM_FENCE);
                        offset_9620 = skip_waves_9621 * wave_sizze_9601;
                        if (slt32(local_tid_9599 + offset_9620,
                                  segred_group_sizze_9294) && ((local_tid_9599 -
                                                                squot32(local_tid_9599,
                                                                        wave_sizze_9601) *
                                                                wave_sizze_9601) ==
                                                               0 &&
                                                               (squot32(local_tid_9599,
                                                                        wave_sizze_9601) &
                                                                (2 *
                                                                 skip_waves_9621 -
                                                                 1)) == 0)) {
                            // read array element
                            {
                                x_9613 = ((__local
                                           bool *) red_arr_mem_9603)[local_tid_9599 +
                                                                     offset_9620];
                            }
                            // apply reduction operation
                            {
                                bool x_9614 = x_9612 && x_9613;
                                
                                x_9612 = x_9614;
                            }
                            // write result of operation
                            {
                                ((__local
                                  bool *) red_arr_mem_9603)[local_tid_9599] =
                                    x_9612;
                            }
                        }
                        skip_waves_9621 *= 2;
                    }
                    // and back to memory with the final result
                    {
                        if (local_tid_9599 == 0) {
                            ((__global bool *) mem_9526)[gtid_9282 * m_9048 +
                                                         gtid_9283] = x_9612;
                        }
                    }
                }
            }
        }
        barrier(CLK_GLOBAL_MEM_FENCE);
        barrier(CLK_LOCAL_MEM_FENCE);
    }
}
__kernel void segred_large_9417(__local volatile
                                int64_t *red_arr_mem_9673_backing_aligned_0,
                                __local volatile
                                int64_t *sync_arr_mem_9675_backing_aligned_1,
                                int32_t l_9129, int32_t n_9130, int32_t m_9131,
                                int32_t num_groups_9414, __global
                                unsigned char *mem_9523, __global
                                unsigned char *mem_9530,
                                int32_t vit_num_groups_9661,
                                int32_t thread_per_segment_9663, __global
                                unsigned char *group_res_arr_mem_9664, __global
                                unsigned char *counter_mem_9666)
{
    const int32_t segred_group_sizze_9412 =
                  batch_simulatezisegred_group_sizze_9411;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict red_arr_mem_9673_backing_0 =
                          (__local volatile
                           char *) red_arr_mem_9673_backing_aligned_0;
    __local volatile char *restrict sync_arr_mem_9675_backing_1 =
                          (__local volatile
                           char *) sync_arr_mem_9675_backing_aligned_1;
    int32_t global_tid_9668;
    int32_t local_tid_9669;
    int32_t group_sizze_9672;
    int32_t wave_sizze_9671;
    int32_t group_tid_9670;
    
    global_tid_9668 = get_global_id(0);
    local_tid_9669 = get_local_id(0);
    group_sizze_9672 = get_local_size(0);
    wave_sizze_9671 = LOCKSTEP_WIDTH;
    group_tid_9670 = get_group_id(0);
    
    int32_t phys_tid_9417 = global_tid_9668;
    __local char *red_arr_mem_9673;
    
    red_arr_mem_9673 = (__local char *) red_arr_mem_9673_backing_0;
    
    __local char *sync_arr_mem_9675;
    
    sync_arr_mem_9675 = (__local char *) sync_arr_mem_9675_backing_1;
    
    int32_t phys_group_id_9677;
    
    phys_group_id_9677 = get_group_id(0);
    for (int32_t i_9678 = 0; i_9678 < squot32(vit_num_groups_9661 -
                                              phys_group_id_9677 +
                                              num_groups_9414 - 1,
                                              num_groups_9414); i_9678++) {
        int32_t virt_group_id_9679 = phys_group_id_9677 + i_9678 *
                num_groups_9414;
        int32_t gtid_9396 = squot32(squot32(virt_group_id_9679,
                                            squot32(num_groups_9414 + smax32(1,
                                                                             l_9129 *
                                                                             n_9130 *
                                                                             m_9131) -
                                                    1, smax32(1, l_9129 *
                                                              n_9130 *
                                                              m_9131))),
                                    n_9130 * m_9131);
        int32_t gtid_9397 = squot32(squot32(virt_group_id_9679,
                                            squot32(num_groups_9414 + smax32(1,
                                                                             l_9129 *
                                                                             n_9130 *
                                                                             m_9131) -
                                                    1, smax32(1, l_9129 *
                                                              n_9130 *
                                                              m_9131))) -
                                    squot32(squot32(virt_group_id_9679,
                                                    squot32(num_groups_9414 +
                                                            smax32(1, l_9129 *
                                                                   n_9130 *
                                                                   m_9131) - 1,
                                                            smax32(1, l_9129 *
                                                                   n_9130 *
                                                                   m_9131))),
                                            n_9130 * m_9131) * (n_9130 *
                                                                m_9131),
                                    m_9131);
        int32_t gtid_9398;
        
        gtid_9398 = squot32(virt_group_id_9679, squot32(num_groups_9414 +
                                                        smax32(1, l_9129 *
                                                               n_9130 *
                                                               m_9131) - 1,
                                                        smax32(1, l_9129 *
                                                               n_9130 *
                                                               m_9131))) -
            squot32(squot32(virt_group_id_9679, squot32(num_groups_9414 +
                                                        smax32(1, l_9129 *
                                                               n_9130 *
                                                               m_9131) - 1,
                                                        smax32(1, l_9129 *
                                                               n_9130 *
                                                               m_9131))),
                    n_9130 * m_9131) * (n_9130 * m_9131) -
            squot32(squot32(virt_group_id_9679, squot32(num_groups_9414 +
                                                        smax32(1, l_9129 *
                                                               n_9130 *
                                                               m_9131) - 1,
                                                        smax32(1, l_9129 *
                                                               n_9130 *
                                                               m_9131))) -
                    squot32(squot32(virt_group_id_9679,
                                    squot32(num_groups_9414 + smax32(1, l_9129 *
                                                                     n_9130 *
                                                                     m_9131) -
                                            1, smax32(1, l_9129 * n_9130 *
                                                      m_9131))), n_9130 *
                            m_9131) * (n_9130 * m_9131), m_9131) * m_9131;
        
        int32_t gtid_9416;
        bool x_acc_9680;
        int32_t chunk_sizze_9681 = smin32(squot32(4 + segred_group_sizze_9412 *
                                                  squot32(num_groups_9414 +
                                                          smax32(1, l_9129 *
                                                                 n_9130 *
                                                                 m_9131) - 1,
                                                          smax32(1, l_9129 *
                                                                 n_9130 *
                                                                 m_9131)) - 1,
                                                  segred_group_sizze_9412 *
                                                  squot32(num_groups_9414 +
                                                          smax32(1, l_9129 *
                                                                 n_9130 *
                                                                 m_9131) - 1,
                                                          smax32(1, l_9129 *
                                                                 n_9130 *
                                                                 m_9131))),
                                          squot32(4 -
                                                  srem32(virt_group_id_9679 *
                                                         segred_group_sizze_9412 +
                                                         local_tid_9669,
                                                         segred_group_sizze_9412 *
                                                         squot32(num_groups_9414 +
                                                                 smax32(1,
                                                                        l_9129 *
                                                                        n_9130 *
                                                                        m_9131) -
                                                                 1, smax32(1,
                                                                           l_9129 *
                                                                           n_9130 *
                                                                           m_9131))) +
                                                  thread_per_segment_9663 - 1,
                                                  thread_per_segment_9663));
        bool x_9418;
        bool x_9419;
        
        // neutral-initialise the accumulators
        {
            x_acc_9680 = 1;
        }
        for (int32_t i_9685 = 0; i_9685 < chunk_sizze_9681; i_9685++) {
            gtid_9416 = srem32(virt_group_id_9679 * segred_group_sizze_9412 +
                               local_tid_9669, segred_group_sizze_9412 *
                               squot32(num_groups_9414 + smax32(1, l_9129 *
                                                                n_9130 *
                                                                m_9131) - 1,
                                       smax32(1, l_9129 * n_9130 * m_9131))) +
                thread_per_segment_9663 * i_9685;
            // apply map function
            {
                bool x_9424 = ((__global bool *) mem_9523)[gtid_9396 * (4 *
                                                                        m_9131 *
                                                                        n_9130) +
                                                           gtid_9397 * (4 *
                                                                        m_9131) +
                                                           gtid_9398 * 4 +
                                                           gtid_9416];
                
                // save map-out results
                { }
                // load accumulator
                {
                    x_9418 = x_acc_9680;
                }
                // load new values
                {
                    x_9419 = x_9424;
                }
                // apply reduction operator
                {
                    bool x_9420 = x_9418 && x_9419;
                    
                    // store in accumulator
                    {
                        x_acc_9680 = x_9420;
                    }
                }
            }
        }
        // to reduce current chunk, first store our result in memory
        {
            x_9418 = x_acc_9680;
            ((__local bool *) red_arr_mem_9673)[local_tid_9669] = x_9418;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        
        int32_t offset_9686;
        int32_t skip_waves_9687;
        bool x_9682;
        bool x_9683;
        
        offset_9686 = 0;
        // participating threads read initial accumulator
        {
            if (slt32(local_tid_9669, segred_group_sizze_9412)) {
                x_9682 = ((__local bool *) red_arr_mem_9673)[local_tid_9669 +
                                                             offset_9686];
            }
        }
        offset_9686 = 1;
        while (slt32(offset_9686, wave_sizze_9671)) {
            if (slt32(local_tid_9669 + offset_9686, segred_group_sizze_9412) &&
                ((local_tid_9669 - squot32(local_tid_9669, wave_sizze_9671) *
                  wave_sizze_9671) & (2 * offset_9686 - 1)) == 0) {
                // read array element
                {
                    x_9683 = ((volatile __local
                               bool *) red_arr_mem_9673)[local_tid_9669 +
                                                         offset_9686];
                }
                // apply reduction operation
                {
                    bool x_9684 = x_9682 && x_9683;
                    
                    x_9682 = x_9684;
                }
                // write result of operation
                {
                    ((volatile __local
                      bool *) red_arr_mem_9673)[local_tid_9669] = x_9682;
                }
            }
            offset_9686 *= 2;
        }
        skip_waves_9687 = 1;
        while (slt32(skip_waves_9687, squot32(segred_group_sizze_9412 +
                                              wave_sizze_9671 - 1,
                                              wave_sizze_9671))) {
            barrier(CLK_LOCAL_MEM_FENCE);
            offset_9686 = skip_waves_9687 * wave_sizze_9671;
            if (slt32(local_tid_9669 + offset_9686, segred_group_sizze_9412) &&
                ((local_tid_9669 - squot32(local_tid_9669, wave_sizze_9671) *
                  wave_sizze_9671) == 0 && (squot32(local_tid_9669,
                                                    wave_sizze_9671) & (2 *
                                                                        skip_waves_9687 -
                                                                        1)) ==
                 0)) {
                // read array element
                {
                    x_9683 = ((__local
                               bool *) red_arr_mem_9673)[local_tid_9669 +
                                                         offset_9686];
                }
                // apply reduction operation
                {
                    bool x_9684 = x_9682 && x_9683;
                    
                    x_9682 = x_9684;
                }
                // write result of operation
                {
                    ((__local bool *) red_arr_mem_9673)[local_tid_9669] =
                        x_9682;
                }
            }
            skip_waves_9687 *= 2;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // first thread saves the result in accumulator
        {
            if (local_tid_9669 == 0) {
                x_acc_9680 = x_9682;
            }
        }
        if (squot32(num_groups_9414 + smax32(1, l_9129 * n_9130 * m_9131) - 1,
                    smax32(1, l_9129 * n_9130 * m_9131)) == 1) {
            // first thread in group saves final result to memory
            {
                if (local_tid_9669 == 0) {
                    ((__global bool *) mem_9530)[gtid_9396 * (m_9131 * n_9130) +
                                                 gtid_9397 * m_9131 +
                                                 gtid_9398] = x_acc_9680;
                }
            }
        } else {
            int32_t old_counter_9688;
            
            // first thread in group saves group result to global memory
            {
                if (local_tid_9669 == 0) {
                    ((__global
                      bool *) group_res_arr_mem_9664)[virt_group_id_9679 *
                                                      segred_group_sizze_9412] =
                        x_acc_9680;
                    mem_fence_global();
                    old_counter_9688 = atomic_add(&((volatile __global
                                                     int *) counter_mem_9666)[srem32(squot32(virt_group_id_9679,
                                                                                             squot32(num_groups_9414 +
                                                                                                     smax32(1,
                                                                                                            l_9129 *
                                                                                                            n_9130 *
                                                                                                            m_9131) -
                                                                                                     1,
                                                                                                     smax32(1,
                                                                                                            l_9129 *
                                                                                                            n_9130 *
                                                                                                            m_9131))),
                                                                                     10240)],
                                                  (int) 1);
                    ((__local bool *) sync_arr_mem_9675)[0] =
                        old_counter_9688 == squot32(num_groups_9414 + smax32(1,
                                                                             l_9129 *
                                                                             n_9130 *
                                                                             m_9131) -
                                                    1, smax32(1, l_9129 *
                                                              n_9130 *
                                                              m_9131)) - 1;
                }
            }
            barrier(CLK_LOCAL_MEM_FENCE);
            barrier(CLK_GLOBAL_MEM_FENCE);
            
            bool is_last_group_9689 = ((__local bool *) sync_arr_mem_9675)[0];
            
            if (is_last_group_9689) {
                if (local_tid_9669 == 0) {
                    old_counter_9688 = atomic_add(&((volatile __global
                                                     int *) counter_mem_9666)[srem32(squot32(virt_group_id_9679,
                                                                                             squot32(num_groups_9414 +
                                                                                                     smax32(1,
                                                                                                            l_9129 *
                                                                                                            n_9130 *
                                                                                                            m_9131) -
                                                                                                     1,
                                                                                                     smax32(1,
                                                                                                            l_9129 *
                                                                                                            n_9130 *
                                                                                                            m_9131))),
                                                                                     10240)],
                                                  (int) (0 -
                                                         squot32(num_groups_9414 +
                                                                 smax32(1,
                                                                        l_9129 *
                                                                        n_9130 *
                                                                        m_9131) -
                                                                 1, smax32(1,
                                                                           l_9129 *
                                                                           n_9130 *
                                                                           m_9131))));
                }
                // read in the per-group-results
                {
                    if (slt32(local_tid_9669, squot32(num_groups_9414 +
                                                      smax32(1, l_9129 *
                                                             n_9130 * m_9131) -
                                                      1, smax32(1, l_9129 *
                                                                n_9130 *
                                                                m_9131)))) {
                        x_9418 = ((__global
                                   bool *) group_res_arr_mem_9664)[(squot32(virt_group_id_9679,
                                                                            squot32(num_groups_9414 +
                                                                                    smax32(1,
                                                                                           l_9129 *
                                                                                           n_9130 *
                                                                                           m_9131) -
                                                                                    1,
                                                                                    smax32(1,
                                                                                           l_9129 *
                                                                                           n_9130 *
                                                                                           m_9131))) *
                                                                    squot32(num_groups_9414 +
                                                                            smax32(1,
                                                                                   l_9129 *
                                                                                   n_9130 *
                                                                                   m_9131) -
                                                                            1,
                                                                            smax32(1,
                                                                                   l_9129 *
                                                                                   n_9130 *
                                                                                   m_9131)) +
                                                                    local_tid_9669) *
                                                                   segred_group_sizze_9412];
                    } else {
                        x_9418 = 1;
                    }
                    ((__local bool *) red_arr_mem_9673)[local_tid_9669] =
                        x_9418;
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // reduce the per-group results
                {
                    int32_t offset_9690;
                    int32_t skip_waves_9691;
                    bool x_9682;
                    bool x_9683;
                    
                    offset_9690 = 0;
                    // participating threads read initial accumulator
                    {
                        if (slt32(local_tid_9669, segred_group_sizze_9412)) {
                            x_9682 = ((__local
                                       bool *) red_arr_mem_9673)[local_tid_9669 +
                                                                 offset_9690];
                        }
                    }
                    offset_9690 = 1;
                    while (slt32(offset_9690, wave_sizze_9671)) {
                        if (slt32(local_tid_9669 + offset_9690,
                                  segred_group_sizze_9412) && ((local_tid_9669 -
                                                                squot32(local_tid_9669,
                                                                        wave_sizze_9671) *
                                                                wave_sizze_9671) &
                                                               (2 *
                                                                offset_9690 -
                                                                1)) == 0) {
                            // read array element
                            {
                                x_9683 = ((volatile __local
                                           bool *) red_arr_mem_9673)[local_tid_9669 +
                                                                     offset_9690];
                            }
                            // apply reduction operation
                            {
                                bool x_9684 = x_9682 && x_9683;
                                
                                x_9682 = x_9684;
                            }
                            // write result of operation
                            {
                                ((volatile __local
                                  bool *) red_arr_mem_9673)[local_tid_9669] =
                                    x_9682;
                            }
                        }
                        offset_9690 *= 2;
                    }
                    skip_waves_9691 = 1;
                    while (slt32(skip_waves_9691,
                                 squot32(segred_group_sizze_9412 +
                                         wave_sizze_9671 - 1,
                                         wave_sizze_9671))) {
                        barrier(CLK_LOCAL_MEM_FENCE);
                        offset_9690 = skip_waves_9691 * wave_sizze_9671;
                        if (slt32(local_tid_9669 + offset_9690,
                                  segred_group_sizze_9412) && ((local_tid_9669 -
                                                                squot32(local_tid_9669,
                                                                        wave_sizze_9671) *
                                                                wave_sizze_9671) ==
                                                               0 &&
                                                               (squot32(local_tid_9669,
                                                                        wave_sizze_9671) &
                                                                (2 *
                                                                 skip_waves_9691 -
                                                                 1)) == 0)) {
                            // read array element
                            {
                                x_9683 = ((__local
                                           bool *) red_arr_mem_9673)[local_tid_9669 +
                                                                     offset_9690];
                            }
                            // apply reduction operation
                            {
                                bool x_9684 = x_9682 && x_9683;
                                
                                x_9682 = x_9684;
                            }
                            // write result of operation
                            {
                                ((__local
                                  bool *) red_arr_mem_9673)[local_tid_9669] =
                                    x_9682;
                            }
                        }
                        skip_waves_9691 *= 2;
                    }
                    // and back to memory with the final result
                    {
                        if (local_tid_9669 == 0) {
                            ((__global bool *) mem_9530)[gtid_9396 * (m_9131 *
                                                                      n_9130) +
                                                         gtid_9397 * m_9131 +
                                                         gtid_9398] = x_9682;
                        }
                    }
                }
            }
        }
        barrier(CLK_GLOBAL_MEM_FENCE);
        barrier(CLK_LOCAL_MEM_FENCE);
    }
}
__kernel void segred_small_9299(__local volatile
                                int64_t *red_arr_mem_9581_backing_aligned_0,
                                int32_t n_9047, int32_t m_9048,
                                int32_t num_groups_9296, __global
                                unsigned char *mem_9521, __global
                                unsigned char *mem_9526,
                                int32_t segment_sizze_nonzzero_9574)
{
    const int32_t segred_group_sizze_9294 = simulatezisegred_group_sizze_9293;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict red_arr_mem_9581_backing_0 =
                          (__local volatile
                           char *) red_arr_mem_9581_backing_aligned_0;
    int32_t global_tid_9576;
    int32_t local_tid_9577;
    int32_t group_sizze_9580;
    int32_t wave_sizze_9579;
    int32_t group_tid_9578;
    
    global_tid_9576 = get_global_id(0);
    local_tid_9577 = get_local_id(0);
    group_sizze_9580 = get_local_size(0);
    wave_sizze_9579 = LOCKSTEP_WIDTH;
    group_tid_9578 = get_group_id(0);
    
    int32_t phys_tid_9299 = global_tid_9576;
    __local char *red_arr_mem_9581;
    
    red_arr_mem_9581 = (__local char *) red_arr_mem_9581_backing_0;
    
    int32_t phys_group_id_9583;
    
    phys_group_id_9583 = get_group_id(0);
    for (int32_t i_9584 = 0; i_9584 < squot32(squot32(n_9047 * m_9048 +
                                                      squot32(segred_group_sizze_9294,
                                                              segment_sizze_nonzzero_9574) -
                                                      1,
                                                      squot32(segred_group_sizze_9294,
                                                              segment_sizze_nonzzero_9574)) -
                                              phys_group_id_9583 +
                                              num_groups_9296 - 1,
                                              num_groups_9296); i_9584++) {
        int32_t virt_group_id_9585 = phys_group_id_9583 + i_9584 *
                num_groups_9296;
        int32_t gtid_9282 = squot32(squot32(local_tid_9577,
                                            segment_sizze_nonzzero_9574) +
                                    virt_group_id_9585 *
                                    squot32(segred_group_sizze_9294,
                                            segment_sizze_nonzzero_9574),
                                    m_9048);
        int32_t gtid_9283;
        
        gtid_9283 = squot32(local_tid_9577, segment_sizze_nonzzero_9574) +
            virt_group_id_9585 * squot32(segred_group_sizze_9294,
                                         segment_sizze_nonzzero_9574) -
            squot32(squot32(local_tid_9577, segment_sizze_nonzzero_9574) +
                    virt_group_id_9585 * squot32(segred_group_sizze_9294,
                                                 segment_sizze_nonzzero_9574),
                    m_9048) * m_9048;
        
        int32_t gtid_9298 = srem32(local_tid_9577, 4);
        
        // apply map function if in bounds
        {
            if (slt32(0, 4) && ((slt32(gtid_9282, n_9047) && slt32(gtid_9283,
                                                                   m_9048)) &&
                                slt32(local_tid_9577, 4 *
                                      squot32(segred_group_sizze_9294,
                                              segment_sizze_nonzzero_9574)))) {
                bool x_9305 = ((__global bool *) mem_9521)[gtid_9282 * (4 *
                                                                        m_9048) +
                                                           gtid_9283 * 4 +
                                                           gtid_9298];
                
                // save map-out results
                { }
                // save results to be reduced
                {
                    ((__local bool *) red_arr_mem_9581)[local_tid_9577] =
                        x_9305;
                }
            } else {
                ((__local bool *) red_arr_mem_9581)[local_tid_9577] = 1;
            }
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        if (slt32(0, 4)) {
            // perform segmented scan to imitate reduction
            {
                bool x_9300;
                bool x_9301;
                bool x_9586;
                bool x_9587;
                int32_t skip_threads_9589;
                
                if (slt32(local_tid_9577, 4 * squot32(segred_group_sizze_9294,
                                                      segment_sizze_nonzzero_9574))) {
                    x_9301 = ((volatile __local
                               bool *) red_arr_mem_9581)[local_tid_9577];
                }
                // in-block scan (hopefully no barriers needed)
                {
                    skip_threads_9589 = 1;
                    while (slt32(skip_threads_9589, 32)) {
                        if (sle32(skip_threads_9589, local_tid_9577 -
                                  squot32(local_tid_9577, 32) * 32) &&
                            slt32(local_tid_9577, 4 *
                                  squot32(segred_group_sizze_9294,
                                          segment_sizze_nonzzero_9574))) {
                            // read operands
                            {
                                x_9300 = ((volatile __local
                                           bool *) red_arr_mem_9581)[local_tid_9577 -
                                                                     skip_threads_9589];
                            }
                            // perform operation
                            {
                                if (!slt32(srem32(local_tid_9577, 4),
                                           local_tid_9577 - (local_tid_9577 -
                                                             skip_threads_9589))) {
                                    bool x_9302 = x_9300 && x_9301;
                                    
                                    x_9301 = x_9302;
                                }
                            }
                        }
                        if (sle32(wave_sizze_9579, skip_threads_9589)) {
                            barrier(CLK_LOCAL_MEM_FENCE);
                        }
                        if (sle32(skip_threads_9589, local_tid_9577 -
                                  squot32(local_tid_9577, 32) * 32) &&
                            slt32(local_tid_9577, 4 *
                                  squot32(segred_group_sizze_9294,
                                          segment_sizze_nonzzero_9574))) {
                            // write result
                            {
                                ((volatile __local
                                  bool *) red_arr_mem_9581)[local_tid_9577] =
                                    x_9301;
                            }
                        }
                        if (sle32(wave_sizze_9579, skip_threads_9589)) {
                            barrier(CLK_LOCAL_MEM_FENCE);
                        }
                        skip_threads_9589 *= 2;
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // last thread of block 'i' writes its result to offset 'i'
                {
                    if ((local_tid_9577 - squot32(local_tid_9577, 32) * 32) ==
                        31 && slt32(local_tid_9577, 4 *
                                    squot32(segred_group_sizze_9294,
                                            segment_sizze_nonzzero_9574))) {
                        ((volatile __local
                          bool *) red_arr_mem_9581)[squot32(local_tid_9577,
                                                            32)] = x_9301;
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // scan the first block, after which offset 'i' contains carry-in for warp 'i+1'
                {
                    int32_t skip_threads_9590;
                    
                    if (squot32(local_tid_9577, 32) == 0 &&
                        slt32(local_tid_9577, 4 *
                              squot32(segred_group_sizze_9294,
                                      segment_sizze_nonzzero_9574))) {
                        x_9587 = ((volatile __local
                                   bool *) red_arr_mem_9581)[local_tid_9577];
                    }
                    // in-block scan (hopefully no barriers needed)
                    {
                        skip_threads_9590 = 1;
                        while (slt32(skip_threads_9590, 32)) {
                            if (sle32(skip_threads_9590, local_tid_9577 -
                                      squot32(local_tid_9577, 32) * 32) &&
                                (squot32(local_tid_9577, 32) == 0 &&
                                 slt32(local_tid_9577, 4 *
                                       squot32(segred_group_sizze_9294,
                                               segment_sizze_nonzzero_9574)))) {
                                // read operands
                                {
                                    x_9586 = ((volatile __local
                                               bool *) red_arr_mem_9581)[local_tid_9577 -
                                                                         skip_threads_9590];
                                }
                                // perform operation
                                {
                                    if (!slt32(srem32(local_tid_9577 * 32 + 32 -
                                                      1, 4), local_tid_9577 *
                                               32 + 32 - 1 - ((local_tid_9577 -
                                                               skip_threads_9590) *
                                                              32 + 32 - 1))) {
                                        bool x_9588 = x_9586 && x_9587;
                                        
                                        x_9587 = x_9588;
                                    }
                                }
                            }
                            if (sle32(wave_sizze_9579, skip_threads_9590)) {
                                barrier(CLK_LOCAL_MEM_FENCE);
                            }
                            if (sle32(skip_threads_9590, local_tid_9577 -
                                      squot32(local_tid_9577, 32) * 32) &&
                                (squot32(local_tid_9577, 32) == 0 &&
                                 slt32(local_tid_9577, 4 *
                                       squot32(segred_group_sizze_9294,
                                               segment_sizze_nonzzero_9574)))) {
                                // write result
                                {
                                    ((volatile __local
                                      bool *) red_arr_mem_9581)[local_tid_9577] =
                                        x_9587;
                                }
                            }
                            if (sle32(wave_sizze_9579, skip_threads_9590)) {
                                barrier(CLK_LOCAL_MEM_FENCE);
                            }
                            skip_threads_9590 *= 2;
                        }
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // carry-in for every block except the first
                {
                    if (!(squot32(local_tid_9577, 32) == 0 ||
                          !slt32(local_tid_9577, 4 *
                                 squot32(segred_group_sizze_9294,
                                         segment_sizze_nonzzero_9574)))) {
                        // read operands
                        {
                            x_9300 = ((volatile __local
                                       bool *) red_arr_mem_9581)[squot32(local_tid_9577,
                                                                         32) -
                                                                 1];
                        }
                        // perform operation
                        {
                            if (!slt32(srem32(local_tid_9577, 4),
                                       local_tid_9577 - (squot32(local_tid_9577,
                                                                 32) * 32 -
                                                         1))) {
                                bool x_9302 = x_9300 && x_9301;
                                
                                x_9301 = x_9302;
                            }
                        }
                        // write final result
                        {
                            ((volatile __local
                              bool *) red_arr_mem_9581)[local_tid_9577] =
                                x_9301;
                        }
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // restore correct values for first block
                {
                    if (squot32(local_tid_9577, 32) == 0) {
                        ((volatile __local
                          bool *) red_arr_mem_9581)[local_tid_9577] = x_9301;
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
            }
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // save final values of segments
        {
            if (slt32(virt_group_id_9585 * squot32(segred_group_sizze_9294,
                                                   segment_sizze_nonzzero_9574) +
                      local_tid_9577, n_9047 * m_9048) && slt32(local_tid_9577,
                                                                squot32(segred_group_sizze_9294,
                                                                        segment_sizze_nonzzero_9574))) {
                ((__global bool *) mem_9526)[squot32(virt_group_id_9585 *
                                                     squot32(segred_group_sizze_9294,
                                                             segment_sizze_nonzzero_9574) +
                                                     local_tid_9577, m_9048) *
                                             m_9048 + (virt_group_id_9585 *
                                                       squot32(segred_group_sizze_9294,
                                                               segment_sizze_nonzzero_9574) +
                                                       local_tid_9577 -
                                                       squot32(virt_group_id_9585 *
                                                               squot32(segred_group_sizze_9294,
                                                                       segment_sizze_nonzzero_9574) +
                                                               local_tid_9577,
                                                               m_9048) *
                                                       m_9048)] = ((__local
                                                                    bool *) red_arr_mem_9581)[(local_tid_9577 +
                                                                                               1) *
                                                                                              segment_sizze_nonzzero_9574 -
                                                                                              1];
            }
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        barrier(CLK_GLOBAL_MEM_FENCE);
        barrier(CLK_LOCAL_MEM_FENCE);
    }
}
__kernel void segred_small_9417(__local volatile
                                int64_t *red_arr_mem_9651_backing_aligned_0,
                                int32_t l_9129, int32_t n_9130, int32_t m_9131,
                                int32_t num_groups_9414, __global
                                unsigned char *mem_9523, __global
                                unsigned char *mem_9530,
                                int32_t segment_sizze_nonzzero_9644)
{
    const int32_t segred_group_sizze_9412 =
                  batch_simulatezisegred_group_sizze_9411;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict red_arr_mem_9651_backing_0 =
                          (__local volatile
                           char *) red_arr_mem_9651_backing_aligned_0;
    int32_t global_tid_9646;
    int32_t local_tid_9647;
    int32_t group_sizze_9650;
    int32_t wave_sizze_9649;
    int32_t group_tid_9648;
    
    global_tid_9646 = get_global_id(0);
    local_tid_9647 = get_local_id(0);
    group_sizze_9650 = get_local_size(0);
    wave_sizze_9649 = LOCKSTEP_WIDTH;
    group_tid_9648 = get_group_id(0);
    
    int32_t phys_tid_9417 = global_tid_9646;
    __local char *red_arr_mem_9651;
    
    red_arr_mem_9651 = (__local char *) red_arr_mem_9651_backing_0;
    
    int32_t phys_group_id_9653;
    
    phys_group_id_9653 = get_group_id(0);
    for (int32_t i_9654 = 0; i_9654 < squot32(squot32(l_9129 * n_9130 * m_9131 +
                                                      squot32(segred_group_sizze_9412,
                                                              segment_sizze_nonzzero_9644) -
                                                      1,
                                                      squot32(segred_group_sizze_9412,
                                                              segment_sizze_nonzzero_9644)) -
                                              phys_group_id_9653 +
                                              num_groups_9414 - 1,
                                              num_groups_9414); i_9654++) {
        int32_t virt_group_id_9655 = phys_group_id_9653 + i_9654 *
                num_groups_9414;
        int32_t gtid_9396 = squot32(squot32(local_tid_9647,
                                            segment_sizze_nonzzero_9644) +
                                    virt_group_id_9655 *
                                    squot32(segred_group_sizze_9412,
                                            segment_sizze_nonzzero_9644),
                                    n_9130 * m_9131);
        int32_t gtid_9397 = squot32(squot32(local_tid_9647,
                                            segment_sizze_nonzzero_9644) +
                                    virt_group_id_9655 *
                                    squot32(segred_group_sizze_9412,
                                            segment_sizze_nonzzero_9644) -
                                    squot32(squot32(local_tid_9647,
                                                    segment_sizze_nonzzero_9644) +
                                            virt_group_id_9655 *
                                            squot32(segred_group_sizze_9412,
                                                    segment_sizze_nonzzero_9644),
                                            n_9130 * m_9131) * (n_9130 *
                                                                m_9131),
                                    m_9131);
        int32_t gtid_9398;
        
        gtid_9398 = squot32(local_tid_9647, segment_sizze_nonzzero_9644) +
            virt_group_id_9655 * squot32(segred_group_sizze_9412,
                                         segment_sizze_nonzzero_9644) -
            squot32(squot32(local_tid_9647, segment_sizze_nonzzero_9644) +
                    virt_group_id_9655 * squot32(segred_group_sizze_9412,
                                                 segment_sizze_nonzzero_9644),
                    n_9130 * m_9131) * (n_9130 * m_9131) -
            squot32(squot32(local_tid_9647, segment_sizze_nonzzero_9644) +
                    virt_group_id_9655 * squot32(segred_group_sizze_9412,
                                                 segment_sizze_nonzzero_9644) -
                    squot32(squot32(local_tid_9647,
                                    segment_sizze_nonzzero_9644) +
                            virt_group_id_9655 *
                            squot32(segred_group_sizze_9412,
                                    segment_sizze_nonzzero_9644), n_9130 *
                            m_9131) * (n_9130 * m_9131), m_9131) * m_9131;
        
        int32_t gtid_9416 = srem32(local_tid_9647, 4);
        
        // apply map function if in bounds
        {
            if (slt32(0, 4) && (((slt32(gtid_9396, l_9129) && slt32(gtid_9397,
                                                                    n_9130)) &&
                                 slt32(gtid_9398, m_9131)) &&
                                slt32(local_tid_9647, 4 *
                                      squot32(segred_group_sizze_9412,
                                              segment_sizze_nonzzero_9644)))) {
                bool x_9424 = ((__global bool *) mem_9523)[gtid_9396 * (4 *
                                                                        m_9131 *
                                                                        n_9130) +
                                                           gtid_9397 * (4 *
                                                                        m_9131) +
                                                           gtid_9398 * 4 +
                                                           gtid_9416];
                
                // save map-out results
                { }
                // save results to be reduced
                {
                    ((__local bool *) red_arr_mem_9651)[local_tid_9647] =
                        x_9424;
                }
            } else {
                ((__local bool *) red_arr_mem_9651)[local_tid_9647] = 1;
            }
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        if (slt32(0, 4)) {
            // perform segmented scan to imitate reduction
            {
                bool x_9418;
                bool x_9419;
                bool x_9656;
                bool x_9657;
                int32_t skip_threads_9659;
                
                if (slt32(local_tid_9647, 4 * squot32(segred_group_sizze_9412,
                                                      segment_sizze_nonzzero_9644))) {
                    x_9419 = ((volatile __local
                               bool *) red_arr_mem_9651)[local_tid_9647];
                }
                // in-block scan (hopefully no barriers needed)
                {
                    skip_threads_9659 = 1;
                    while (slt32(skip_threads_9659, 32)) {
                        if (sle32(skip_threads_9659, local_tid_9647 -
                                  squot32(local_tid_9647, 32) * 32) &&
                            slt32(local_tid_9647, 4 *
                                  squot32(segred_group_sizze_9412,
                                          segment_sizze_nonzzero_9644))) {
                            // read operands
                            {
                                x_9418 = ((volatile __local
                                           bool *) red_arr_mem_9651)[local_tid_9647 -
                                                                     skip_threads_9659];
                            }
                            // perform operation
                            {
                                if (!slt32(srem32(local_tid_9647, 4),
                                           local_tid_9647 - (local_tid_9647 -
                                                             skip_threads_9659))) {
                                    bool x_9420 = x_9418 && x_9419;
                                    
                                    x_9419 = x_9420;
                                }
                            }
                        }
                        if (sle32(wave_sizze_9649, skip_threads_9659)) {
                            barrier(CLK_LOCAL_MEM_FENCE);
                        }
                        if (sle32(skip_threads_9659, local_tid_9647 -
                                  squot32(local_tid_9647, 32) * 32) &&
                            slt32(local_tid_9647, 4 *
                                  squot32(segred_group_sizze_9412,
                                          segment_sizze_nonzzero_9644))) {
                            // write result
                            {
                                ((volatile __local
                                  bool *) red_arr_mem_9651)[local_tid_9647] =
                                    x_9419;
                            }
                        }
                        if (sle32(wave_sizze_9649, skip_threads_9659)) {
                            barrier(CLK_LOCAL_MEM_FENCE);
                        }
                        skip_threads_9659 *= 2;
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // last thread of block 'i' writes its result to offset 'i'
                {
                    if ((local_tid_9647 - squot32(local_tid_9647, 32) * 32) ==
                        31 && slt32(local_tid_9647, 4 *
                                    squot32(segred_group_sizze_9412,
                                            segment_sizze_nonzzero_9644))) {
                        ((volatile __local
                          bool *) red_arr_mem_9651)[squot32(local_tid_9647,
                                                            32)] = x_9419;
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // scan the first block, after which offset 'i' contains carry-in for warp 'i+1'
                {
                    int32_t skip_threads_9660;
                    
                    if (squot32(local_tid_9647, 32) == 0 &&
                        slt32(local_tid_9647, 4 *
                              squot32(segred_group_sizze_9412,
                                      segment_sizze_nonzzero_9644))) {
                        x_9657 = ((volatile __local
                                   bool *) red_arr_mem_9651)[local_tid_9647];
                    }
                    // in-block scan (hopefully no barriers needed)
                    {
                        skip_threads_9660 = 1;
                        while (slt32(skip_threads_9660, 32)) {
                            if (sle32(skip_threads_9660, local_tid_9647 -
                                      squot32(local_tid_9647, 32) * 32) &&
                                (squot32(local_tid_9647, 32) == 0 &&
                                 slt32(local_tid_9647, 4 *
                                       squot32(segred_group_sizze_9412,
                                               segment_sizze_nonzzero_9644)))) {
                                // read operands
                                {
                                    x_9656 = ((volatile __local
                                               bool *) red_arr_mem_9651)[local_tid_9647 -
                                                                         skip_threads_9660];
                                }
                                // perform operation
                                {
                                    if (!slt32(srem32(local_tid_9647 * 32 + 32 -
                                                      1, 4), local_tid_9647 *
                                               32 + 32 - 1 - ((local_tid_9647 -
                                                               skip_threads_9660) *
                                                              32 + 32 - 1))) {
                                        bool x_9658 = x_9656 && x_9657;
                                        
                                        x_9657 = x_9658;
                                    }
                                }
                            }
                            if (sle32(wave_sizze_9649, skip_threads_9660)) {
                                barrier(CLK_LOCAL_MEM_FENCE);
                            }
                            if (sle32(skip_threads_9660, local_tid_9647 -
                                      squot32(local_tid_9647, 32) * 32) &&
                                (squot32(local_tid_9647, 32) == 0 &&
                                 slt32(local_tid_9647, 4 *
                                       squot32(segred_group_sizze_9412,
                                               segment_sizze_nonzzero_9644)))) {
                                // write result
                                {
                                    ((volatile __local
                                      bool *) red_arr_mem_9651)[local_tid_9647] =
                                        x_9657;
                                }
                            }
                            if (sle32(wave_sizze_9649, skip_threads_9660)) {
                                barrier(CLK_LOCAL_MEM_FENCE);
                            }
                            skip_threads_9660 *= 2;
                        }
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // carry-in for every block except the first
                {
                    if (!(squot32(local_tid_9647, 32) == 0 ||
                          !slt32(local_tid_9647, 4 *
                                 squot32(segred_group_sizze_9412,
                                         segment_sizze_nonzzero_9644)))) {
                        // read operands
                        {
                            x_9418 = ((volatile __local
                                       bool *) red_arr_mem_9651)[squot32(local_tid_9647,
                                                                         32) -
                                                                 1];
                        }
                        // perform operation
                        {
                            if (!slt32(srem32(local_tid_9647, 4),
                                       local_tid_9647 - (squot32(local_tid_9647,
                                                                 32) * 32 -
                                                         1))) {
                                bool x_9420 = x_9418 && x_9419;
                                
                                x_9419 = x_9420;
                            }
                        }
                        // write final result
                        {
                            ((volatile __local
                              bool *) red_arr_mem_9651)[local_tid_9647] =
                                x_9419;
                        }
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
                // restore correct values for first block
                {
                    if (squot32(local_tid_9647, 32) == 0) {
                        ((volatile __local
                          bool *) red_arr_mem_9651)[local_tid_9647] = x_9419;
                    }
                }
                barrier(CLK_LOCAL_MEM_FENCE);
            }
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // save final values of segments
        {
            if (slt32(virt_group_id_9655 * squot32(segred_group_sizze_9412,
                                                   segment_sizze_nonzzero_9644) +
                      local_tid_9647, l_9129 * n_9130 * m_9131) &&
                slt32(local_tid_9647, squot32(segred_group_sizze_9412,
                                              segment_sizze_nonzzero_9644))) {
                ((__global bool *) mem_9530)[squot32(virt_group_id_9655 *
                                                     squot32(segred_group_sizze_9412,
                                                             segment_sizze_nonzzero_9644) +
                                                     local_tid_9647, n_9130 *
                                                     m_9131) * (m_9131 *
                                                                n_9130) +
                                             squot32(virt_group_id_9655 *
                                                     squot32(segred_group_sizze_9412,
                                                             segment_sizze_nonzzero_9644) +
                                                     local_tid_9647 -
                                                     squot32(virt_group_id_9655 *
                                                             squot32(segred_group_sizze_9412,
                                                                     segment_sizze_nonzzero_9644) +
                                                             local_tid_9647,
                                                             n_9130 * m_9131) *
                                                     (n_9130 * m_9131),
                                                     m_9131) * m_9131 +
                                             (virt_group_id_9655 *
                                              squot32(segred_group_sizze_9412,
                                                      segment_sizze_nonzzero_9644) +
                                              local_tid_9647 -
                                              squot32(virt_group_id_9655 *
                                                      squot32(segred_group_sizze_9412,
                                                              segment_sizze_nonzzero_9644) +
                                                      local_tid_9647, n_9130 *
                                                      m_9131) * (n_9130 *
                                                                 m_9131) -
                                              squot32(virt_group_id_9655 *
                                                      squot32(segred_group_sizze_9412,
                                                              segment_sizze_nonzzero_9644) +
                                                      local_tid_9647 -
                                                      squot32(virt_group_id_9655 *
                                                              squot32(segred_group_sizze_9412,
                                                                      segment_sizze_nonzzero_9644) +
                                                              local_tid_9647,
                                                              n_9130 * m_9131) *
                                                      (n_9130 * m_9131),
                                                      m_9131) * m_9131)] =
                    ((__local bool *) red_arr_mem_9651)[(local_tid_9647 + 1) *
                                                        segment_sizze_nonzzero_9644 -
                                                        1];
            }
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        barrier(CLK_GLOBAL_MEM_FENCE);
        barrier(CLK_LOCAL_MEM_FENCE);
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
class device_api:
  entry_points = {"batch_simulate": (["[]i32", "i32", "[][][]i32"],
                                     ["[][][]i32"]), "simulate": (["[]i32",
                                                                   "i32",
                                                                   "[][]i32"],
                                                                  ["[][]i32"])}
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
                                       required_types=["i32", "bool"],
                                       user_sizes=sizes,
                                       all_sizes={"batch_simulate.segmap_group_size_9355": {"class": "group_size",
                                                                                  "value": None},
                                        "batch_simulate.segmap_group_size_9439": {"class": "group_size",
                                                                                  "value": None},
                                        "batch_simulate.segmap_num_groups_9441": {"class": "num_groups",
                                                                                  "value": None},
                                        "batch_simulate.segred_group_size_9411": {"class": "group_size",
                                                                                  "value": None},
                                        "batch_simulate.segred_num_groups_9413": {"class": "num_groups",
                                                                                  "value": None},
                                        "simulate.segmap_group_size_9243": {"class": "group_size", "value": None},
                                        "simulate.segmap_group_size_9315": {"class": "group_size", "value": None},
                                        "simulate.segmap_num_groups_9317": {"class": "num_groups", "value": None},
                                        "simulate.segred_group_size_9293": {"class": "group_size", "value": None},
                                        "simulate.segred_num_groups_9295": {"class": "num_groups", "value": None}})
    self.segmap_9238_var = program.segmap_9238
    self.segmap_9310_var = program.segmap_9310
    self.segmap_9348_var = program.segmap_9348
    self.segmap_9432_var = program.segmap_9432
    self.segred_large_9299_var = program.segred_large_9299
    self.segred_large_9417_var = program.segred_large_9417
    self.segred_small_9299_var = program.segred_small_9299
    self.segred_small_9417_var = program.segred_small_9417
    counter_mem_9666 = np.zeros(10240, dtype=np.int32)
    static_mem_9699 = opencl_alloc(self, 40960, "static_mem_9699")
    if (40960 != 0):
      cl.enqueue_copy(self.queue, static_mem_9699,
                      normaliseArray(counter_mem_9666), is_blocking=synchronous)
    self.counter_mem_9666 = static_mem_9699
    counter_mem_9596 = np.zeros(10240, dtype=np.int32)
    static_mem_9702 = opencl_alloc(self, 40960, "static_mem_9702")
    if (40960 != 0):
      cl.enqueue_copy(self.queue, static_mem_9702,
                      normaliseArray(counter_mem_9596), is_blocking=synchronous)
    self.counter_mem_9596 = static_mem_9702
  def futhark_batch_simulate(self, ruleset_mem_9512, seed_states_mem_9513,
                             l_9129, n_9130, m_9131, sizze_9132,
                             num_steps_9134):
    dim_match_9136 = (np.int32(18) == sizze_9132)
    empty_or_match_cert_9137 = True
    assert dim_match_9136, ("Error at\n `-> ./clcell/device_api.fut:30:1-36:51\n\n: %s" % ("function arguments of wrong shape",))
    eq_x_zz_9139 = (np.int32(0) == l_9129)
    ni_9149 = (n_9130 - np.int32(1))
    mi_9150 = (m_9131 - np.int32(1))
    eq_x_zz_9152 = (np.int32(0) == n_9130)
    eq_x_zz_9162 = (np.int32(0) == m_9131)
    loop_nonempty_9502 = slt32(np.int32(0), num_steps_9134)
    l_9433 = sext_i32_i64(l_9129)
    n_9434 = sext_i32_i64(n_9130)
    m_9435 = sext_i32_i64(m_9131)
    y_9437 = (n_9434 * m_9435)
    nest_sizze_9438 = (l_9433 * y_9437)
    segmap_group_sizze_9440 = self.sizes["batch_simulate.segmap_group_size_9439"]
    max_num_groups_9633 = self.sizes["batch_simulate.segmap_num_groups_9441"]
    num_groups_9442 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((nest_sizze_9438 + sext_i32_i64(segmap_group_sizze_9440)) - np.int64(1)),
                                                         sext_i32_i64(segmap_group_sizze_9440)),
                                                 sext_i32_i64(max_num_groups_9633))))
    binop_x_9519 = (l_9433 * n_9434)
    binop_x_9521 = (m_9435 * binop_x_9519)
    bytes_9516 = (np.int64(4) * binop_x_9521)
    mem_9523 = opencl_alloc(self, bytes_9516, "mem_9523")
    if ((1 * (np.long(num_groups_9442) * np.long(segmap_group_sizze_9440))) != 0):
      self.segmap_9432_var.set_args(np.int32(l_9129), np.int32(n_9130),
                                    np.int32(m_9131), np.int32(ni_9149),
                                    np.int32(mi_9150),
                                    np.int32(num_groups_9442), mem_9523)
      cl.enqueue_nd_range_kernel(self.queue, self.segmap_9432_var,
                                 ((np.long(num_groups_9442) * np.long(segmap_group_sizze_9440)),),
                                 (np.long(segmap_group_sizze_9440),))
      if synchronous:
        self.queue.finish()
    nest_sizze_9410 = (np.int64(4) * nest_sizze_9438)
    segred_group_sizze_9412 = self.sizes["batch_simulate.segred_group_size_9411"]
    max_num_groups_9643 = self.sizes["batch_simulate.segred_num_groups_9413"]
    num_groups_9414 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((nest_sizze_9410 + sext_i32_i64(segred_group_sizze_9412)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_9412)),
                                                 sext_i32_i64(max_num_groups_9643))))
    mem_9530 = opencl_alloc(self, binop_x_9521, "mem_9530")
    if slt32(np.int32(8), segred_group_sizze_9412):
      segment_sizze_nonzzero_9644 = np.int32(4)
      num_threads_9645 = (num_groups_9414 * segred_group_sizze_9412)
      if ((1 * (np.long(num_groups_9414) * np.long(segred_group_sizze_9412))) != 0):
        self.segred_small_9417_var.set_args(cl.LocalMemory(np.long((np.int32(1) * segred_group_sizze_9412))),
                                            np.int32(l_9129), np.int32(n_9130),
                                            np.int32(m_9131),
                                            np.int32(num_groups_9414), mem_9523,
                                            mem_9530,
                                            np.int32(segment_sizze_nonzzero_9644))
        cl.enqueue_nd_range_kernel(self.queue, self.segred_small_9417_var,
                                   ((np.long(num_groups_9414) * np.long(segred_group_sizze_9412)),),
                                   (np.long(segred_group_sizze_9412),))
        if synchronous:
          self.queue.finish()
    else:
      vit_num_groups_9661 = (squot32(((num_groups_9414 + smax32(np.int32(1),
                                                                ((l_9129 * n_9130) * m_9131))) - np.int32(1)),
                                     smax32(np.int32(1),
                                            ((l_9129 * n_9130) * m_9131))) * ((l_9129 * n_9130) * m_9131))
      num_threads_9662 = (num_groups_9414 * segred_group_sizze_9412)
      thread_per_segment_9663 = (squot32(((num_groups_9414 + smax32(np.int32(1),
                                                                    ((l_9129 * n_9130) * m_9131))) - np.int32(1)),
                                         smax32(np.int32(1),
                                                ((l_9129 * n_9130) * m_9131))) * segred_group_sizze_9412)
      group_res_arr_mem_9664 = opencl_alloc(self,
                                            (np.int32(1) * (segred_group_sizze_9412 * vit_num_groups_9661)),
                                            "group_res_arr_mem_9664")
      counter_mem_9666 = self.counter_mem_9666
      if ((1 * (np.long(num_groups_9414) * np.long(segred_group_sizze_9412))) != 0):
        self.segred_large_9417_var.set_args(cl.LocalMemory(np.long((np.int32(1) * segred_group_sizze_9412))),
                                            cl.LocalMemory(np.long(np.int32(1))),
                                            np.int32(l_9129), np.int32(n_9130),
                                            np.int32(m_9131),
                                            np.int32(num_groups_9414), mem_9523,
                                            mem_9530,
                                            np.int32(vit_num_groups_9661),
                                            np.int32(thread_per_segment_9663),
                                            group_res_arr_mem_9664,
                                            counter_mem_9666)
        cl.enqueue_nd_range_kernel(self.queue, self.segred_large_9417_var,
                                   ((np.long(num_groups_9414) * np.long(segred_group_sizze_9412)),),
                                   (np.long(segred_group_sizze_9412),))
        if synchronous:
          self.queue.finish()
    mem_9523 = None
    segmap_group_sizze_9356 = self.sizes["batch_simulate.segmap_group_size_9355"]
    segmap_group_sizze_9357 = sext_i32_i64(segmap_group_sizze_9356)
    y_9358 = (segmap_group_sizze_9357 - np.int64(1))
    x_9359 = (y_9358 + nest_sizze_9438)
    if loop_nonempty_9502:
      x_9505 = squot64(x_9359, segmap_group_sizze_9357)
      segmap_usable_groups_64_9361 = x_9505
    else:
      segmap_usable_groups_64_9361 = np.int64(0)
    segmap_usable_groups_9362 = sext_i64_i32(segmap_usable_groups_64_9361)
    game_state_expanded_mem_9531 = seed_states_mem_9513
    i_9183 = np.int32(0)
    one_9701 = np.int32(1)
    for counter_9700 in range(num_steps_9134):
      mem_9538 = opencl_alloc(self, bytes_9516, "mem_9538")
      if ((1 * (np.long(segmap_usable_groups_9362) * np.long(segmap_group_sizze_9356))) != 0):
        self.segmap_9348_var.set_args(np.int32(l_9129), np.int32(n_9130),
                                      np.int32(m_9131), ruleset_mem_9512,
                                      mem_9530, game_state_expanded_mem_9531,
                                      mem_9538)
        cl.enqueue_nd_range_kernel(self.queue, self.segmap_9348_var,
                                   ((np.long(segmap_usable_groups_9362) * np.long(segmap_group_sizze_9356)),),
                                   (np.long(segmap_group_sizze_9356),))
        if synchronous:
          self.queue.finish()
      game_state_expanded_mem_tmp_9692 = mem_9538
      game_state_expanded_mem_9531 = game_state_expanded_mem_tmp_9692
      i_9183 += one_9701
    res_mem_9539 = game_state_expanded_mem_9531
    mem_9530 = None
    y_9225 = (eq_x_zz_9152 or eq_x_zz_9162)
    old_empty_9226 = (eq_x_zz_9139 or y_9225)
    both_empty_9227 = (old_empty_9226 and old_empty_9226)
    dim_match_9228 = (m_9131 == n_9130)
    dim_match_9229 = (n_9130 == m_9131)
    y_9230 = (dim_match_9228 and dim_match_9229)
    empty_or_match_9231 = (both_empty_9227 or y_9230)
    empty_or_match_cert_9232 = True
    assert empty_or_match_9231, ("Error at\n |-> ./clcell/device_api.fut:30:1-36:51\n `-> ./clcell/device_api.fut:30:1-36:51\n\n: %s%d%s%d%s%d%s" % ("Function return value does not match shape of type [",
                                                                                                                                                     l_9129,
                                                                                                                                                     "][",
                                                                                                                                                     m_9131,
                                                                                                                                                     "][",
                                                                                                                                                     n_9130,
                                                                                                                                                     "]i32"))
    binop_x_9543 = (l_9433 * m_9435)
    binop_x_9545 = (n_9434 * binop_x_9543)
    bytes_9540 = (np.int64(4) * binop_x_9545)
    mem_9546 = opencl_alloc(self, bytes_9540, "mem_9546")
    if (((l_9129 * (m_9131 * n_9130)) * np.int32(4)) != 0):
      cl.enqueue_copy(self.queue, mem_9546, res_mem_9539,
                      dest_offset=np.long(np.int32(0)),
                      src_offset=np.long(np.int32(0)),
                      byte_count=np.long(((l_9129 * (m_9131 * n_9130)) * np.int32(4))))
    if synchronous:
      self.queue.finish()
    res_mem_9539 = None
    out_arrsizze_9630 = l_9129
    out_arrsizze_9631 = m_9131
    out_arrsizze_9632 = n_9130
    out_mem_9629 = mem_9546
    return (out_mem_9629, out_arrsizze_9630, out_arrsizze_9631,
            out_arrsizze_9632)
  def futhark_simulate(self, ruleset_mem_9512, seed_state_mem_9513, n_9047,
                       m_9048, sizze_9049, num_steps_9051):
    dim_match_9053 = (np.int32(18) == sizze_9049)
    empty_or_match_cert_9054 = True
    assert dim_match_9053, ("Error at\n `-> ./clcell/device_api.fut:23:1-27:81\n\n: %s" % ("function arguments of wrong shape",))
    ni_9056 = (n_9047 - np.int32(1))
    mi_9057 = (m_9048 - np.int32(1))
    loop_nonempty_9478 = slt32(np.int32(0), num_steps_9051)
    n_9311 = sext_i32_i64(n_9047)
    m_9312 = sext_i32_i64(m_9048)
    nest_sizze_9314 = (n_9311 * m_9312)
    segmap_group_sizze_9316 = self.sizes["simulate.segmap_group_size_9315"]
    max_num_groups_9563 = self.sizes["simulate.segmap_num_groups_9317"]
    num_groups_9318 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((nest_sizze_9314 + sext_i32_i64(segmap_group_sizze_9316)) - np.int64(1)),
                                                         sext_i32_i64(segmap_group_sizze_9316)),
                                                 sext_i32_i64(max_num_groups_9563))))
    bytes_9516 = (np.int64(4) * nest_sizze_9314)
    mem_9521 = opencl_alloc(self, bytes_9516, "mem_9521")
    if ((1 * (np.long(num_groups_9318) * np.long(segmap_group_sizze_9316))) != 0):
      self.segmap_9310_var.set_args(np.int32(n_9047), np.int32(m_9048),
                                    np.int32(ni_9056), np.int32(mi_9057),
                                    np.int32(num_groups_9318), mem_9521)
      cl.enqueue_nd_range_kernel(self.queue, self.segmap_9310_var,
                                 ((np.long(num_groups_9318) * np.long(segmap_group_sizze_9316)),),
                                 (np.long(segmap_group_sizze_9316),))
      if synchronous:
        self.queue.finish()
    segred_group_sizze_9294 = self.sizes["simulate.segred_group_size_9293"]
    max_num_groups_9573 = self.sizes["simulate.segred_num_groups_9295"]
    num_groups_9296 = sext_i64_i32(smax64(np.int32(1),
                                          smin64(squot64(((bytes_9516 + sext_i32_i64(segred_group_sizze_9294)) - np.int64(1)),
                                                         sext_i32_i64(segred_group_sizze_9294)),
                                                 sext_i32_i64(max_num_groups_9573))))
    mem_9526 = opencl_alloc(self, nest_sizze_9314, "mem_9526")
    if slt32(np.int32(8), segred_group_sizze_9294):
      segment_sizze_nonzzero_9574 = np.int32(4)
      num_threads_9575 = (num_groups_9296 * segred_group_sizze_9294)
      if ((1 * (np.long(num_groups_9296) * np.long(segred_group_sizze_9294))) != 0):
        self.segred_small_9299_var.set_args(cl.LocalMemory(np.long((np.int32(1) * segred_group_sizze_9294))),
                                            np.int32(n_9047), np.int32(m_9048),
                                            np.int32(num_groups_9296), mem_9521,
                                            mem_9526,
                                            np.int32(segment_sizze_nonzzero_9574))
        cl.enqueue_nd_range_kernel(self.queue, self.segred_small_9299_var,
                                   ((np.long(num_groups_9296) * np.long(segred_group_sizze_9294)),),
                                   (np.long(segred_group_sizze_9294),))
        if synchronous:
          self.queue.finish()
    else:
      vit_num_groups_9591 = (squot32(((num_groups_9296 + smax32(np.int32(1),
                                                                (n_9047 * m_9048))) - np.int32(1)),
                                     smax32(np.int32(1),
                                            (n_9047 * m_9048))) * (n_9047 * m_9048))
      num_threads_9592 = (num_groups_9296 * segred_group_sizze_9294)
      thread_per_segment_9593 = (squot32(((num_groups_9296 + smax32(np.int32(1),
                                                                    (n_9047 * m_9048))) - np.int32(1)),
                                         smax32(np.int32(1),
                                                (n_9047 * m_9048))) * segred_group_sizze_9294)
      group_res_arr_mem_9594 = opencl_alloc(self,
                                            (np.int32(1) * (segred_group_sizze_9294 * vit_num_groups_9591)),
                                            "group_res_arr_mem_9594")
      counter_mem_9596 = self.counter_mem_9596
      if ((1 * (np.long(num_groups_9296) * np.long(segred_group_sizze_9294))) != 0):
        self.segred_large_9299_var.set_args(cl.LocalMemory(np.long((np.int32(1) * segred_group_sizze_9294))),
                                            cl.LocalMemory(np.long(np.int32(1))),
                                            np.int32(n_9047), np.int32(m_9048),
                                            np.int32(num_groups_9296), mem_9521,
                                            mem_9526,
                                            np.int32(vit_num_groups_9591),
                                            np.int32(thread_per_segment_9593),
                                            group_res_arr_mem_9594,
                                            counter_mem_9596)
        cl.enqueue_nd_range_kernel(self.queue, self.segred_large_9299_var,
                                   ((np.long(num_groups_9296) * np.long(segred_group_sizze_9294)),),
                                   (np.long(segred_group_sizze_9294),))
        if synchronous:
          self.queue.finish()
    mem_9521 = None
    segmap_group_sizze_9244 = self.sizes["simulate.segmap_group_size_9243"]
    segmap_group_sizze_9245 = sext_i32_i64(segmap_group_sizze_9244)
    y_9246 = (segmap_group_sizze_9245 - np.int64(1))
    x_9247 = (y_9246 + nest_sizze_9314)
    if loop_nonempty_9478:
      x_9481 = squot64(x_9247, segmap_group_sizze_9245)
      segmap_usable_groups_64_9249 = x_9481
    else:
      segmap_usable_groups_64_9249 = np.int64(0)
    segmap_usable_groups_9250 = sext_i64_i32(segmap_usable_groups_64_9249)
    game_state_mem_9527 = seed_state_mem_9513
    i_9087 = np.int32(0)
    one_9704 = np.int32(1)
    for counter_9703 in range(num_steps_9051):
      mem_9532 = opencl_alloc(self, bytes_9516, "mem_9532")
      if ((1 * (np.long(segmap_usable_groups_9250) * np.long(segmap_group_sizze_9244))) != 0):
        self.segmap_9238_var.set_args(np.int32(n_9047), np.int32(m_9048),
                                      ruleset_mem_9512, mem_9526,
                                      game_state_mem_9527, mem_9532)
        cl.enqueue_nd_range_kernel(self.queue, self.segmap_9238_var,
                                   ((np.long(segmap_usable_groups_9250) * np.long(segmap_group_sizze_9244)),),
                                   (np.long(segmap_group_sizze_9244),))
        if synchronous:
          self.queue.finish()
      game_state_mem_tmp_9622 = mem_9532
      game_state_mem_9527 = game_state_mem_tmp_9622
      i_9087 += one_9704
    res_mem_9533 = game_state_mem_9527
    mem_9526 = None
    out_arrsizze_9561 = n_9047
    out_arrsizze_9562 = m_9048
    out_mem_9560 = res_mem_9533
    return (out_mem_9560, out_arrsizze_9561, out_arrsizze_9562)
  def batch_simulate(self, ruleset_mem_9512_ext, num_steps_9134_ext,
                     seed_states_mem_9513_ext):
    try:
      assert ((type(ruleset_mem_9512_ext) in [np.ndarray,
                                              cl.array.Array]) and (ruleset_mem_9512_ext.dtype == np.int32)), "Parameter has unexpected type"
      sizze_9132 = np.int32(ruleset_mem_9512_ext.shape[0])
      if (type(ruleset_mem_9512_ext) == cl.array.Array):
        ruleset_mem_9512 = ruleset_mem_9512_ext.data
      else:
        ruleset_mem_9512 = opencl_alloc(self,
                                        np.int64(ruleset_mem_9512_ext.nbytes),
                                        "ruleset_mem_9512")
        if (np.int64(ruleset_mem_9512_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, ruleset_mem_9512,
                          normaliseArray(ruleset_mem_9512_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]i32",
                                                                                                                            type(ruleset_mem_9512_ext),
                                                                                                                            ruleset_mem_9512_ext))
    try:
      num_steps_9134 = np.int32(ct.c_int32(num_steps_9134_ext))
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("i32",
                                                                                                                            type(num_steps_9134_ext),
                                                                                                                            num_steps_9134_ext))
    try:
      assert ((type(seed_states_mem_9513_ext) in [np.ndarray,
                                                  cl.array.Array]) and (seed_states_mem_9513_ext.dtype == np.int32)), "Parameter has unexpected type"
      l_9129 = np.int32(seed_states_mem_9513_ext.shape[0])
      n_9130 = np.int32(seed_states_mem_9513_ext.shape[1])
      m_9131 = np.int32(seed_states_mem_9513_ext.shape[2])
      if (type(seed_states_mem_9513_ext) == cl.array.Array):
        seed_states_mem_9513 = seed_states_mem_9513_ext.data
      else:
        seed_states_mem_9513 = opencl_alloc(self,
                                            np.int64(seed_states_mem_9513_ext.nbytes),
                                            "seed_states_mem_9513")
        if (np.int64(seed_states_mem_9513_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, seed_states_mem_9513,
                          normaliseArray(seed_states_mem_9513_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #2 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[][][]i32",
                                                                                                                            type(seed_states_mem_9513_ext),
                                                                                                                            seed_states_mem_9513_ext))
    (out_mem_9629, out_arrsizze_9630, out_arrsizze_9631,
     out_arrsizze_9632) = self.futhark_batch_simulate(ruleset_mem_9512,
                                                      seed_states_mem_9513,
                                                      l_9129, n_9130, m_9131,
                                                      sizze_9132,
                                                      num_steps_9134)
    return cl.array.Array(self.queue, (out_arrsizze_9630, out_arrsizze_9631,
                                       out_arrsizze_9632), ct.c_int32,
                          data=out_mem_9629)
  def simulate(self, ruleset_mem_9512_ext, num_steps_9051_ext,
               seed_state_mem_9513_ext):
    try:
      assert ((type(ruleset_mem_9512_ext) in [np.ndarray,
                                              cl.array.Array]) and (ruleset_mem_9512_ext.dtype == np.int32)), "Parameter has unexpected type"
      sizze_9049 = np.int32(ruleset_mem_9512_ext.shape[0])
      if (type(ruleset_mem_9512_ext) == cl.array.Array):
        ruleset_mem_9512 = ruleset_mem_9512_ext.data
      else:
        ruleset_mem_9512 = opencl_alloc(self,
                                        np.int64(ruleset_mem_9512_ext.nbytes),
                                        "ruleset_mem_9512")
        if (np.int64(ruleset_mem_9512_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, ruleset_mem_9512,
                          normaliseArray(ruleset_mem_9512_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]i32",
                                                                                                                            type(ruleset_mem_9512_ext),
                                                                                                                            ruleset_mem_9512_ext))
    try:
      num_steps_9051 = np.int32(ct.c_int32(num_steps_9051_ext))
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("i32",
                                                                                                                            type(num_steps_9051_ext),
                                                                                                                            num_steps_9051_ext))
    try:
      assert ((type(seed_state_mem_9513_ext) in [np.ndarray,
                                                 cl.array.Array]) and (seed_state_mem_9513_ext.dtype == np.int32)), "Parameter has unexpected type"
      n_9047 = np.int32(seed_state_mem_9513_ext.shape[0])
      m_9048 = np.int32(seed_state_mem_9513_ext.shape[1])
      if (type(seed_state_mem_9513_ext) == cl.array.Array):
        seed_state_mem_9513 = seed_state_mem_9513_ext.data
      else:
        seed_state_mem_9513 = opencl_alloc(self,
                                           np.int64(seed_state_mem_9513_ext.nbytes),
                                           "seed_state_mem_9513")
        if (np.int64(seed_state_mem_9513_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, seed_state_mem_9513,
                          normaliseArray(seed_state_mem_9513_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #2 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[][]i32",
                                                                                                                            type(seed_state_mem_9513_ext),
                                                                                                                            seed_state_mem_9513_ext))
    (out_mem_9560, out_arrsizze_9561,
     out_arrsizze_9562) = self.futhark_simulate(ruleset_mem_9512,
                                                seed_state_mem_9513, n_9047,
                                                m_9048, sizze_9049,
                                                num_steps_9051)
    return cl.array.Array(self.queue, (out_arrsizze_9561, out_arrsizze_9562),
                          ct.c_int32, data=out_mem_9560)