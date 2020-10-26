# TODO Needs updating in the future.

import sys
from typing import Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

RedisType = Union[bytes, str, int, float]

class GithubDataType(TypedDict):
    name: str
    current_no_of_releases: int

class GithubMonitorDataType(TypedDict):
    name: str
    github_monitor_last_monitoring_round: int

class SystemDataType(TypedDict):
    name: str
    chain_name: str
    process_cpu_seconds_total: int
    process_memory_usage: int
    virtual_memory_usage: int
    open_file_descriptors: int
    system_cpu_usage: int
    system_ram_usage: int
    system_storage_usage: int
    system_network_transmit_bytes_per_second: int
    system_network_receive_bytes_per_second: int
    system_network_receive_bytes_total: int
    system_network_transmit_bytes_total: int
    system_disk_io_time_seconds_total: int
    system_disk_io_time_seconds_in_interval: int

class SystemMonitorDataType(TypedDict):
    name: str
    system_monitor_last_monitoring_round: int

class AlertDataType(TypedDict):
    chain_name: str
    origin: str
    alert_name: str
    severity: str
    message: str
    timestamp: str