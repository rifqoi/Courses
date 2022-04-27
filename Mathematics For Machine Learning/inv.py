import numpy as np
matriks = np.array([
                [2,6,10],
                [2,6,12],
                [10,10,20],
            ], dtype=np.float_).T

matriks_inverse = np.linalg.inv(matriks)
total_vektor = np.array([[108, 204, 376]]).T

hasil = matriks_inverse @ total_vektor
print(matriks)
print(hasil)
