import multiprocessing

bind = "unix:/tmp/itosvita_simply_co_ua_gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
proc_name = "itosvita"
