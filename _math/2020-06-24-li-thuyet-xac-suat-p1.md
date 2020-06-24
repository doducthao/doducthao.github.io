---
layout: post
title: Lý thuyết cơ bản của xác suất (Phần 1)
# subtitle: ""
excerpt_separator: 
categories: [Probability-Statistics]
tags: [math, prob, statistics, distribution, axioms]
date: June 24, 2020 
comments: true
mathjax: true
---

**Nội dung bài viết**

* TOC
{:toc}

# Lý thuyết về tập hợp
Người ta vẫn hay hỏi nhau rằng xác suất có trước hay thống kê có trước, đây giống như chuyện con gà và quả trứng vậy, nếu nhìn theo hướng tiến trình lịch sử thì có thể thấy xác suất "có vẻ" được nghiên cứu sau thống kê [(xem thêm)](https://en.wikipedia.org/wiki/Timeline_of_probability_and_statistics). Xác suất thống kê về sau đã được coi như là **một ngành khoa học riêng có liên quan chặt chẽ với Toán học**, bạn có thể xem thêm ở [đây](https://www.facebook.com/DataAnalysisSchool/videos/568645617361005/UzpfSTEwMDAwNTc5Njg1MzE5MjoxMzYwODA4NTAwNzg5MDMy/). Bài viết này, tôi chỉ tập viết về xác suất và những lý thuyết đẹp đẽ của nó.

Thiếu đi không gian mẫu (sample place), các bài toán về xác suất sẽ không thể giải quyết.
> Không gian mẫu, \\(S\\), là tập hợp tất cả kết quả có thể có của một thí nghiệm cụ thể.

Một ví dụ dễ gặp là việc khi ta tung một đồng xu, đương nhiên kết quả chỉ có thể xảy ra hoặc sấp hoặc ngửa (tails or head), do đó không gian mẫu là \\(S = \left\lbrace S, N\right\rbrace\\). Một ví dụ khác, không gian mẫu của các số không âm là \\(S = \[0, +\infty\)\\). Trên đây là hai ví dụ của hai loại không gian mẫu mà ta có thể phân loại: Đếm được và không đếm được. Nếu các phần tử của một không gian mẫu có thể đặt vào một song ánh 1-1 với một tập con của \\(\mathbb{N}\\), thì không gian mẫu đó đếm được, ngược lại là không đếm được. Một ví dụ về không gian mẫu vô hạn đếm được là \\(S = \left\lbrace 0,1,2,\ldots\right\rbrace\\).

> Một sự kiện, \\(A\\), là một họ bất kỳ của các kết quả có thể có của một thí nghiệm, tức là \\(A\subset S\\).

Về mặt tập hợp, chúng ta đã quá quen thuộc với các mệnh đề và định nghĩa sau
\\[A\subset B \Leftrightarrow x\in A\Rightarrow x\in B;\\]
\\[A = B \Leftrightarrow A\subset B \text{ và } B\subset A.\\]
\\[A \cup B=\{x: x \in A \text { hoặc } x \in B\}\\]
\\[A \cap B=\{x: x \in A \text { và } x \in B\}\\]
\\[A^{c}=\{x: x \notin A\}\\]
**Một số các tính chất của tập hợp**

(Giao hoán)
\\[A \cup B=B \cup A, A \cap B=B \cap A \\]
(Kết hợp)
\\[A \cup(B \cup C)=(A \cup B) \cup C, A \cap(B \cap C)=(A \cap B) \cap C\\]
(Phân phối)
\\[A \cap(B \cup C)=(A \cap B) \cup(A \cap C), A \cup(B \cap C)=(A \cup B) \cap(A \cup C)\\]
(De Morgan)
\\[(A \cup B)^{c}=A^{c} \cap B^{c}, (A \cap B)^{c}=A^{c} \cup B^{c}\\]
Các tính chất kể trên khá là dễ để chứng minh, tôi chỉ giới thiệu lại cho bạn một cái nhìn toàn cảnh.

> Hai sự kiện \\(A, B\\) được goị là rời rạc (disjoint) nếu \\(A\cap B=\varnothing\\). Các sự kiện \\(A_1, A_2, \ldots\\) được gọi là đôi một rời rạc (pairwise disjoint) nếu \\(A_i \cap A_j =\varnothing, \forall i\ne j\\).

> Nếu \\(A_1, A_2,\ldots\\) là đôi một rời rạc và \\(\cup_{i=1}^{\infty} A_{i}=S\\) thì \\(A_i,i=\overline{1,\infty}\\) tạo thành một phân vùng của \\(S\\).

# Nền tảng của lí thuyết xác suất
Mỗi một ngành khoa học đều có nền tảng vững chắc của riêng mình, chắc đa số chúng ta vẫn còn nhớ [hệ tiên đề hình học Euclid](https://vi.wikipedia.org/wiki/H%C3%ACnh_h%E1%BB%8Dc_Euclid) là cơ sở để xây dựng lý thuyết hình học sơ cấp. Hay đi xa hơn là Hilbert, một nhà Toán học người Đức, vào năm 1899 cũng đã đưa ra [hệ tiên đề đầy đủ của hình học](https://en.wikipedia.org/wiki/Hilbert%27s_axioms), tìm hiểu khi viết bài này, tôi bắt gặp một [bài viết](https://viethungpham.com/2013/12/16/ve-he%CC%A3-tien-de-hilbert-on-hilberts-set-of-axioms/) rất hay của GS. PV Hùng có phân tích về tính đầy đủ, độc lập và phi mâu thuẫn của hệ tiên đề này. Ngoài ra, có thể kể tới các tiên đề [Dirac-Von Neumman](https://en.wikipedia.org/wiki/Dirac%E2%80%93von_Neumann_axioms), [Peano](https://en.wikipedia.org/wiki/Peano_axioms),...

Nước Nga ở thế kỷ 20 xuất hiện nhiều nhà khoa học kiệt xuất, đóng góp cho nền khoa học Nga nói riêng và thế giới nói chung những phát kiến lớn, một trong số đó là [Andrey Kolmogorov](https://en.wikipedia.org/wiki/Andrey_Kolmogorov), người được nhắc đến là ông tổ của lý thuyết xác suất hiện đại với hệ tiên đề mang tên mình. 

## Hệ ba tiên đề Kolmogorov
Ở đây, để dễ theo dõi, tôi sẽ bỏ qua phần sigma đại số, vốn là nền tảng của việc xây dựng tiên đề, các bạn có thể xem tại [đây](https://en.wikipedia.org/wiki/%CE%A3-algebra).

Hệ ba tiên đề này được phát biểu như sau
> Cho trước một không gian mẫu \\(S\\) và sigma đại số \\(\beta\\), một hàm xác suất là một ánh xạ \\(P\\) với miền \\(\beta\\) thỏa mãn
1. \\(P(A)\ge 0, \forall A\in \beta\\)
2. \\(P(S)=1\\)
3. Nếu \\(A_1, A_2,\ldots \in \beta\\) là đôi một rời nhau thì \\(P\left(\cup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} P\left(A_{i}\right)\\)

Vì là tiên đề nên không có chứng minh, một ví dụ cho phần này đó là ví dụ về tung đồng xu (giả thiết cân đối, đồng chất) với đầu ra hoặc sấp hoặc ngửa (T hoặc H). Như vậy có thể "đoán" rằng \\(P(T)=P(H)=\dfrac{1}{2}\ge 0\\), từ đó thấy được \\[1 = P(S)=P(\left\lbrace H,T\right\rbrace) = P(H\cup T)=P(H) + P(T).\\] 
Định lý sau chỉ giới thiệu mà không chứng minh
> Cho \\(S=\left\lbrace s_{1}, \ldots, s_{n}\right\rbrace\\) là tập hữu hạn và \\(\beta\\) là sigma đại số của các tập con của \\(S\\). Đặt \\(p_1, p_2,\ldots,p_n\\) là các số không âm có tổng bằng \\(1\\). Với mọi \\(A\in \beta\\), định nghĩa 
\\[P(A) = \sum_{\left\lbrace i: s_{i} \in A\right\rbrace} p_{i}.\\]
Khi đó \\(P\\) là một hàm xác suất trên \\(\beta\\). Điều này vẫn đúng nếu \\(S=\left\lbrace s_{1}, \ldots, s_{n}\right\rbrace\\) là tập đếm được.

> Nếu \\(P\\) là một hàm xác suất và \\(A, B \in \beta\\) là các tập bất kỳ, thì
1. \\(P\left(B \cap A^{c}\right)=P(B)-P(A \cap B)\\)
2. \\(P(A \cup B)=P(A)+P(B)-P(A \cap B)\\)
3. \\(A \subset B \Rightarrow P(A) \leq P(B)\\)


## Các phép tính của xác suất

Từ hệ tiên đề Kolmogorov, các phép toán trên đó cũng được hình thành, lần lượt dưới dạng các định lý sau
> Nếu \\(P\\) là một hàm xác suất và \\(A\\) là một tập bất kỳ của \\(\beta\\) thì
1. \\(P(\varnothing)=0\\)
2. \\(P(A)\le 1\\)
3. \\(P(A^c)=1-P(A)\\)

> Nếu \\(P\\) là một hàm xác suất và \\(A, B\\) là các tập bất kỳ trong \\(\beta\\) thì
1. \\(P\left(B \cap A^{\mathrm{c}}\right)=P(B)-P(A \cap B)\\)
2. \\(P(A \cup B)=P(A)+P(B)-P(A \cap B)\\)
3. \\(\text {Nếu } A \subset B, \text { thì } P(A) \leq P(B)\\)

Từ (2.) cho ta một bất đẳng thức hữu ích. Do \\(P(A \cup B) \leq 1\\), ta được 
\\[P(A \cap B) \geq P(A)+P(B)-1.\\]

Đây là ví dụ đặc biệt của bất đẳng thức [Bonferroni](https://mathworld.wolfram.com/BonferroniInequalities.html), cho phép chúng ta tìm cận dưới của xác suất một sự kiện là giao của hai sự kiện bất kỳ. Bất đẳng thức này tỏ ra cực kỳ hữu ích khi \\(A\cap B\\) là sự kiện khó có thể xác định được xác suất xảy ra.

> Nếu \\(P\\) là một hàm xác suất thì
1. \\(P(A)=\sum_{i=1}^{\infty} P\left(A \cap C_{i}\right) \text { với mọi phần riêng } C_{1}, C_{2}, \ldots, \forall C_1, C_2,\ldots\\)
2. \\(P\left(\cup_{i=1}^{\infty} A_{i}\right) \leq \sum_{i=1}^{\infty} P\left(A_{i}\right), \forall A_1, A_2,\ldots \text{ (Bất đẳng thức Boole)}\\)

**Chứng minh**

1. Do \\(C_1, C_2,\ldots\\) là rời nhau, ta có \\(C_i\cap C_j = \varnothing, \forall i\ne j\\), và \\(S=\cup_{i=1}^{\infty} C_{i}\\). Do vậy
\\[A=A \cap S=A \cap\left(\bigcup_{i=1}^{\infty} C_{i}\right)=\bigcup_{i=1}^{\infty}\left(A \cap C_{i}\right).\\]
Hiển nhiên thu được 
\\[P(A)=P\left(\bigcup_{i=1}^{\infty}\left(A \cap C_{i}\right)\right).\\]
Lúc này, do các \\(C_i\\) là rời nhau, các tập \\(A\cap C_i\\) cũng rời nhau, từ tính cộng tính của hàm xác suất ta được 
\\[P\left(\bigcup_{i=1}^{\infty}\left(A \cap C_{i}\right)\right)=\sum_{i=1}^{\infty} P\left(A \cap C_{i}\right)\\]

2. Ta định nghĩa lần lượt
 \\[A_{1}^{'}=A_{1}, \quad A_{i}^{'}=A_{i} \setminus\left(\bigcup_{j=1}^{i-1} A_{j}\right), \quad i=2,3, \ldots\\]
 Ở đây, hiểu \\(A\setminus B = A\cap B^{c}\\).
 Ta chứng tỏ các \\(A_i^{'}\\) rời nhau như sau
\\[
\begin{aligned}
A_{i}^{'} \cap A_{k}^{'} &=\left\lbrace A_{i} \setminus\left(\bigcup_{j=1}^{i-1} A_{j}\right)\right\rbrace \cap\left\lbrace A_{k} \setminus\left(\bigcup_{j=1}^{k-1} A_{j}\right)\right\rbrace \\\
&=\left\lbrace A_{i} \cap\left(\bigcup_{j=1}^{i-1} A_{j}\right)\right\rbrace \cap\left\lbrace A_{k} \cap\left(\bigcup_{j=1}^{k-1} A_{j}\right)\right\rbrace \\\
&=\left\lbrace A_{i} \cap \bigcap_{j=1}^{i-1} A_{j}^{c}\right\rbrace \cap\left\lbrace A_{k} \cap \bigcap_{j=1}^{k-1} A_{j}^{c}\right\rbrace
\end{aligned}
\\]
 Dễ thấy rằng \\(\cup_{i=1}^{\infty} A_{i}^{'}=\cup_{i=1}^{\infty} A_{i}\\), do đó ta có 
 \\[P\left(\bigcup_{i=1}^{\infty} A_{i}\right)=P\left(\bigcup_{i=1}^{\infty} A_{i}^{'}\right)=\sum_{i=1}^{\infty} P\left(A_{i}^{'}\right)\\]
 Do \\(A_{i}^{'} \subset A_{i}\\) nên \\(P\left(A_{i}^{'}\right) \leq P\left(A_{i}\right)\\), thu được \\(\sum_{i=1}^{\infty} P\left(A_{i}^{*}\right) \leq \sum_{i=1}^{\infty} P\left(A_{i}\right)\\), kết thúc chứng minh.
 \\(~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\blacksquare\\)

## Phép đếm (Cộng - Nhân - Giai thừa - Tổ hợp - Chỉnh hợp)

Trong chương trình Toán lớp 11, trước khi nhắc tới xác suất, sách giáo khoa có dạy trước về hai quy tắc cơ bản: Quy tắc cộng và quy tắc nhân.
> Quy tắc cộng: Nếu một công việc có thể thực hiện theo \\(n\\) cách. Trong đó cách thứ \\(i, i=\overline{1,n}\\) có \\(m_i\\) cách thực hiện thì công việc đó có thể hoàn thành trong \\(\sum_i m_i\\) cách.
> Quy tắc nhân: Nếu một công việc có \\(n\\) nhiệm vụ cần hoàn thành. Trong đó nhiệm vụ thứ \\(i, i=\overline{n}\\) có \\(m_i\\) cách thực hiện thì công việc đó có thể hoàn thành trong \\(m_{1} \times m_{2} \times \cdots \times m_{k}\\) cách. 

Tiếp đó, là khái niệm về giai thừa
> Với \\(n\\) là số nguyên dương, \\(n!\\) (đọc là n giai thừa) được định nghĩa như sau
\\[n !=n \times(n-1) \times(n-2) \times \cdots \times 3 \times 2 \times 1.\\]
Quy ước \\(0!=1\\), có một lí giải thú vị cho quy ước này tại [đây](https://www.mathvn.com/2020/06/tai-sao-lai-quy-uoc-01.html).

Tiếp tục đến với tổ hợp và chỉnh hợp
> Với các số nguyên không âm \\(n, r\\), trong đó \\(n\ge r\\), ta định nghĩa tổ hợp chập \\(r\\) của \\(n\\) phần tử như sau
\\[\left(\begin{array}{l}
n \\\
r
\end{array}\right)=\frac{n !}{r !(n-r) !}
\\]
Trong SGK của Việt Nam, kí hiệu tổ hợp trên là \\(C_n^r\\).

> Chỉnh hợp là khi mà ta có tính tới thứ tự thực hiện công việc (tổ hợp không đề cập tới thứ tự). 
 Với giả thiết trên, chỉnh hợp chập \\(r\\) của \\(n\\) phần tử được định nghĩa
\\[A_n^r = r!\times C_n^r\\]

Bài toán về tổ hợp và chỉnh hợp rất đa dạng và phong phú, thường bắt gặp ở các bài toán đố, thi chọn HSG, việc giải quyết được các bài toán này là tiền đề cho việc giải quyết bài toán xác suất (chương trình THPT). Trong khuôn khổ bài viết, tôi chỉ giới thiệu lại để có cái nhìn toàn cảnh.

Chú ý: Các kĩ thuật đếm này chỉ hữu hiệu khi không gian mẫu \\(S\\) hữu hạn phần tử và các kết quả của \\(S\\) **có khả năng xảy ra như nhau** (equally likely).

Bài đã hơi dài và nhàm chán, tôi sẽ viết tiếp ở bài sau để tiện theo dõi.

Cảm ơn bạn đã quan tâm đọc đến đây. Mến chào bạn.

# Tài liệu tham khảo
[Timeline_of_probability_and_statistics](https://en.wikipedia.org/wiki/Timeline_of_probability_and_statistics)
- [xs](https://vi.wikipedia.org/wiki/X%C3%A1c_su%E1%BA%A5t)

<!-- {% include citation.html key="highlight" %} -->
