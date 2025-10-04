# SỬ DỤNG IMAGE ALPINE
FROM python:3.11-alpine

WORKDIR /app

# 1. Cài đặt các gói cần thiết (Flask, bash, và Docker client)
RUN apk update && \
    apk add --no-cache bash curl docker && \
    pip install Flask

# 2. BẮT BUỘC: COPY các file từ thư mục host sang thư mục làm việc trong container
COPY webhook_server.py ./
COPY recovery.sh ./

# 3. Đảm bảo recovery.sh có quyền thực thi (Sau khi file đã được COPY)
RUN chmod +x recovery.sh

CMD ["python", "webhook_server.py"]