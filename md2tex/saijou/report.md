細胞情報学教室
10191043 鈴木健一

# 大腸菌を用いたリコンビナントタンパク質の精製

## 目的
タンパク質精製手法のうち最も汎用されている大腸菌を利用したGTS融合タンパク質の精製を行い、
その手法と原理を学ぶ。

## 実験方法
実習書に基づきTAの指示にしたがって実験を行った。
今回実習に我々の班が用いたタンパク質はAとCの2つである。
また切断に用いる制限酵素のペアは
「EcoR V・Not I」と「EcoR I・Xho I」である。


## 結果・考察

AとCのSDS-PAGEの結果は以下のようになった。
\piccap{edo_a.jpg}{10}{SDS-PAGE A}
\piccap{edo_c.jpg}{10}{SDS-PAGE C}

それぞれのGST融合タンパク質の塩基対の数を$k$としたとき、
SDS-PAGEに現れるバンドの位置$t$kDaは以下のようにして求められる。

\[t = \frac{k}{25} + 26 \]

したがってmASK1 CTのバンドの位置は78付近に、
DASK1 NTのバンドの位置は63付近に現れると考えられる。
hTrxは途中に終始コドンがコードされるため、翻訳されるタンパク質の大きさは38程度になると考えられる。

画像を参照するとAは38付近にバンドが現れていることから、AがhTrxであると判別される。

Cは48と63の位置に強いバンドが現れている。
1番左のレーンは大腸菌を破砕した後の上清であり、2番目はその沈殿である。
本来は2番目ではなく、３・4番目により強いバンドが現れるはずだったが、
攪拌などの操作が足りなかったので2番目にバンドが出たと考えられる。
Cは63kDaのバンドをもとにしてDASK1 NT であると判別された。

続いてDNAの電気泳動の結果である。
\piccap{plus.jpg}{10}{DNAの電気泳動}

画像を見ると1600bp以下のバンドがタンパク質A・Cの両方でどちらの制限酵素を用いても現れなかった。
このことから、DNAの抽出まではできているが、その後で制限酵素が全く作用しなかったと推測される。
ピペッティングや制限酵素を付与する際の操作に不備があったと思われる。

電気泳動の結果からは全くタンパク質の判別ができなかったため、SDS-PAGEの結果から本来は何本のバンドが生じていたかを記述する。

今回用いたタンパク質はhTRxとDASK1 NTであり、それぞれ以下の表の通りのバンドの数が検出されたはずであった。

\begin{table}[H]
\centering
\begin{tabular}{@{}ccc@{}}
\toprule
         & EcoR V \& Not I & EcoR I \& Xho I \\ \midrule
hTrx     & 2本              & 2本              \\
DASK1 NT & 4本              & 2本              \\ \bottomrule
\end{tabular}
\end{table}


## 課題

\begin{enumerate}
\mon{1} 上述の通りである。

\mon{2} タンパク質生成によって高純度のタンパク質を得ることが可能であるならば、
例えば抗体医薬に用いられる医薬品として用いられる抗体を効率よく精製することが可能となる。

\mon{3} EcoR I, EcoR V, Not I の3つの制限酵素で同時に切断する。
環状プラスミドが EcoR I, EcoR V, Not I によって合計4箇所切断されるので
4つのバンドとして観測される。
塩基対は長い方から順に 3.1kbp, 1.8kbp, 1054bp, 248bp となる。
\end{enumerate}