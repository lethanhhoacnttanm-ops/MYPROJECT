#!/bin/bash
SERVICE=$1
echo "[Recovery] Restarting service: $SERVICE"
docker start $SERVICE

