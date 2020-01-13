import sys
import json
import requests
import datetime

class Slims():

    def __init__(self, url, username, pwd):
        self.url = url
        self.username = username
        self.pwd = pwd

    def get_attachment(self, proj, exp, step, attm, output):
        """Download a file from a slims experiment attachment step."""

        if output is None:
            output = attm

        project = requests.get(self.url + "/Project/advanced",
                             auth=(self.username, self.pwd),
                             headers={"Content-Type":"application/json"},
                             json={"criteria":{"operator":"and",
                                               "criteria":[
                                                   {"fieldName":"prjc_name",
                                               "operator":"equals",
                                               "value":proj},
                                                   {"fieldName":"user_userName",
                                               "operator":"equals",
                                               "value":self.username}
                                               ]}
                                  })
    
        if len(project.json()["entities"]) > 1:
            sys.exit("Multiple projects found for" + proj + ". Make sure projects names are unique.")

        experiment_run = requests.get(self.url + "/ExperimentRun/advanced",
                             auth=(self.username, self.pwd),
                             headers={"Content-Type":"application/json"},
                             json={"criteria":{"operator":"and",
                                               "criteria":[
                                                   {"fieldName":"xprn_fk_project",
                                               "operator":"equals",
                                               "value":project.json()["entities"][0]["pk"]},
                                                   {"fieldName":"xprn_name",
                                               "operator":"equals",
                                               "value":exp},
                                                   {"fieldName":"user_userName",
                                               "operator":"equals",
                                               "value":self.username}
                                               ]}
                                  })
    
        if len(experiment_run.json()["entities"]) > 1:
            sys.exit("Multiple experiments found for" + exp + ". Make sure experiments names are unique.")

        experiment_step = requests.get(self.url + "/ExperimentRunStep/advanced",
                             auth=(self.username, self.pwd),
                             headers={"Content-Type":"application/json"},
                             json={"criteria":{"operator":"and",
                                               "criteria":[
                                                   {"fieldName":"xprs_fk_experimentRun",
                                               "operator":"equals",
                                               "value": experiment_run.json()['entities'][0]['pk']},
                                                   {"fieldName":"xpst_type",
                                               "operator":"equals",
                                               "value": "ATTACHMENT_STEP"},
                                                   {"fieldName":"xpst_name",
                                               "operator":"equals",
                                               "value": step}
                                                          ]}
                                  })

        if len(experiment_step.json()["entities"]) > 1:
            sys.exit("Multiple steps found for" + exp + "/" + step + ". Make sure steps names are unique.")

        attachment = requests.get(self.url + "/Attachment/advanced",
                             auth=(self.username, self.pwd),
                             headers={"Content-Type":"application/json"},
                             json={"criteria":{"operator":"and",
                                               "criteria":[
                                                   {"fieldName":"attm_name",
                                               "operator":"equals",
                                               "value":attm},
                                                   {"fieldName":"user_userName",
                                               "operator":"equals",
                                               "value":self.username}
                                                          ]}
                                  })

        attachment = [[{"attm_file_filename":e1["value"], "pk":e0["pk"]} for e1 in e0["columns"] if e1["name"] == "attm_file_filename"][0] for e0 in attachment.json()["entities"]]

        attachment_link = requests.get(self.url + "/AttachmentLink/advanced",
                             auth=(self.username, self.pwd),
                             headers={"Content-Type":"application/json"},
                             json={"criteria":{"operator":"and",
                                               "criteria":[
                                                   {"fieldName":"atln_recordTable",
                                               "operator":"equals",
                                               "value":"ExperimentRunStep"},
                                                   {"fieldName":"atln_recordPk",
                                               "operator":"equals",
                                               "value":experiment_step.json()['entities'][0]['pk']}
                                                          ]}
                                  })

        attachment_link_pk = [e2[0] for e2 in [[e1["value"] for e1 in e0["columns"] if e1["name"] == "atln_fk_attachment" and (e1["value"] in [e2["pk"] for e2 in attachment])] for e0 in attachment_link.json()["entities"]] if e2]

        if len(attachment_link_pk) > 1:
            sys.exit("Multiple attachments found for " + attm + " in " + exp + "/" + step + ". Make sure attachments names are unique.")

        # Download the attachement
        with requests.get(self.url + "/repo/" + str(attachment_link_pk[0]),
                      auth=(self.username, self.pwd),
                      stream=True) as r:
            r.raise_for_status()
            with open(output, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

        # Save metadata
        metadata = {"url":self.url + "/repo/" + str(attachment_link_pk[0]),
            "creator":self.username,
            "project_name":proj,
            "experiment_name":exp,
            "step_name":step,
            "attachment_name":attm,
            "attachment_file_filename":[e["attm_file_filename"] for e in attachment if e["pk"] == attachment_link_pk[0]][0],
            "file_name":output,
            "created":datetime.datetime.now(datetime.timezone.utc).isoformat(sep='T')}

        with open(output + "_metadata.txt", "w") as f:
            json.dump(metadata, f, indent=2)
