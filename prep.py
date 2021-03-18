import socket
import pymongo

hostname = socket.gethostname()
fqdn = hostname + ".younifi.cloud"
client = pymongo.MongoClient("mongodb://127.0.0.1:27117/ace")
mdb = client.ace
mdb.setting.delete_one({"key":"super_mgmt"})
mdb.setting.insert_one({
   "key":"super_mgmt",
   "discoverable":False,
   "minimum_usable_hd_space":500,
   "autobackup_enabled":True,
   "autobackup_cron_expr":"0 0 * * *",
   "autobackup_days":30,
   "autobackup_timezone":"UTC",
   "enable_analytics":False,
   "multiple_sites_enabled":False,
   "data_retention_time_enabled":False,
   "data_retention_time_in_hours_for_5minutes_scale":24,
   "data_retention_time_in_hours_for_hourly_scale":720,
   "data_retention_time_in_hours_for_daily_scale":2160,
   "data_retention_time_in_hours_for_monthly_scale":8760,
   "data_retention_time_in_hours_for_others":2160,
   "time_series_per_client_stats_enabled":True,
   "backup_to_cloud_enabled":True,
   "autobackup_post_actions":[
      "copy_cloud"
   ],
   "analytics_disapproved_for":"6.0.45",
   "override_inform_host":True,
   "live_updates":"auto",
   "autobackup_max_files":7
})
mdb.setting.delete_one({"key":"super_identity"})

mdb.setting.insert_one({
    "key" : "super_identity",
    "name" : "UniFi Network",
    "hostname" : fqdn
})

