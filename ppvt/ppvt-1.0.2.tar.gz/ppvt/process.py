import csv

from .version_checker import Pypi


class ProcessInput:
    def __init__(self, in_f, out_f, package, all_versions, l_version, gt_versions):
        self.pypi = Pypi()
        self.in_f = in_f
        self.package = package
        self.all_versions = all_versions
        self.l_version = l_version
        self.gt_versions = gt_versions
        self.out_f = out_f
        self.process()

    def process(self):
        if self.out_f:
            self.create_csv()

        if self.package:
            self.handle_package(self.package)

        if self.in_f:
            self.handle_file(self.in_f)

        return

    def create_csv(self):
        self.csv_file = open(self.out_f, "w")
        self.csv = csv.writer(self.csv_file)
        self.csv.writerow(["package", "version", "python_version"])

    def handle_package(self, package):
        resp, package, version = self._handle_package(package)
        for rec in resp:
            self.handle_output([package, rec["version"], rec["python_version"]])

    def _handle_package(self, package):
        """
        handle package version as well.
        """

        package = package.strip()
        s_package = package.split("==")
        version = 0
        if len(s_package) == 2:
            package, version = s_package
        else:
            package, version = package, version

        resp = self.pypi.get(package)
        if resp["status"] == "failure":
            return (
                [dict(version=None, python_version=None)],
                "No package found with name " + package,
                None,
            )

        data = resp["releases"]
        if self.all_versions:
            resp = self.pypi.all(data)
        elif self.gt_versions:
            resp = self.pypi.greater(data, str(version))
        elif self.l_version:
            resp = self.pypi.latest(data)

        return resp, package, version

    def write_to_csv(self, data):
        """
        write data into csv file
        """
        self.csv.writerow(data)
        self.csv_file.flush()

        return

    def handle_file(self, file_name):
        """
        handle file data
        """
        f_obj = open(file_name)
        for rec in f_obj:
            self.handle_package(rec)

    def handle_output(self, data):
        """
        handle sysout and write to csv
        """
        if self.out_f:
            self.write_to_csv(data)
        else:
            print(
                "Package Name : {0}, Package Version : {1}, Required Python Version : {2}".format(
                    data[0], data[1], data[2]
                )
            )
