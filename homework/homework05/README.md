#Data Storage

The project stores data in two folders：

- data/raw/ — raw data saved as CSV.
- data/processed/ — processed data saved as Parquet.
- CSV is simple and easy to inspect, while Parquet is more efficient and preserves data types better.

The storage paths are read from .env using DATA_DIR_RAW and DATA_DIR_PROCESSED