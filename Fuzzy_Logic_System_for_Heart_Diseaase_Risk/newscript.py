from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# إعداد المتصفح
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # فتح صفحة تسجيل الدخول
    driver.get("https://www.facebook.com/login")
    
    # ملء بيانات تسجيل الدخول
    email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys("01009894633")
    
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "pass")))
    password_field.send_keys("Hamo@12345")
    password_field.send_keys(Keys.RETURN)

    # التحقق من نجاح تسجيل الدخول
    print("Current URL after login attempt:", driver.current_url)
    WebDriverWait(driver, 20).until(EC.url_contains("facebook.com/home.php"))  # أو أي URL يظهر بعد تسجيل الدخول
    
    # لو ظهر CAPTCHA، اعطي وقت يدوي لحله
    time.sleep(5)  # اضبط الوقت حسب الحاجة

    # الانتقال لصفحة الأمان
    driver.get("https://www.facebook.com/settings?tab=security")
    
    # انتظار قسم الجلسات (تحديث الـ XPath حسب التفتيش اليدوي)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Where You’re Logged In') or contains(text(), 'مكان تسجيل دخولك')]")))
    
    # التمرير لتحميل كل الجلسات
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # استخراج الجلسات (تحديث الـ XPath حسب الهيكلية الحالية)
    sessions = driver.find_elements(By.XPATH, "//div[@role='listitem']")
    
    print("\n📌 Facebook Login History:")
    if sessions:
        for session in sessions:
            try:
                device = session.find_element(By.XPATH, ".//span[1]").text  # تحديث حسب الهيكل
                location = session.find_element(By.XPATH, ".//span[2]").text  # تحديث حسب الهيكل
                print(f"📌 Device: {device} | 🌍 Location: {location}")
            except Exception as e:
                print(f"⚠️ خطأ في جلسة: {e}")
    else:
        print("⚠️ لم يتم العثور على جلسات.")

except Exception as e:
    print(f"⚠️ خطأ عام: {e}")
    print("Current URL at failure:", driver.current_url)  # لمعرفة وين وقف الكود

finally:
    driver.quit()