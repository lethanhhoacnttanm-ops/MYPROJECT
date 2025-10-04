from flask import Flask, request
import subprocess

app = Flask(__name__)

SERVICE_CONTAINER_MAP = {
    "web_service": "myproject-web_service-1", 
    "db_service": "myproject-db_service-1",
    "nginx_exporter": "myproject-nginx_exporter-1", 
    "mysql_exporter": "myproject-db_exporter-1",
    
    
    "host_cleanup": "host_cleanup_script.sh", # Tên script/hành động phục hồi trên Host
}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and "alerts" in data:
        for alert in data["alerts"]:
            alertname = alert["labels"].get("alertname")
            severity = alert["labels"].get("severity")
            service_name = alert["labels"].get("service_to_recover")
            container_name = SERVICE_CONTAINER_MAP.get(service_name)
            
            # DANH SÁCH CÁC ALERT CÓ AUTO-RECOVERY
            RECOVERY_ALERTS = [
                "WebServiceDown", "DBServiceDown", "NginxExporterDown",
                "HighCPUUsage", "HighMemoryUsage", "NginxHighConnections",
                "DiskAlmostFull" # Bổ sung tất cả các alert cần phục hồi
            ]

            # LOGIC PHỤC HỒI TỔNG QUÁT:
            # 1. Phải là cảnh báo 'warning'
            # 2. Phải có service_to_recover được định nghĩa (container_name != None)
            # 3. Alertname phải nằm trong danh sách RECOVERY_ALERTS
            if severity == "warning" and container_name and alertname in RECOVERY_ALERTS:
                
                # Xử lý đặc biệt cho Disk Cleanup (nếu bạn tạo script riêng)
                if service_name == "host_cleanup":
                    # Giả sử bạn có một script riêng để xóa log/cache
                    subprocess.run(["sh", "./cleanup_host.sh"])
                    print(f"[Webhook] Auto-recovery executed: Running HOST CLEANUP script.")
                else:
                    # Xử lý phục hồi container thông thường (docker start)
                    subprocess.run(["sh", "./recovery.sh", container_name])
                    print(f"[Webhook] Auto-recovery executed for {alertname} service: {service_name} (Container: {container_name})")

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
