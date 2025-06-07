import re
import statistics

from datetime import datetime

filepath_client_tcp_log="logs/clientTCPLog.txt"

filepath_client_udp_log="logs/clientUDPLog.txt"


client_tcp_timestamps=[]

client_udp_timestamps=[]

def read_log(filepath):
    latency_timestamps=[]

    with open(filepath, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            
            server_time=re.search(r'ST(.*?)RT', line)
            trimmed_server_time = server_time.group(1).strip()
            print(trimmed_server_time)  

            server_timestamp = datetime.strptime(trimmed_server_time, "%Y-%m-%d %H:%M:%S.%f")

            client_time=re.search(r'RT(.*)', line)
            trimmed_client_time = client_time.group(1).strip()
            client_timestamp = datetime.strptime(trimmed_client_time, "%Y-%m-%d %H:%M:%S.%f")

            latency_timestamps.append(client_timestamp-server_timestamp)

    return latency_timestamps

def calculate_jitter(latency_values):
    
    inter_arrival_times=[]
    for i in range (len(latency_values)-1):

        inter_arrival_times.append(abs(latency_values[i+1]-latency_values[i])) 
    
    average_jitter = statistics.mean(inter_arrival_times)

    return average_jitter


latency_array_tcp=read_log(filepath_client_tcp_log)

latency_array_udp=read_log(filepath_client_udp_log)

for i in range(len(latency_array_tcp)):
    latency_array_tcp[i]=latency_array_tcp[i].total_seconds()
    latency_array_udp[i]=latency_array_udp[i].total_seconds()


print(latency_array_tcp)

#print(latency_array_udp)


print(f"Latencia promedio Transmisión TCP:{statistics.mean(latency_array_tcp)} seg")
print(f"Latencia Máxima transmisión TCP:{max(latency_array_tcp)} seg")
print(f"Latencia Mínima transmisión TCP:{min(latency_array_tcp)} seg")
print(f"Jitter:{calculate_jitter(latency_array_tcp)} seg")
print("----------------------------------------------------------------------------------")
print(f"Latencia promedio Transmisión UDP:{statistics.mean(latency_array_udp)} seg")
print(f"Latencia Máxima transmisión UDP:{max(latency_array_udp)} seg")
print(f"Latencia Mínima transmisión UDP:{min(latency_array_udp)} seg")
print(f"Jitter:{calculate_jitter(latency_array_udp)} seg")