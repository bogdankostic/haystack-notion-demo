from pathlib import Path

from haystack import Pipeline
from notion_haystack import NotionExporter
from dotenv import load_dotenv

# Load API keys
load_dotenv("secrets.env")


# Load indexing Pipeline from YAML configuration
indexing_pipeline = Pipeline.load_from_yaml(
    path=Path("pipelines/notion-search.haystack-pipeline.yml"),
)
# Index Notion pages
indexing_pipeline.run(file_paths=[])  # Add your Notion page IDs here
