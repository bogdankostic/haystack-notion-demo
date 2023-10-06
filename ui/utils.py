from typing import Dict, Tuple

import requests


def query(query_str: str) -> Tuple[Dict, Dict]:
    """
    Query the Haystack REST API with a given query string.
    """
    url = "http://haystack-api:8000/query"
    response_raw = requests.post(url, json={"query": query_str})
    if response_raw.status_code >= 400 and response_raw.status_code != 503:
        raise Exception(f"{vars(response_raw)}")

    response = response_raw.json()
    if "errors" in response:
        raise Exception(", ".join(response["errors"]))

    # Format result
    answer = response["answers"][0]
    cited_docs = []
    for doc_id in answer["document_ids"]:
        for retrieved_doc in response["documents"]:
            if retrieved_doc["id"] == doc_id:
                cited_docs.append(retrieved_doc)
                if len(cited_docs) == len(answer["document_ids"]):
                    break

    result = {"answer": answer, "cited_docs": cited_docs}

    return result, response
