# Monitor System Resources Using Netdata
<img width="1901" height="994" alt="Screenshot 2025-08-15 112608" src="https://github.com/user-attachments/assets/31b23001-1373-4823-8b3c-34ed131c3806" />

## Objective
Install Netdata and visualize system and application performance metrics using Docker.

## Prerequisites
- Docker Desktop installed and running
- Windows PowerShell or Command Prompt
- Web browser for accessing dashboard

## Quick Start

### 1. Run Netdata Container
```bash
docker run -d --name=netdata -p 19999:19999 netdata/netdata
```

### 2. Access Dashboard
Open your browser and navigate to: http://localhost:19999

### 3. Monitor Key Metrics
- **CPU Usage**: Real-time processor utilization
- **Memory**: RAM usage and availability
- **Disk I/O**: Read/write operations and space usage
- **Network**: Traffic and connection statistics
- **Docker Containers**: Container resource usage

## Features Explored

### Dashboard Sections
- **System Overview**: CPU, RAM, disk, network at a glance
- **Applications**: Process-level monitoring
- **Containers**: Docker container metrics
- **Alerts**: Configurable threshold notifications
- **Logs**: System and application log monitoring

### Key Monitoring Areas
1. **Performance Metrics**
   - CPU utilization per core
   - Memory usage patterns
   - Disk I/O performance
   - Network throughput

2. **Container Monitoring**
   - Resource usage per container
   - Container health status
   - Performance comparisons

3. **Alert System**
   - Threshold-based notifications
   - Custom alert configurations
   - Historical alert data

## Log Locations
- Container logs: `/var/log/netdata` (inside container)
- Access logs via: `docker logs netdata`

## Useful Commands
```bash
# Check container status
docker ps | grep netdata

# View container logs
docker logs netdata

# Stop monitoring
docker stop netdata

# Remove container
docker rm netdata

# Restart with persistent data
docker run -d --name=netdata -p 19999:19999 -v netdata-data:/var/lib/netdata netdata/netdata
```

## Dashboard Screenshots
Screenshots of key dashboard sections are saved in the `screenshots/` directory.

## Outcome
Successfully implemented lightweight monitoring solution providing:
- Real-time system resource visualization
- Container performance tracking
- Alert system for proactive monitoring
- Historical data analysis capabilities
