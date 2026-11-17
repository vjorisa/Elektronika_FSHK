# Studimi dhe Analiza e Pjestuesit te Tensionit dhe Qarqeve me Ngarkese

## Informacioni i Punimit
* **Departamenti:** Departamenti i Fizikës  
* **Lënda:** Elektronika  
* **Studentët:** Vjorisa Cani, Kejsi Seferi, Memo Kojdheli, Andja Milloshi, Azem Elezi  
* **Data e punimit:** 11.11.2026  
* **Data e dorëzimit:** 17.11.2026  
* **Pranuan:** Ervin Kafexhiu, Gerti Xhixha  

---

## 1. Qëllimi i Eksperimentit
Ky punim laboratorik ka për qëllim shqyrtimin dhe vërtetimin praktik të skemave të pjesëtimit të tensionit (voltage divider), si dhe vëzhgimin e sjelljes së qarqeve gjatë lidhjes së një rezistence ngarkese ($R_L$), duke bërë një krahasim midis të dhënave të regjistruara në eksperiment dhe parashikimeve teorike.

---

## 2. Përmbajtja e Folderit
* `Raport.ipynb` – Notebook-u kryesor me shpjegimet, formulat dhe analizën e plotë të eksperimentit.
* `data` – Skedari i të dhënave dhe vlerave të matura gjatë laboratorit.
* `gjenero_grafiket.py` – Skripti në Python për gjenerimin automatik të grafikëve nga të dhënat.
* `figs/` – Folderi që përmban grafikët e gjeneruar:
  * `grafiket_laboratorike.png` – Paraqitja vizuale e rezultateve për Eksperimentin 1, 2 dhe 3.

---

## 3. Rezultatet dhe Grafikët e Eksperimentit
Grafikët e mëposhtëm shfaqin krahasimin ndërmjet vlerave teorike dhe atyre të matura në laborator:

* **Eksperimenti 1:** Analiza dhe krahasimi i vlerave të tensionit në dalje midis llogaritjeve teorike dhe matjeve direkte.
* **Eksperimenti 2:** Vëzhgimi i qarkut të hapur me rezistenca të larta (megaohmë).
* **Eksperimenti 3:** Studimi i ndikimit të rezistencës së ngarkesës ($R_L$) në rënien e tensionit në dalje ($V_{out}$).

---

## 4. Përfundime
* Gjetjet praktike vërtetojnë shprehjet teorike të përdorura për pjesëtimin e tensionit.
* Futja e rezistencës së ngarkesës ($R_L$) modifikon rezistencën e përgjithshme ekuivalente të degës së poshtme ($R_2 \parallel R_L$), duke sjellë si pasojë një zvogëlim të tensionit në dalje ($V_{out}$) krahasuar me gjendjen pa ngarkesë.
* Të dhënat e marra përkojnë saktësisht me parashikimet, duke marrë parasysh tolerancat e komponentëve dhe rezistencën e brendshme të instrumenteve matëse.
