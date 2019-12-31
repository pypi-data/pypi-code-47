# -*- coding: utf-8 -*-
DESC = "tiems-2019-04-16"
INFO = {
  "CreateService": {
    "params": [
      {
        "name": "Scaler",
        "desc": "扩缩容配置"
      },
      {
        "name": "ServiceConfigId",
        "desc": "服务配置Id"
      },
      {
        "name": "Name",
        "desc": "服务名称"
      },
      {
        "name": "ScaleMode",
        "desc": "扩缩容方式，支持AUTO, MANUAL，分别表示自动扩缩容和手动扩缩容"
      },
      {
        "name": "Cpu",
        "desc": "处理器配置, 单位为1/1000核；范围[100, 256000]"
      },
      {
        "name": "Memory",
        "desc": "内存配置, 单位为1M；范围[100, 256000]"
      },
      {
        "name": "Cluster",
        "desc": "集群，不填则使用默认集群"
      },
      {
        "name": "ResourceGroupId",
        "desc": "部署要使用的资源组Id，默认为共享资源组"
      },
      {
        "name": "Authentication",
        "desc": "默认为空，表示不需要鉴权，TOKEN 表示选择 Token 鉴权方式"
      },
      {
        "name": "Gpu",
        "desc": "GPU算力配置，单位为1/1000 卡，范围 [0, 256000]"
      },
      {
        "name": "GpuMemory",
        "desc": "显存配置, 单位为1M，范围 [0, 256000]"
      },
      {
        "name": "Description",
        "desc": "备注"
      },
      {
        "name": "GpuType",
        "desc": "GPU类型"
      }
    ],
    "desc": "创建服务"
  },
  "ExposeService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务Id"
      },
      {
        "name": "ExposeType",
        "desc": "暴露方式，支持 EXTERNAL（外网暴露），VPC （VPC内网打通）"
      },
      {
        "name": "VpcId",
        "desc": "暴露方式为 VPC 时，填写需要打通的私有网络Id"
      },
      {
        "name": "SubnetId",
        "desc": "暴露方式为 VPC 时，填写需要打通的子网Id"
      }
    ],
    "desc": "暴露服务"
  },
  "DeleteServiceConfig": {
    "params": [
      {
        "name": "ServiceConfigId",
        "desc": "服务配置Id"
      },
      {
        "name": "ServiceConfigName",
        "desc": "服务配置名称"
      }
    ],
    "desc": "删除服务配置"
  },
  "CreateServiceConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "配置名称"
      },
      {
        "name": "Runtime",
        "desc": "运行环境"
      },
      {
        "name": "ModelUri",
        "desc": "模型地址，支持cos路径，格式为 cos://bucket名-appid.cos.region名.myqcloud.com/模型文件夹路径。为模型文件的上一层文件夹地址。"
      },
      {
        "name": "Description",
        "desc": "配置描述"
      }
    ],
    "desc": "创建服务配置"
  },
  "CreateRuntime": {
    "params": [
      {
        "name": "Name",
        "desc": "全局唯一的运行环境名称"
      },
      {
        "name": "Image",
        "desc": "运行环境镜像地址"
      },
      {
        "name": "Framework",
        "desc": "运行环境框架"
      },
      {
        "name": "Description",
        "desc": "运行环境描述"
      },
      {
        "name": "HealthCheckOn",
        "desc": "是否支持健康检查，默认为False"
      }
    ],
    "desc": "创建运行环境"
  },
  "UpdateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "任务 Id"
      },
      {
        "name": "JobAction",
        "desc": "任务更新动作，支持：Cancel"
      },
      {
        "name": "Description",
        "desc": "备注"
      }
    ],
    "desc": "更新任务"
  },
  "CreateJob": {
    "params": [
      {
        "name": "Name",
        "desc": "任务名称"
      },
      {
        "name": "WorkerCount",
        "desc": "同时处理任务的 Worker 个数"
      },
      {
        "name": "ConfigId",
        "desc": "使用的配置 Id"
      },
      {
        "name": "Cpu",
        "desc": "处理器配置, 单位为1/1000核；范围[100, 256000]"
      },
      {
        "name": "Memory",
        "desc": "内存配置, 单位为1M；范围[100, 256000]"
      },
      {
        "name": "Cluster",
        "desc": "运行集群"
      },
      {
        "name": "PredictInput",
        "desc": "预测输入"
      },
      {
        "name": "Description",
        "desc": "任务描述"
      },
      {
        "name": "ResourceGroupId",
        "desc": "使用的资源组 Id，默认使用共享资源组"
      },
      {
        "name": "Gpu",
        "desc": "GPU算力配置，单位为1/1000 卡，范围 [0, 256000]"
      },
      {
        "name": "GpuMemory",
        "desc": "显存配置, 单位为1M，范围 [0, 256000]"
      },
      {
        "name": "GpuType",
        "desc": "GPU类型"
      }
    ],
    "desc": "创建任务"
  },
  "DeleteJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "任务 Id"
      }
    ],
    "desc": "删除任务"
  },
  "DeleteRuntime": {
    "params": [
      {
        "name": "Runtime",
        "desc": "要删除的Runtime名"
      }
    ],
    "desc": "删除运行环境"
  },
  "DescribeServiceConfigs": {
    "params": [
      {
        "name": "Filters",
        "desc": "筛选选项，支持按照name等进行筛选"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为1000"
      },
      {
        "name": "Order",
        "desc": "输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列"
      },
      {
        "name": "OrderField",
        "desc": "排序的依据字段， 取值范围 \"CREATE_TIME\", \"UPDATE_TIME\", \"NAME\""
      },
      {
        "name": "PageByName",
        "desc": "是否按照配置名分页"
      }
    ],
    "desc": "描述服务配置"
  },
  "DeleteService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务Id"
      }
    ],
    "desc": "删除服务"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "筛选选项"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为200"
      },
      {
        "name": "Order",
        "desc": "输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列"
      },
      {
        "name": "OrderField",
        "desc": "排序的依据字段， 取值范围 \"CREATE_TIME\", \"UPDATE_TIME\", \"NAME\""
      },
      {
        "name": "ResourceGroupId",
        "desc": "要查询的资源组 ID"
      }
    ],
    "desc": "获取节点列表"
  },
  "DescribeServices": {
    "params": [
      {
        "name": "Filters",
        "desc": "筛选选项，支持按照name等字段进行筛选"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100"
      },
      {
        "name": "Order",
        "desc": "输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列"
      },
      {
        "name": "OrderField",
        "desc": "排序的依据字段， 取值范围 \"CREATE_TIME\" \"UPDATE_TIME\""
      }
    ],
    "desc": "描述服务"
  },
  "DescribeRuntimes": {
    "params": [],
    "desc": "描述服务运行环境"
  },
  "UpdateService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务Id"
      },
      {
        "name": "Scaler",
        "desc": "扩缩容配置"
      },
      {
        "name": "ServiceConfigId",
        "desc": "服务配置Id"
      },
      {
        "name": "ScaleMode",
        "desc": "支持AUTO, MANUAL，分别表示自动扩缩容，手动扩缩容"
      },
      {
        "name": "ServiceAction",
        "desc": "支持STOP(停止) RESUME(重启)"
      },
      {
        "name": "Description",
        "desc": "备注"
      },
      {
        "name": "GpuType",
        "desc": "GPU卡类型"
      }
    ],
    "desc": "更新服务"
  }
}