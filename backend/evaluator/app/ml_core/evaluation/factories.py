from app.ml_core.evaluation.similarity import calculate_cosine_similarity


class SimilarityFactory:

    _available_similarity_metrics = {"cosine_similarity": calculate_cosine_similarity}

    @classmethod
    def get_similarity_metric(cls, metric: str):
        """
        Returns the similarity metric function based on the metric name

        :param metric: The name of the metric
        :return: The similarity metric function
        """
        return cls._available_similarity_metrics[metric]
