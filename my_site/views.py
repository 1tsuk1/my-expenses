import matplotlib

matplotlib.use("Agg")  #!重要
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, View


# Create your views here.
class IndexView(TemplateView):
    template_name = "my_site/index.html"

    def get_context_data(self, **kwargs):

        # TODO: draw_graphを呼び出して、パスを取得する
        output_path = IndexView.draw_graph()

        img_path = "/".join(output_path.split("/")[1:])  # TODO:なんとかいい感じにする
        context = {"img_path": img_path}

        return context

    @classmethod
    def draw_graph(cls):
        # money = Money.objects.filter(
        #     use_date__year=year, use_date__month=month
        # ).order_by("use_date")
        # last_day = calendar.monthrange(int(year), int(month))[1] + 1
        # day = [i for i in range(1, last_day)]
        # cost = [0 for i in range(len(day))]
        # for m in money:
        #     cost[int(str(m.use_date).split("-")[2]) - 1] += int(m.cost)
        # plt.figure()
        # plt.bar(day, cost, color="#00bfff", edgecolor="#0000ff")
        # plt.grid(True)
        # plt.xlim([0, 31])
        # plt.xlabel("日付", fontsize=16)
        # plt.ylabel("支出額(円)", fontsize=16)
        # # staticフォルダの中にimagesというフォルダを用意しておきその中に入るようにしておく

        #!
        year = 2021
        month = 1
        output_path = f"my_site/static/images/bar_{year}_{month}.svg"

        y1_value = [1, 2, 4, 8, 16, 32, 64, 128, 256, 1028]
        x1_value = range(1, len(y1_value) + 1)

        y2_value = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        x2_value = range(1, len(y2_value) + 1)

        # fig = plt.figure(figsize=(10, 6))

        plt.plot(x1_value, y1_value, label="test1")
        plt.plot(x2_value, y2_value, label="test2")

        plt.title("Test Graph", {"fontsize": 20})
        plt.xlabel("Numbers", {"fontsize": 20})
        plt.ylabel("Value", {"fontsize": 20})
        plt.tick_params(labelsize=20)
        plt.legend(prop={"size": 20}, loc="best")
        plt.savefig(output_path, transparent=True)
        return output_path
