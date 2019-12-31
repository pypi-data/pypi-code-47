from runner.job import JobFactory, JobProcess, JobDockerProcess
from toil.common import Toil
from toil.job import Job


class mapping():

    __metaclass__ = JobFactory

    def __init__(self, ref, r1, r2, output, n_threads, *args, **kwargs):

        self.command_str = """ bash -c "bwa mem -t {n_threads} {ref}\
           {r1} {r2} -o {output}" """.format(ref=ref,
                                             r1=r1,
                                             r2=r2,
                                             n_threads=n_threads,
                                             output=output)
        super(mapping, self).__init__(image='gmap:license1.0',
                                      network_mode='host',
                                      ipc='host',
                                      volumes={
                                          "/mnt": {
                                              "bind": "/mnt",
                                              "mode": "rw"
                                          },
                                          "/Genowis": {
                                              "bind": "/Genowis",
                                              "mode": "rw"
                                          }
                                      },
                                      *args,
                                      **kwargs)

    def pre_process(self):
        pass

    def post_process(self):
        pass

    def get_command_line(self):
        return self.command_str


if __name__ == "__main__":
    options = Job.Runner.getDefaultOptions('/mnt/sdb/yinlh/umi/jobstore')
    options.jobname = 'mapping'
    options.clean = 'always'
    job = mapping(
        ref='/mnt/sdb/yinlh/ref/human.fa',
        r1='/mnt/sdb/yinlh/bwa_sim/sim_1M_150bp.bwa.read1.fastq.gz',
        r2='/mnt/sdb/yinlh/bwa_sim/sim_1M_150bp.bwa.read2.fastq.gz',
        output='/mnt/sdb/yinlh/bwa_sim/sim_1M_150bp.bwa.read1.fastq.bam',
        n_threads=20,
        cores=20,
        memory='8G')

    with Toil(options) as toil:
        if not toil.options.restart:
            toil.start(job)
        else:
            toil.restart()