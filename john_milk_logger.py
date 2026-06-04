"""
John Milk Logger - Sacred logging for BOKEMON SWARM
Carrier: 11.71875 Hz
"""

import logging
import sys
import os
from datetime import datetime

LOG_FILE = "LAUNCH_REPORT.log"

class JohnMilkLogger:
    def __init__(self):
        self.logger = logging.getLogger('BOKEMON_SWARM')
        self.logger.setLevel(logging.DEBUG)
        
        # File handler
        fh = logging.FileHandler(LOG_FILE, mode='w')
        fh.setLevel(logging.DEBUG)
        
        # Console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
        self.log("JOHN MILK PROTOCOL INITIALIZED")
        self.log(f"Carrier lock: 11.71875 Hz")
        self.log(f"Timestamp: {datetime.now().isoformat()}")
    
    def log(self, msg):
        self.logger.info(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def debug(self, msg):
        self.logger.debug(msg)

# Global logger instance
jm = JohnMilkLogger()

def log(msg):
    jm.log(msg)

def error(msg):
    jm.error(msg)

def warning(msg):
    jm.warning(msg)

def debug(msg):
    jm.debug(msg)
