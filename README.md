# Giảng viên: TS. Lê Nhật Duy
# Sinh viên thực hiện:
    20001955 - Trương Văn Thông

# Bài Tập Mã Hoá RSA
Giải thuật RSA gồm các bước sau:
1. Chọn hai số nguyên tố $p$ và $q$ khác nhau.
2. Tính $n = p \times q$.
3. Tính $\phi(n) = (p-1) \times (q-1)$.
4. Chọn số nguyên $e$ sao cho $1 < e < \phi(n)$ và $e$ là số nguyên tố cùng nhau với $\phi(n)$.
5. Tính $d$ sao cho $d \times e \equiv 1 \pmod{\phi(n)}$.
6. Khóa công khai là cặp số $(n, e)$.
7. Khóa bí mật là cặp số $(n, d)$.
8. Mã hóa một số $m$ thành $c$ bằng cách tính $c = m^e \pmod{n}$.
9. Giải mã một số $c$ thành $m$ bằng cách tính $m = c^d \pmod{n}$.

## Bài tập trên lớp:
Cho $p = 17$ và $q = 29$ là các số nguyen tố khác nhau <br>

***a. Tạo bộ khoá dùng RSA*** <br>
1. Chọn hai số nguyên tố $p$ và $q$ khác nhau.
$$p = 17, q = 29$$

2. Tính $n = p \times q$.
$$n = 17 \times 29 = 493$$

3. Tính $\phi(n) = (p-1) \times (q-1)$.
$$\phi(n) = (17-1) \times (29-1) = 448$$

4. Chọn số nguyên $e$ sao cho $1 < e < \phi(n)$ và $e$ là số nguyên tố cùng nhau với $\phi(n)$. <br>
Một số thích hợp cho e là 3 (Vì 3 là số nguyên tố và 3 không chia hết cho $448$) <br>
        $\rightarrow e = 3$

5. Tính $d$ sao cho $d \times e \equiv 1 \pmod{\phi(n)}$. <br>
    Để tìm $ d $ ta cần giải phương trình $ 3d \equiv 1 \pmod{448} $ (với $ e = 3 $ và $ \phi(n) = 448 $). 

    - Thuật toán Euclid mở rộng

        Mục tiêu chính của thuật toán là tìm $d$ sao cho:
        $$3d + 448x = 1$$

        Bắt đầu bằng việc tìm UCLN của 448 và 3:

        1. Bước 1:
        $$448 = 3 \times 149 + 1$$
        $$\text{Trong đó, phần dư là 1.}$$

        2. Bước 2:
        $$3 = 1 \times 3$$
        $$\text{Với phần dư 0.}$$

        Từ đây, ta có $UCLN(448, 3) = 1.$ Nhưng bước này không đủ để tìm giá trị của $d$. Ta cần tiếp tục sử dụng Thuật toán Euclid mở rộng.

        Áp dụng Thuật toán Euclid mở rộng, chúng ta có thể biểu diễn phần dư $1$ từ bước $1$:

        $$1 = 448 - 3 \times 149$$

        Từ đây, ta có $d = -149$. Nhưng giá trị này là số âm. Ta cần một giá trị dương, vì vậy chúng ta sẽ cộng thêm $\phi(n)$ cho giá trị của $d$:

        $$d = -149 + 448 = 299$$

        Với việc khi nhân $d$ với $e = 3$ và lấy modulo $\phi(n) = 448$, kết quả sẽ bằng 1:

        $$3 \times 299 \equiv 1 \pmod{448}$$

        $ \rightarrow d = 299$

*Vậy:*
+ Khoá công khai là cặp số $(n, e) = (493, 3)$.
+ Khoá bí mật là cặp số $(n, d) = (493, 299)$.

***b. Thực hiện mã hoá m=4*** <br>
Để mã hoá một số $m$ thành $c$ bằng cách tính: <br>
$c = m^e \pmod{n}$. <br>
$c = 4^3 \pmod{493} $<br>
$c= 64 \pmod{493} $<br>
$c= 64$

Vậy, số m = 4 sau khi mã hoá sẽ là $c = 64$.

***c. Giải mã*** <br>
Để giải mã một số $c$ thành $m$ bằng cách tính: <br>
$m = c^d \pmod{n}$. <br>
$m = 64^{299} \pmod{493} $<br>
$m = 4 \pmod{493} $<br>
$m = 4$

Vậy, số $c = 64$ sau khi giải mã sẽ là $m = 4$.


***d. Sơ đồ minh hoạ cho quá trình mã hoá, giải mã và truyền dữ liệu của RSA:***

1. **Khởi tạo khoá**:
    - Người gửi và người nhận đều biết khoá công khai $(n, e)$.
    - Chỉ người nhận biết khoá bí mật $(n, d)$.

2. **Mã hoá**:
    - Người gửi sử dụng khoá công khai $(n, e)$ để mã hoá tin nhắn $m$ thành $c$.

3. **Truyền dữ liệu**:
    - Tin nhắn mã hoá $c$ được truyền từ người gửi đến người nhận.

4. **Giải mã**:
    - Người nhận sử dụng khoá bí mật $(n, d)$ để giải mã $c$ trở lại thành $m$.

**Sơ đồ minh hoạ**:

```
Người nhận
   |
   | (1) Tạo khoá công khai (n, e) và khoá bí mật (n, d)
   |
   | Công khai (n, e) cho tất cả (bao gồm người gửi)
   ↓
Người gửi
   |
   | (2) Sử dụng khoá công khai (n, e) để mã hoá tin nhắn m thành c
   ↓
Người nhận
   |
   | (3) Nhận tin nhắn mã hoá c từ người gửi
   |
   | (4) Giải mã c thành m sử dụng khoá bí mật (n, d)
   ↓
   m
```

***e. Nếu bạn là attacker thì bạn có gì? Muốn gì?***

Nếu tôi là một attacker và biết về quá trình RSA đã mô tả ở trên:

1. **Thông tin mà attacker có**:
    - Khoá công khai $(n, e) = (493, 3)$: Điều này là công khai và bất kỳ ai cũng có thể biết.
    - Tin nhắn mã hoá $c = 64$: Nếu attacker có khả năng nghe trộm hoặc chặn được tin nhắn truyền đi.

2. **Thông tin mà attacker muốn**:
    - Khoá bí mật $d$: Để giải mã tin nhắn.
    - Tin nhắn gốc $m$: Để biết nội dung thực sự được truyền đi.

3. **Cách tấn công**:
    - **Tấn công trực tiếp**: Cố gắng phá khoá bằng cách tìm $d$ từ $(n, e)$. Tuy nhiên, với RSA, việc này rất khó và tốn kém về mặt thời gian nếu $n$ lớn.
    - **Tấn công theo bên**: Như đã nói ở trên, sử dụng thông tin phụ như tiêu thụ năng lượng hoặc thời gian thực thi.
    - **Tấn công "man-in-the-middle"**: Attacker giả mạo mình là một bên trong cuộc trao đổi, thay đổi hoặc nghe trộm thông tin.
    - **Tấn công lý thuyết**: Tìm lỗ hổng trong cách triển khai RSA hoặc sử dụng các lỗ hổng đã biết.

Vậy, nếu tôi là một attacker, tôi sẽ muốn thu thập khoá bí mật và tin nhắn gốc. Tuy nhiên, RSA là một thuật toán mã hoá rất an toàn nếu được triển khai đúng cách và với đủ độ dài khoá. Trong ví dụ của bạn, $n = 493$ là một giá trị rất nhỏ, nên một attacker có thể dễ dàng tấn công. Nhưng trong thực tế, $n$ thường có hàng trăm chữ số, làm cho việc tấn công trở nên rất khó khăn.

***f. Độ an toàn của RSA dựa vào đâu?***<br>
Độ an toàn của RSA chủ yếu dựa vào một số yếu tố sau:

1. **Độ khó của việc phân tích số nguyên tố**: Khó khăn trong việc phân giải một số lớn thành các thừa số nguyên tố của nó. Đặc biệt, khi $ n $ là một số có hai thừa số nguyên tố $ p $ và $ q $ (đều là số nguyên tố lớn), việc tìm ra $ p $ và $ q $ từ $ n $ trong một khoảng thời gian hợp lý là một vấn đề chưa được giải quyết hiệu quả.

2. **Độ dài của khoá**: Độ dài của $ n $ (thường được gọi là độ dài khoá) cũng quan trọng. Khoá dài hơn sẽ làm tăng độ an toàn nhưng cũng làm chậm quá trình mã hoá và giải mã. Trong thực tế, khoá RSA thường có độ dài từ 2048 bit trở lên để đảm bảo an toàn.

3. **Lựa chọn của $ e $ và $ d $**: Trong khi $ e $ thường có giá trị tiêu chuẩn như 3 hoặc $ 2^{16} + 1 $, $ d $ phải được giữ bí mật và được chọn sao cho nó không dễ dàng bị suy ra từ $ e $ và $ n $.

4. **Triển khai an toàn**: Cách triển khai của RSA cũng rất quan trọng. Các lỗ hổng trong phần mềm hoặc phần cứng có thể làm giảm độ an toàn của RSA, ngay cả khi thuật toán lý thuyết là an toàn.

5. **Chống lại các tấn công theo bên**: RSA cần phải được triển khai sao cho nó không tiết lộ thông tin thông qua các kênh phụ như tiêu thụ năng lượng, thời gian thực thi, hoặc tiếng ồn từ thiết bị.

6. **Sử dụng chế độ hoạt động an toàn**: Chỉ mã hoá trực tiếp với RSA thường không an toàn. Thay vào đó, RSA thường được sử dụng để mã hoá một khoá ngẫu nhiên, sau đó khoá này được sử dụng trong một thuật toán mã hoá đối xứng để mã hoá dữ liệu thực sự.

- Độ an toàn của RSA không chỉ dựa vào thuật toán lý thuyết mà còn dựa vào cách nó được triển khai và sử dụng trong thực tế.

---
# Web App RSA:
https://rsa-by-thong.streamlit.app/