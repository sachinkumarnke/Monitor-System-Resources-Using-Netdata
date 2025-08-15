# Netdata Monitoring Guide

## Dashboard Overview

### Main Sections to Explore

#### 1. System Overview
- **CPU**: Real-time CPU usage per core
- **Load**: System load averages
- **RAM**: Memory usage and availability
- **Swap**: Virtual memory usage
- **Disk**: I/O operations and space usage
- **Network**: Interface traffic and errors

#### 2. Applications Monitoring
- **Processes**: Top processes by CPU/Memory
- **Users**: Resource usage per user
- **Groups**: Process group statistics

#### 3. Container Monitoring (Docker)
- **Container CPU**: Per-container CPU usage
- **Container Memory**: Memory consumption
- **Container Network**: Network I/O per container
- **Container Disk**: Disk I/O per container

## Key Metrics to Monitor

### Performance Indicators
```
CPU Usage: < 80% (sustained)
Memory Usage: < 85%
Disk I/O Wait: < 10%
Network Errors: < 0.1%
Load Average: < Number of CPU cores
```

### Alert Thresholds
- **Critical**: CPU > 90%, Memory > 95%
- **Warning**: CPU > 80%, Memory > 85%
- **Info**: Disk space < 10% free

## Useful Dashboard Features

### 1. Time Range Selection
- Real-time (default)
- Last hour/day/week
- Custom time ranges

### 2. Chart Interactions
- Zoom in/out on time periods
- Pan through historical data
- Toggle data series on/off

### 3. Alert Configuration
- Navigate to "Alarms" tab
- Configure custom thresholds
- Set notification methods

## Container Log Access

### View Netdata Logs
```bash
# Container logs
docker logs netdata

# Follow logs in real-time
docker logs -f netdata

# Access container shell
docker exec -it netdata /bin/bash

# View internal logs (inside container)
ls -la /var/log/netdata/
```

## Performance Optimization Tips

### 1. Reduce Data Retention
- Default: 1 hour of data
- Modify in `/etc/netdata/netdata.conf`
- Balance between history and performance

### 2. Disable Unnecessary Plugins
- Edit configuration to disable unused collectors
- Reduces CPU and memory overhead

### 3. Adjust Update Frequency
- Default: 1-second updates
- Increase interval for less critical metrics

## Troubleshooting

### Common Issues
1. **Dashboard not accessible**
   - Check container status: `docker ps`
   - Verify port mapping: `-p 19999:19999`

2. **Missing Docker metrics**
   - Ensure Docker socket is mounted
   - Check container permissions

3. **High resource usage**
   - Review enabled plugins
   - Adjust data retention settings

### Health Checks
```bash
# Container health
docker inspect netdata | grep Health

# Resource usage
docker stats netdata

# Port accessibility
netstat -an | findstr 19999
```