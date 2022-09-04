from django.shortcuts import render

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):
    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        return labels

    def get_providers(self):
            """Return names of datasets."""
            return ["Leigos", "Logica", "C","Java","Python","BD"]

    def get_data(self):
            """Return 6 datasets to plot.
            Cada linha representa um dataset
            cada coluna representa um label
            a quantidade de dados precisa ser igual aos datasets/labels
            12 labels entao 12 coluans
            6 dataset, enta 6 linhas
            """

            dados = []
            for l in range(6):
                for c in range(12):
                    dado = [
                        randint(1, 200), #j
                        randint(1, 200),#f
                        randint(1, 200),#m
                        randint(1, 200),#a
                        randint(1, 200),#m
                        randint(1, 200),#j
                        randint(1, 200),#j
                        randint(1, 200),#a
                        randint(1, 200),#s
                        randint(1, 200),#o
                        randint(1, 200),#n
                        randint(1, 200),#d
                    ]
                dados.append(dado)
            return dados