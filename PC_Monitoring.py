import psutil
import time

def get_cpu_usage():
    
    print(psutil.cpu_percent(interval=0.1, percpu=True))
    print(psutil.cpu_times_percent(interval=1, percpu=True))
    print(psutil.cpu_count(logical=True))
    print(psutil.cpu_stats())
    print(psutil.cpu_freq(percpu=True))
    print(psutil.getloadavg(percpu=True, interval=1))

def get_cpu_temperature():
    
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            core_temps = temps['coretemp']
            if core_temps:
                return core_temps[0].current
    except Exception as e:
        print(f"Error getting CPU temperature: {e}")
    return None
def get_gpu_usage():

    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].load * 100
    except Exception as e:
        print(f"Error getting GPU usage: {e}")
    return None
def get_gpu_temperature():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].temperature
    except Exception as e:
        print(f"Error getting GPU temperature: {e}")
    return None

def get_memory_usage():
    """Get the current memory usage percentage.    
    Returns:
        float: The current memory usage percentage."""
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
   
    net_info = psutil.net_io_counters()
    return net_info.bytes_sent, net_info.bytes_recv
