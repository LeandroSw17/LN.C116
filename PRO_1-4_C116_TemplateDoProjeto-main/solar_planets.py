import cv2

# Carrega a imagem
img = cv2.imread("sistema-solar.PNG")

# Exibe a imagem
cv2.imshow("resultado", img)

# Aguarda pressionamento de tecla
cv2.waitKey(0)

# Salva a imagem com os nomes dos planetas
cv2.imwrite("Solar_system_with_name.jpg", img)

# Fecha a janela após exibição
cv2.destroyAllWindows()
