from feast import FileSource
import os
from dotenv import load_dotenv
# Load .env file
load_dotenv()
# Access environment variables
DATA_SOURCE_PATH = os.getenv("DATA_SOURCE_PATH")


driver_stats = FileSource(
    name="driver_stats_source",
    path="gs://feast-workshop-feast-workshop/driver_stats.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
    description="A table describing the stats of a driver based on hourly logs",
    owner="test2@gmail.com",
)
print(driver_stats.path)

