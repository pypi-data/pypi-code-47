from decimal import Decimal
import logging
from pathlib import Path
from pprint import pformat
from typing import (
    Any, Optional,
    Collection, Set,
    Mapping, MutableMapping,
    Sequence, List,
    Tuple,
)
import uuid

import attr

from ai.backend.common.logging import BraceStyleAdapter
from ai.backend.agent.resources import (
    AbstractComputeDevice, AbstractComputePlugin,
    AbstractAllocMap, DiscretePropertyAllocMap,
)
try:
    from ai.backend.agent.resources import get_resource_spec_from_container  # type: ignore
except ImportError:
    from ai.backend.agent.docker.resources import get_resource_spec_from_container
from ai.backend.agent.stats import (
    StatContext, MetricTypes,
    NodeMeasurement, ContainerMeasurement, Measurement,
)
from ai.backend.common.types import (
    BinarySize, MetricKey,
    DeviceName, DeviceId, DeviceModelInfo,
    SlotName, SlotTypes,
)
from . import __version__, smi
from .exception import NoRocmDeviceError, GenericRocmError, RocmUtilFetchError, RocmMemFetchError
from .hip import libhip

__all__ = (
    'PREFIX',
    'ROCmDevice',
    'ROCmPlugin',
    'init',
)

PREFIX = 'rocm'

log = BraceStyleAdapter(logging.getLogger('ai.backend.accelerator.rocm'))


async def init(config: Mapping[str, str]):
    raw_device_mask = config.get('device_mask')
    if raw_device_mask is not None:
        ROCmPlugin.device_mask = [
            *map(lambda dev_id: DeviceId(dev_id), raw_device_mask.split(','))
        ]
    try:
        detected_devices = await ROCmPlugin.list_devices()
        log.info('detected devices:\n' + pformat(detected_devices))
        log.info('ROCm acceleration is enabled.')
    except (ImportError, NoRocmDeviceError, GenericRocmError):
        log.warning('could not load the ROCm HIP library.')
        log.info('ROCm acceleration is disabled.')
        ROCmPlugin.enabled = False
    except RuntimeError as e:
        log.warning('ROCm init error: {}', e)
        log.info('ROCm acceleration is disabled.')
        ROCmPlugin.enabled = False
    return ROCmPlugin


@attr.s(auto_attribs=True)
class ROCmDevice(AbstractComputeDevice):
    model_name: str
    uuid: str


class ROCmPlugin(AbstractComputePlugin):

    key = DeviceName('rocm')
    slot_types: Sequence[Tuple[SlotName, SlotTypes]] = (
        (SlotName('rocm.device'), SlotTypes('count')),
    )

    device_mask: Sequence[DeviceId] = []
    enabled: bool = True

    @classmethod
    async def list_devices(cls) -> Collection[ROCmDevice]:
        if not cls.enabled:
            return []
        all_devices = []
        num_devices = libhip.get_device_count()
        for dev_id in map(lambda idx: DeviceId(str(idx)), range(num_devices)):
            if dev_id in cls.device_mask:
                continue
            smi_name = f'card{dev_id}'
            # Use HIP only for fetching multiProcessorCount
            raw_info = libhip.get_device_props(int(dev_id))
            pci_bus_id = smi.getBus(smi_name)
            sysfs_node_path = "/sys/bus/pci/devices/" \
                              f"{pci_bus_id}/numa_node"
            node: Optional[int]
            try:
                node = int(Path(sysfs_node_path).read_text().strip())
            except OSError:
                node = None
            dev_uuid, raw_dev_uuid = None, smi.getUniqueId(smi_name)
            if raw_dev_uuid is not None:
                dev_uuid = str(uuid.UUID(bytes=raw_dev_uuid))
            else:
                dev_uuid = '00000000-0000-0000-0000-000000000000'
            dev_info = ROCmDevice(
                device_id=dev_id,
                hw_location=pci_bus_id,
                numa_node=node,
                memory_size=smi.getMemInfo(smi_name, 'vram')[1],
                # TODO: Find way to fetch multiProcessorCount without using HIP
                processing_units=raw_info['multiProcessorCount'],
                model_name=raw_info['name'],
                uuid=dev_uuid,
            )
            all_devices.append(dev_info)
        return all_devices

    @classmethod
    async def available_slots(cls) -> Mapping[SlotName, Decimal]:
        devices = await cls.list_devices()
        return {
            SlotName('rocm.device'): Decimal(len(devices)),
        }

    @classmethod
    def get_version(cls) -> str:
        return __version__

    @classmethod
    async def extra_info(cls) -> Mapping[str, Any]:
        if cls.enabled:
            try:
                return {
                    'rocm_support': True,
                    'driver_version': smi.getVersion('driver'),
                }
            except (GenericRocmError, ImportError):
                cls.enabled = False
        return {
            'rocm_support': False,
        }

    @classmethod
    async def gather_node_measures(
            cls, ctx: StatContext,
            ) -> Sequence[NodeMeasurement]:
        dev_count = 0
        mem_avail_total = 0
        mem_used_total = 0
        mem_stats = {}
        util_total = 0
        util_stats = {}
        if cls.enabled:
            try:
                for dev_id in map(lambda idx: DeviceId(str(idx)), smi.listDevices(False)):
                    if dev_id in cls.device_mask:
                        continue

                    mem_used, mem_total = smi.getMemInfo(dev_id, 'vram')
                    gpu_util = smi.getGpuUse(dev_id)

                    mem_avail_total += int(mem_total)
                    mem_used_total += int(mem_used)
                    mem_stats[dev_id] = Measurement(Decimal(mem_used),
                                                    Decimal(mem_total))
                    util_total += gpu_util
                    util_stats[dev_id] = Measurement(Decimal(gpu_util), Decimal(100))
            except (RocmUtilFetchError, RocmMemFetchError) as e:
                # libhip is not installed.
                # Return an empty result.
                log.exception(e)
                cls.enabled = False
        return [
            NodeMeasurement(
                MetricKey('rocm_mem'),
                MetricTypes.USAGE,
                unit_hint='bytes',
                stats_filter=frozenset({'max'}),
                per_node=Measurement(Decimal(mem_used_total), Decimal(mem_avail_total)),
                per_device=mem_stats,
            ),
            NodeMeasurement(
                MetricKey('rocm_util'),
                MetricTypes.USAGE,
                unit_hint='percent',
                stats_filter=frozenset({'avg', 'max'}),
                per_node=Measurement(Decimal(util_total), Decimal(dev_count * 100)),
                per_device=util_stats,
            ),
        ]

    @classmethod
    async def gather_container_measures(
            cls, ctx: StatContext,
            container_ids: Sequence[str],
            ) -> Sequence[ContainerMeasurement]:
        return []

    @classmethod
    async def create_alloc_map(cls) -> AbstractAllocMap:
        devices = await cls.list_devices()
        return DiscretePropertyAllocMap(
            devices=devices,
            prop_func=lambda dev: 1)

    @classmethod
    async def get_hooks(cls, distro: str, arch: str) -> Sequence[Path]:
        return []

    @classmethod
    async def generate_docker_args(cls, docker,
                                   device_alloc: Mapping[SlotName, Mapping[DeviceId, Decimal]]) \
                                   -> Mapping[str, Any]:
        if not cls.enabled:
            return {}
        active_device_ids = set()
        for slot_type, per_device_alloc in device_alloc.items():
            for dev_id, alloc in per_device_alloc.items():
                if alloc > 0:
                    active_device_ids.add(dev_id)
        device_list_str = ','.join(sorted(active_device_ids))
        return {
            'HostConfig': {
                'Devices': [
                    { "PathOnHost": "/dev/kfd", "PathInContainer": "/dev/kfd", "CgroupPermissions": "mrw"},
                    { "PathOnHost": "/dev/dri", "PathInContainer": "/dev/dri", "CgroupPermissions": "mrw"}
                ],
                # 'Privileged': True,
                'GroupAdd': ['video'],
                'SecurityOpt': ['seccomp=unconfined']
            },
            'Env': [
                f"ROCR_VISIBLE_DEVICES={device_list_str}",
            ],
        }

    @classmethod
    async def get_attached_devices(
            cls, device_alloc: Mapping[SlotName, Mapping[DeviceId, Decimal]],
            ) -> Sequence[DeviceModelInfo]:
        device_ids: List[DeviceId] = []
        if SlotName('rocm.devices') in device_alloc:
            device_ids.extend(device_alloc[SlotName('rocm.devices')].keys())
        available_devices = await cls.list_devices()
        attached_devices: List[DeviceModelInfo] = []
        for device in available_devices:
            if device.device_id in device_ids:
                proc = device.processing_units
                mem = BinarySize(device.memory_size)
                attached_devices.append({  # TODO: update common.types.DeviceModelInfo
                    'device_id': device.device_id,
                    'model_name': device.model_name,
                    'smp': proc,
                    'mem': mem,
                })
        return attached_devices

    @classmethod
    async def restore_from_container(
            cls, container,
            alloc_map: AbstractAllocMap,
            ) -> None:
        if not cls.enabled:
            return
        resource_spec = await get_resource_spec_from_container(container)
        if resource_spec is None:
            return
        alloc_map.allocations[SlotName('rocm.device')].update(
            resource_spec.allocations.get(
                DeviceName('rocm'), {}
            ).get(
                SlotName('rocm.device'), {}
            )
        )

    @classmethod
    async def generate_resource_data(
            cls, device_alloc: Mapping[SlotName, Mapping[DeviceId, Decimal]],
            ) -> Mapping[str, str]:
        data: MutableMapping[str, str] = {}
        if not cls.enabled:
            return data

        active_device_id_set: Set[DeviceId] = set()
        for slot_type, per_device_alloc in device_alloc.items():
            for dev_id, alloc in per_device_alloc.items():
                if alloc > 0:
                    active_device_id_set.add(dev_id)
        active_device_ids = sorted(active_device_id_set, key=lambda v: int(v))
        data['ROCm_GLOBAL_DEVICE_IDS'] = ','.join(
            f'{local_idx}:{global_id}'
            for local_idx, global_id in enumerate(active_device_ids))
        return data
