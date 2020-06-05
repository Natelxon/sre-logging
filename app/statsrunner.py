import collections
import time

class StatsRunner():

    def __init__(self, log_file):
        self.log_file = log_file
        self.top_count = 5
        self.last_line = None
        self.request_list = []

    def watch(self):
        # Watch log file for changes
        open_file = open(self.log_file, 'r')
        open_file.seek(0, 1)

        while True:
            line = open_file.readline()
            if not line:
                time.sleep(0.1)
                continue
            if line == "\n":
                time.sleep(0.1)
                continue
            yield line

    def analyze(self):
        lines = self.watch()

        for line in lines:
            try:
                print(line)
                split = line.split(' ')
                print(split)

                ip = split[0]
                http_req = split[5][1:]  # Remove leading quotation
                http_code = split[8]
                # Remove leading and trailing quotation
                referer = split[10][1:-1]

                self.request_list.append({
                    "ip": ip,
                    "httpreq": http_req,
                    "httpcode": http_code,
                    "referer": referer
                })

                self.last_line = line
            except Exception as e:
                print(e)

    def summary(self):
        # Calculate metrics from in memory data
        total_count = len(self.request_list)

        unique_counts_ip = collections.Counter(
            e['ip'] for e in self.request_list)

        unique_counts_http = collections.Counter(
            e['httpcode'] for e in self.request_list)

        filtered_get_req = [
            x for x in self.request_list if x['httpreq'] == "GET"]

        # Count GET requests by referer and convert to dictionary
        unique_counts_referer = collections.Counter(
            e['referer'] for e in filtered_get_req).most_common(self.top_count)

        unique_counts_referer_dict = {item[0]: item[1]
                                      for item in unique_counts_referer}

        summary = {
            "logFile": self.log_file,
            "totalRequests": total_count,
            "countByIp": unique_counts_ip,
            "uniqueIps": len(unique_counts_ip),
            "httpCodeDistribution": unique_counts_http,
            "topReferers": unique_counts_referer_dict
        }

        return summary
