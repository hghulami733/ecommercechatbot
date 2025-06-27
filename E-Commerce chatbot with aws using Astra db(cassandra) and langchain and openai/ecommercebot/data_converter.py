import pandas as pd
from langchain_core.documents import Document

def dataconverter():

    data_path = "../data/flipkart_product_review.csv"

    data = pd.read_csv(data_path)

    data = data[["product_title", "review"]]

    product_list = []

    # Iterate over the rows of the Datafram
    for index, row in data.iterrows():
        # Construct an object with 'product_name' and 'review' attributes
        obj = {
            "product_name": row["product_title"],
            "review": row["review"]
        }

        # Append objects to the list
        product_list.append(obj)

    # Print the list of objects
    # for obj in product_list:
    #     print(obj)

    docs = []

    for entry in product_list:
        metadata = {"product_name": entry["product_name"]}
        doc = Document(page_content=entry["review"], metadata=metadata)
        docs.append(doc)

    return docs