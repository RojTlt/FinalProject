from classes import Func
from test_data import valid_phone, valid_email, valid_login, valid_password, invalid_per_acc, \
    invalid_login, invalid_email, invalid_password, invalid_phone, valid_per_acc, valid_phone_8, \
    long_password, void_password, void_phone

fn = Func()

def test_log_in_with_correct_telephone():
    '''Проверяет вход в аккаунт с валидными значениями телефона и пароля'''
    cur_url = fn.log_in('t-btn-tab-phone', valid_phone, valid_password)
    assert 'b2c.passport.rt.ru/account_b2c' in cur_url

def test_log_in_with_correct_email():
    '''Проверяет вход в аккаунт с валидными значениями почты и пароля'''
    cur_url = fn.log_in('t-btn-tab-mail', valid_email, valid_password)
    assert 'b2c.passport.rt.ru/account_b2c' in cur_url

def test_log_in_with_correct_login():
    '''Проверяет вход в аккаунт с валидными значениями логина и пароля'''
    cur_url = fn.log_in('t-btn-tab-login', valid_login, valid_password)
    assert 'b2c.passport.rt.ru/account_b2c' in cur_url

def test_log_in_with_correct_per_acc():
    '''Проверяет вход в аккаунт с валидными значениями лицевого счёта и пароля'''
    cur_url = fn.log_in('t-btn-tab-ls', valid_per_acc, valid_password)
    assert 'b2c.passport.rt.ru/account_b2c' in cur_url

def test_dont_login_with_incorrect_telephone():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе невалидного значения телефона'''
    cur_url = fn.log_in('t-btn-tab-phone', invalid_phone, valid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_incorrect_email():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе невалидного значения почты'''
    cur_url = fn.log_in('t-btn-tab-mail', invalid_email, valid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_incorrect_login():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе невалидного значения логина'''
    cur_url = fn.log_in('t-btn-tab-login', invalid_login, valid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_incorrect_per_acc():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе невалидного значения лицевого счёта'''
    cur_url = fn.log_in('t-btn-tab-ls', invalid_per_acc, valid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_correct_telephone_and_incorrect_password():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе валидного значения телефона и невалидного пароля'''
    cur_url = fn.log_in('t-btn-tab-phone', valid_phone, invalid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_correct_email_and_incorrect_password():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе валидного значения почты и невалидного пароля'''
    cur_url = fn.log_in('t-btn-tab-mail', valid_email, invalid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_correct_login_and_incorrect_password():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе валидного значения логина и невалидного пароля'''
    cur_url = fn.log_in('t-btn-tab-login', valid_login, invalid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_correct_per_acc_and_incorrect_password():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе валидного значения лицевого счёта и невалидного пароля'''
    cur_url = fn.log_in('t-btn-tab-ls', valid_per_acc, invalid_password)
    assert 'login-actions/authenticate' in cur_url

def test_dont_login_with_correct_per_acc_and_long_password():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе валидного значения лицевого счёта и длинного пароля (>5000)'''
    cur_url = fn.log_in('t-btn-tab-ls', valid_per_acc, long_password)
    assert 'login-actions/authenticate' in cur_url

def test_log_in_with_correct_telephone8():
    '''Проверяет вход в аккаунт с валидными значениями телефона (написание через 8) и пароля'''
    cur_url = fn.log_in('t-btn-tab-phone', valid_phone_8, valid_password)
    assert 'b2c.passport.rt.ru/account_b2c' in cur_url

def test_dont_login_with_void_telephone_and_password():
    '''Проверяет то, что вход в аккаунт не выполнится при вводе пустых строк в поля логина и пароля'''
    cur_url = fn.log_in('t-btn-tab-phone', void_phone, void_password)
    print(cur_url)
    assert ' https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth' in cur_url

def test_open_page_forgot_password():
    '''Проверяет то, что при нажатии на надпись "Забыл пароль" произойдет переход на страницу восстановления пароля'''
    cur_url = fn.open_page('forgot_password')
    assert 'login-actions/reset-credentials' in cur_url

def test_open_page_registration():
    '''Проверяет то, что при нажатии на надпись "Зарегистрироваться" произойдет переход на страницу регистрации'''
    cur_url = fn.open_page('kc-register')
    assert 'login-actions/registration' in cur_url
