import requests
import json
import schedule
import time
import datetime

import logging
logging.basicConfig(filename="./log/status_logger.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(message)s')


def load_conf(file):
    logging.debug("Loading configuration")
    json_file = open(file)
    config_json = json.load(json_file)

    conf = {"url": config_json["url"], "accesskey": config_json["accesskey"]}
    logging.debug("Configuration:")
    logging.debug(conf)
    return conf


def write_json(data, time):
    logging.debug("Writing data to file")

    json_data = {}
    for user in data:
        for key, value in user.items():
            if key == 'status_id':
                if value in json_data:
                    json_data[value] += 1
                else:
                    json_data[value] = 1
    logging.debug("JSON Data: " + str(json_data))

    x = datetime.datetime.now()
    with open("./out/" + x.strftime("%d-%m-%Y") + "_" + time + ".json", "w") as outfile:
        json.dump(json_data, outfile)

    logging.debug("Writing finished")


def call_api(time, tries=None):
    if tries is None:
        tries = 1
        logging.debug("Calling api")
    else:
        logging.debug("Calling api at try " + str(tries))

    response = requests.get(config["url"] + config["accesskey"])
    data = json.loads(response.text)

    if data["success"]:
        logging.debug("Code: " + str(response.status_code))
        logging.debug("Call successfull")
        write_json(data["data"], time)
    elif tries <= 5:
        logging.debug("Code: " + str(response.status_code))
        logging.debug("Call failed, retry")
        call_api(time, tries+1)
    else:
        logging.debug("Code: " + str(response.status_code))
        logging.debug("Call failed for the 5th time, aborting")


schedule.every().day.at("00:00").do(call_api, "00")
schedule.every().day.at("08:00").do(call_api, "08")
schedule.every().day.at("12:00").do(call_api, "12")
schedule.every().day.at("16:00").do(call_api, "16")
schedule.every().day.at("20:00").do(call_api, "20")


def main():
    logging.debug("Logging started")
    global config
    config = load_conf('config.json')
    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()