import matplotlib.pyplot as plt
import plotly
import re
import csv
import pathlib

class Plotter:
    def __init__(self, show=False, save=False):
        self.round_up_amount = 2
        results_path = "results/"
        results_directory = pathlib.Path(results_path)
        current_pattern = "*.md"

        for fp in results_directory.glob(current_pattern):
            results = self.get_results_from_file(fp)
            self.create_plots(results)
            if show:
                plt.show()
            if save:
                fp = re.sub(".md", ".png", str(fp))
                fp = re.sub("results/", "results/plot/", fp)
                plt.savefig(fp)
            plt.cla()
            plt.clf()

    def get_results_from_file(self, fp):
        print("Getting results from ", fp)
        with open(fp, 'r') as f:
            f.readline()
            f.readline()
            csv_reader = csv.reader(f, delimiter='|')
            graphs = {}
            for row in csv_reader:
                row = [value.strip() for value in row if value.strip()]
                db = row[0]
                method = row[1]
                result = row[2]
                if not graphs.get(db):
                    graphs[db] = {}

                if not graphs.get(db).get(method):
                    graphs[db][method] = []

                graphs[db][method].append(result)
            return graphs


    def reduce_results(self, arr):
        reduced = {}
        for val in arr:
            rounded = round(float(val), self.round_up_amount)
            if not reduced.get(rounded):
                reduced[rounded] = 1
            else:
                reduced[rounded] = reduced[rounded] + 1
        return reduced


    def reduced_to_plot_format(self, reduced):
        formated = []
        for k, v in reduced.items():
            for _ in range(v):
                formated.append(k)
        return formated


    def create_plots(self, results):
        for db, method in results.items():
            for method_name, method_results in method.items():
                reduced = self.reduce_results(method_results)
                formated = self.reduced_to_plot_format(reduced)
                plt.hist(formated, rwidth=0.90, label=self.get_db_name(db), bins=2)
                plt.xlabel("Segundos")
                plt.ylabel("Quantidade")
                plt.title(self.get_plot_title(method_name))
                plt.legend(loc='upper right')

    def get_db_name(self, name):
        db_name_map = {
            "SqlQueries": "MySQL",
            "DgraphQueries": "DgraphDB",
        }

        return db_name_map.get(name, "notfound")


    def get_plot_title(self, name):
        title_map = {
            "find_judge_with_more_lawsuits": "Juizes que julgaram mais processos",
            "find_every_related_data": "Todos dados relacionados ao juiz",
            "find_thousand_lawsuits_numbers": "Encontrar o numero de 1000 processo",
        }
        return title_map.get(name, "notfound")

p = Plotter(save=True)
