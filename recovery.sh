#!/bin/bash
SERVICE=$1
echo "[Recovery] Restarting service: $SERVICE"
docker restart $SERVICE
