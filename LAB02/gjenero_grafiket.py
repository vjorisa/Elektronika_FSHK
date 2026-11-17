import os
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

# Sigurohu qe folderi figs ekziston
os.makedirs('figs', exist_ok=True)

# Të dhënat nga skedari i matjeve
# Eksperimenti 1
V_in_exp1 = 15.35
V_out_exp1 = 7.50
V_out_teorik = V_in_exp1 * (7.78 / (7.55 + 7.78))

# Eksperimenti 2: Qarku i hapur
V_in_exp2 = 6.82
V_out_exp2 = 6.71

# Eksperimenti 3: Qarku me rezistencë ngarkese
v_matur_ngarkese = [7.76, 7.71]
r_l_labels = ['R_L = 3.30 MOhm', 'R_L = 2.34 MOhm']

# Krijimi i 3 grafikëve krah për krah
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

# 1. Grafiku për Eksperimentin 1
kategorite_exp1 = ['V_out Teorik', 'V_out i Matur']
vlerat_exp1 = [V_out_teorik, V_out_exp1]
ax1.bar(kategorite_exp1, vlerat_exp1, color=['#4C72B0', '#55A868'])
ax1.set_ylabel('Tensioni (V)')
ax1.set_title('Eksperimenti 1: Pjestuesi i Tensionit')
ax1.set_ylim(0, 10)
for i, v in enumerate(vlerat_exp1):
    ax1.text(i, v + 0.2, f"{v:.2f} V", ha='center', fontweight='bold')

# 2. Grafiku për Eksperimentin 2 (Qarku i Hapur)
kategorite_exp2 = ['V_in (Hyrja)', 'V_out (Dalja)']
vlerat_exp2 = [V_in_exp2, V_out_exp2]
ax2.bar(kategorite_exp2, vlerat_exp2, color=['#DD8452', '#8172B3'])
ax2.set_ylabel('Tensioni (V)')
ax2.set_title('Eksperimenti 2: Qarku i Hapur')
ax2.set_ylim(0, 8)
for i, v in enumerate(vlerat_exp2):
    ax2.text(i, v + 0.2, f"{v:.2f} V", ha='center', fontweight='bold')

# 3. Grafiku për Eksperimentin 3 (Ngarkesa)
ax3.plot(r_l_labels, v_matur_ngarkese, marker='o', color='#C44E52', linestyle='-', linewidth=2, markersize=8)
ax3.set_ylabel('Tensioni i Matur V_out (V)')
ax3.set_title('Eksperimenti 3: Qarku me Ngarkesë')
ax3.set_ylim(7.5, 7.9)
for i, v in enumerate(v_matur_ngarkese):
    ax3.text(i, v + 0.01, f"{v} V", ha='center', fontweight='bold')

plt.tight_layout()

# Ruajtja e imazhit të përditësuar te figs/
plt.savefig('figs/grafiket_laboratorike.png', dpi=300)
print("Të tre grafikët u gjeneruan dhe u ruajtën te figs/grafiket_laboratorike.png!")

plt.show()
