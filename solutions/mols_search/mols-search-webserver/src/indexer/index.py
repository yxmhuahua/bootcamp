import logging as log
from milvus import *
from common.config import MILVUS_HOST, MILVUS_PORT, VECTOR_DIMENSION
import traceback


def milvus_client():
    try:
        milvus = Milvus(MILVUS_HOST, MILVUS_PORT)
        return milvus
    except Exception as e:
        log.error(e)
        log.error(traceback.format_exc())
        return None


def create_table(client, table_name=None, dimension=VECTOR_DIMENSION,
                 index_file_size=256, metric_type=MetricType.JACCARD):
    table_param = {
        'collection_name': table_name,
        'dimension': dimension,
        'index_file_size':index_file_size,
        'metric_type': metric_type
    }
    try:
        status = client.create_collection(table_param)
        return status
    except Exception as e:
        log.error(e)


def insert_vectors(client, table_name, vectors):
<<<<<<< HEAD
    if not client.has_collection(collection_name=table_name):
=======
    if not client.has_collection(table_name):
>>>>>>> d37d04782f5bfde3ce51ceb580ae59e0e1fc1f7d
        log.error("table %s not exist", table_name)
        return
    try:
        status, ids = client.insert(collection_name=table_name, records=vectors)
<<<<<<< HEAD
=======
        print(status, ids)
>>>>>>> d37d04782f5bfde3ce51ceb580ae59e0e1fc1f7d
        return status, ids
    except Exception as e:
        log.error(e)


def create_index(client, table_name):
    index_param = {'nlist': 2048}
    status = client.create_index(table_name, IndexType.IVFLAT, index_param)
    return status


def delete_table(client, table_name):
    status = client.drop_collection(table_name)
    print(status)
    return status


def search_vectors(client, table_name, vectors, top_k):
    status, res = client.search(collection_name=table_name, query_records=vectors, top_k=top_k, params={'nprobe':64})
    return status, res


def has_table(client, table_name):
    status = client.has_collection(collection_name=table_name)
    return status


def count_table(client, table_name):
    status, num = client.count_entities(collection_name=table_name)
    print(status)
    return num