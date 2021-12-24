import japanize_matplotlib
import matplotlib

matplotlib.use("Agg")  #!重要
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, View

from my_site.preprocessing_data import preprocessing_data


# Create your views here.
class IndexView(TemplateView):
    template_name = "my_site/index.html"

    def get_context_data(self, **kwargs):

        # TODO: draw_graphを呼び出して、パスを取得する
        month_path = IndexView.bar_graph("月")
        category_path = IndexView.bar_graph("カテゴリ")

        context = {
            "month_path": month_path,
            "category_path": category_path,
        }

        return context

    @classmethod
    def bar_graph(cls, colname):

        output_path = f"my_site/static/images/{colname}.svg"

        df = preprocessing_data()

        agg_df = df.groupby([colname])["支払総額"].sum()
        agg_df = agg_df.sort_values(ascending=False)
        # agg_df = df.groupby(["月", "category"])["支払総額"].sum()
        # print(agg_df)

        # TODO:
        plt.bar(
            agg_df.index,
            agg_df.values,
            color="#FF5B70",
            edgecolor="#CC4959",
            linewidth=4,
        )

        plt.xticks(rotation=45)
        plt.savefig(output_path, transparent=True)
        img_path = "/".join(output_path.split("/")[1:])  # TODO:なんとかいい感じにする

        plt.clf()  # 一回描画したfigを削除する（重ねて描画されてしまうため）

        return img_path
