    @staticmethod
    def margin_of_error(prop, nsamples):
        return 1.96 * math.sqrt(prop * (1-prop) / nsamples)


    # Update margins of error.
                if False:
                    if total_cpu_samples != 0 and n_cpu_samples != 0:
                        moe_cpu = scalene.margin_of_error(n_cpu_samples / total_cpu_samples, total_cpu_samples)
                        max_moe_cpu = max(moe_cpu, max_moe_cpu)
