import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="expansao_zapflow")

collection.upsert(
    documents=[
        "A Zapflow vai abrir escritório no Brasil.",
        "A Zapflow vai abrir escritório no França.",
        "A Zapflow vai abrir escritório no Japão.",
        "A Zapflow vai abrir escritório no Alemanha.",
        "A Zapflow vai abrir escritório no Canadá.",
        "A Zapflow vai abrir escritório no Austrália.",
        "A Zapflow vai abrir escritório no Itália.",
        "A Zapflow vai abrir escritório no Argentina.",
        "A Zapflow vai abrir escritório no Espanha.",
        "A Zapflow vai abrir escritório no Rússia.",
        "A Zapflow vai abrir escritório no China."
    ],
    ids=["pais1", "pais2", "pais3","pais4","pais5","pais6","pais7","pais8","pais9","pais10","pais11"]
)

resultado = collection.query(
    query_texts=["O Zapflow vai ter escritório no Rio de Janeiro?"],
    n_results=3
)

print(resultado)