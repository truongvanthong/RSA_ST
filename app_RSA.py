import streamlit as st
import math

# =========================== Hàm tìm nghịch đảo của a trong Zm= =========================== #
def modinv(a, m):
    '''
    Hàm tìm nghịch đảo của a trong Zm
    Input: 
        a: số cần tìm nghịch đảo
        m: module
        
    Output: 
        a^-1 mod m
    '''
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# =========================== Hàm tìm các giá trị e hợp lệ =========================== #
def find_possible_e_values(phi):
    '''
    Hàm tìm các giá trị e hợp lệ
    Input: 
        phi: giá trị hàm số Euler
    Output:
        Danh sách các giá trị e hợp lệ
    '''
    # Trả về danh sách các giá trị e hợp lệ sao cho gcd(e, phi) = 1
    possible_e_values = [e for e in range(2, phi) if math.gcd(e, phi) == 1]
    return possible_e_values

# =========================== Hàm tạo khoá công khai và khoá bí mật =========================== #
def generate_keys(p, q, e):
    '''
    Hàm tạo khoá công khai và khoá bí mật
    
    Input:
        p, q: hai số nguyên tố
        e: số nguyên tố cùng nhau với phi = (p-1)*(q-1)
    Output:
        n: module
        e: khoá công khai
        d: khoá bí mật
    '''
    n = p * q
    phi = (p-1) * (q-1)
    d = modinv(e, phi)
    return (n, e, d)

# =========================== Hàm kiểm tra số nguyên tố =========================== #
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# =========================== APP =========================== #
def main():
    st.title("Mã hóa RSA")
    st.write("Vui lòng nhập hai số nguyên tố khác nhau p và q:")

    col1, col2 = st.columns(2)
    
    with col1:
        p = st.number_input("Số nguyên tố p:", min_value=2, value=17, step=1)
    with col2:
        q = st.number_input("Số nguyên tố q:", min_value=2, value=29, step=1)
    
    if p == q:
        st.warning("Vui lòng nhập hai số nguyên tố khác nhau!")
        return

    if not (is_prime(p) and is_prime(q)):
        st.warning("Vui lòng nhập số nguyên tố cho p và q!")
        return

    phi = (p-1) * (q-1)
    possible_e_values = find_possible_e_values(phi)

    if not possible_e_values:
        st.warning("Không tìm thấy giá trị e hợp lệ. Vui lòng thử lại với các số nguyên tố khác.")
        return
    
    e = st.selectbox("Chọn giá trị e từ danh sách sau:", possible_e_values)

    n, e, d = generate_keys(p, q, e)
    
    st.subheader("Khoá")
    st.write(f"Khoá công khai: ({n}, {e})")
    
    # Thêm button ẩn hiện khoá bí mật
    if st.button("Hiện khoá bí mật"):
        st.write(f"Khoá bí mật: ({n}, {d})")
    
    st.subheader("Mã hóa")
    m = st.number_input("Nhập tin nhắn:", min_value=0, value=4, step=1, max_value=n-1)
    
    # Nút mã hóa
    if st.button("Mã hóa"):
        if m < n:
            c = pow(m, e, n)
            st.success(f"Tin nhắn gốc: {m}")
            st.success(f"Tin nhắn mã hoá: {c}")
        else:
            st.warning("Vui lòng chọn một tin nhắn nhỏ hơn giá trị n!")
    
    st.subheader("Giải mã")
    c_dec = st.number_input("Nhập tin nhắn mã hoá để giải mã:", min_value=0, step=1, max_value=n-1)
    
    # Nút giải mã
    if st.button("Giải mã"):
        m_decrypted = pow(c_dec, d, n)
        st.success(f"Tin nhắn gốc: {m}")
        st.success(f"Tin nhắn mã hoá: {c_dec}")
        st.success(f"Tin nhắn giải mã: {m_decrypted}")
    
if __name__ == "__main__":
    main()
