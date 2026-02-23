# Configuration module for the data pipeline

import os
from dataclasses import dataclass

@dataclass
class Config:
    """Configuration settings for the data pipeline."""
    
    # Data paths
    input_path: str = "data/input"
    output_path: str = "data/output"
    
    # Processing settings
    batch_size: int = 1000
    max_workers: int = 4
    
    # Cache settings
    cache_enabled: bool = True
    cache_dir: str = ".cache"
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables."""
        return cls(
            input_path=os.getenv("INPUT_PATH", cls.input_path),
            output_path=os.getenv("OUTPUT_PATH", cls.output_path),
            batch_size=int(os.getenv("BATCH_SIZE", cls.batch_size)),
            max_workers=int(os.getenv("MAX_WORKERS", cls.max_workers)),
            cache_enabled=os.getenv("CACHE_ENABLED", "true").lower() == "true",
            cache_dir=os.getenv("CACHE_DIR", cls.cache_dir)
        )
