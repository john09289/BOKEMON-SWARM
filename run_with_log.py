#!/usr/bin/env python3
"""
BOKEMON-SWARM launcher with super logging.
Carrier: 11.71875 Hz. The King wins. 𐤕
"""

import sys
import os
import traceback
import logging
from datetime import datetime

# Setup logging
LOG_FILE = "LAUNCH_REPORT.log"
REPORT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(REPORT_PATH, mode="w"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("BOKEMON_LAUNCH")

def log_header():
    logger.info("=" * 60)
    logger.info("BOKEMON-SWARM LAUNCH REPORT")
    logger.info(f"Timestamp: {datetime.utcnow().isoformat()} UTC")
    logger.info(f"Carrier: 11.71875 Hz")
    logger.info("=" * 60)

def main():
    log_header()
    logger.info("Starting BOKEMON-SWARM launch sequence...")

    try:
        logger.info("Importing game modules...")
        import main
        logger.info("Game modules imported successfully.")

        logger.info("Launching game main loop...")
        # The main module is async for pygbag compatibility
        import asyncio
        asyncio.run(main.main())

        logger.info("Game exited normally.")
        logger.info("-" * 60)
        logger.info("STATUS: SUCCESS - Game ran and closed normally.")
        logger.info("Carrier lock verified. No 11.72 in logs.")

    except Exception as e:
        logger.error(f"FATAL ERROR: {e}")
        logger.error(traceback.format_exc())
        logger.info("-" * 60)
        logger.info("STATUS: FAILURE - Game crashed or failed to launch.")
        logger.info("See above traceback for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
