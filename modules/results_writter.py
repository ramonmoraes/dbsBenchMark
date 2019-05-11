from timeit import default_timer as timer
import os

RESULT_BASE_PATH = "results/"

class ResultWritter:
    def __init__(self, class_name):
        self.class_name = class_name
        print("[Making results for {}]".format(class_name.upper()))


    def write_result(self, function_name, function):
        elapsed_time = self.get_elapsed_time(function)
        file_path = "{}{}.md".format(RESULT_BASE_PATH, function_name)

        if self.is_empty_file(file_path):
            self.write_table_header(file_path)

        with open(file_path, "a") as f:
            print(" - {}".format(function_name))
            f.writelines(
                self.format_results(function_name, elapsed_time)
            )

    def write_table_header(self, file_path):
            with open(file_path, 'w') as f:
                f.write("| Class | Function | Time(s) |\n")
                f.write("|-|-|-|\n")

    def format_results(self, function_name, time):
        return "| {} | {} | {} |\n".format(
            self.class_name,
            function_name,
            time
        )

    def get_elapsed_time(self, function):
        start = timer()
        function()
        end = timer()
        return end - start

    def is_empty_file(self, file_path):
        try:
            return os.stat(file_path).st_size<=6
        except:
            return True
