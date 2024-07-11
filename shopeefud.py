import threading
from ping3 import ping
import time

# Daftar domain
domains = [
    "www.shopeefood.co.id",
    "shopeefood.co.id",
    "www.staging.shopeefood.co.id",
    "www.live-test.shopeefood.co.id",
    "email.comms.shopeefood.co.id",
    "www.test.shopeefood.co.id",
    "email.mailer.shopeefood.co.id",
    "live-test.shopeefood.co.id",
    "test.shopeefood.co.id",
    "www.test-stable.shopeefood.co.id",
    "email.mg.shopeefood.co.id",
    "uat.shopeefood.co.id",
    "www.uat.shopeefood.co.id",
    "staging.shopeefood.co.id",
    "test-stable.shopeefood.co.id",
    # Menambahkan domain shopee.co.id dan beberapa subdomain
    "shopee.co.id",
    "partner.api.shopee.co.id",
    "mall.shopee.id",
    "c-api-bit.shopeemobile.com",
    "patronus.idata.shopeemobile.com",
    "food-driver.business.accounts.shopee.co.id",
    "deo.shopeemobile.com",
    "content-autofill.googleapis.com",
    "patronus.idata.shopeemobile.com"
]

# Interval waktu antara setiap ping dalam detik
interval = 5

# Fungsi untuk melakukan ping terus-menerus ke domain
def continuous_ping(domain):
    while True:
        response = ping(domain)
        if response:
            print(f"Ping ke {domain} berhasil, waktu respons: {response} detik")
        else:
            print(f"Ping ke {domain} gagal")
        time.sleep(interval)

# Membuat thread untuk setiap domain
threads = []
for domain in domains:
    thread = threading.Thread(target=continuous_ping, args=(domain,))
    threads.append(thread)
    thread.start()

# Menunggu semua thread selesai (script akan berjalan terus-menerus)
for thread in threads:
    thread.join()
