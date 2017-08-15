""" Redis and MongoDB settings
"""
#MongoDB settings
MONGODB_JOBS = "mongodb://mongo:27017/mrq" # MongoDB URI for the jobs, scheduled_jobs & workers database.Defaults to mongodb://127.0.0.1:27017/mrq
MONGODB_LOGS = 0 #MongoDB URI for the logs database."0" will disable remote logs, "1" will use main MongoDB.Defaults to 1
MONGODB_LOGS_SIZE = None #If provided, sets the log collection to capped to that amount of bytes.
NO_MONGODB_ENSURE_INDEXES = None #If provided, skip the creation of MongoDB indexes at worker startup.

#Redis settings
REDIS = "redis://redis:6379" #Redis URI.Defaults to redis://127.0.0.1:6379
REDIS_PREFIX = "mrq" #Redis key prefix.Default to "mrq".
REDIS_MAX_CONNECTIONS = 1000 #Redis max connection pool size.Defaults to 1000.
REDIS_TIMEOUT = 30 #Redis connection pool timeout to wait for an available connection.Defaults to 30.

""" mrq-dashboard settings
"""
DASHBOARD_HTTPAUTH = "" #HTTP Auth for the Dashboard. Format is user
DASHBOARD_QUEUE = "default" #Default queue for dashboard actions.
DASHBOARD_PORT = 5555 #Use this port for mrq-dashboard.Defaults to port 5555.
DASHBOARD_IP = "0.0.0.0" #Bind the dashboard to this IP. Default is 0.0.0.0, use 127.0.0.1 to restrict access.
