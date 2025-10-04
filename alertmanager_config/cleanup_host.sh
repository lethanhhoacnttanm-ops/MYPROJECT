#!/bin/bash
echo "[Cleanup Script] Starting host cleanup process..."
# Giả lập hành động dọn dẹp bằng cách xóa file rác (hoặc file dd giả lập)
# LƯU Ý: Lệnh này CHỈ chạy bên trong container webhook, không trực tiếp trên Host.
# Tuy nhiên, đối với báo cáo, chỉ cần chứng minh script được kích hoạt.
echo "[Cleanup Script] Deleting old logs and temporary files (Simulated)."
echo "[Cleanup Script] Cleanup finished."