from elasticsearch import Elasticsearch, helpers
import pandas as pd

es = Elasticsearch("http://localhost:9200", verify_certs=False)

if not es.ping():
    raise ConnectionError("No se pudo conectar a Elasticsearch.")

df = pd.read_csv("clash_royale_cards.csv")
print(f"Cargado CSV con {len(df)} registros.")

index_name = "clashroyale_2025"

# Eliminar índice anterior
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

es.indices.create(index=index_name)


actions = [
    {"_index": index_name, "_source": row.dropna().to_dict()}
    for _, row in df.iterrows()
]

success, failed = helpers.bulk(es, actions, stats_only=True)

print(f"Carga completa: {success} OK, {failed} fallos")