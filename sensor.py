import psutil
import requests
import socket

def get_active_connections():
    connections = []
    
    # Grab all active network connections
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED' and conn.raddr:
                ip = conn.raddr.ip
                port = conn.raddr.port
                pid = conn.pid
                
                # Skip local loopback
                if ip in ('127.0.0.1', '0.0.0.0', '::1'):
                    continue
                    
                process_name = "Unknown"
                if pid:
                    try:
                        process = psutil.Process(pid)
                        process_name = process.name()
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                
                try:
                    remote_hostname = socket.gethostbyaddr(ip)[0]
                except Exception:
                    remote_hostname = "Unknown Host"

                connections.append({
                    "local_ip": conn.laddr.ip if conn.laddr else '',
                    "local_port": conn.laddr.port if conn.laddr else '',
                    "remote_ip": ip,
                    "remote_port": port,
                    "remote_hostname": remote_hostname,
                    "status": conn.status,
                    "pid": pid,
                    "process_name": process_name
                })
    except psutil.AccessDenied:
        print("Warning: Run as administrator to see all connections.")
            
    # Deduplicate by process and remote IP
    unique_conns = []
    seen = set()
    for c in connections:
        sig = (c['process_name'], c['remote_ip'])
        if sig not in seen:
            seen.add(sig)
            unique_conns.append(c)
            
    return unique_conns

def geolocate_ip(ip):
    try:
        # Using ip-api which is free for non-commercial
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=2)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return {
                    "country": data.get("country"),
                    "city": data.get("city"),
                    "lat": data.get("lat"),
                    "lon": data.get("lon"),
                    "isp": data.get("isp")
                }
    except Exception:
        pass
    
    return {
        "country": "Unknown",
        "city": "Unknown",
        "lat": 0,
        "lon": 0,
        "isp": "Unknown"
    }

def get_footprint_data():
    conns = get_active_connections()
    # To avoid rate limits on the free IP API (45 req/min), we'll limit the results at first
    conns = conns[:15]
    
    results = []
    for c in conns:
        geo = geolocate_ip(c['remote_ip'])
        c.update(geo)
        results.append(c)
    
    return results

if __name__ == "__main__":
    print(get_footprint_data())
