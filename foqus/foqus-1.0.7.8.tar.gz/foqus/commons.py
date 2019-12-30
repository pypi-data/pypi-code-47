import uuid
from decimal import *
from multiprocessing.pool import ThreadPool, TimeoutError
from os import listdir
from os.path import isfile, join

import urllib.request


from PIL import Image
from keras.preprocessing import image
from foqus.azure_configuration import *
from foqus.aws_configuration import *
from foqus.configuration import *
from foqus.customers import create_or_update_user_apikey

import logging
import coloredlogs
from ip2geotools.databases.noncommercial import DbIpCity
import os, time, datetime, calendar, hashlib, xlrd, csv, inspect, requests

AWS_ACCESS_KEY = AWS_KEY_ID
AWS_ACCESS_SECRET = AWS_SECRET_KEY

if USE_LOG_AZURE:

    from azure_storage_logging.handlers import TableStorageHandler
    # configure the handler and add it to the logger
    logger = logging.getLogger(__name__)
    handler = TableStorageHandler(account_name=LOG_AZURE_ACCOUNT_NAME,
                                  account_key=LOG_AZURE_ACCOUNT_KEY,
                                  extra_properties=('%(hostname)s',
                                                    '%(levelname)s'))
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
else:

    logger = logging.getLogger(__name__)
    coloredlogs.install()
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(LOG_PATH + 'trynfit_debug.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s', '%d/%b/%Y %H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)


class MultiTaskPool:
    def __init__(self):
        self.pool = ThreadPool(processes=MAX_ALLOWED_THREADS)
        self.async_results = []
        return

    def push_thread(self, thread, args):
        self.async_results.append(
            self.pool.apply_async(func=thread, args=args))

        return self.get_tasks_count() - 1

    def pop_thread(self, index):
        try:
            response = self.async_results[index].get(timeout=THREAD_RESPONSE_TIMEOUT_IN_SECONDS)
            del self.async_results[index]
            logger.info("Removing thread index: " + str(index))
        except TimeoutError:
            logger.warning("Thread still running! Index: " + str(index))
            response = None
        except:
            response = None
        return response

    def get_tasks_count(self):
        return len(self.async_results)

    def clean_pool(self):
        for i in range(self.get_tasks_count()):
            self.pop_thread(i)


def update_the_database(db, filename):

    try:
        url = db.get_url_from_hash(hash=filename.split("/")[-1])
        db.create_history_table(table_name=filename.split('/')[-3])
        db.create_or_update_history(table_name=filename.split('/')[-3], url=url)
        db.delete_hash(hash=filename.split('/')[-1])
        db.delete_smilitaries(table_name=filename.split('/')[-3], url=url)
        logger.info("Successfully updated database  ")

    except Exception as e:
        logger.error("Erreur updating the database ... (%s) " % e)


def ping(hostname="127.0.0.1", port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((hostname, port))
        logger.info("Target reachable")
        result = True
    except socket.error as e:
        logger.error("Error on connect: %s" % e)
        result = False
    s.close()
    return result


def download(url, filename):
    # As long as the file is opened in binary mode, both Python 2 and Python 3
    # can write response body to it without decoding.
    try:
        urllib.request.urlretrieve(url.replace(' ', '+'), filename)
    except Exception as e:
        logger.error("Error when downloading/writing file %s error %s ..." %(filename, e) )


def remove(db, filename):
    update_the_database(db, filename)
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return 0
        else:
            logger.info("File doesn't exist... Nothing to remove")
            return -1
    except:
        logger.error("Error when removing file '" + filename + "'...")
        return -1


def get_file_hash(filename):
    hash_result = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_result.update(chunk)
    return hash_result.hexdigest()


def get_remote_file_hash(url, max_file_size=100 * 1024 * 1024):
    try:
        temporary_file = '/tmp/' + str(uuid.uuid4())
        download(url, temporary_file)
        file_hash = get_file_hash(temporary_file)
        os.remove(temporary_file)
        return file_hash
    except:
        logger.error("Error when trying to calculate REMOTE file hash")
        return None


def image_extension(image_url):
    r = requests.head(image_url)
    if (r.headers["content-type"]):
        return (r.headers["content-type"].split('/')[1])
    else:
        return image_url.split('.')[-1]

def download_or_remove(urls, each_url_product, download_operation=1, customer_name=None, customer_type=None,
                       db=None, path_out=None, project_name=None):
    if customer_name is None or customer_type is None or db is None:
        logger.error("Cannot download image: missing parameters")
        return

    if path_out is None:
        path_out = INPUT_PATH + customer_type + '/' + customer_name + '/images/' + project_name
    input_s3 = INPUT_S3 + customer_type + '/' + customer_name + '/images/' + project_name + '/'
    input_azure = AZURE_INPUT_PATH + customer_type + "/" + customer_name + "/images/" + project_name + '/'
    resized_path = OUTPUT_PATH + customer_type + '/' + customer_name + '/images' + project_name + '/'
    output_3 = OUTPUT_S3 + customer_type + '/' + customer_name + '/images/' + project_name + '/'
    hash_files = ""
    for url in urls.split(' '):
        hash_file = get_remote_file_hash(url)
        if ('.jpg' in url) or ('.JPG' in url):
            filename = hash_file + ".jpg"
        elif ('.png' in url) or ('.PNG' in url):
            filename = hash_file + ".png"
        elif ('.jpeg' in url) or ('.JPEG' in url):
            filename = hash_file + ".jpeg"
        else:
            filename = hash_file
        fichier = path_out + '/' + filename
        resized_fichier = resized_path + '/' + filename

        logger.info("Retrieving image from URL...")

        logger.info("Image URL: " + url)
        if download_operation == 1:
            db.create_client_products_table(customer_name.replace(' ', '_'))

            if os.path.exists(fichier) and os.stat(fichier).st_size == 0:
                logger.info("File exists but size is 0... Download again!")
                download(url, fichier)
            elif not os.path.exists(fichier):
                logger.info("File doesn't exist... Downloading...")
                download(url, fichier)
            else:
                logger.info("File exists and not empty... Ignoring download.")

            if os.path.exists(fichier) and os.stat(fichier).st_size == 0:
                logger.info("File exists but size is 0... Download again!")
                download(url, fichier)
            elif not os.path.exists(fichier):
                logger.info("File doesn't exist... Downloading...")
                download(url, fichier)
            else:
                logger.info("File downloaded successfully.")

            if USE_AWS:
                upload_file_into_s3(fichier, input_s3 + fichier.split('/')[-2] + '/')
            retries = 0
            while get_file_hash(fichier) != hash_file and retries < MAX_DOWNLOAD_FILE_RETRIES:
                logger.warning("File exists but hash is incorrect... Download again!")
                hash_file = get_remote_file_hash(url)
                download(url, fichier)
                if USE_AWS:
                    upload_file_into_s3(fichier, input_s3 + fichier.split('/')[-2] + '/')
                retries += 1

            if get_file_hash(fichier) != hash_file:
                logger.error("File wasn't downloaded correctly! " + fichier)
            else:
                logger.info("File was successfully downloaded (hash OK) >>> File path: " + fichier)

            hash_files = hash_files + filename + " "
            if USE_AZURE:
                if fichier.split('/')[-2] == project_name:
                    upload_folder_into_azure(
                        local_path=path_out,
                        directory_path=input_azure)

                else:
                    upload_folder_into_azure(local_path=path_out,
                                             directory_path=input_azure + fichier.split('/')[-2])
        else:
            if remove(db, resized_fichier) == 0 and delete_from_s3(
                                            output_3 + fichier.split('/')[-2] + '/' + filename) == 0:
                logger.info("Obsolete ad... Removing file from Output local and S3")
            if remove(db, fichier) == 0 and delete_from_s3(input_s3 + fichier.split('/')[-2] + '/' + filename) == 0:
                logger.info("Obsolete ad... Removing file from Input local and S3")

    data_product = db.get_product_details(customer_name.replace(' ', '_'), each_url_product, project_name)

    if data_product:
        urls_base = data_product[1]
        hash_base = data_product[3]
        urls_references_base = data_product[1].split(' ')
        hash_references_base = data_product[3].split(' ')
        urls_references = urls.split(' ')
        hash_references = hash_files.split(' ')
        # hash_references = list(dict.fromkeys(hash_references))
        for i in range(0, len(urls_references)-1):
            for j in range(0, len(urls_references_base)-1):
                print("url reference, url base  1")
                print(urls_references[i], urls_references_base[j])
                if urls_references[i] == urls_references_base[j]:
                    if hash_references[i] != hash_references_base[j]:
                        print("hash reference, hash base n 1")
                        print(hash_references[i], hash_references_base[j])
                        # urls_base.replace(urls_references_base[j], urls_references[i])
                        hash_base.replace(hash_references_base[j], hash_references[j])
        # Url image has been changed
        for i in range(0, len(hash_references) - 1):
            for j in range(0, len(hash_references_base) - 1):
                if hash_references[i] not in hash_references_base:
                    hash_references_base.append(hash_references[i])
                    urls_base = urls + urls_references_base[j] + " "
                if hash_references[i] == hash_references_base[j]:
                    if urls_references[i] != urls_references_base[j]:
                        urls.replace(urls_references_base[j], urls_references[i])

    if each_url_product == '':
        db.add_or_update_images(table_name=customer_name.replace(' ', '_'), reference=urls, urlProduit="", hash_code=hash_files,
                                 project_name=project_name)
    else:
        db.add_or_update_products(table_name=customer_name.replace(' ', '_'), reference=urls, urlProduit=each_url_product,
                                   hash_code=hash_files, project_name=project_name, update=data_product)


# hash with the url image
def download_or_remove_new(url, each_url_product, download_operation=1, customer_name=None, customer_type=None, db=None, path_out=None, project_name = None, count=None, rest_photos=None , itr= None , nb_iteration = None):
    if customer_name is None or customer_type is None or db is None:
        logger.error("Cannot download image: missing parameters")
        return

    if path_out is None:
        path_out = INPUT_PATH + customer_type + '/' + customer_name + '/images/' + project_name
    input_s3 = INPUT_S3 + customer_type + '/' + customer_name + '/images/' +project_name + '/'
    input_azure = AZURE_INPUT_PATH + customer_type + "/" + customer_name + "/images/" + project_name + '/'
    resized_path = OUTPUT_PATH + customer_type + '/' + customer_name + '/images' + project_name + '/'
    output_3 = OUTPUT_S3 + customer_type + '/' + customer_name + '/images/'+ project_name + '/'

    hash_file= str(uuid.uuid3(uuid.NAMESPACE_URL, url.split('?')[0]))
    filename = hash_file + "." + image_extension(url)
    fichier = path_out + '/' + filename
    resized_fichier = resized_path + '/' + filename

    logger.info("Retrieving image from URL...")

    logger.info("Image URL: " + url)
    if download_operation == 1:
        if os.path.exists(fichier) and os.stat(fichier).st_size == 0:
            logger.info("File exists but size is 0... Download again!")
            download(url, fichier)
        elif not os.path.exists(fichier):
            logger.info("File doesn't exist... Downloading...")
            download(url, fichier)
        else:
            logger.info("File exists and not empty... Ignoring download.")

        if os.path.exists(fichier) and os.stat(fichier).st_size == 0:
            logger.info("File exists but size is 0... Download again!")
            download(url, fichier)
        elif not os.path.exists(fichier):
            logger.info("File doesn't exist... Downloading...")
            download(url, fichier)
        else:
            logger.info("File downloaded successfully.")

        if USE_AWS:
            upload_file_into_s3(fichier, input_s3 + fichier.split('/')[-2] + '/')
        retries = 0
        while get_file_hash(fichier) != hash_file and retries < MAX_DOWNLOAD_FILE_RETRIES:
            logger.warning("File exists but hash is incorrect... Download again!")
            hash_file = get_remote_file_hash(url)
            if ('.jpg' in url) or ('.JPG' in url):
                filename = hash_file + ".jpg"
            elif ('.png' in url) or ('.PNG' in url):
                filename = hash_file + ".png"
            elif ('.jpeg' in url) or ('.JPEG' in url):
                filename = hash_file + ".jpeg"
            else:
                filename = hash_file


            hash_file = get_remote_file_hash(url)
            download(url, fichier)
            if USE_AWS:
                upload_file_into_s3(fichier, input_s3 + fichier.split('/')[-2] + '/')
            retries += 1

        if get_file_hash(fichier) != hash_file:
            logger.error("File wasn't downloaded correctly! " + fichier)
        else:
            logger.info("File was successfully downloaded (hash OK) >>> File path: " + fichier)

            db.add_or_update_url_hash(url=url,
                                      hash=filename)

            db.create_client_products_table(customer_name.replace(' ', '_'))
            db.add_or_update_products(table_name=customer_name.replace(' ', '_'), reference=url, urlProduit=each_url_product, count = count, rest_photos=rest_photos, itr = itr, nb_iteration= nb_iteration)

        #upload input directory in azure
        if USE_AZURE:
            if fichier.split('/')[-2] == project_name:
                upload_folder_into_azure(
                    local_path=path_out,
                    directory_path=input_azure)

            else:
                upload_folder_into_azure(local_path=path_out,
                                         directory_path=input_azure + fichier.split('/')[-2])

    else:
        if remove(db, resized_fichier) == 0 and delete_from_s3(output_3 + fichier.split('/')[-2]+ '/' + filename) == 0:
            logger.info("Obsolete ad... Removing file from Output local and S3")
        if remove(db, fichier) == 0 and delete_from_s3(input_s3 + fichier.split('/')[-2] + '/' + filename) == 0:
            logger.info("Obsolete ad... Removing file from Input local and S3")


def safe_download(url, file_path):
    hash_file = get_remote_file_hash(url)
    if hash_file is None:
        logger.error("hash file is none ")

    logger.info("Retrieving file from URL...")
    logger.info("File URL: " + url)
    if os.path.exists(file_path) and os.stat(file_path).st_size == 0:
        logger.info("File exists but size is 0... Download again!")
        download(url, file_path)
    elif not os.path.exists(file_path):
        logger.info("File doesn't exist... Downloading...")
        download(url, file_path)
    else:
        logger.info("File exists and not empty... Ignoring download.")

    if os.path.exists(file_path) and os.stat(file_path).st_size == 0:
        logger.info("File exists but size is 0... Download again!")
        download(url, file_path)
    elif not os.path.exists(file_path):
        logger.info("File doesn't exist... Downloading...")
        download(url, file_path)
    else:
        logger.info("File downloaded successfully.")

    retries = 0
    while get_file_hash(file_path) != hash_file and retries < MAX_DOWNLOAD_FILE_RETRIES:
        logger.warning("File exists but hash is incorrect... Download again!")
        hash_file = get_remote_file_hash(url)
        download(url, file_path)
        retries += 1

    if get_file_hash(file_path) != hash_file:
        logger.error("File wasn't downloaded correctly! " + file_path)
    else:
        logger.info("File was successfully downloaded (hash OK) >>> File path: " + file_path)


def resize_images(target=TARGET_RESOLUTION, customer_name=None, customer_type=None,project_name=None):

    if customer_name is None or customer_type is None:
        logger.error("Customer name and type must be provided")
        return
    input_path = INPUT_PATH + customer_type + '/' + customer_name + '/images/'+ project_name

    resized_path = OUTPUT_PATH + customer_type + '/' + customer_name + '/images/'+ project_name
    resized_paths3 = OUTPUT_S3 + customer_type + '/' + customer_name + '/images/'+project_name + '/'

    if not os.path.isdir(resized_path):
        try:
            os.makedirs(resized_path)
        except:
            logger.error("Cannot create output directory for customer. "
                         "Please verify permissions or change the path in your '")
            return

    folders = list(filter(lambda x: os.path.isdir(os.path.join(input_path, x)), os.listdir(input_path)))

    if folders != []:
        for folder in folders:
            input_path = INPUT_PATH + customer_type + '/' + customer_name + '/images/' + project_name+ '/' + folder
            resized_path = OUTPUT_PATH + customer_type + '/' + customer_name + '/images/'+ project_name+ '/' + folder
            if not os.path.isdir(input_path):
                try:
                    os.makedirs(input_path)
                except:
                    logger.error("Cannot create output directory for customer. "
                                 "Please verify permissions or change the path in your '")
                    return
            if not os.path.isdir(resized_path):
                try:
                    os.makedirs(resized_path)
                except:
                    logger.error("Cannot create output directory for customer. "
                                 "Please verify permissions or change the path in your '")
                    return

            image_files = [f for f in listdir(input_path) if
                           isfile(join(input_path, f)) and (f.endswith("G") or f.endswith("g"))]

            resizing_image(image_files, input_path, target, resized_path, resized_paths3 + folder + '/')

            logger.info('Resizing images in directory %s' %folder)
    else:
        image_files = [f for f in listdir(input_path) if
                       isfile(join(input_path, f)) and (f.endswith("G") or f.endswith("g"))]
        resizing_image(image_files, input_path, target, resized_path, resized_paths3)

    logger.info("All downloaded images are successfully resized")


def resizing_image(image_files, input_path, target ,resized_path, resized_paths3):

    for im in image_files:
        try:
            im1 = Image.open(join(input_path, im))
            original_width, original_height = im1.size
            ratio = Decimal(original_width) / Decimal(original_height)
            if ratio > 1:
                width = target
                height = int(width / ratio)
            else:
                height = target
                width = int(height * ratio)
            testing_images_to_resize = resized_path + "/" + im

            if (not os.path.exists(testing_images_to_resize)) or (os.stat(testing_images_to_resize).st_size == 0):
                logger.info("Resizing image " + join(input_path, im) + "...")
                im2 = im1.resize((width, height), Image.ANTIALIAS)  # linear interpolation in a 2x2 environment
                im2.save(resized_path + "/" + im)
            else:
                logger.info("Image " + join(input_path, im) + " already resized.")
                pass
            if USE_AWS:
                upload_file_into_s3(resized_path + "/" + im, resized_paths3)
        except Exception as e:
            logger.error("Error when resizing image '" + im + "'..." + str(e))
    if USE_AZURE:
        upload_folder_into_azure(local_path=resized_path,directory_path=resized_paths3.split('BACKUP/')[1])
    logger.info("All downloaded images are successfully resized")


def open_img(path):
    if not path.lower().endswith(('.png', '.jpg', '.jpeg')):
        return None
    return image.load_img(path, target_size=(244, 244))


def load_image(resized_filename):
    '''
    :param resized_filename: image to load
    :return: loaded image
    '''

    try:
        img = open_img(resized_filename)
        img = img.astype('float32')
        return img
    except Exception as e:
        logger.error('Exception in loading image %s, error %s' %(resized_filename, e))


def get_client_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except Exception as e:
        ip = request.environ.get('REMOTE_ADDR')
    return ip


def get_client_code_country(adress):
    if adress == "":
        code_country = ""
    elif adress == "127.0.0.1" or "192.168.100" in adress:
        code_country = "FR"
    else:
        response = DbIpCity.get(adress, api_key='free')
        code_country = response.country
        code_country =code_country.lower()
        logger.info(" The code country is %s" %code_country)
    return code_country


def get_client_country(adress):
    if adress == "":
        country = ""
    elif adress == "127.0.0.1" or "192.168.100" in adress:
        country = "France"
    else:
        response = DbIpCity.get(adress, api_key='free')
        country = response.city
        logger.info(" The code country is %s" %country)
    return country


def compact(*names):
    caller = inspect.stack()[1][0] # caller of compact()
    vars = {}
    for n in names:
        if n in caller.f_locals:
            vars[n] = caller.f_locals[n]
        elif n in caller.f_globals:
            vars[n] = caller.f_globals[n]
    return vars


def date_gmdate(str_formate, int_timestamp=None):
    if int_timestamp == None:
        return time.strftime(str_formate, time.gmtime())
    else:
        return time.strftime(str_formate, time.gmtime(int_timestamp))


def get_api_version_shopify():
    from datetime import date
    year = date.today().strftime("%Y")
    month = date.today().strftime("%m")
    if month not in ['01', '04', '07', '10']:

        if int(month) > 10:
            api_version = year + '-10'
        elif int(month) > 7:
            api_version = year + '-07'
        elif int(month) > 4:
            api_version = year + '-04'
        else:
            api_version = year + '-01'
    else:
        api_version = year + '-' + month
    return api_version


def excel_valid(excel_path=None, customer_name=None,customer_type= None, customer_universe= None):
    try:
        if not os.path.isdir(STREAMS_PATH + customer_type + '/' + customer_name + '/detection_erreur/' + customer_universe):
            try:

                os.makedirs(STREAMS_PATH + customer_type + '/' + customer_name + '/detection_erreur/' + customer_universe)
            except:
                logger.error("Cannot create streams directory for customer. Please verify permissions or change "
                             "the path in your 'config.ini'")
                pass
        path_excel_download = STREAMS_PATH + customer_type + '/' + customer_name + '/detection_erreur/' + customer_universe + '/' + \
                              excel_path.split('/')[-1].split('.xlsx')[0] + '.xlsx'
        if '://' in excel_path:
            download(excel_path, path_excel_download)

        if path_excel_download is None or customer_name is None:
            logger.error("Corrupted Excel")
            return False
        if str(path_excel_download).endswith('.xlsx'):
            workbook = xlrd.open_workbook(path_excel_download)
            sheet = workbook.sheet_by_name(workbook.sheet_names()[0])
            nRows = sheet.nrows

        elif str(path_excel_download).endswith('.csv'):
            # workbook =  open(excel_path, 'rb')
            workbook = open(excel_path,  "rt")
            records = csv.reader(workbook)
            sheet = []
            for index, line in enumerate(records):
                sheet.append(line)
            nRows = len(sheet)
        for i in range(0, nRows):
            try:
                row_values = sheet.row_values(i)

                try:
                    customer_universe_file = str(int(row_values[6])).replace(' ', '')
                except:
                    customer_universe_file = str(row_values[6]).replace(' ', '')

                if customer_universe != customer_universe_file:
                    logger.error("*********Verify your customer_universe in your excel file**********")
                    return False
            except Exception as e:
                row_values = sheet[i]

                try:
                    customer_universe_file = str(int(row_values[6])).replace(' ', '')
                except:
                    customer_universe_file = str(row_values[6]).replace(' ', '')

                if customer_universe != customer_universe_file:
                    logger.error("*********Verify your customer_universe in your CSV file**********")
                    return False
        return True
    except Exception as e:
        logger.error(e)
        return False


def get_valid_post(customer, customer_type):
    year = datetime.datetime.today().strftime("%Y")
    month = datetime.datetime.today().strftime("%m")
    logger.info('counter for client %s for year %s and month %s' % (customer, year, month))
    last_day = calendar.monthrange(int(year), int(month))[1]
    date_start = "%s-%s-01" % (year, month)
    date_fin = "%s-%s-%s" % (year, month, last_day)
    post_counter = db.get_counter_post(customer, customer_type, date_start, date_fin)[0]
    if not post_counter:
        post_counter = 0
    plan_client = db.get_client_payment(customer, customer_type)[5]
    max_post = db.max_post(plan_client)[0]
    return max_post < post_counter


def max_number_product_exceeded(customer_name, customer_type, body):
    try:
        payment = db.get_client_payment(customer_name, customer_type)
        plan_name = payment[5]
        plan = db.get_plan_form_name(plan_name)
        max_number_training_image = int(plan[4])
        somme = 0
        for category in body.json()[customer_name + '_' + customer_type]:
            somme += len(category['Photos'])
        logger.info("products count %s for file %s client %s type %s" % (somme, body, customer_name, customer_type))
        if somme > max_number_training_image:
            return True
        else:
            return False
    except Exception as e:
        logger.error("error in getting products count for client %s with type %s file %s error %s"
                     % (customer_name, customer_type, body, e))
        return False


def add_max_post():
    for plan in db.get_all_plans_payement("plan"):
        if plan[3] == "FREE":
            db.update_max_number_post(100, "FREE")
        elif plan[3] == "PRO":
            db.update_max_number_post(5000, "PRO")
        else:
            db.update_max_number_post(10000, plan[3])


def products_related_data(url_images, url_produits, each_picture, each_url_product, path, status,
                          customer_name, customer_type, project_name):
    if each_url_product != '' and each_url_product in url_produits.keys():
        reference = url_produits[each_url_product]['images']
        new_reference = reference + " " + each_picture
        url_produits[each_url_product] = {"images": new_reference,
                                          "path": path, "status": status,
                                          "customer_name": customer_name,
                                          "customer_type": customer_type,
                                          "project_name": project_name}
    elif each_url_product != '':
        url_produits[each_url_product] = {"images": each_picture,
                                          "path": path, "status": status,
                                          "customer_name": customer_name,
                                          "customer_type": customer_type,
                                          "project_name": project_name}
    else:
        url_images.append({"images": each_picture,
                           "path": path, "status": status,
                           "customer_name": customer_name,
                           "customer_type": customer_type,
                           "project_name": project_name})


def download_commit_db_images(count, itr, nb_iteration, rest_photos, url_images, url_produits):
    if count == 100:
        count = 0
        itr += 1
        if url_images:
            for image in url_images:
                download_or_remove(image['images'], "", image['status'], image["customer_name"],
                                   image['customer_type'], db, image['path'],
                                   image['project_name'])
        else:
            for product in url_produits.keys():
                download_or_remove(url_produits[product]['images'], product, url_produits[product]['status'],
                                   url_produits[product]["customer_name"],
                                   url_produits[product]['customer_type'], db, url_produits[product]['path'],
                                   url_produits[product]['project_name'])

        db.commit_db_changes()
        logger.info("Data commited into table client successfully")
    if count == rest_photos and itr == nb_iteration + 1:
        if url_images:
            for image in url_images:
                download_or_remove(image['images'], "", image['status'],
                                   image["customer_name"],
                                   image['customer_type'], db, image['path'],
                                   image['project_name'])
        else:
            try:
                for product in url_produits.keys():
                    download_or_remove(url_produits[product]['images'], product, url_produits[product]['status'],
                                       url_produits[product]["customer_name"],
                                       url_produits[product]['customer_type'], db, url_produits[product]['path'],
                                       url_produits[product]['project_name'])
            except Exception as e:
                logger.error('Error_download_commit_db_images: %s ' % e)
        db.commit_db_changes()
        logger.info("Rest of data commited into table  successfully")


def get_payment_details_cms_shopify(customer_name, customer_type, domain, access_token):
    try:
        logger.info('access_token for client with domain %s is %s' % (domain, access_token))
        headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json"
        }
        api_version = get_api_version_shopify()
        endpoint = "/admin/api/%s/recurring_application_charges.json" % api_version
        response = requests.get("https://{0}{1}".format(domain,
                                                        endpoint), headers=headers)
        if response.status_code == 200:
            data_retreived = json.loads(response.text)
            for payment in data_retreived['recurring_application_charges']:
                if payment['status'] == "active":
                    payment_client = db.get_client_payment(customer_name, customer_type)
                    db.update_client_payement(customer_name, customer_type, payment_client[11], payment['name'], 1,
                                              "paypal", float(payment["price"]) * 11)
                    db.update_transction_id(customer_name, customer_type, payment["id"], payment['name'],
                                            payment_client[11], 'paypal')
                    create_or_update_user_apikey(user=customer_name, period_in_hours=8040)
                    return True
    except Exception as e:
        logger.error("Payment shopify error")
        return False


def get_count_product_validation(token, url_shop, plan):
    api_version = get_api_version_shopify()
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    count_point = "/admin/api/%s/products/count.json" % api_version

    count_products = requests.get("https://{0}{1}".format(url_shop, count_point), headers=headers)
    count_json = json.loads(count_products.text)
    counter = int(count_json['count'])
    max_images_training = db.get_plan_form_name(plan)[4]

    if counter > max_images_training:
        return False
    else:
        return True