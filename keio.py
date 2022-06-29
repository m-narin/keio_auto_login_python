from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
import os

load_dotenv()

# chromedriverの実行ファイルのパスを指定
# Windowsの場合は、"./chromedriver.exe"
CHROMEDRIVER = "./chromedriver"
DOMAIN_BASE = "https://auth.keio.jp/"
LOGIN_ID = os.getenv('KEIO_LOGIN_ID')
PASSWORD = os.getenv('KEIO_LOGIN_PASSWORD')

def get_driver():
    driver = webdriver.Chrome(CHROMEDRIVER)
    return driver

def do_login(driver):
    login_url = DOMAIN_BASE + "idp/profile/SAML2/Redirect/SSO?"
    driver.get(login_url)

    # ログインページに遷移するための記述
    elem_btn_pre = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="wrap"]/div/section/div/article/div[2]/ul/li/a'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(elem_btn_pre)
    actions.click(elem_btn_pre)
    actions.perform()


    # ユーザー名入力
    elem_id = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "j_username"))
    )

    # パスワード入力してログインボタンを押す
    try:
        elem_password = driver.find_element_by_name("j_password")

        if elem_id and elem_password:

            elem_id.send_keys(LOGIN_ID)

            elem_password.send_keys(PASSWORD)

            elem_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/section[3]/button'))
            )

            actions = ActionChains(driver)
            actions.move_to_element(elem_btn)
            actions.click(elem_btn)
            actions.perform()

            time.sleep(3)

            perform_url = driver.current_url
            print("login_url",login_url)
            print("perform_url",perform_url)

            # ログインできてauthのURLが変わったら
            if perform_url.find(login_url) == -1:
                return True
            else:
                return False            
        else:
            return False
    except:
        return False
    
if __name__ == "__main__":

    driver = get_driver()

    login_flg = do_login(driver)

    if(login_flg):
        print("慶應アカウントに自動ログイン完了")