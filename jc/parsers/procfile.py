"""jc - JSON Convert Proc file output parser

<<Short procfile description and caveats>>

Usage (cli):

    $ cat /proc/<file> | jc --procfile

Usage (module):

    import jc
    result = jc.parse('procfile', proc_file)

Schema:

    [
      {
        "procfile":     string,
        "bar":     boolean,
        "baz":     integer
      }
    ]

Examples:

    $ procfile | jc --procfile -p
    []

    $ procfile | jc --procfile -p -r
    []
"""
import re
from typing import List, Dict
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = 'Proc file parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']


__version__ = info.version


def _process(proc_data: List[Dict]) -> List[Dict]:
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured to conform to the schema.
    """

    # process the data here
    # rebuild output for added semantic information
    # use helper functions in jc.utils for int, float, bool
    # conversions and timestamps

    return proc_data


def _parse_uptime():
    print('uptime')


def _parse_loadavg():
    print('loadavg')


def _parse_cpuinfo():
    print('cpuinfo')


def _parse_meminfo():
    print('meminfo')


def _parse_version():
    print('version')


def _parse_crypto():
    print('crypto')


def _parse_diskstats():
    print('diskstats')


def _parse_filesystems():
    print('filesystems')


def _parse_interrupts():
    print('interrupts')


def _parse_iomem():
    print('iomem')


def _parse_ioports():
    print('ioports')


def _parse_locks():
    print('locks')


def _parse_modules():
    print('modules')


def _parse_mtrr():
    print('mtrr')


def _parse_partitions():
    print('partitions')


def _parse_buddyinfo():
    print('buddyinfo')


def _parse_pagetypeinfo():
    print('pagetypinfo')


def _parse_vmallocinfo():
    print('vmallocinfo')


def _parse_softirqs():
    print('softirqs')


def _parse_stat():
    print('stat')


def _parse_swaps():
    print('swaps')


def _parse_slabinfo():
    print('slabinfo')


def _parse_consoles():
    print('consoles')


def _parse_devices():
    print('devices')


def _parse_vmstat():
    print('vmstat')


def _parse_zoneinfo():
    print('zoneinfo')

####

def _parse_driver_rtc():
    print('driver rtc')

####

def _parse_net_arp():
    print('net arp')

def _parse_net_dev():
    print('net dev')

def _parse_net_dev_mcast():
    print('net dev_mcast')

def _parse_net_igmp():
    print('net igmp')

def _parse_net_igmp6():
    print('net igmp6')

def _parse_net_if_inet6():
    print('net if_inet6')

def _parse_net_ipv6_route():
    print('net ipv6_route')

def _parse_net_netlink():
    print('net netlink')

def _parse_net_netstat():
    print('net netstat')

def _parse_net_packet():
    print('net packet')

def _parse_net_protocols():
    print('net protocols')

def _parse_net_route():
    print('net route')

def _parse_net_unix():
    print('net unix')

####


def _parse_pid_status():
    print('pid status')


def _parse_pid_statm():
    print('pid statm')


def _parse_pid_stat():
    print('pid stat')


def _parse_pid_smaps():
    print('pid smaps')


def _parse_pid_maps():
    print('pid maps')


def _parse_pid_numa_maps():
    print('pid numa_maps')


def _parse_pid_io():
    print('pid io')


def _parse_pid_mountinfo():
    print('pid mountinfo')


def _parse_pid_fdinfo():
    print('pid fdinfo')

####

def _parse_scsi_scsi():
    print('scsi scsi')

def _parse_scsi_device_info():
    print('scsi device_info')


def parse(
    data: str,
    raw: bool = False,
    quiet: bool = False
) -> List[Dict]:
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) unprocessed output if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        List of Dictionaries. Raw or processed structured data.
    """
    jc.utils.compatibility(__name__, info.compatible, quiet)
    jc.utils.input_type_check(data)

    raw_output: List = []

    if jc.utils.has_data(data):

        # signatures
        buddyinfo_p = re.compile(r'^Node \d+, zone\s+\w+\s+(?:\d+\s+){11}\n')
        consoles_p = re.compile(r'^\w+\s+[\-WUR]{3} \([ECBpba ]+\)\s+\d+:\d+\n')
        cpuinfo_p = re.compile(r'^processor\s+:.*\nvendor_id\s+:.*\ncpu family\s+:.*\n')
        crypto_p = re.compile(r'^name\s+:.*\ndriver\s+:.*\nmodule\s+:.*\n')
        devices_p = re.compile(r'^Character devices:\n\s+\d+ .*\n')
        diskstats_p = re.compile(r'^\s*\d+\s+\d\s\w+\s(?:\d+\s){16}\d\n')
        filesystems_p = re.compile(r'^(?:(?:nodev\t|\t)\w+\n){3}')
        interrupts_p = re.compile(r'^\s+(?:CPU\d+ +)+\n\s*\d+:\s+\d+')
        iomem_p = re.compile(r'^00000000-[0-9a-f]{8} : .*\n[0-9a-f]{8}-[0-9a-f]{8} : ')
        ioports_p = re.compile(r'^0000-[0-9a-f]{4} : .*\n\s*0000-[0-9a-f]{4} : ')
        loadavg_p = re.compile(r'^\d+.\d\d \d+.\d\d \d+.\d\d \d+/\d+ \d+$')
        locks_p = re.compile(r'^\d+: (?:POSIX|FLOCK|OFDLCK)\s+(?:ADVISORY|MANDATORY)\s+(?:READ|WRITE) ')
        meminfo_p = re.compile(r'^MemTotal:.*\nMemFree:.*\nMemAvailable:.*\n')
        modules_p = re.compile(r'^\w+ \d+ \d+ (?:-|\w+,).*0x[0-9a-f]{16}\n')
        mtrr_p = re.compile(r'^reg\d+: base=0x[0-9a-f]+ \(')
        pagetypeinfo_p = re.compile(r'^Page block order:\s+\d+\nPages per block:\s+\d+\n\n')
        partitions_p = re.compile(r'^major minor  #blocks  name\n\n\s*\d+\s+\d+\s+\d+ \w+\n')
        slabinfo_p = re.compile(r'^slabinfo - version: \d+.\d+\n')
        softirqs_p = re.compile(r'^\s+(CPU\d+\s+)+\n\s+HI:\s+\d')
        stat_p = re.compile(r'^cpu\s+(?: \d+){10}.*intr ', re.DOTALL)
        swaps_p = re.compile(r'^Filename\t\t\t\tType\t\tSize\t\tUsed\t\tPriority\n')
        uptime_p = re.compile(r'^\d+.\d\d \d+.\d\d$')
        version_p = re.compile(r'^.+\sversion\s[^\n]+$')
        vmallocinfo_p = re.compile(r'^0x[0-9a-f]{16}-0x[0-9a-f]{16}\s+\d+ \w+\+\w+/\w+ ')
        vmstat_p = re.compile(r'nr_free_pages \d+\n.* \d$', re.DOTALL)
        zoneinfo_p = re.compile(r'^Node \d+, zone\s+\w+\n')

        driver_rtc_p = re.compile(r'^rtc_time\t: .*\nrtc_date\t: .*\nalrm_time\t: .*\n')

        net_arp_p = re.compile(r'^IP address\s+HW type\s+Flags\s+HW address\s+Mask\s+Device\n')
        net_dev_p = re.compile(r'^Inter-\|\s+Receive\s+\|\s+Transmit\n')
        net_dev_mcast_p = re.compile(r'^\d+\s+\w+\s+\d+\s+\d+\s+[0-9a-f]{12}')
        net_if_inet6_p = re.compile(r'^[0-9a-f]{32} \d\d \d\d \d\d \d\d\s+\w+')
        net_igmp_p = re.compile(r'^Idx\tDevice\s+:\s+Count\s+Querier\tGroup\s+Users\s+Timer\tReporter\n')
        net_igmp6_p = re.compile(r'^\d+\s+\w+\s+[0-9a-f]{32}\s+\d+\s+[0-9A-F]{8}\s+\d+')
        net_ipv6_route_p = re.compile(r'^[0-9a-f]{32} \d\d [0-9a-f]{32} \d\d [0-9a-f]{32} (?:[0-9a-f]{8} ){4}\s+\w+')
        net_netlink_p = re.compile(r'^sk\s+Eth Pid\s+Groups\s+Rmem\s+Wmem')
        net_netstat_p = re.compile(r'^TcpExt: SyncookiesSent SyncookiesRecv SyncookiesFailed')
        net_packet_p = re.compile(r'^sk       RefCnt Type Proto  Iface R Rmem   User   Inode\n')
        net_protocols_p = re.compile(r'^protocol  size sockets  memory press maxhdr  slab module     cl co di ac io in de sh ss gs se re sp bi br ha uh gp em\n')
        net_route_p = re.compile(r'^Iface\tDestination\tGateway \tFlags\tRefCnt\tUse\tMetric\tMask\t\tMTU\tWindow\tIRTT\s+\n')
        net_unix_p = re.compile(r'^Num       RefCount Protocol Flags    Type St Inode Path\n')

        pid_status_p = re.compile(r'^Name:\t.+\nUmask:\t\d+\nState:\t.+\nTgid:\t\d+\n')
        pid_statm_p = re.compile(r'^\d+ \d+ \d+\s\d+\s\d+\s\d+\s\d+$')
        pid_stat_p = re.compile(r'^\d+ \(.{1,16}\) \w \d+ \d+ \d+ \d+ -?\d+ (?:\d+ ){43}\d+$')
        pid_smaps_p = re.compile(r'^[0-9a-f]{12}-[0-9a-f]{12} [rwxsp\-]{4} [0-9a-f]{8} [0-9a-f]{2}:[0-9a-f]{2} \d+ [^\n]+\nSize:\s+\d+ \S\S\n')
        pid_maps_p = re.compile(r'^[0-9a-f]{12}-[0-9a-f]{12} [rwxsp\-]{4} [0-9a-f]{8} [0-9a-f]{2}:[0-9a-f]{2} \d+ ')
        pid_numa_maps_p = re.compile(r'^[a-f0-9]{12} default [^\n]+\n')
        pid_io_p = re.compile(r'^rchar: \d+\nwchar: \d+\nsyscr: \d+\n')
        pid_mountinfo_p = re.compile(r'^\d+ \d+ \d+:\d+ /.+\n')
        pid_fdinfo_p = re.compile(r'^pos:\t\d+\nflags:\t\d+\nmnt_id:\t\d+\n')

        scsi_device_info = re.compile(r"^'\w+' '.+' 0x\d+")
        scsi_scsi_p = re.compile(r'^Attached devices:\nHost: \w+ ')

        procmap = {
            buddyinfo_p: _parse_buddyinfo,
            consoles_p: _parse_consoles,
            cpuinfo_p: _parse_cpuinfo,
            crypto_p: _parse_crypto,
            devices_p: _parse_devices,
            diskstats_p: _parse_diskstats,
            filesystems_p: _parse_filesystems,
            interrupts_p: _parse_interrupts,
            iomem_p: _parse_iomem,
            ioports_p: _parse_ioports,
            loadavg_p: _parse_loadavg,
            locks_p: _parse_locks,
            meminfo_p: _parse_meminfo,
            modules_p: _parse_modules,
            mtrr_p: _parse_mtrr,
            pagetypeinfo_p: _parse_pagetypeinfo,
            partitions_p: _parse_partitions,
            slabinfo_p: _parse_slabinfo,
            softirqs_p: _parse_softirqs,
            stat_p: _parse_stat,
            swaps_p: _parse_swaps,
            uptime_p: _parse_uptime,
            version_p: _parse_version,
            vmallocinfo_p: _parse_vmallocinfo,
            vmstat_p: _parse_vmstat,
            zoneinfo_p: _parse_zoneinfo,

            driver_rtc_p: _parse_driver_rtc,

            net_arp_p: _parse_net_arp,
            net_dev_p: _parse_net_dev,
            net_if_inet6_p: _parse_net_if_inet6,
            net_igmp_p: _parse_net_igmp,
            net_igmp6_p: _parse_net_igmp6,
            net_netlink_p: _parse_net_netlink,
            net_netstat_p: _parse_net_netstat,
            net_packet_p: _parse_net_packet,
            net_protocols_p: _parse_net_protocols,
            net_route_p: _parse_net_route,
            net_unix_p: _parse_net_unix,
            net_ipv6_route_p: _parse_net_ipv6_route,  # before net_dev_mcast
            net_dev_mcast_p: _parse_net_dev_mcast,    # after net_ipv6_route

            pid_fdinfo_p: _parse_pid_fdinfo,
            pid_io_p: _parse_pid_io,
            pid_mountinfo_p: _parse_pid_mountinfo,
            pid_numa_maps_p: _parse_pid_numa_maps,
            pid_stat_p: _parse_pid_stat,
            pid_statm_p: _parse_pid_statm,
            pid_status_p: _parse_pid_status,
            pid_smaps_p: _parse_pid_smaps,  # before pid_maps
            pid_maps_p: _parse_pid_maps,    # after pid_smaps

            scsi_device_info: _parse_scsi_device_info,
            scsi_scsi_p: _parse_scsi_scsi
        }

        for reg_pattern, parse_func in procmap.items():
            if reg_pattern.search(data):
                parse_func()
                break

        # for line in filter(None, data.splitlines()):

        #     # parse the content here
        #     # check out helper functions in jc.utils
        #     # and jc.parsers.universal

        #     pass

    return raw_output if raw else _process(raw_output)
