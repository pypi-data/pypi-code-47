import io
import os
import pickle
import warnings

import lz4.frame
import minio

import upside_down_rl


class MinioSaver:
    def __init__(self, run_name):
        self.run_name = run_name

    def __call__(self, config: upside_down_rl.udrl.URLDConfig, model):
        if "MINIO_ACCESS_KEY" not in os.environ:
            msg = (
                "Could not save to minio, please add "
                "MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET, "
                "MINIO_HOST environment vars"
            )
            warnings.warn(msg)
            return
        access_key = os.environ["MINIO_ACCESS_KEY"]
        secret_key = os.environ["MINIO_SECRET_KEY"]
        bucket = os.environ["MINIO_BUCKET"]
        host = os.environ["MINIO_HOST"]

        client = minio.Minio(
            endpoint=host, access_key=access_key, secret_key=secret_key, secure=False
        )

        try:
            client.make_bucket(bucket)
        except minio.error.BucketAlreadyOwnedByYou:
            pass
        except minio.error.BucketAlreadyExists:
            pass

        with io.BytesIO() as output_io:
            pickle.dump(model, output_io)
            data = lz4.frame.compress(output_io.getvalue())
        fname = self.run_name + "/{}.pkl.lz4".format(config.global_step)
        with io.BytesIO(data) as res_io:
            client.put_object(bucket, fname, res_io, len(data))
