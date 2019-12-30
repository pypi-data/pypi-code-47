import base64
import logging
import uuid
from pathlib import Path

from django.core.cache import cache
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from django_file_form import conf
from django_file_form.models import UploadedFile
from django_file_form.util import check_permission


logger = logging.getLogger(__name__)


class TusUpload(View):
    tus_api_version = '1.0.0'
    tus_api_version_supported = ['1.0.0', ]
    tus_api_extensions = ['creation', 'termination', 'file-check']

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        check_permission(self.request)

        override_method = self.request.META.get('HTTP_X_HTTP_METHOD_OVERRIDE', None)
        if override_method:
            self.request.method = override_method
        logger.info("TUS dispatch", extra={'requestMETA': self.request.META, "requestMethod": self.request.method})

        return super(TusUpload, self).dispatch(*args, **kwargs)

    def get_tus_response(self):
        response = HttpResponse()
        response['Tus-Resumable'] = self.tus_api_version
        response['Tus-Version'] = ",".join(self.tus_api_version_supported)
        response['Tus-Extension'] = ",".join(self.tus_api_extensions)
        response['Tus-Max-Size'] = conf.MAX_FILE_SIZE
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Methods'] = "PATCH,HEAD,GET,POST,OPTIONS"
        response['Access-Control-Expose-Headers'] = "Tus-Resumable,upload-length,upload-metadata,Location,Upload-Offset"
        response['Access-Control-Allow-Headers'] = "Tus-Resumable,upload-length,upload-metadata,Location,Upload-Offset,content-type"
        response['Cache-Control'] = 'no-store'

        return response

    def get(self, request, *args, **kwargs):
        metadata = {}
        response = self.get_tus_response()

        if request.META.get("HTTP_TUS_RESUMABLE", None) is None:
            return HttpResponse(status=405, content="Method Not Allowed")

        for kv in request.META.get("HTTP_UPLOAD_METADATA", None).split(","):
            (key, value) = kv.split(" ")
            metadata[key] = base64.b64decode(value)

        if metadata.get("filename", None) and metadata.get(
                "filename").upper() in [f.upper() for f in Path(conf.UPLOAD_DIR).iterdir()]:
            response['Tus-File-Name'] = metadata.get("filename")
            response['Tus-File-Exists'] = True
        else:
            response['Tus-File-Exists'] = False
        return response

    def options(self, request, *args, **kwargs):
        response = self.get_tus_response()
        response.status_code = 204
        return response

    def post(self, request, *args, **kwargs):
        response = self.get_tus_response()

        if request.META.get("HTTP_TUS_RESUMABLE", None) is None:
            logger.warning("Received File upload for unsupported file transfer protocol")
            response.status_code = 500
            response.reason_phrase = "Received File upload for unsupported file transfer protocol"

        if request.method == 'OPTIONS':
            response['Tus-Extension'] = ",".join(self.tus_api_extensions)
            response['Tus-Max-Size'] = conf.MAX_FILE_SIZE
            response.status_code = 204
            return response

        metadata = {}
        upload_metadata = request.META.get("HTTP_UPLOAD_METADATA", None)

        message_id = request.META.get("HTTP_MESSAGE_ID", None)
        if message_id:
            message_id = base64.b64decode(message_id)
            metadata["message_id"] = message_id
        logger.info("TUS Request", extra={'request': request.META})

        if upload_metadata:
            for kv in upload_metadata.split(","):
                (key, value) = kv.split(" ")
                metadata[key] = base64.b64decode(value).decode("utf-8")

        file_size = int(request.META.get("HTTP_UPLOAD_LENGTH", "0"))
        resource_id = str(uuid.uuid4())

        cache.add("tus-uploads/{}/filename".format(resource_id), metadata.get("filename"), conf.TIMEOUT)
        cache.add("tus-uploads/{}/file_size".format(resource_id), file_size, conf.TIMEOUT)
        cache.add("tus-uploads/{}/offset".format(resource_id), 0, conf.TIMEOUT)
        cache.add("tus-uploads/{}/metadata".format(resource_id), metadata, conf.TIMEOUT)

        try:
            with Path(conf.UPLOAD_DIR).joinpath(resource_id).open("wb") as f:
                pass
        except IOError as e:
            logger.error("Unable to create file: {}".format(e), exc_info=True, extra={
                'request': request,
            })
            response.status_code = 500
            return response

        response.status_code = 201
        response['Location'] = '{}{}'.format(request.build_absolute_uri(), resource_id)
        return response

    def head(self, request, *args, **kwargs):
        response = self.get_tus_response()
        resource_id = kwargs.get('resource_id', None)

        offset = cache.get("tus-uploads/{}/offset".format(resource_id))
        file_size = cache.get("tus-uploads/{}/file_size".format(resource_id))
        if offset is None:
            response.status_code = 404
            return response

        else:
            response.status_code = 200
            response['Upload-Offset'] = offset
            response['Upload-Length'] = file_size

        return response

    def patch(self, request, *args, **kwargs):
        response = self.get_tus_response()

        resource_id = kwargs.get('resource_id', None)

        filename = cache.get("tus-uploads/{}/filename".format(resource_id))
        file_size = int(cache.get("tus-uploads/{}/file_size".format(resource_id)))
        metadata = cache.get("tus-uploads/{}/metadata".format(resource_id))
        offset = cache.get("tus-uploads/{}/offset".format(resource_id))

        file_offset = int(request.META.get("HTTP_UPLOAD_OFFSET", 0))
        chunk_size = int(request.META.get("CONTENT_LENGTH", 102400))

        upload_file_path = Path(conf.UPLOAD_DIR).joinpath(resource_id)
        if filename is None or not upload_file_path.exists():
            response.status_code = 410
            return response

        if file_offset != offset:  # check to make sure we're in sync
            response.status_code = 409  # HTTP 409 Conflict
            return response

        logger.info("patch", extra={'request': self.request.META, 'tus': {
            "resource_id": resource_id,
            "filename": filename,
            "file_size": file_size,
            "metadata": metadata,
            "offset": offset,
            "upload_file_path": upload_file_path,
        }})

        file = None
        try:
            file = upload_file_path.open("r+b")
        except IOError:
            file = upload_file_path.open("wb")
        finally:
            if file:
                file.seek(file_offset)
                file.write(request.body)
                file.close()

        try:
            new_offset = cache.incr("tus-uploads/{}/offset".format(resource_id), chunk_size)
        except ValueError:
            response.status_code = 404
            return response

        response['Upload-Offset'] = new_offset

        response.status_code = 204

        if file_size == new_offset:
            self.remove_from_cache(resource_id)

            self.create_uploaded_file_in_db(
                field_name=metadata.get('fieldName'),
                file_id=resource_id,
                form_id=metadata.get('formId'),
                original_filename=metadata.get('filename'),
                uploaded_file=upload_file_path
            )

        return response

    def remove_from_cache(self, resource_id):
        cache.delete_many([
            "tus-uploads/{}/file_size".format(resource_id),
            "tus-uploads/{}/filename".format(resource_id),
            "tus-uploads/{}/offset".format(resource_id),
            "tus-uploads/{}/metadata".format(resource_id),
        ])

    def delete(self, request, *args, **kwargs):
        response = self.get_tus_response()
        resource_id = kwargs.get('resource_id', None)

        upload_file_path = Path(conf.UPLOAD_DIR).joinpath(resource_id)

        if upload_file_path.exists():
            upload_file_path.unlink()

        uploaded_file = UploadedFile.objects.try_get(file_id=resource_id)

        if uploaded_file:
            uploaded_file.delete()

        self.remove_from_cache(resource_id)

        response.status_code = 204 if uploaded_file else 404
        return response

    def create_uploaded_file_in_db(self, field_name, file_id, form_id, original_filename, uploaded_file):
        values = dict(
            file_id=file_id,
            form_id=form_id,
            uploaded_file=str(uploaded_file),
            original_filename=original_filename
        )

        if field_name:
            values['field_name'] = field_name

        UploadedFile.objects.create(**values)
