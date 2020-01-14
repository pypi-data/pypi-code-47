import sys, datetime, os, json
import code_score

if __name__ == "__main__":

    try:
        data = os.environ.get('DORA_DATA', "/data")
        result_model = code_score.score(sys.argv[1:])
        timestamp = datetime.datetime.now()

        with open(os.path.join(data + "/", "output/", "result-" + timestamp.strftime("%m-%d-%Y-%H:%M:%S") + ".json"), "wb") as file:
            result = dict()
            result["statusCode"] = "success"
            result["result"] = result_model
            file.write(json.dumps(result).encode('utf8'))
            print("Please check your path result output for more details: " + str(file))

    except Exception as e:
        data = os.environ.get('DORA_DATA', "/data")
        error = str(e)
        timestamp = datetime.datetime.now()

        with open(os.path.join(data + "/", "error/", "error-" + timestamp.strftime("%m-%d-%Y-%H:%M:%S") + ".json"), "wb") as file:
            result = dict()
            result["statusCode"] = "error"
            result["result"] = error
            file.write(json.dumps(result).encode('utf8'))
            print("Please check your path error output for more details: " + str(file))

        print("Error: " + str(e))