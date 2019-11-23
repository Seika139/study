実習レポート 分子薬物動態学教室
10191043 鈴木健一

\begin{flushright}
実験日 : 2019/7/1 $\sim$ 2019/7/4

実習班 : グループB-3班
\end{flushright}

# 1日目

## $in \ vivo$ 動物実験
### 動物実験のプロトコル
* 5班：対照群
* 阻害群がFLV(fluvastatin)、OLM(olmesaltan)を投与するのに対し、対照群は生理用食塩水を投与する。
* ラット体重：312g
* 投薬スケジュール
	priming doseとしてRIF溶液(30 mM　in 生理食塩水)0.39 mLを頸静脈より瞬時投与する。その後、RIF溶液(3.75mM　in 生理食塩水)1.248 mL/hrを頸静脈に定速静脈内投与する。定速投与20分後にFLV、OLMを各0.670 umol分、2.0 mM溶液を0.312 mL頸動脈に瞬時投与する。
* 採血スケジュール
	生理用食塩水を瞬時投与後、1,3,5,10,15,30,60,90分後にヘパリン2 $\rm \mu$Lを入れたチューブに大腿動脈から採血する予定だったが、血の出が悪かったため頸静脈から採血を行った。それに応じて採血のタイムスケジュールが3,4,5,10,15,30,60,90分となった。


# 2日目

## FLV, OLM, RIFの血漿中・臓器中濃度測定のための準備
* 検量線作成のための溶液を調整する。
* $in \ vivo$実験で得た肝臓・腎臓サンプル、血漿サンプルをLC-MS/MS測定用に調整する。

## RIFの蛋白非結合形薬物分率の測定
* 非特異的な膜やデバイスへの薬物の定着を測定するために 30 $\rm \mu M$ RIFのPBS溶液を調整する。
* サンプルを遠心機で限外濾過する。

# 3日目
## 生理学的薬物速度論(PBPK)モデルを用いた薬物動態の$in \ silico$解析

> ### (1)
> 表1の実測値を片対数グラフにプロットして
> $$C=A \exp(-\alpha t) + B \exp(- \beta t)$$
> を満たすパラメータを残差法で求める。

### 結果

残差法で求めた初期値は以下のようになった。
\begin{table}[H]
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
& A   & B    & α    & β           \\ \hline
HX1 & 81 & 4.3 & 0.63  & 0.047  \\ \hline
LX1 & 56   & 17 & 16.64 & 0.5264 \\ \hline
\end{tabular}
\end{center}
\end{table}


> ### (2)
> 残差法で求めた初期値をもとに、非線形最小二乗法プログラムによってA,B,α,βの最適値を求める。また、それをもとに全身クリアランス$\rm CL_{tot}$を求める。

プログラムを実行した結果パラメータの最適値は以下のようになった。

\begin{table}[H]
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
& A   & B    & α    & β           \\ \hline
HX1 & 89.82 & 4.439 & 0.6698  & 0.04503  \\ \hline
LX1 & 55.00   & 17.28 & 0.3215 & 0.009237 \\ \hline
\end{tabular}
\end{center}
\end{table}

これをもとにして全身クリアランス$\rm CL_{tot}$を求める。

$$C=A \exp(-\alpha t) + B \exp(- \beta t)$$

の両辺を $t=0$ から $t=\infty$ まで積分すると

$$\int_0^\infty C \ dt= \rm{AUC}=\frac{A}{\alpha}+\frac{B}{\beta}$$

である。

また、HX1とLX1は胆汁排泄でのみ消失するので、
$$\rm CL_{tot} = CL_H$$
が成り立つ。また、
$$\rm CL_{tot}=\frac{Dose}{AUC}$$
$$\rm CL_{int,H}=\frac{Q_h \cdot CL_H}{f_B \cdot (Q_h-CL_H)}$$
以上の式からAUC,$\ \rm CL_{tot}, \ CL_{int,H}$は以下のようになる。

\begin{table}[H]
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
& AUC & $\rm CL_{tot}$     & $\rm CL_{int,H}$             \\ \hline
HX1 & 232.7 & 42.9 & 505.0 \\ \hline
LX1 & 2043.6 & 4.89 & 17.77 \\ \hline
\end{tabular}
\end{center}
\end{table}

> ### (3)
> ラット$in \ vivo$ における$\rm PS_{inf}, \ CL_{bile}, \ PS_{eff}$を求める。

肝細胞数が30 ($10^6$cells/g liver)、肝臓の臓器容積が29.75(mL/kg rat)、肝比重が1.0(g/mL)であるから、

$$\rm PS_{inf} \  [mL/min/kg \ rat]= PS_{inf} \ [mL/min/10^6 cells] \times 30 \times 29.75 \times 1.0$$

として$\rm PS_{inf}, \ CL_{bile}$を求める。また、実習書2-9にある式をもとに、$\rm CL_{met} = 0$であることから
$$\rm CL_{int,all} = PS_{inf} \times \frac{CL_{bile}}{PS_{eff} + CL_{bile}}$$
に$\rm PS_{inf}, \ CL_{bile}$を代入して$\rm PS_{eff}$を得る。以上をHX1,LX1について計算した結果以下のようになった。


\begin{table}[H]
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
 & PSinf    & CLbile   & PSeff     \\ \hline
HX1 & 520 & 1.34 & 0.0408 \\ \hline
LX1 & 18.7  & 1.81  & 0.0986 \\ \hline
\end{tabular}
\end{center}
\end{table}

> ### (4)
> LX1,HX1の消失過程の律速段階を理解する。

HX1は$\rm Q_h$=60 ml/min/kg、$\rm f_BCL_{int,H}$=151 ml/min/kgであるため血流律速よりではあるが固有クリアランスの値も無視はできない程度である。
LX1は$\rm Q_h$=60 ml/min/kg、$\rm f_BCL_{int,H}$=5.33 ml/min/kgであるから、固有クリアランス律速であると言える。
また、固有クリアランスに対する律速段階は、どちらも肝臓から血液へのbuckflux($\rm PS_{eff}$)が胆汁排出($\rm CL_{bile}$)に対して小さいため
$$\rm CL_{int,all} = PS_{inf}$$
に近似され、肝取り込み律速といえる。

> ### (5)
> 各コンパートメントにおける物質収支式を立てる。

\begin{eqnarray}
\rm \frac{dC_{br}}{dt} & = & \frac{Q_{br}}{V_{br}} \left(C_a - \frac{C_{br}}{kp_{br}}\right) \label{eq:c_br} \\

\rm \frac{dC_{mu}}{dt} & = & \frac{Q_{mu}}{V_{mu}} \left(C_a - \frac{C_{mu}}{kp_{mu}}\right) \label{eq:c_mu} \\

\rm \frac{dC_{he}}{dt} & = & \frac{1}{V_{he}} \left( Q_h\left(C_a - C_{he}\right) - f_B \ PS_{inf} \ C_{he} + f_h \ PS_{eff} \ C_h \right) \label{eq:c_he} \\

\rm \frac{dC_{h}}{dt} & = & \frac{1}{V_{h}} \left( f_B \ PS_{inf} \ C_{he} - f_h \ PS_{eff} \ C_{h} - f_h \ CL_{bile} \ C_h \right) \label{eq:c_h} \\

\rm \frac{dX_{bile}}{dt} & = & f_h \ CL_{bile} \ C_h \label{eq:x_bile} \\

\rm \frac{dC_{a}}{dt} & = & \frac{1}{V_a} \left(C_v - C_a \right)\left(Q_{br} + Q_{mu} + Q_h \right) \label{eq:c_a} \\

\rm V_v \frac{dC_{v}}{dt} & = & Q_{br}\frac{C_{br}}{kp_{br}} + Q_{mu}\frac{C_{mu}}{kp_{mu}} + Q_{he}C_{he} - \left( Q_{br} + Q_{mu} + Q_h\right) C_v \label{eq:c_v}

\end{eqnarray}
> ### (6)
> (5)のモデルをプログラム上で記述し、以下の課題に取り組む

プログラムで求めた結果HX1、LX1のそれぞれの数値のグラフは以下のようになった。

#### HX1
\pict{imgs/hx1_cv.png}{10}
\pict{imgs/hx1_ch.png}{10}
\pict{imgs/hx1_xb.png}{10}

#### LX1
\pict{imgs/lx1_cv.png}{10}
\pict{imgs/lx1_ch.png}{10}
\pict{imgs/lx1_xb.png}{10}

まず式を整理するにあたって律速段階を確認する。

#### HX1 - $\rm CL_H$
$$\rm Q_H: f_B CL_{int,H}= 60 :151$$
より「やや血流律速」と言えるので、肝クリアランス$\rm CL_{H}$は、$\rm Q_H$の変動に大きく影響される。  また、$\rm f_B CL_{int,H}$の変動にもわずかに影響される。
\begin{equation}
\rm CL_H = \frac{Q_H f_B CL_{int,H}}{Q_H +  f_B CL_{int,H}}
\label{eq:hx1_clh}
\end{equation}

#### HX1 - $\rm CL_{int,H}$

$$\rm CL_{bile}: PS_{eff}= 1.34 :0.0408$$
より「取り込み律速」と言えるので、肝固有クリアランス$\rm CL_{int,H}$は、$\rm PS_{inf}$の変動に大きく影響され、$\rm CL_{bile}$や$\rm PS_{eff}$の変動にはほとんど影響されない。

\begin{equation}
\rm CL_{int,H} \approx  PS_{inf}
\label{eq:hx1_clinth}
\end{equation}

#### LX1 - $\rm CL_H$

$$\rm Q_H: f_B CL_{int,H}= 60 :5.33$$
より「固有クリアランス律速」と言えるので、肝クリアランスは、$\rm f_B CL_{int,H}$の変動に大きく影響され、$\rm Q_H$の変動にはほとんど影響されない。

\begin{equation}
\rm CL_H \approx f_B CL_{int,H}
\label{eq:lx1_clh}
\end{equation}

#### LX1 - $\rm CL_{int,H}$
$$\rm CL_{bile}: PS_{eff}= 1.81 :0.0986$$
より「取り込み律速」と言えるので、肝固有クリアランス$\rm CL_{int,H}$は、$\rm PS_{inf}$の変動に大きく影響され、$\rm CL_{bile}$や$\rm PS_{eff}$の変動にはほとんど影響されない。

\begin{equation}
\rm CL_{int,H} \approx  PS_{inf}
\label{eq:lx1_clinth}
\end{equation}

### 課題1

#### HX1

定常状態では静注速度と消失速度が等しいことから
$$\rm I = CL_{tot} \cdot C_{ss}$$
またHX1は肝臓から胆汁を介する経路でのみ消失するので
$$\rm CL_{tot}=CL_H$$
として良い。これと式(\ref{eq:hx1_clh})より
$$\rm C_{p,ss} = I \cdot \frac{Q_H + f_B \cdot CL_{int,H}}{Q_H \cdot f_B \cdot CL_{int,H}}$$
と表される。HX1は「やや血流律速」であるため、$\rm f_B$が3倍になると血漿中濃度は1/3とまでは行かないが、かなり減少することがグラフからも確認される。

また、定常状態では胆汁排泄速度$\rm \frac{dX_{bile}}{dt}$が静注速度$I$と等しいので、式(\ref{eq:x_bile})より
$$\rm C_{H,ss} = \frac{I}{f_h \cdot CL_{bile}}$$
が成り立つ。したがって肝臓臓器中濃度は$\rm f_B$に依存しないので、濃度の上限は変わらない。しかし、濃度の変化については式(\ref{eq:}c_h)より$\rm f_B$に依存する項があるため、立ち上がりが早くなることがわかる。

最後に胆汁排泄速度$\rm \frac{dX_{bile}}{dt}$は式(\ref{eq:x_bile})より$\rm C_H$に依存するので、グラフの立ち上がりが早いほど胆汁排泄速度のグラフの立ち上がりも早いことがわかる。

#### LX1

LX1はHX1とは異なって固有クリアランス律速であるため、式(\ref{eq:lx1_clh})より
$$\rm C_{p,ss} =  \frac{I}{f_B \cdot CL_{int,H}}$$
が成り立つ。したがって、$\rm f_B$が3倍になると血漿中濃度は1/3になることがグラフからも認められる。
一方、$\rm C_H$に変化がないため、肝臓臓器中濃度と胆汁排泄速度のグラフに関しては変化が生じなかった。

### 課題4

#### HX1

HX1は取り込み律速の薬物なので、式(\ref{eq:hx1_clinth})より$\rm CL_{bile}$が1/2倍になっても、肝固有クリアランスはほとんど変動せず、血漿中濃度もほとんど変化しない。しかし$\rm CL_{bile}$が1/10倍になると取り込み律速とは言えなくなるため、肝固有クリアランスが減少する。だが、HX1は血流律速寄りであるため、肝固有クリアランスの変動の影響を受けにくく、血漿中濃度はさほど変化しない。
一方、肝臓臓器中濃度は
$$\rm C_{H,ss} = \frac{I}{f_h \cdot CL_{bile}}$$
が成り立つので$\rm CL_{bile}$の変動が直接影響する。同様に$\rm \frac{dX_{bile}}{dt}$も式(\ref{eq:x_bile})より$\rm CL_{bile}$に依存するため、$\rm CL_{bile}$が減少すると、グラフの立ち上がりが遅くなり、濃度の最大値が増加する。また、胆汁排泄速度$\rm \frac{dX_{bile}}{dt}$は式(\ref{eq:x_bile})より$\rm CL_{bile}$に依存するので、$\rm CL_{bile}$が減少に応じてグラフの立ち上がりが遅くなることがわかる。

#### LX1

LX1もHX1と同様に取り込み律速なので、$\rm CL_{bile}$が1/2倍になっても、肝固有クリアランスはほとんど変動せず、血漿中濃度もほとんど変化しない。しかし$\rm CL_{bile}$が1/10倍になると取り込み律速とは言えなくなるため、肝固有クリアランスが減少する。LX1は固有クリアランス律速なので、固有クリアランス減少の影響を受けやすいが、$\rm CL_{bile}$の減少に対してもそれほど血漿中濃度が増加しないことがグラフからわかる。
肝臓臓器中濃度と胆汁排泄速度についてはHX1と同じ議論が可能となるため、変化の具合もHX1と同じようになった。

## FLV, OLMの肝細胞への取り込みに対する阻害効果の解析

RIFの濃度が$\rm 100\mu M$のときの取り込み(\％ of control)を \％ $\rm P_{dif}$ の初期値、取り込み(\％ of control)がだいたい$50 + 0.5 \times \％P_{dif}$になるようなRIF濃度の$\rm \mu M$を$\rm K_i$の初期値とした。

初期値を入力して、

$$\rm \%CL = \frac{1}{1+\frac{I_{RIF}}{K_i}}\cdot \left( 100 - \%P_{diff} \right) + \%P_{diff} $$

の式に非線形最小二乗法プログラムによってfittingを行い、$\rm \%P_{dif}, K_i$の最適値を計算させると結果は以下のようになった。

\begin{table}[H]
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
& FLV    & OLM        \\ \hline
$\rm K_i$     & 2.10 & 1.57 \\ \hline
$\rm \%P_{dif}$ & 34.1 & 7.97 \\ \hline
\end{tabular}
\end{table}

# 4日目

## 限外濾過法によるRIFの蛋白非結合形薬物分率の算出

$1 \sim 3$班の平均回収率が0.381、$4 \sim 6$班の平均回収率が0.167、であったので、RIFの蛋白非結合形薬物分率は
$$f_b = 0.381 \div 0.167 =0.439$$
となった。

## $in \ vivo$動物実験における体内動態の解析

LC-MS/MSの定量データ・検量線データから算出されたFLV,OLM,RIFの濃度は下表の通りとなった。FLVは1班のデータを借りている。

\begin{table}[H]
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
min                 & 1    & 3    & 5    & 10   & 15    & 30    & 60    & 90   \\ \hline
FLV濃度推移 ($\rm \mu M$)& 8.31 & 2.2  & 1.44 & 0.74 & 0.641 & 0.543 & 0.429 & 0.29 \\ \hline
OLM濃度推移 ($\rm \mu M$)  & 13.7 & 9.87 & 8.85 & 4.06 & 1.79  & 0.821 & 0.117 &   0   \\ \hline
RIF濃度推移 ($\rm \mu M$)    & 28.2 & 33.6 & 41.8 & 42.7 & 45.1  & 45.9  & 55    & 57.7 \\ \hline
\end{tabular}
\end{center}
\end{table}

\pict{imgs/3p.png}{10}

ここから4班のFLV、OLMの体内動態パラメータを算出する。
$\rm AUC_{0-90}$は1min,3minのデータから線形的に0minの数値を計算し、台形法で求める。さらに$\rm AUC_{0-\infty}$は、値のないところを消失相の傾きから外挿して計算する。FLVは60minと90minから消失相の傾きを求め、OLMは30minと60minから消失相の傾きを求め、90minの値に外挿して求めた。
そして、測定されたDoseの濃度を用いて、$\rm CL_{tot}$を
$$\rm CL_{tot}=\frac{Dose}{AUC_{0-\infty}}$$
より計算した。最後に薬物濃度を90minでの血漿中薬物濃度で割ることで$\rm K_p$を算出した。

\begin{table}[H]
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
& 単位            & FLV         & OLM                      \\ \hline
$\rm AUC_{0-90}$   & nmol・min/mL & 67.135      & 139.255     \\ \hline
$\rm AUC_{p, 0-\infty}$ & nmol・min/mL & 89.3529094  & 141.0565251 \\ \hline
$\rm CL_{p, tot}$      & mL/min/kg   & 22.38315477 & 0.987228346 \\ \hline
$\rm CL_{b,tot}$       & mL/min/kg   & 33.40769368 & 21.16225835 \\ \hline
$\rm CL_{int,h}$       & mL/min/kg   & 376.8875097 & 1720.702117 \\ \hline
$\rm C_{liver,90min}$  & nmol/mL     & 2.42        & 0.46        \\ \hline
$\rm K_{p,app,liver}$  &             & 8.344827586 & 3.931623932 \\ \hline
\end{tabular}
\end{center}
\end{table}


全ての班のFLV,OLMの濃度推移は以下のグラフのようになった。

\pict{imgs/c-f.png}{10}
\pict{imgs/c-o.png}{10}
\pict{imgs/s-f.png}{10}
\pict{imgs/s-o.png}{10}
\pict{imgs/g-rif.png}{10}

また動態パラメータの表は以下のようになる。
#### FLV
\pic{imgs/flv-t.png}
#### OLM
\pic{imgs/olm-t.png}

今回の実習で用いたRIFは肝細胞の血管側に発現する取り込みトランスポーターであるOATP類を阻害する。したがって肝臓への取り込み阻害がなされると薬物の血中濃度が上昇することが想定される。今回の実習では薬物としてFLVとOLMを用いた。その濃度推移について見てみると、FLVはコントロール群と阻害群であまり変化がないのに対して、OLMは阻害群のほうが濃度の低下が食い止められていることが認められる。したがってOLMはOATP類が主となって肝取り込みをしていることが想定される。


> 一般的に未知のペアの薬物について、薬物間相互作用を予測する上で、なんのパラメーターを考慮する必要があるか。

薬物の取り込み・排出において、非線形的な挙動の原因となるのがトランスポーター、代謝酵素、血漿蛋白・組織蛋白との飽和である。これらが薬物同士で競合したり、影響し合わないかを考慮する必要がある。
今回の実習では肝取り込みトランスポーターの阻害係数$\rm K_i$や拡散の影響$\rm \%P_{dif}$に注目したが、それ以外にも胆汁排泄ベシクルや肝臓内の代謝酵素への阻害効果も検証する必要がある。また、薬によっては尿細管などでの再吸収トランスポーターを阻害することで尿中排泄効率を高める場合も考えられるなど、様々な要因を考慮する必要がある。
