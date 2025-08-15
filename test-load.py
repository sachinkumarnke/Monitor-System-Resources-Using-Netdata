#!/usr/bin/env python3
"""
Test script to generate system load for monitoring with Netdata
Creates CPU, memory, and disk I/O load for demonstration purposes
"""

import time
import threading
import os
import random
import multiprocessing

class SystemLoadGenerator:
    def __init__(self):
        self.running = False
        self.threads = []
    
    def cpu_load(self, duration=30, intensity=0.7):
        """Generate CPU load"""
        print(f"Starting CPU load test (intensity: {intensity*100}%)")
        end_time = time.time() + duration
        
        while time.time() < end_time and self.running:
            # Busy work
            if random.random() < intensity:
                sum(i*i for i in range(1000))
            else:
                time.sleep(0.01)
    
    def memory_load(self, duration=30, size_mb=100):
        """Generate memory load"""
        print(f"Starting memory load test ({size_mb}MB)")
        data = []
        
        try:
            # Allocate memory in chunks
            for i in range(size_mb):
                if not self.running:
                    break
                chunk = bytearray(1024 * 1024)  # 1MB chunks
                data.append(chunk)
                time.sleep(0.1)
            
            # Hold memory for duration
            time.sleep(duration)
            
        finally:
            # Clean up
            del data
            print("Memory load test completed")
    
    def disk_load(self, duration=30, file_size_mb=10):
        """Generate disk I/O load"""
        print(f"Starting disk I/O test ({file_size_mb}MB)")
        filename = "test_load_file.tmp"
        
        try:
            end_time = time.time() + duration
            
            while time.time() < end_time and self.running:
                # Write test
                with open(filename, 'wb') as f:
                    data = os.urandom(file_size_mb * 1024 * 1024)
                    f.write(data)
                
                # Read test
                if os.path.exists(filename):
                    with open(filename, 'rb') as f:
                        f.read()
                
                time.sleep(1)
                
        finally:
            # Cleanup
            if os.path.exists(filename):
                os.remove(filename)
            print("Disk I/O test completed")
    
    def start_load_test(self, duration=60):
        """Start comprehensive load test"""
        print("="*50)
        print("Starting System Load Test for Netdata Monitoring")
        print("="*50)
        print(f"Duration: {duration} seconds")
        print("Monitor the dashboard at: http://localhost:19999")
        print("="*50)
        
        self.running = True
        
        # Start different load types in parallel
        cpu_threads = []
        cpu_count = multiprocessing.cpu_count()
        
        # CPU load (use multiple threads for multi-core)
        for i in range(min(cpu_count, 4)):
            thread = threading.Thread(
                target=self.cpu_load, 
                args=(duration, 0.6)
            )
            cpu_threads.append(thread)
            thread.start()
        
        # Memory load
        memory_thread = threading.Thread(
            target=self.memory_load, 
            args=(duration, 200)
        )
        memory_thread.start()
        
        # Disk I/O load
        disk_thread = threading.Thread(
            target=self.disk_load, 
            args=(duration, 5)
        )
        disk_thread.start()
        
        # Wait for completion
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            print("\nStopping load test...")
        
        self.running = False
        
        # Wait for all threads to complete
        for thread in cpu_threads:
            thread.join()
        memory_thread.join()
        disk_thread.join()
        
        print("="*50)
        print("Load test completed!")
        print("Check Netdata dashboard for the generated metrics")
        print("="*50)

def main():
    generator = SystemLoadGenerator()
    
    print("System Load Generator for Netdata Testing")
    print("This will generate CPU, memory, and disk load")
    print("Make sure Netdata is running at http://localhost:19999")
    
    try:
        duration = int(input("Enter test duration in seconds (default 60): ") or "60")
        generator.start_load_test(duration)
    except ValueError:
        print("Invalid duration, using default 60 seconds")
        generator.start_load_test(60)
    except KeyboardInterrupt:
        print("\nTest cancelled by user")

if __name__ == "__main__":
    main()