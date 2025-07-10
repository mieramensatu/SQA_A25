from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def register_test(email, username, nomor_hp, password, valid_password):
    driver = webdriver.Chrome()
    driver.get("https://proyek-3-proyek.github.io/register/")
    time.sleep(2)

    # Isi form register
    email_input = driver.find_element(By.NAME, "email")
    username_input = driver.find_element(By.NAME, "username")
    nomor_input = driver.find_element(By.NAME, "nomor_hp")
    password_input = driver.find_element(By.NAME, "password")
    validpassword_input = driver.find_element(By.NAME, "valid_password")

    email_input.send_keys(email)
    username_input.send_keys(username)
    nomor_input.send_keys(nomor_hp)
    password_input.send_keys(password)
    validpassword_input.send_keys(valid_password)

    # Klik tombol register
    register_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    register_button.click()

    time.sleep(2)

    # Cek hasil register
    if "inventory" in driver.current_url:
        print(f"[✅] daftar berhasil: 'dengan email {email}', username {username}, nomor hp{nomor_hp} password: '{password}' dan valid password: '{valid_password}'")
    else:
        # Coba cari pesan error (jika ada)
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
            print(f"[❌] register gagal - Pesan error: {error_message}")
        except:
            print(f"[❌] register gagal tanpa pesan error - Username: '{username}'")

    driver.quit()

# 🔎 Jalankan test:

# 1. Test login berhasil
register_test("cilok@gmail.com", "cilok", "08123456789", "secret_sauce", "secret_sauce")

# # 2. Test login gagal - username salah
# login_test("salah_user", "secret_sauce")

# # 3. Test login gagal - password salah
# login_test("standard_user", "salah_password")

# # 4. Test login gagal - keduanya salah
# login_test("user_x", "pass_x")