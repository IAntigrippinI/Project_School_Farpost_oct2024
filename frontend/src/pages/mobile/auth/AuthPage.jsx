import './AuthPage.css'
import logo from './../../../images/logo.jpeg'
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

import Button from '../../../components/auth/Button/Button';
import ButtonLogin from '../../../components/auth/Button/ButtonLogin'
import InputFields from '../../../components/auth/InputFields/InputFields'

const AuthPage = () => {

    let api = 'http://127.0.0.1:8000/auth/login'
    const navigate = useNavigate()
    const [phone, setPhone] = useState('');
    const [password, setPassword] = useState('');

    function onChangePhone(e) {
        console.log('change')
        setPhone(e.target.value)
        console.log(phone)
    }
    function onChangePassword(e) {
        setPassword(e.target.value)
        console.log(password)
    }

    function onClickLogin(e) {
        console.log('press login')
        // const data = JSON.stringify({ phone: login, password: password });
        const data = {
            phone: phone,
            password: password,
        };
        axios.post(api, data, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
        }).then((resp) => {
            // console.log(resp.data);
            document.cookie = 'access_token=' + resp.data.token
            navigate('/')
        });
    }

    return (
        <div className="auth">
            <div className="window-auth">
                <div className="auth-field">
                    <div className="logo">
                        <img className='logo-102' src={logo}></img>
                    </div>

                    <div className="auth-btns-switch">
                        <div className="auth-btn-block-1">
                            <Button text={'Вход с паролем'} />
                        </div>

                        <div className="auth-btn-block-2">
                            <Button text={'Регистрация'} />
                        </div>
                    </div>
                    <div className="auth-inp-block">
                        <InputFields onChange={onChangePhone} description={'Телефон/Логин'} />
                        <InputFields onChange={onChangePassword} description={'Пароль'} />
                    </div>
                    <div className="auth-btns-login-field">
                        <ButtonLogin onClick={onClickLogin} text={'Войти'} style={'auth-btn-login-orange'} />
                        <ButtonLogin text={'Войти через телеграм'} style={'auth-btn-login-white'} />
                    </div>
                </div>
            </div>
        </div>

    );
}

export default AuthPage;