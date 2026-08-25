# 轨迹文件和拓扑文件
xtc_file = "step5_1_1209_c_no_10us.xtc"
tpr_file = "step5_1.gro"

# 提取帧的时间区间(ps)
period = [
#    [2000, 5000,],              # 时间区间，如 2000 ps 到 5000 ps
#    [60000, 120000, 1000],      # 时间区间，如 60000 ps 到 12000 ps，步长为 1000 ps
#    80000,                      # 时间点，如 8000 ps
#    56000,
#    [13560, 35700],
#    [47000, 98000],
    7500,
    34000,
    83900,
    90300,
    90500,
    90700,
    90800,
    285800,
    292600,
    368400,
    383300,
    395300,
    396200,
    411600,
    420300,
    702700,
    1095100,
    1113300,
    2330700,
    2330800,
    2331500,
    2333500,
    2333600,
    2334800,
    2394500,
    2411600,
    2417900,
    2447600,
    2452500,
    2452700,
    2453500,
    2453600,
    2454000,
    2454300,
    2454400,
    2454800,
    2455300,
    2455400,
    2455500,
    2455700,
    2455900,
    2456800,
    2457400,
    2457600,
    2457700,
    2457900,
    2459200,
    2459400,
    2459500,
    2460400,
    2463200,
    2463500,
    2464000,
    2464600,
    2465700,
    2466400,
    2467600,
    2469400,
    2470900,
    2473000,
    2473700,
    2473800,
    2474300,
    2474700,
    2475100,
    2476900,
    2477500,
    2478100,
    2478700,
    2496800,
    2507100,
    2522100,
    2532000,
    2540100,
    2585500,
    2586500,
    2586700,
    2588000,
    2589600,
    2589700,
    2590700,
    2592000,
    2592700,
    2611000,
    2622100,
    2623800,
    2624100,
    2624900,
    2625000,
    2625300,
    2625800,
    2626200,
    2628800,
    2629600,
    2629800,
    2632200,
    2635200,
    2641900,
    2645600,
    2646000,
    2646800,
    2647900,
    2648500,
    2681800,
    2684700,
    2688500,
    2699100,
    2700100,
    2700900,
    2703000,
    2746600,
    2746700,
    2748100,
    3462900,
    3546100,
    3905000,
    3906200,
    3922200,
    3922500,
    3922700,
    3922800,
    3937700,
    3944800,
    3955500,
    3963800,
    3964400,
    3971200,
    3971500,
    3971700,
    3973200,
    3973500,
    4000800,
    4456100,
    4472100,
    4963400,
    4963500,
    4963700,
    4966400,
    5012300,
    5013100,
    5015600,
    5493700,
    5495300,
    5511400,
    5515100,
    5515200,
    5612800,
    5840800,
    5881200,
    5883600,
    5883900,
    5884700,
    5907400,
    5908400,
    5909300,
    5914900,
    5928500,
    7133800,
    7135400,
    7139800,
    7144800,
    7145000,
    7171100,
    7172300,
    7220500,
    7220900,
    7221100,
    7224100,
    7240600,
    7240800,
    7249300,
    7250000,
    7250100,
    7250800,
    7250900,
    7278400,
    7283500,
    7296800,
    7313300,
    7317900,
    7318300,
    7318400,
    7320700,
    7320800,
    7321100,
    7321400,
    7321500,
    7322000,
    7323100,
    7325100,
    7325200,
    7328100,
    7329300,
    7330600,
    7330900,
    7333000,
    7335000,
    7337300,
    7338500,
    7338700,
    7338800,
    7338900,
    7340600,
    7349300,
    7351600,
    7354000,
    7355000,
    7355100,
    7356800,
    7358700,
    7359000,
    7359100,
    7360400,
    7361300,
    7362900,
    7363300,
    7363600,
    7365700,
    7365900,
    7366400,
    7366600,
    7367400,
    7372200,
    7372700,
    7372800,
    7373000,
    7373700,
    7374900,
    7375800,
    7376100,
    7376200,
    7376800,
    7377400,
    7377800,
    7378400,
    7378600,
    7379000,
    7379400,
    7387400,
    7387900,
    7388000,
    7389600,
    7389900,
    7394200,
    7395400,
    7396000,
    7396300,
    7396400,
    7396600,
    7396700,
    7396800,
    7397200,
    7398100,
    7398500,
    7398700,
    7399000,
    7399600,
    7400400,
    7400800,
    7402700,
    7403000,
    7404700,
    7406400,
    7406800,
    7406900,
    7407900,
    7409400,
    7409800,
    7410000,
    7411400,
    7411500,
    7411600,
    7412500,
    7412900,
    7414500,
    7415400,
    7415600,
    7423800,
    7423900,
    7424000,
    7424800,
    7425300,
    7425900,
    7430000,
    7430200,
    7431200,
    7431400,
    7431500,
    7432500,
    7434800,
    7437100,
    7439100,
    7439300,
    7439400,
    7440300,
    7442000,
    7442100,
    7444600,
    7444700,
    7445500,
    7446700,
    7447000,
    7447200,
    7447500,
    7447700,
    7448100,
    7448800,
    7449800,
    7455000,
    7455700,
    7502300,
    7502600,
    7504400,
    7504600,
    7516500,
    7516700,
    7517000,
    7518400,
    7519700,
    7521300,
    7523000,
    7523200,
    7528300,
    7532600,
    7533900,
    7536700,
    7536800,
    7538100,
    7538200,
    7538400,
    7540200,
    7540300,
    7541400,
    7541600,
    7542500,
    7542700,
    7542900,
    7543100,
    7543200,
    7543400,
    7543500,
    7543700,
    7543800,
    7544100,
    7544400,
    7608000,
    7609200,
    7611600,
    7631500,
    7631900,
    7632000,
    7632700,
    7633200,
    7633900,
    7634000,
    7636000,
    7636100,
    7636500,
    7636700,
    7638700,
    7639000,
    7639100,
    7639200,
    7639300,
    7639600,
    7696900,
    7728500,
    7730100,
    7733200,
    7735400,
    7735900,
    7743600,
    7770400,
    7807500,
    8214100,
    8657800,
    8658200,
    8658400,
    8661300,
    8676700,
    8678100,
    8684100,
    8684300,
    8685600,
    8698300,
    8707900,
    8708700,
    8715500,
    8716800,
    8717100,
    8725300,
    8727500,
    8733200,
    8733500,
    8733600,
    8734400,
    8775100,
    8819000,
    8821500,
    8821600,
    8821700,
    8822500,
    8822600,
    8822700,
    8822800,
    8826000,
    8830900,
    8831200,
    8833200,
    8838400,
    8839300,
    8839500,
    8843900,
    8849500,
    8851400,
    8852600,
    8852900,
    8853700,
    8882900,
    8913500,
    8915100,
    8915200,
    8919600,
    8919700,
    8920300,
    8920400,
    8920700,
    8920900,
    8921400,
    8921600,
    8921800,
    8922000,
    8922600,
    8922900,
    8923500,
    8923700,
    8923900,
    8924200,
    8924700,
    8925200,
    8925700,
    8925900,
    8926300,
    8927000,
    8927800,
    8932200,
    8932600,
    8934800,
    8935300,
    8935400,
    8935500,
    8935900,
    8936200,
    8936400,
    8936500,
    8936800,
    8937200,
    8937900,
    8938000,
    8938300,
    8938600,
    8938800,
    8938900,
    8939300,
    8943300,
    8944400,
    8944600,
    8944700,
    8945100,
    8945200,
    8945300,
    8945500,
    8945800,
    8945900,
    8946500,
    8946700,
    8947100,
    8948100,
    8949800,
    8949900,
    8950200,
    8952500,
    8953300,
    8953400,
    8953600,
    8962500,
    8962700,
    8962800,
    8987700,
    8999000,
    9019800,
    9021900,
    9022900,
    9023000,
    9027400,
    9027800,
    9028100,
    9029300,
    9029500,
    9030400,
    9036800,
    9053000,
    9053500,
    9070200,
    12723100,
    12743000,
    12858200,
    12924300,
    12934200,
    13579700,
    13623300,
    13672600,
    13743600,
    13747200,
    13751100,
    13751300,
    13752000,

]

# 结构联配/对齐的时刻（通常选极值点）
reference = 0
# 最小二乘拟合的参考组 least squares fit group
lsq_fit_group = 4
# 几何中心居中参考组 centering group
centering_group = 1
# 输出轨迹的参考组 output group
extract_group = 1

# Group  0 (      System) has N elements
# Group  1 (     Protein) has N elements
# Group  2 (   Protein-H) has N elements
# Group  3 (     C-alpha) has N elements
# Group  4 (    Backbone) has N elements
# Group  5 (   MainChain) has N elements
# Group  6 (MainChain+Cb) has N elements
# Group  7 ( MainChain+H) has N elements
# Group  8 (   SideChain) has N elements
# Group  9 ( SideChain-H) has N elements
# Group 10 ( Prot-Masses) has N elements
# Group 11 ( non-Protein) has N elements
# Group 12 (       Other) has N elements
# Group 13 (         GTP) has N elements
# Group 14 (          MG) has N elements
# Group 15 (         POT) has N elements
# Group 16 (         CLA) has N elements
# Group 17 (        TIP3) has N elements
# Group 18 (         Ion) has N elements

######################################################
#################### 开发人员分界线 ####################
######################################################

print("\n" + "*"*10 + "\n 开始执行\n" + "*"*10 + "\n")

import shutil
from pathlib import Path
import subprocess
import MDAnalysis as mda
import numpy as np
from MDAnalysis.analysis.rms import rmsd
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="MDAnalysis")

folder = Path('custom_conformations')
folder.mkdir(exist_ok=True)

print("#####\n# 1 # 提取自定义时段构象\n#####\n")

for frac in period:
    # 执行命令（严格串行）
    try:
        if isinstance(frac, list) and len(frac) == 2:
            outfilename = f"./custom_conformations/_extracted_{frac[0]}_{frac[1]}.xtc"
            # 使用 subprocess.run 替代 Popen 简化同步逻辑
            result = subprocess.run(
                [
                    "gmx", "trjconv",
                    "-s", tpr_file,
                    "-f", xtc_file,
                    "-b", str(frac[0]),
                    "-e", str(frac[1]),
                    "-o", outfilename,
                ],
                input=f"{extract_group}\n".encode(),  # 一次性发送输入
                stdout=subprocess.PIPE,     # 可选：捕获输出
                stderr=subprocess.PIPE,     # 可选：捕获错误
                check=True,               # <=== 加上这个！
            )
            print(result.stdout.decode())
            print(f'[gmx_trjconv] 时段 {frac} {outfilename} 已写入\n'+'-'*10)

        elif isinstance(frac, list) and len(frac) == 3:
            outfilename = f"./custom_conformations/_extracted_{frac[0]}_{frac[1]}_{frac[2]}.xtc"
            # 使用 subprocess.run 替代 Popen 简化同步逻辑
            result = subprocess.run(
                [
                    "gmx", "trjconv",
                    "-s", tpr_file,
                    "-f", xtc_file,
                    "-b", str(frac[0]),
                    "-e", str(frac[1]),
                    "-dt", str(frac[2]),
                    "-o", outfilename,
                ],
                input=f"{extract_group}\n".encode(),  # 一次性发送输入
                stdout=subprocess.PIPE,     # 可选：捕获输出
                stderr=subprocess.PIPE,     # 可选：捕获错误
                check=True,               # <=== 加上这个！
            )
            print(result.stdout.decode())
            print(f'[gmx_trjconv] 时段 {frac}: {outfilename} 已写入\n'+'-'*10)

        elif isinstance(frac, int):
            outfilename = f"./custom_conformations/_extracted_frame_{frac}.xtc"
            # 使用 subprocess.run 替代 Popen 简化同步逻辑
            result = subprocess.run(
                [
                    "gmx", "trjconv",
                    "-s", tpr_file,
                    "-f", xtc_file,
                    "-dump", str(frac),
                    "-o", outfilename,
                ],
                input=f"{extract_group}\n".encode(),  # 一次性发送输入
                stdout=subprocess.PIPE,     # 可选：捕获输出
                stderr=subprocess.PIPE,     # 可选：捕获错误
                check=True,               # <=== 加上这个！
            )
            print(result.stdout.decode())
            print(f'[gmx_trjconv] 时段 {frac} {outfilename} 已写入\n'+'-'*10)
        
        else:
            print(f'[gmx_trjconv] 不认识的时间区段, 跳过\n'+'-'*10)

    except subprocess.CalledProcessError as e:
        print(f"命令执行失败，返回码 {e.returncode}")
        print("错误输出:", e.stderr.decode())
        continue  # 或终止循环（raise）
    except subprocess.TimeoutExpired:
        print("命令执行超时！")
        continue
    except Exception as e:
        print(f"未知异常: {e}")
        continue

# 合并  
pdb_files = list(folder.glob("_extracted*.xtc"))

try:
# 使用 subprocess.run 替代 Popen 简化同步逻辑
    result = subprocess.run(
        [
            "gmx", "trjcat", "-cat",
            "-f", *map(str, pdb_files),
            "-o", '1_1_extracted_combined.xtc',
        ],
        stdout=subprocess.PIPE,     # 可选：捕获输出
        stderr=subprocess.PIPE,     # 可选：捕获错误
        check=True,               # <=== 加上这个！
    )
    print(result.stdout.decode())

    outfilename = Path("./custom_conformations/1_1_extracted_combined.xtc")
    # 如果文件已存在，先删掉
    if outfilename.exists():
        outfilename.unlink()
    shutil.move("1_1_extracted_combined.xtc", str(outfilename))
    print(f'[gmx_trjcat] 已合并所有构象到 {outfilename}\n'+'-'*10)

except subprocess.CalledProcessError as e:
    print("STDOUT:\n", e.stdout)
    print("STDERR:\n", e.stderr)   # ← GROMACS 的真实报错在这里
    raise

for fi in pdb_files:
    fi.unlink()

print(f'[python Path.unlink()] 已删除构象提取临时文件 {pdb_files}\n'+'-'*10)

try:
    outfilename = "./custom_conformations/1_2_reference_frac.pdb"
    # 使用 subprocess.run 替代 Popen 简化同步逻辑
    result = subprocess.run(
        [
            "gmx", "trjconv",
            "-s", tpr_file,
            "-f", xtc_file,
            "-dump", str(reference),
            "-o", outfilename,
        ],
        input=f"{extract_group}\n".encode(),  # 一次性发送输入
        stdout=subprocess.PIPE,     # 可选：捕获输出
        stderr=subprocess.PIPE,     # 可选：捕获错误
        check=True,               # <=== 加上这个！
    )
    print(result.stdout.decode())
    print(f'[gmx_trjconv] 参考匹配构象 {reference}: {outfilename} 已写入\n'+'-'*10)

except subprocess.CalledProcessError as e:
    print("STDOUT:\n", e.stdout)
    print("STDERR:\n", e.stderr)   # ← GROMACS 的真实报错在这里
    raise

print()

############################################################3
print("#####\n# 2 # 帧与参考结构对齐\n#####\n")

# gmx trjconv -f extracted.xtc -s ref.pdb -o aligned.xtc -fit rot+trans -pbc nojump -center

try:
    outfilename = f"./custom_conformations/2_1_aligned.xtc"
    # 使用 subprocess.run 替代 Popen 简化同步逻辑
    result = subprocess.run(
        [
            "gmx", "trjconv",
            "-s", "./custom_conformations/1_2_reference_frac.pdb",
            "-f", "./custom_conformations/1_1_extracted_combined.xtc",
            "-o", outfilename,
            "-fit", "rot+trans", "-center",
        ],
        input=f"{lsq_fit_group}\n{centering_group}\n{extract_group}\n".encode(),  # 一次性发送输入
        stdout=subprocess.PIPE,     # 可选：捕获输出
        stderr=subprocess.PIPE,     # 可选：捕获错误
        check=True,               # <=== 加上这个！
    )
    print(result.stdout.decode())
    print(f'[gmx_trjconv] 各帧与参考结构对齐, {outfilename} 已写入\n'+'-'*10)
        

except subprocess.CalledProcessError as e:
    print(f"命令执行失败，返回码 {e.returncode}")
    print("错误输出:", e.stderr.decode())
except subprocess.TimeoutExpired:
    print("命令执行超时！")
except Exception as e:
    print(f"未知异常: {e}")

print()

######################################################3

print("#####\n# 3 # 计算平均虚拟构象和最近构象\n#####\n")

def average_positions(u, selection="backbone", start=None, stop=None, step=None):
    """
    计算给定原子选择在指定帧窗口上的平均坐标（Å）
    """
    ag = u.select_atoms(selection)
    sum_xyz = np.zeros((ag.n_atoms, 3), dtype=np.float64)
    n = 0
    for ts in u.trajectory[start:stop:step]:
        sum_xyz += ag.positions  # Å
        n += 1
    if n == 0:
        raise ValueError("选定的帧窗口为空，请检查 start/stop/step。")
    return sum_xyz / n, selection

def closest_frame_to_average(u, mean_xyz, selection, start=None, stop=None, step=None, return_frame=False):
    """
    计算每一帧相对平均构象的RMSD（Å），返回最小RMSD对应的帧索引与时间。
    注意：假设 u 对齐过（aligned.xtc），故不再做逐帧拟合。
    """
    ag = u.select_atoms(selection)
    if ag.n_atoms != mean_xyz.shape[0]:
        raise ValueError("mean_xyz 原子数与选择集不匹配。")

    best_idx, best_time, best_rmsd = None, None, np.inf
    rmsd_list = []

    for ts in u.trajectory[start:stop:step]:
        curr = ag.positions  # Å
        val = rmsd(curr, mean_xyz, center=False)  # 已对齐，无需居中/拟合
        rmsd_list.append(val)
        if val < best_rmsd:
            best_rmsd = val
            best_idx = ts.frame
            best_time = ts.time  # ps

    if return_frame:
        return best_idx, best_time, best_rmsd, np.asarray(rmsd_list)
    return best_idx, best_time, best_rmsd

def write_frame_as_pdb(u, frame_index, outfile, selection="all"):
    """
    将指定帧写为PDB（默认写全体系；可用 selection 控制输出原子集）
    """
    u.trajectory[frame_index]
    ag = u.atoms if selection == "all" else u.select_atoms(selection)
    with mda.Writer(outfile, multiframe=False) as W:
        W.write(ag)

# ====== 用法示例 ======
# aligned.xtc 已经对齐；reference_frac.pdb 仅提供拓扑（原子顺序/名字）
u = mda.Universe("./custom_conformations/1_2_reference_frac.pdb", "./custom_conformations/2_1_aligned.xtc")

sel = "protein"      # 或 "name CA" / "protein"
start, stop, step = None, None, None   # 可按需要设置帧窗口与步长

# 🔑 常用选择关键字
# 整体
# "all" → 所有原子
# "protein" → 蛋白质（包括所有原子）
# "nucleic" → 核酸（DNA/RNA）
# "backbone" → 蛋白主链 (N, CA, C, O)
# "name CA" → 仅 Cα 原子
# "resname LIG" → 残基名为 LIG 的小分子/配体
# "segid A" → 段 ID 为 A 的分子

# 逻辑组合
# "protein and name CA" → 蛋白里的 Cα 原子
# "backbone or resname LIG" → 蛋白主链 + LIG 配体
# "protein and not name H*" → 蛋白但不含氢

# 按编号
# "resid 10" → 第 10 号残基
# "resid 10:20" → 残基 10–20
# "bynum 1:1000" → 原子编号 1–1000

# 几何条件
# "around 5 protein" → 蛋白 5 Å 范围内的原子
# "point 10 20 30 5" → 距离点 (10,20,30) 5 Å 内的原子

# 化学类别
# "hydrogen" → 所有氢原子
# "heavy" → 非氢原子
# "polar" / "apolar" → 极性/非极性原子
# "charged" → 带电原子

# 1) 平均构象
mean_xyz, sel_used = average_positions(u, selection=sel, start=start, stop=stop, step=step)

# 2) 逐帧 RMSD 并找最接近的帧
best_idx, best_time_ps, best_rmsd_A, rmsd_series = closest_frame_to_average(
    u, mean_xyz, sel_used, start=start, stop=stop, step=step, return_frame=True,
)

print(f"Closest frame: index={best_idx}, time={best_time_ps:.3f} ps, RMSD={best_rmsd_A:.3f} Å")

# 可选：也把平均构象写出来（只含所选原子集）
sel_ag = u.select_atoms(sel_used)
sel_ag.positions = mean_xyz
with mda.Writer("./custom_conformations/3_1_avg_selected.pdb", multiframe=False) as W:
    W.write(sel_ag)

# 3) 导出最接近帧（整体系或同一选择集）
write_frame_as_pdb(u, best_idx, "./custom_conformations/3_2_closest_to_avg.pdb", selection=sel_used)   # 或 selection=sel_used

print("\n[Python MDAnalysis] 最近构象 ./custom_conformations/3_2_closest_to_avg.pdb 已写入\n")
print('-'*10)
print("\nPowered by Sandy, ChatGPT 5, ChatGPT 5 Thinking\n")
print("Aug 2025\n")
print('-'*10)
print("\n" + "*"*10 + "\n 运行结束 :)\n" + "*"*10 + "\n")

