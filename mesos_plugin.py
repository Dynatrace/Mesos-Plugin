import requests
import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name

class DemoPlugin(BasePlugin):
    def query(self, **kwargs):
        pgi = self.find_single_process_group(pgi_name('mesosphere.marathon.Main'))
        pgi_id = pgi.group_instance_id
        stats_url = "http://localhost/mesos/metrics/snapshot"
        stats = json.loads(requests.get(stats_url).content.decode())
		
		#CPU Related Metrics
        self.results_builder.absolute(key='cpus_used', value=stats['master/cpus_used'], entity_id=pgi_id)
        self.results_builder.absolute(key='cpus_percent', value=stats['master/cpus_percent'], entity_id=pgi_id)
        self.results_builder.absolute(key='cpus_total', value=stats['master/cpus_total'], entity_id=pgi_id)
        #Disk Related Metrics
        self.results_builder.absolute(key='disk_percent', value=stats['master/disk_percent'], entity_id=pgi_id)
        self.results_builder.absolute(key='disk_used', value=stats['master/disk_used'], entity_id=pgi_id)
        self.results_builder.absolute(key='disk_total', value=stats['master/disk_total'], entity_id=pgi_id)
        #Memory Related
        self.results_builder.absolute(key='mem_percent', value=stats['master/mem_percent'], entity_id=pgi_id)
        self.results_builder.absolute(key='mem_used', value=stats['master/mem_used'], entity_id=pgi_id)
        self.results_builder.absolute(key='mem_total', value=stats['master/mem_total'], entity_id=pgi_id)
        #Master Election Related
        self.results_builder.absolute(key='master_elected', value=stats['master/elected'], entity_id=pgi_id)
        self.results_builder.absolute(key='uptime_secs', value=stats['master/uptime_secs'], entity_id=pgi_id)
        #Node Related Metrics
        self.results_builder.absolute(key='system_cpus_total', value=stats['system/cpus_total'], entity_id=pgi_id)
        self.results_builder.absolute(key='system_load_15min', value=stats['system/load_15min'], entity_id=pgi_id)
        self.results_builder.absolute(key='system_load_5min', value=stats['system/load_5min'], entity_id=pgi_id)
        self.results_builder.absolute(key='system_load_1min', value=stats['system/load_1min'], entity_id=pgi_id)
        self.results_builder.absolute(key='system_mem_free_bytes', value=stats['system/mem_free_bytes'], entity_id=pgi_id)
        self.results_builder.absolute(key='system_total_free_bytes', value=stats['system/mem_total_bytes'], entity_id=pgi_id)
        #Mesos Slaves Related Metrics
        self.results_builder.absolute(key='slave_registrations', value=stats['master/slave_registrations'], entity_id=pgi_id)
        self.results_builder.absolute(key='slave_removals', value=stats['master/slave_removals'], entity_id=pgi_id)
        self.results_builder.absolute(key='slave_reregistrations', value=stats['master/slave_reregistrations'], entity_id=pgi_id)
        self.results_builder.absolute(key='slave_shutdowns_scheduled', value=stats['master/slave_shutdowns_scheduled'], entity_id=pgi_id)
        self.results_builder.absolute(key='slave_shutdowns_canceled', value=stats['master/slave_shutdowns_canceled'], entity_id=pgi_id)
        self.results_builder.absolute(key='slave_shutdowns_completed', value=stats['master/slave_shutdowns_completed'], entity_id=pgi_id)
        self.results_builder.absolute(key='slaves_active', value=stats['master/slaves_active'], entity_id=pgi_id)
        self.results_builder.absolute(key='slaves_connected', value=stats['master/slaves_connected'], entity_id=pgi_id)
        self.results_builder.absolute(key='slaves_disconnected', value=stats['master/slaves_disconnected'], entity_id=pgi_id)
        self.results_builder.absolute(key='slaves_inactive', value=stats['master/slaves_inactive'], entity_id=pgi_id)