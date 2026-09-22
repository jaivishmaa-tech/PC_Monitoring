import psutil
import time
import GPUtil

def get_cpu():
    def cpu_percent():
        print(psutil.cpu_percent(interval=0.1, percpu=True))
        if 'cpupercent' in locals():
            cpu_percent = locals()['cpupercent']
            if cpu_percent is not None:
                print(cpu_percent[0].current)
    def get_cpu_up_time():
        uptime = None
        try:
            uptime = psutil.cpu_io_counters().busy_time
            return uptime
        except Exception as e:
            print(f"Error getting CPU uptime: {e}")
    def Cpu_utilization():
        utilization = psutil.cpu_percent(interval=1)
        print(f"CPU Utilization: {utilization}%")
    print(psutil.cpu_times_percent(interval=1, percpu=True))
    print(psutil.cpu_count(logical=True))
    print(psutil.cpu_stats())
    print(psutil.getloadavg(percpu=True, interval=1))
    def get_cpu_frequency():
        freq = psutil.cpu_freq(percpu=False)
        if freq:
            Ghz = freq[0].current / 1000
            print(f"CPU Frequency: {Ghz:.2f} GHz")

def get_gpu():
    gpus = GPUtil.getGPUs()
    if gpus:
        return gpus[0]
    return None

def get_gpu_up_time():
    uptime_gpu = None
    try:
        uptime_gpu = GPUtil.getGPUs()[0].load
        print(f"GPU Uptime: {uptime_gpu}")
    except Exception as e:
        print(f"Error getting GPU uptime: {e}")
def get_cpu_temperature():
    try:
        temps = psutil.gpu_temperatures(interval=1)
        if 'gputemp' in temps:
            gpu_temps = temps['gputemp']
            if gpu_temps:
                return gpu_temps[0].current
    except Exception as e:
        print(f"Error getting GPU temperature: {e}")
    return None
def get_gpu_usage():
    try:
        gpumaxload = GPUtil.maxload()
        if gpumaxload is not None:
            return gpumaxload * 100
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
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_activetime = psutil.disk_io_counters().busy_time
    disk_activetime = time.time() - (disk_activetime / 1000)
    disk_activetime = time.time() - psutil.boot_time()  # Convert milliseconds to seconds

    return (disk_info.used / disk_info.total) * 100

def get_network_usage():
    net_info = psutil.net_io_counters(interval=1)
    print(net_info.bytes_sent)
    print(net_info.bytes_recv)
