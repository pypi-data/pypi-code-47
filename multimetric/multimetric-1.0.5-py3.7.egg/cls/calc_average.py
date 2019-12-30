from multimetric.cls.metric import AverageMetric
import statistics


class Average(AverageMetric):

    def __init__(self, args):
        super().__init__(args)

    def get_results(self, metrics, files="files", overall="overall"):
        print("def")
        for k in metrics[overall].keys():
            print("abc")
            metrics[overall]["mean_{}".format(k)] = statistics.mean([v[k] for x,v in metrics[files].items() if not isinstance(v[k], list)])
            metrics[overall]["sd_{}".format(k)] = statistics.stdev([v[k] for x,v in metrics[files].items() if not isinstance(v[k], list)])
            metrics[overall]["median_{}".format(k)] = statistics.median([v[k] for x,v in metrics[files].items() if not isinstance(v[k], list)])
        return super().get_results(metrics, files="files", overall="overall")
