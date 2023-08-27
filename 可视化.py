
import math
import tkinter as tk

# 定义了一系列变量和函数，包括q、q1、f、w、m、l和z等。

# 函数yun1(q, k)返回一个值，表示在给定的q和k下的计算结果。

# 函数yun2(q)根据给定的q计算并更新变量z、f、m和l的值。

# 函数suanfa()根据一些数学计算来计算变量k的值。

# 使用一个无限循环来接收用户的输入，根据用户选择的不同执行不同的代码块。

def yun1(q, k):
    return 1 - math.pow(q, k) + 1.0 / k


def yun2(q):
    # 计算 fq 的值
    global z, f, m, l
    for a in range(f - 1, -1, -1):
        z[a] = 1.0 - math.pow(q, m[a]) + 1.0 / m[a] + 1.0 / (l[a] * m[a]) - math.pow(q, l[a] * m[a]) / m[a]


def suanfa():
    # 计算 k 的值
    global q
    a = math.ceil(math.sqrt(-1 / (q * q * math.log(q))))
    if a > 3:
        k = a
    else:
        k = 3
    while True:
        b = math.pow(q, k) * (q - 1) + 1 / (k * (k + 1))
        c = math.pow(q, k - 1) * (q - 1) + 1 / (k * (k - 1))
        if b < 0:
            break
        k += 1
    return k - 1

def calculate():
    global q, f, w, m, l, z
    q = float(q_entry.get())
    while q <= q1:
        output_text.insert(tk.END, "输入 q 值错误, 请重新输入！\n")
        q_entry.delete(0, tk.END)
        q = float(q_entry.get())
    k = suanfa()
    if q <= math.pow(q1, 1 / 3.0):
        output_text.insert(tk.END, "只能进行一次分组！\n")
        output_text.insert(tk.END, "可得 k 的值为：" + str(k) + "\n")
        output_text.insert(tk.END, "一次分组预期最小人均检验次数为：" + str(yun1(q, k)) + "\n")
    else:
        a = int(math.log(q1) / math.log(q))
        m1 = k if k < a else a  # 中间变量
        for m2 in range(3, m1 + 1):
            for l1 in range(3, k + 1):
                b = math.pow(q, m2 * l1) * ((math.pow(q, m2)) - 1) + 1 / (l1 * (l1 + 1))
                if b <= 0:
                    m[f] = m2
                    l[f] = l1
                    f += 1
        m2 += 1
        yun2(q)
        min_val = z[f - 1]
        for d in range(f - 1, -1, -1):
            if z[d] <= min_val:
                min_val = z[d]
                w = d
        output_text.insert(tk.END, "可得k的值为：" + str(k) + "\n")
        output_text.insert(tk.END, "可得m的值为：" + str(m[w]) + "\n")
        output_text.insert(tk.END, "可得l的值为：" + str(l[w]) + "\n")
        output_text.insert(tk.END, "一次分组预期最小人均检验次数：" + str(yun1(q, k)) + "\n")
        output_text.insert(tk.END, "二次分组预期最小人均检验次数：" + str(min_val) + "\n")

def exit_program():
    root.destroy()

q = 0
q1 = 1 / math.pow(3, 1 / 3.0)
f = 0  # 数据个数的控制
w = f - 1
m = [0] * 20000
l = [0] * 20000
z = [0] * 20000

root = tk.Tk()
root.title("分组核酸检测")
root.geometry("400x400")

q_label = tk.Label(root, text="输入 q 的值：")
q_label.pack()

q_entry = tk.Entry(root)
q_entry.pack()

calculate_button = tk.Button(root, text="确定", command=calculate)
calculate_button.pack()

output_text = tk.Text(root)
output_text.pack()

exit_button = tk.Button(root, text="退出", command=exit_program)
exit_button.pack()

root.mainloop()


