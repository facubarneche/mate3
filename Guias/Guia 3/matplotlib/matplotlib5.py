"""
5. Un grupo de amigos, decidieron registrar durante 6 días, cuántas tazas ingerían de café, té y agua. Con esos datos, necesitan un gráfico de barras apiladas para visualizar quién ingiere más líquidos y quién menos.
cafe = np.array([5, 5, 7, 6, 7, 4])
te = np.array([1, 2, 0, 2, 1, 3])
agua = np.array([10, 0, 14, 12, 15, 13])
nombres = ['María', 'Pablo', 'Ema', 'Franco', 'Estefanía', 'Pedro']
Podrían representarse los datos anteriores con un diagrama de cajas?
"""
import matplotlib.pyplot as plt
import numpy as np

def main():

    cafe = np.array([5, 5, 7, 6, 7, 4])
    te = np.array([1, 2, 0, 2, 1, 3])
    agua = np.array([10, 0, 14, 12, 15, 13])
    nombres = ['María', 'Pablo', 'Ema', 'Franco', 'Estefanía', 'Pedro']

  
    plt.figure(figsize=(9,7))
    plt.bar(nombres,cafe,color="green",label="Café")
    plt.bar(nombres,te,color="yellow",bottom=np.array(cafe),label="Té")
    plt.bar(nombres,agua,color="red",bottom=np.array(cafe)+np.array(te),label="Agua")

    plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
    plt.show()

if __name__ == "__main__":
    main()
