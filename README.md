
# Demo Streamlit App for Integrating Notion to Haystack RAG Pipelines

This repository contains a [Streamlit](https://docs.streamlit.io/) application that works together with [Haystack](https://haystack.deepset.ai)
and [Weaviate](https://weaviate.io). It shows you how to integrate your [Notion](https://www.notion.so/) pages into a
retrieval-augmented generative search application by exporting them and indexing them into your Weaviate database.


## Steps to Run this Demo
1. Create a Notion integration and connect it to the pages you want to export. Follow [this guide](https://developers.notion.com/docs/create-a-notion-integration#getting-started)
   from the Notion documentation for more details about this step.
2. Add your Notion API key and OpenAI API key to the `secrets.env` file.
3. Run `docker-compose up` from the root directory of this repository. This will start the following three services: 
    * `haystack-api`: This service runs the Haystack REST API and serves as the backend of our application.
    * `weaviate`: This service runs Weaviate and serves as the database of our application.
    * `ui`: This service runs streamlit and serves as the user interface of our application.
4. Add the IDs of the pages you want to extract to `index_notion_pages.py` and run it via `python index_notion_pages.py`.
   This will index the pages into your Weaviate Document Store. You can find the ID of a page in the URL of that page.
5. Open your browser and go to `localhost:8501` to access the application.
6. Start asking question! 🎉
