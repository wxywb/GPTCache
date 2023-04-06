from gptcache.adapter import openai
from gptcache.core import cache
from gptcache.cache.factory import get_data_manager
from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation
import numpy as np


d = 8


def mock_embeddings(data, **kwargs):
    return np.random.random((d, )).astype('float32')


def run():
    data_manager = get_data_manager("sqlite", "faiss", dimension=d)
    cache.init(embedding_func=mock_embeddings,
               data_manager=data_manager,
               similarity_evaluation=SearchDistanceEvaluation(),
               )
    cache.set_openai_key()

    answer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "what's chatgpt"}
        ],
    )
    print(answer)


if __name__ == '__main__':
    run()