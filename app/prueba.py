import pandas as pd
import utils
from google.cloud import storage

# utils.autenticar()

# df_chile = carga.get_chile_limpio()
df_japon = utils.get_japon_limpio()
# df_eeuu = carga.get_eeuu_limpio()

print(df_japon.head(5))


def download_blob_into_memory(bucket_name, blob_name):
    """Downloads a blob into memory."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(blob_name)
    contents = blob.download_as_string()

    print(
        "Downloaded storage object {} from bucket {} as the following string: {}.".format(
            blob_name, bucket_name, contents
        )
    )


# download_blob_into_memory('buket-geodata', 'datos_japon_etl.json')
